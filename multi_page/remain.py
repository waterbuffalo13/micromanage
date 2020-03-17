from datetime import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from apps import index
from apps import app1
from apps import app2
from apps import app3
#from apps import app3
from apps.index import index_page
# git push origin master
from collections import deque
import random
import time
import plotly
import plotly.graph_objs as go
from apps.index import *
import pandas as pd
import plotly.figure_factory as ff

# quotes
# "We are what we repeatedly do. Excellence, then, is not an act, but a habit."

# "My philosophy, in essence, is the concept of man as a heroic being,
# with his own happiness as the moral purpose of his life,
# with productive achievement as his noblest activity,
# and reason as his only absolute"
#
# "With the new day comes new strength and new thoughts"

# It does not matter how slowly you go as long as you do not stop.


X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

app = dash.Dash()

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# Page 1 callback
@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)


@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Index Page callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index_page
    if pathname == '/app1':
        return app1.page_1_layout
    elif pathname == '/app2':
        return app2.page_2_layout
    elif pathname == '/app3':
        return app3.page_3_layout
    else:
        return '404'


@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def graph_update(n):
    X.append(X[-1] + 1)
    Y.append(Y[-1] + Y[-1] * random.uniform(-0.1, 0.1))

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines',  # +markers',
    )

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                yaxis=dict(range=[min(Y), max(Y)]), height=400, paper_bgcolor="#f7f7f7",
                                                plot_bgcolor="#f7f7f7")}


# callback for todolist
# takes input and stores input into database, then updates records
@app.callback(Output("table", "data"),
              [Input('submit-button', 'n_clicks')],
              [State('task_content', 'value'), State('date-picker', 'date'), State('start_task', 'value'),
               State('stop_task', 'value'), State('task_nature', 'value')])
def update_output(n_clicks, task_contents, date_pickers, start_task, stop_task, task_nature):
    #read from database
    base = pd.read_csv("apps/todolist.csv")
    #remove all redundant columns
    base = base.loc[:, ~base.columns.str.contains('^Unnamed')]
    #convert the created data from the input into a specific datetime format
    created = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #attempt to parse the date picker as an input
    try:
        date_pickers_obj = datetime.datetime.strptime(date_pickers, "%Y-%m-%d %H:%M:%S")
    except:
        print("try other date")
    try:
        date_pickers_obj = datetime.datetime.strptime(date_pickers, "%Y-%m-%d")
    except:
        print("ripperino in pepperoni")
    #convert back into string
    date_pickers_str = date_pickers_obj.strftime("%d/%m/%Y")
    #stor
    task_data = [[task_contents, created, date_pickers_str, start_task, stop_task, task_nature]]
    updated = pd.DataFrame(task_data, columns=['task_name', 'created_date', 'deadline', 'start_task', 'stop_task', "task_nature"])
    updated = base.append(updated, sort=False)
    # updated = updated.dropna()
    updated = updated[pd.notnull(updated["task_name"])]
    updated.to_csv("apps/todolist.csv", index=False)
    return updated.to_dict('records')
    # return task_contents

@app.callback(Output("gantt-id", "figure"),
              [Input('table', 'data_previous'), Input("submit-button", "n_clicks"), Input("table", "data")],
              [State('table', 'data')])
def showRemovedRows(previous, n_clicks, data, current, ):
    current_df = pd.read_csv("apps/todolist.csv")
    x = None
    if previous is None:
        df_gantt = current_df[["task_name", "start_task", "stop_task", "task_nature"]].copy()
        df_gantt.columns = ["Task", "Start", "Finish", "Resource"]
        df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format="%d/%m/%Y %H:%M")
        df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format="%d/%m/%Y %H:%M")
        
        nochanges = ff.create_gantt(df_gantt, show_colorbar=True, group_tasks = True)
        dash.exceptions.PreventUpdate()
        return nochanges
    else:
        for row in previous:
            if row not in current:
                # time.sleep(0.10)
                x = row
                x_df = pd.DataFrame.from_dict(x, orient="index", columns=["task_name"])
                #this is probably not a good way of adding information
                final_df = pd.merge(current_df, x_df, on=['task_name', 'task_name'], how="outer", indicator=True)
                final_df = final_df[final_df['_merge'] == 'left_only']
                final_df = final_df.drop(columns=["_merge"])
                final_df.to_csv("apps/todolist.csv", index=False)
                df_gantt = final_df[["task_name", "start_task", "stop_task","task_nature"]].copy()
                df_gantt.columns = ["Task", "Start", "Finish", "Resource"]
                df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format="%d/%m/%Y %H:%M")
                df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format="%d/%m/%Y %H:%M")
                add_or_remove = ff.create_gantt(df_gantt, show_colorbar=True, group_tasks = True)
                
                return add_or_remove

@app.callback(Output("journal_time_series", "figure"),
              [Input('submit-journal', 'n_clicks')],
              [State('journal_content', 'value'), State('emotional_state', 'value')])
def add_to_wellbeinglist(n_clicks, journal_contents, emotional_states):
    wellbeing_df = pd.read_csv("apps/wellbeing.csv")
    created = str(datetime.datetime.now())#.strftime("%d/%m/%Y %H:%M:%S")
    journal_data  = [[created, journal_contents, emotional_states]]
    updated = pd.DataFrame(journal_data, columns=['time_stamp', 'journal_contents', 'wellbeing_value'])
    wellbeing_df = wellbeing_df.append(updated, sort=False)
    wellbeing_df = wellbeing_df[pd.notnull(wellbeing_df["journal_contents"])]
    wellbeing_df.to_csv("apps/wellbeing.csv", index=False)

    data = plotly.graph_objs.Scatter(
        x=wellbeing_df["time_stamp"],
        y=wellbeing_df["wellbeing_value"],
        name='Scatter',
        mode='lines',  # +markers',
    )
    return {'data': [data], 'layout': go.Layout(title="Self-Actualization", xaxis=dict(range=[min(wellbeing_df["time_stamp"]), max(wellbeing_df["time_stamp"])]),
                                                yaxis=dict(range=[min(wellbeing_df["wellbeing_value"]), max(wellbeing_df["wellbeing_value"])]),
                                                height=400, paper_bgcolor="#f7f7f7",
                                                plot_bgcolor="#f7f7f7")}


# @app.callback(Output("reading_list", "data"), [Input("add_book", "n_clicks")], [State("book_name", "value"), State("book_size", "value"), State("current_page","value")])
# def add_to_readinglist(n_clicks, book_names, book_sizes, current_pages):
#     df_reading_list = pd.read_csv("apps/readinglist.csv")
#     book_data = [[book_names, book_sizes, current_pages, "N/A", "N/A", "N/A"]]
#     updated = pd.DataFrame(book_data, columns =["book_names", "length", "current_page", "end_timestamp", "initial_timestamp", "page_update"])
#     updated = df_reading_list.append(updated, sort=False)
#     updated = updated[pd.notnull(updated["book"])]
#     updated.to_csv("apps/readinglist.csv")
#     return updated.to_dict('records')
#
    #return u'Input 1 is "{}" and Input 2 is "{}" and Input 3 is"{}"'.format(book_names, book_sizes, current_pages)
    
if __name__ == '__main__':
    app.run_server(debug=True)
