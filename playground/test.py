import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
#
df = [dict(Task="Waterbuffalo Micromanagement", Start='2020-04-26', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

# df = pd.read_csv(r"C:\Users\Patrick\Desktop\wms2\multi_page\apps\todolist.csv")
# df_gantt = df[["task_name", "start_task", "stop_task"]].copy()
# df_gantt.columns = ["Task", "Start", "Finish"]

gantt = ff.create_gantt(df)
# fig = dcc.Graph(id='a_graph', figure={'data': [go.Bar(y=['giraffes', 'orangutans', 'monkeys'],x=[20, 14, 23],name = "SF ZOO", orientation='h')]})

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=gantt, id='gantt', title = "WMS Micro"),




])
if __name__ == '__main__':
    app.run_server(debug=True)
