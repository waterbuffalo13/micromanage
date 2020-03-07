import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
#
# df = [
#     dict(Task='Morning Sleep', Start='2016-01-01', Finish='2016-01-01 6:00:00'),
#     dict(Task='Breakfast', Start='2016-01-01 7:00:00', Finish='2016-01-01 7:30:00'),
#     dict(Task='Work', Start='2016-01-01 9:00:00', Finish='2016-01-01 11:25:00'),
#     dict(Task='Break', Start='2016-01-01 11:30:00', Finish='2016-01-01 12:00:00'),
#     dict(Task='Lunch', Start='2016-01-01 12:00:00', Finish='2016-01-01 13:00:00'),
#     dict(Task='Work', Start='2016-01-01 13:00:00', Finish='2016-01-01 17:00:00'),
#     dict(Task='Exercise', Start='2016-01-01 17:30:00', Finish='2016-01-01 18:30:00'),
#     dict(Task='Post Workout Rest', Start='2016-01-01 18:30:00', Finish='2016-01-01 19:00:00'),
#     dict(Task='Dinner', Start='2016-01-01 19:00:00', Finish='2016-01-01 20:00:00'),
#     dict(Task='Evening Sleep', Start='2016-01-01 21:00:00', Finish='2016-01-01 23:59:00')
# ]

df = pd.read_csv(r"C:\Users\Patrick\Desktop\wms2\multi_page\apps\todolist.csv")
df_gantt = df[["task_name", "start_task", "stop_task"]].copy()
df_gantt.columns = ["Task", "Start", "Finish"]

gantt = ff.create_gantt(df_gantt)
# fig = dcc.Graph(id='a_graph', figure={'data': [go.Bar(y=['giraffes', 'orangutans', 'monkeys'],x=[20, 14, 23],name = "SF ZOO", orientation='h')]})

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=gantt, id='gantt'),




])
if __name__ == '__main__':
    app.run_server(debug=True)
