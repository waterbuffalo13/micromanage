from wms2B.app import app
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
# from wms2B.index import index_page
import dash
import datetime
import plotly.figure_factory as ff


################################################
###TO-DO LIST
################################################
@app.callback(Output("table", "data"),
              [Input('todo_submit', 'n_clicks')],
              [State('todo_content', 'value')])
def update_output(n_clicks, task_contents):
    base = pd.read_csv("datastores/todolist.csv")

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
        updated.to_csv("datastores/todolist.csv", index=False)

        return updated.to_dict('records')


@app.callback(Output("hidden_div", "figure"),
              [Input('table', 'data_previous'), Input("table", "data")],
              [State('table', 'data')])
def delete_from_todo(previous, data, current):
    current_df = pd.read_csv("datastores/todolist.csv")
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
                final_df.to_csv("datastores/todolist.csv", index=False)
                return final_df.to_dict('records')

################################################
###GANTT
################################################

@app.callback(Output("schedule-table", "data"),
              [Input('submit-schedule', 'n_clicks')],
              [State('task_content', 'value'), State('task_start', 'value'),
               State('task_stop', 'value')])
def update_output(n_clicks, task_contents, start_task, stop_task):
    # read from database
    task_nature = "---"
    base = pd.read_csv("datastores/gantt.csv")
    bool = task_contents == ""
    if bool == True:
        dash.exceptions.PreventUpdate()
        return base.to_dict('records')
    base = base.loc[:, ~base.columns.str.contains('^Unnamed')]
    created = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    task_data = [[task_contents, created, start_task, stop_task, task_nature]]
    updated = pd.DataFrame(task_data, columns=['task_name', 'created_date', 'start_task', 'stop_task', "task_nature"])
    updated = base.append(updated, sort=False)
    updated = updated[pd.notnull(updated["task_name"])]
    updated.to_csv("datastores/gantt.csv", index=False)
    return updated.to_dict('records')


@app.callback(Output("gantt_chart", "figure"),
              [Input('schedule-table', 'data_previous'), Input("submit-schedule", "n_clicks"),
               Input("schedule-table", "data")],
              [State('schedule-table', 'data')])
def showRemovedRows(old_table, n_clicks, data, new_table, ):
    gantt_df = pd.read_csv("datastores/gantt.csv")
    x = None
    if old_table is None:
        ganttChart = convertToGanttFormat(gantt_df)
        setGanttLayout(ganttChart)
        dash.exceptions.PreventUpdate()
        return ganttChart
    else:
        for row in old_table:
            if row not in new_table:
                final_df = addToGantt(gantt_df, row)
                ganttChart = convertToGanttFormat(final_df)
                setGanttLayout(ganttChart)
                return ganttChart


################################################
###Methods to simplify
################################################
def addToGantt(current_df, row):
    x_df = pd.DataFrame.from_dict(row, orient="index", columns=["task_name"])
    final_df = pd.merge(current_df, x_df, on=['task_name', 'task_name'], how="outer", indicator=True)
    final_df = final_df[final_df['_merge'] == 'left_only']
    final_df = final_df.drop(columns=["_merge"])
    final_df.to_csv("datastores/gantt.csv", index=False)
    return final_df


def setGanttLayout(ganttChart):
    ganttChart.update_layout(autosize=True, margin=dict(l=10, r=10, b=10, t=0))
    ganttChart["layout"].pop("height", None)
    ganttChart["layout"].pop("width", None)


def convertToGanttFormat(final_df):
    df_gantt = final_df[["task_name", "start_task", "stop_task", "task_nature"]].copy()
    df_gantt.columns = ["Task", "Start", "Finish", "Resource"]
    df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format="%d/%m/%Y %H:%M")
    df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format="%d/%m/%Y %H:%M")
    df_gantt= df_gantt.sort_values(by="Start", ascending=False)
    add_or_remove = ff.create_gantt(df_gantt, show_colorbar=True, group_tasks=True)
    return add_or_remove
