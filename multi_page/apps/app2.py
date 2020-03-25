import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt, datetime, timedelta
import plotly.figure_factory as ff
import dash_table
import pandas as pd

df = [dict(Task="Fasanara", Start='2020-01-26', Finish='2020-02-24'),
      dict(Task="Method", Start='2020-02-26', Finish='2021-03-24'),
      dict(Task="WMS", Start='2020-03-01', Finish='2021-01-01'),
      dict(Task="stress test", Start='2020-02-24', Finish='2021-02-29')]
fig = ff.create_gantt(df)

df_wellbeing = pd.read_csv("apps/wellbeing.csv")

productivity_time_series = dcc.Graph(id='journal_time_series', animate=True)

table = dash_table.DataTable(
    id='table_journal',
    columns=[{"name": i, "id": i, "deletable":False} for i in df_wellbeing.columns],
    row_deletable=True,
    # editable=True,
    #data= [] #df.to_dict('records'),
)

page_2_layout = html.Div([
    html.Div([
        html.Div([
            html.H2("Waterbuffalo Micromanagement v2.01"),
            html.Img(src="/assets/stock-icon.png")], className="banner", style={"textAlign": "center"}),
        # , "box-shadow": "5px 0px 2px grey"}),
        html.Div([
            html.A(html.Button('Home', className='three columns'),
                   href='/'),
            html.A(html.Button('Todo list', className='three columns'),
                   href='/app1'),
            html.A(html.Button('Journal', className='three columns'),
                   href='/app2'),
            html.A(html.Button('EXT2', className='three columns'),
                   href='/app3'),
        ], className="container", style={"textAlign": "center"})

    ], style={"background-color": "#f5f5f5"}),
html.Br(),
html.Br(),
        html.Div([html.H1('Journal')], style={"textAlign": "center"}),
html.Div([
        html.Div([
            # dcc.Graph(figure=fig, id='gantt-id'),
            # html.Div([html.H6('An ideal future')],style={"textAlign": "center"}),
            # "Big boi goes to school",
            # productivity_time_series,
            table,
            dcc.Textarea(
                id = "journal_content",
                placeholder="What's on your mind?",
                # value='This is a TextArea component',
                style={'width': '100%', 'height': '300px' }
            ),
            dcc.RadioItems(
                id = "emotional_state",
                options=[
                    {'label': 'Suicidal', 'value': -3},
                    {'label': 'Depressed', 'value': -2},
                    {'label': 'Dissatisfied', 'value': -1},
                    {'label': 'Neutral', 'value': 0},
                    {'label': 'Content', 'value': 1},
                    {'label': 'Happy', 'value': 2},
                    {'label': 'Ecstatic', 'value': 3},
                ],
                value=3,
                labelStyle={'display': 'inline-block'}
            ),
            html.Button(id='submit-journal', n_clicks=0, children='Submit')
         ], className = "container", style = {"textAlign": "center"}),
        dcc.RadioItems(
            id='page-2-radios',
            options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
            value='Orange'
        ),
        html.Div(id='page-2-content'),
        html.Br(),
        dcc.Link('Go to Page 1', href='/app1'),
        html.Br(),
        dcc.Link('Go back to home', href='/')
        ])
])