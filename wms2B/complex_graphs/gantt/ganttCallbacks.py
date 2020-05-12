from wms2B.app import app
from dash.dependencies import Input, Output, State
import pandas as pd
import dash
from datetime import datetime, timedelta
import plotly.figure_factory as ff
import time
# from datetime import datetime as dt, datetime, timedelta

#add task to database
@app.callback([Output("schedule-table", "data"), Output('task_start', 'value'), Output('task_stop', 'value')],
              [Input('submit-schedule', 'n_clicks')],
              [State('task_content', 'value'), State('task_start', 'value'),
               State('task_stop', 'value')])
def update_gantt_table(n_clicks, task_contents, start_task, stop_task):
    base = pd.read_csv("data/gantt.csv")
    if n_clicks is not None and n_clicks > 0:
        updated = add_to_table_gantt(base, start_task, stop_task, task_contents, "---")
        updated.to_csv("data/gantt.csv", index=False)
        start_task = stop_task
        stop_task = (datetime.strptime(start_task, "%d/%m/%Y %H:%M")+timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
        print("easy")
        return updated.to_dict('records'), start_task, stop_task
    else:
        dash.exceptions.PreventUpdate()
        return base.to_dict('records'), start_task, stop_task

def add_to_table_gantt(base, start_task, stop_task, task_contents, task_nature):
    base = base.loc[:, ~base.columns.str.contains('^Unnamed')]
    created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    task_data = [[task_contents, created, start_task, stop_task, task_nature]]
    updated = pd.DataFrame(task_data, columns=['task_name', 'created_date', 'start_task', 'stop_task', "task_nature"])
    updated = base.append(updated, sort=False)
    updated = updated[pd.notnull(updated["task_name"])]

    return updated

@app.callback(Output("gantt_chart", "figure"),
              [Input('schedule-table', 'data_previous'), Input("submit-schedule", "n_clicks"), Input("schedule-table", "data")],
              [State('schedule-table', 'data')])
def update_gantt_figure(old_table, n_clicks, data, new_table, ):
    gantt_df = pd.read_csv("data/gantt.csv")
    x = None
    if old_table is None:
        ganttChart = convertToGanttFormat(gantt_df)
        setGanttLayout(ganttChart)
        dash.exceptions.PreventUpdate()
        return ganttChart
    else:
        for row in old_table:
            if row not in new_table:
                final_df = removeFromGantt(gantt_df, row)
                ganttChart = convertToGanttFormat(final_df)
                setGanttLayout(ganttChart)
                return ganttChart

################################################
###Methods to simplify
################################################
def convertToGanttFormat(final_df):
    #temporary fix to index-deleting problem (regathering data from data)
    final_df = pd.read_csv("data/gantt.csv")

    df_gantt = final_df[["task_name", "start_task", "stop_task", "task_nature"]].copy()
    df_gantt.columns = ["Task", "Start", "Finish", "Resource"]
    df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format="%d/%m/%Y %H:%M")
    df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format="%d/%m/%Y %H:%M")

    add_or_remove = ff.create_gantt(df_gantt, show_colorbar=True, group_tasks=True)
    return add_or_remove

def removeFromGantt(current_df, row):
    x_df = pd.DataFrame.from_dict(row, orient="index", columns=["task_name"])
    final_df = pd.merge(current_df, x_df, on=['task_name', 'task_name'], how="outer", indicator=True)
    final_df = final_df[final_df['_merge'] == 'left_only']
    final_df = final_df.drop(columns=["_merge"])
    final_df.to_csv("data/gantt.csv", index=False)
    return final_df

def setGanttLayout(ganttChart):
    ganttChart.update_layout(autosize=True, margin=dict(l=10, r=10, b=10, t=0))
    ganttChart["layout"].pop("height", None)
    ganttChart["layout"].pop("width", None)




