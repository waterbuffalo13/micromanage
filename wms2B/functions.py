import wms2B.complex_graphs.gantt.ganttCallbacks as import_gantt_callbacks
from wms2B.app import app
from dash.dependencies import Input, Output, State
import pandas as pd
import dash
import datetime
from wms2B.dashboard import index_page


import_gantt_callbacks

################################################
###TO-DO LIST
################################################
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/':
        return index_page
    else:
        return '404'

@app.callback(Output("table", "data"),
              [Input('todo_submit', 'n_clicks')],
              [State('todo_content', 'value')])
def update_output(n_clicks, task_contents):
    base = pd.read_csv("data/todolist.csv")

    if (task_contents == "") == True:
        dash.exceptions.PreventUpdate()
        return base.to_dict('records')
    else:
        base = base.loc[:, ~base.columns.str.contains('^Unnamed')]
        created = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        task_data = [[created, task_contents]]
        updated = pd.DataFrame(task_data, columns=['created_date', "task_contents"])
        updated = base.append(updated, sort=False)
        updated = updated[pd.notnull(updated["task_contents"])]
        updated.to_csv("data/todolist.csv", index=False)

        return updated.to_dict('records')


@app.callback(Output("hidden_div", "figure"),
              [Input('table', 'data_previous'), Input("table", "data")],
              [State('table', 'data')])
def delete_from_todo(previous, data, current):
    current_df = pd.read_csv("data/todolist.csv")
    if previous is None:
        dash.exceptions.PreventUpdate()
        return current_df.to_dict('records')
    else:
        for row in previous:
            if row not in current:
                x_df = pd.DataFrame.from_dict(row, orient="index", columns=["created_date"])
                final_df = pd.merge(current_df, x_df, on=['created_date', 'created_date'], how="outer", indicator=True)
                final_df = final_df[final_df['_merge'] == 'left_only']
                final_df = final_df.drop(columns=["_merge"])
                final_df.to_csv("data/todolist.csv", index=False)
                return final_df.to_dict('records')

