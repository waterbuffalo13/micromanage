from wms2B.app import app
from dash.dependencies import Input, Output, State
import pandas as pd
import dash
from datetime import datetime, timedelta
import plotly.figure_factory as ff
import plotly.graph_objects as go
from pytimeparse.timeparse import timeparse
from wms2B.db_conn import Database

p = Database(":memory:")

colors = dict(Meal = '#00ba03',
              Work = '#1c7813',
              Recreation = '#193c12',
              Exercise = '#000000',
              Rest = 'rgb(107, 127, 135)')

@app.callback([Output("schedule-table", "data"), Output('task_start', 'value'), Output('task_stop', 'value')],
              [Input('submit-schedule', 'n_clicks')],
              [State('task_content', 'value'), State('task_start', 'value'),
               State('task_stop', 'value'), State('task_type','value')])
def update_gantt_datatable(n_clicks, task_contents, start_task, stop_task, subtype_task):
    created = datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")
    base = pd.read_sql("SELECT * FROM Activity", p.connection)

    hours_expended_str = str(datetime.strptime(stop_task, "%d/%m/%Y %H:%M") - datetime.strptime(start_task, "%d/%m/%Y %H:%M"))
    if n_clicks is not None and n_clicks > 0:

        #Activity(created, task_contents, subtype_task, start_task, stop_task, "---", "-")
        p.execute("INSERT INTO Activity VALUES (?, ?, ?, ?, ?, ?, ?)", (created, task_contents, subtype_task, start_task, stop_task, "---", hours_expended_str))
        updated = pd.read_sql("SELECT * FROM Activity", p.connection)

        start_task = stop_task
        stop_task = (datetime.strptime(start_task, "%d/%m/%Y %H:%M") + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")

        return updated.to_dict('records'), start_task, stop_task
    else:
        dash.exceptions.PreventUpdate()
        return base.to_dict('records'), start_task, stop_task


# remove task
@app.callback([Output("gantt_chart", "figure"), Output('pie-chart', 'figure'), Output('horizontal-stats', 'figure')],
              [Input('schedule-table', 'data_previous'), Input("submit-schedule", "n_clicks"),
               Input("schedule-table", "data")],
              [State('schedule-table', 'data')])
def update_graphs(old_table, n_clicks, data, new_table):
    # gantt_df = pd.read_csv("data/gantt.csv")
    gantt_df = pd.read_sql("SELECT * FROM Activity", p.connection)

    gantt_df["hours_expended_int"] = gantt_df["hours_expended"].apply(lambda x: timeparse(x) / (60 * 60))
    sleep_count = gantt_df.loc[gantt_df["activity_name"] == "Sleep", "hours_expended_int"].sum()
    work_count = gantt_df.loc[gantt_df["activity_name"] == "Work", "hours_expended_int"].sum()
    recreation_count = gantt_df.loc[gantt_df["activity_name"] == "Recreation", "hours_expended_int"].sum()

    if old_table is None:
        df_gantt = gantt_df[["activity_name", "start_time", "stop_time", "task_nature"]].copy()
        df_gantt.columns = ["Task", "Start", "Finish", "Resource"]
        df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format="%d/%m/%Y %H:%M")
        df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format="%d/%m/%Y %H:%M")
        add_or_remove = ff.create_gantt(df_gantt, group_tasks=True, showgrid_x=True, showgrid_y=True)
        ganttChart = add_or_remove
        set_gantt_layout(ganttChart)
        pie_figure = pie_layout(gantt_df)

        horizontal_stats = go.Figure(go.Bar(
            x=[work_count, sleep_count, recreation_count],
            y=['work', 'sleep', 'recr'],
            orientation='h',
            # marker_color= piecolours[1:],

        ))
        horizontal_stats.update_layout(
            margin=dict(
                l=0,
                r=10,
                b=10,
                t=10,
            ),
            paper_bgcolor="#ddd",

        )
        horizontal_stats.update_traces(
            # marker_color='rgb(158,202,225)',
            marker_line_color='rgb(0,0,0)',
            marker_line_width=1,
        )

        return ganttChart, pie_figure, horizontal_stats
    else:
        for row in old_table:
            if row not in new_table:
                p.execute("DELETE FROM Activity WHERE created = (:created)",{"created": row["created"]})
                final_df = pd.read_sql("SELECT * FROM Activity", p.connection)
                # final_df = remove_from_csv(gantt_df, row)
                ganttChart = convert_to_gantt(final_df)
                pie_figure = pie_layout(final_df)

                final_df["hours_expended_int"] = final_df["hours_expended"].apply(lambda x: timeparse(x) / (60 * 60))
                sleep_count = final_df.loc[final_df["activity_name"] == "Sleep", "hours_expended_int"].sum()
                work_count = final_df.loc[final_df["activity_name"] == "Work", "hours_expended_int"].sum()
                recreation_count = final_df.loc[final_df["activity_name"] == "Recreation", "hours_expended_int"].sum()

                horizontal_stats = go.Figure(go.Bar(
                    x=[work_count, sleep_count, recreation_count],
                    y=['work', 'sleep', 'recr'],
                    orientation='h',
                    # marker_color= piecolours[1:],

                ))
                horizontal_stats.update_layout(
                    margin=dict(
                        l=0,
                        r=10,
                        b=10,
                        t=10,
                    ),
                    paper_bgcolor="#ddd",

                )
                horizontal_stats.update_traces(
                    # marker_color='rgb(158,202,225)',
                    marker_line_color='rgb(0,0,0)',
                    marker_line_width=1,
                )


                return ganttChart, pie_figure, horizontal_stats


