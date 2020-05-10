from dash.dependencies import Input, Output, State
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from wms2B.dashboard import index_page
import dash
import datetime
import plotly.figure_factory as ff
from wms2B.app import app
import wms2B.functions


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/':
        return index_page
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)

    # if pathname == '/app1':
    #     return financials.page_1_layout
    # elif pathname == '/app2':
    #     return data_analysis.page_2_layout
    # elif pathname == '/app3':
    #     return correlations.page_3_layout