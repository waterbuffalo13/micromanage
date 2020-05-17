
from dash.dependencies import Input, Output, State
import pandas as pd
import dash
import datetime
import plotly.figure_factory as ff
from wms2B.app import app
colors = dict(Meal = 'rgb(46, 137, 205)',
              Work = '#00ba03',
              Recreation = 'rgb(198, 47, 105)',
              Exercise = 'rgb(58, 149, 136)',
              Rest = 'rgb(107, 127, 135)')


schedule_df = pd.read_csv("data/gantt.csv")

df_gantt = schedule_df[["task_name", "start_task", "stop_task", "task_nature"]].copy()
df_gantt.columns = ["Task", "Start", "Finish", "Resource"]
df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format="%d/%m/%Y %H:%M")
df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format="%d/%m/%Y %H:%M")

gantt_diagram = ff.create_gantt(df_gantt, group_tasks=True, showgrid_x=True, showgrid_y=True, colors=colors, index_col='Task', title ="Today's Schedule")
gantt_diagram.update_layout(autosize=True,
                            margin=dict(
                                l=10,
                                r=10,
                                b=10,
                                t=0))

gantt_diagram["layout"].pop("height", None)
gantt_diagram["layout"].pop("width", None)