def convert_to_gantt(final_df):
    gantt = final_df[["activity_name", "start_time", "stop_time", "task_nature"]].copy()
    gantt.columns = ["Task", "Start", "Finish", "Resource"]
    gantt["Start"] = pd.to_datetime(gantt["Start"], format="%d/%m/%Y %H:%M")
    gantt["Finish"] = pd.to_datetime(gantt["Finish"], format="%d/%m/%Y %H:%M")
    remove = ff.create_gantt(gantt, group_tasks=True, showgrid_x=True, showgrid_y=True)
    ganttChart = remove
    set_gantt_layout(ganttChart)
    return ganttChart


def pie_layout(base):
    base["hours_expended_int"] = base["hours_expended"].apply(lambda x: timeparse(x) / (60 * 60))
    sleep_count = base.loc[base["activity_name"] == "Sleep", "hours_expended_int"].sum()
    work_count = base.loc[base["activity_name"] == "Work", "hours_expended_int"].sum()
    study_count = base.loc[base["activity_name"] == "Study", "hours_expended_int"].sum()
    exercise_count = base.loc[base["activity_name"] == "Exercise", "hours_expended_int"].sum()
    routine_count = base.loc[base["activity_name"] == "Routine", "hours_expended_int"].sum()
    recreation_count = base.loc[base["activity_name"] == "Recreation", "hours_expended_int"].sum()
    indulgence_count = base.loc[base["activity_name"] == "Indulgence", "hours_expended_int"].sum()

    # labels = ['Sleep', 'Work', 'Study', 'Exercise', 'Routine', 'Recreation', 'Indulgence']
    # values = [sleep_count, work_count, study_count, exercise_count, routine_count, recreation_count, indulgence_count]

    pie_figure = go.Figure(data=[
        go.Pie(labels=['Sleep', 'Work', 'Study', 'Exercise', 'Routine', 'Recreation', 'Indulgence'],
               values=[sleep_count, work_count, study_count, exercise_count, routine_count, recreation_count, indulgence_count],
               hole=.4,
               textinfo='label+percent',
               automargin=False,
               textposition="inside"
               )])
    pie_figure.update_layout(autosize=True, margin=dict(l=10, r=10, b=10, t=10), paper_bgcolor="white",showlegend=False,  )
    pie_figure.update_yaxes(automargin=True)
    pie_figure.update_traces(hoverinfo='label+percent'#, marker=dict(colors=['#171717', '#193c12', '#1c7813', '#990000'])
                             )#test
    return pie_figure


#dependent
def set_gantt_layout(ganttChart):
    ganttChart.update_layout(autosize=True, margin=dict(l=10, r=10, b=10, t=0), plot_bgcolor="lightgrey")
    ganttChart["layout"].pop("height", None)
    ganttChart["layout"].pop("width", None)
