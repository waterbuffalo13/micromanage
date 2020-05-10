import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
#
df = [
    dict(Task="Waterbuffalo Micromanagement", Start='2020-05-10', Finish='2020-09-01'),
    dict(Task="Waterbuffalo Treasury", Start='2020-09-01', Finish='2021-09-01'),
    dict(Task="Job search", Start='2020-06-01', Finish='2021-01-01')
]

# df = pd.read_csv(r"C:\Users\Patrick\Desktop\wms2\multi_page\apps\todolist.csv")
# df_gantt = df[["task_name", "start_task", "stop_task"]].copy()
# df_gantt.columns = ["Task", "Start", "Finish"]

gantt = ff.create_gantt(df)
# fig = dcc.Graph(id='a_graph', figure={'data': [go.Bar(y=['giraffes', 'orangutans', 'monkeys'],x=[20, 14, 23],name = "SF ZOO", orientation='h')]})

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=gantt, id='gantt'),




])
if __name__ == '__main__':
    app.run_server(debug=True)
