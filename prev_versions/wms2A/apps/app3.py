import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt, datetime, timedelta
import plotly.figure_factory as ff
# import dash_gif_component as Gif


df = [dict(Task="Fasanara", Start='2020-01-26', Finish='2020-02-24'),
      dict(Task="Method", Start='2020-02-26', Finish='2021-03-24'),
      dict(Task="WMS", Start='2020-03-01', Finish='2021-01-01'),
      dict(Task="stress test", Start='2020-02-24', Finish='2021-02-29')]

fig = ff.create_gantt(df)


# "border-style": "dotted",233
page_3_layout = html.Div([
    html.Div([
        html.Div([], className="sidebar"),
        html.Div([], className="ten columns", style={"border-style": "dotted", "width": "95%", "text-align":"center", "background-color":"gray", "height": "233px", "max-height":"233px", "background-size":"cover"})

    ])



])