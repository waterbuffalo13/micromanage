import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

import plotly.graph_objects as go

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
# fig = dcc.Graph(id='a_graph', figure={'data': [go.Bar(y=['giraffes', 'orangutans', 'monkeys'],x=[20, 14, 23],name = "SF ZOO", orientation='h')]})

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=fig, id='gantt'),
])
if __name__ == '__main__':
    app.run_server(debug=True)
