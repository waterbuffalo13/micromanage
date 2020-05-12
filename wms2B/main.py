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

if __name__ == '__main__':
    app.run_server(debug=True)

