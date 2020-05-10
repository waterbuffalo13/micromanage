
from dash.dependencies import Input, Output, State
import pandas as pd
import dash
import datetime
import plotly.figure_factory as ff
from wms2B.app import app


schedule_df = pd.read_csv("data/gantt.csv")

df_gantt = schedule_df[["task_name", "start_task", "stop_task", "task_nature"]].copy()
df_gantt.columns = ["Task", "Start", "Finish", "Resource"]

df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format="%d/%m/%Y %H:%M")
df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format="%d/%m/%Y %H:%M")

gantt_diagram = ff.create_gantt(df_gantt, group_tasks=True)
gantt_diagram.update_layout(autosize=True,
                            margin=dict(
                                l=10,
                                r=10,
                                b=10,
                                t=0, )
                            )

gantt_diagram["layout"].pop("height", None)
gantt_diagram["layout"].pop("width", None)
