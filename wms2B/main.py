from dash.dependencies import Input, Output, State
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from wms2B.index import index_page
import dash
import datetime
import plotly.figure_factory as ff

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index_page
    # if pathname == '/app1':
    #     return financials.page_1_layout
    # elif pathname == '/app2':
    #     return data_analysis.page_2_layout
    # elif pathname == '/app3':
    #     return correlations.page_3_layout
    else:
        return '404'



@app.callback(Output("table", "data"),
              [Input('todo_submit', 'n_clicks')],
              [State('todo_content', 'value')])
def update_output(n_clicks, task_contents):
        base = pd.read_csv("todolist.csv")
        bool = task_contents== ""
        if bool == True:
            dash.exceptions.PreventUpdate()
            return base.to_dict('records')
        else:
            base = base.loc[:, ~base.columns.str.contains('^Unnamed')]
            created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            task_data = [[created, task_contents]]

            updated = pd.DataFrame(task_data, columns=['created_date', "task_contents"])
            updated = base.append(updated, sort=False)
            updated = updated[pd.notnull(updated["task_contents"])]
            updated.to_csv("todolist.csv", index=False)


            return updated.to_dict('records')

@app.callback(Output("hidden_div", "figure"),
              [Input('table', 'data_previous'), Input("table", "data")],
              [State('table', 'data')])
def delete_from_todo(previous, data, current):
    current_df = pd.read_csv("todolist.csv")
    if previous is None:
        dash.exceptions.PreventUpdate()
        return current_df.to_dict('records')
    else:
        for row in previous:
            if row not in current:
                x = row
                x_df = pd.DataFrame.from_dict(x, orient="index", columns=["created_date"])
                final_df = pd.merge(current_df, x_df, on=['created_date', 'created_date'], how="outer", indicator=True)
                final_df = final_df[final_df['_merge'] == 'left_only']
                final_df = final_df.drop(columns=["_merge"])
                final_df.to_csv("todolist.csv", index=False)
                return final_df.to_dict('records')

@app.callback(Output("schedule-table", "data"),
              [Input('submit-schedule', 'n_clicks')],
              [State('task_content', 'value'), State('task_start', 'value'),
               State('task_stop', 'value')])
def update_output(n_clicks, task_contents, start_task, stop_task):
    # read from database
    base = pd.read_csv("gantt.csv")
    bool = task_contents == "name"
    if bool == True:
        dash.exceptions.PreventUpdate()
        return base.to_dict('records')

    # remove all redundant columns
    base = base.loc[:, ~base.columns.str.contains('^Unnamed')]
    # convert the created data from the input into a specific datetime format
    created = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    task_nature= "---"
    # stor
    task_data = [[task_contents, created, start_task, stop_task, task_nature]]
    updated = pd.DataFrame(task_data,
                           columns=['task_name', 'created_date', 'start_task', 'stop_task', "task_nature"])
    updated = base.append(updated, sort=False)
    # updated = updated.dropna()
    updated = updated[pd.notnull(updated["task_name"])]
    updated.to_csv("gantt.csv", index=False)
    return updated.to_dict('records')

@app.callback(Output("gantt_chart", "figure"),
              [Input('schedule-table', 'data_previous'), Input("submit-schedule", "n_clicks"), Input("schedule-table", "data")],
              [State('schedule-table', 'data')])
def showRemovedRows(previous, n_clicks, data, current, ):
    current_df = pd.read_csv("gantt.csv")
    x = None
    if previous is None:
        df_gantt = current_df[["task_name", "start_task", "stop_task", "task_nature"]].copy()
        df_gantt.columns = ["Task", "Start", "Finish", "Resource"]
        df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format="%d/%m/%Y %H:%M")
        df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format="%d/%m/%Y %H:%M")

        nochanges = ff.create_gantt(df_gantt, show_colorbar=True, group_tasks=True)
        nochanges.update_layout(autosize=True,
                                    margin=dict(
                                        l=10,
                                        r=10,
                                        b=10,
                                        t=0, )
                                    )

        nochanges["layout"].pop("height", None)
        nochanges["layout"].pop("width", None)
        dash.exceptions.PreventUpdate()
        return nochanges
    else:
        for row in previous:
            if row not in current:
                x = row
                x_df = pd.DataFrame.from_dict(x, orient="index", columns=["task_name"])
                # this is probably not a good way of adding information
                final_df = pd.merge(current_df, x_df, on=['task_name', 'task_name'], how="outer", indicator=True)
                final_df = final_df[final_df['_merge'] == 'left_only']
                final_df = final_df.drop(columns=["_merge"])
                final_df.to_csv("gantt.csv", index=False)
                df_gantt = final_df[["task_name", "start_task", "stop_task", "task_nature"]].copy()
                df_gantt.columns = ["Task", "Start", "Finish", "Resource"]
                df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format="%d/%m/%Y %H:%M")
                df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format="%d/%m/%Y %H:%M")
                add_or_remove = ff.create_gantt(df_gantt, show_colorbar=True, group_tasks=True)
                add_or_remove.update_layout(autosize=True,
                                            margin=dict(
                                                l=10,
                                                r=10,
                                                b=10,
                                                t=0, )
                                            )

                add_or_remove["layout"].pop("height", None)
                add_or_remove["layout"].pop("width", None)

                return add_or_remove


if __name__ == '__main__':
    app.run_server(debug=True)