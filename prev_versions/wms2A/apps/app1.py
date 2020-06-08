import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
from datetime import datetime as dt, datetime, timedelta
import plotly.figure_factory as ff
import numpy as np

# todo  BUILD TODO LIST
# create start and finish attribute
# create todolist dataframe and filter for ones with start and end dates

df = pd.read_csv("apps/todolist.csv")
df_gantt = df[["task_name", "start_task", "stop_task", "task_nature"]].copy()
df_gantt.columns = ["Task", "Start", "Finish", "Resource"]

df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format = "%d/%m/%Y %H:%M")
df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format = "%d/%m/%Y %H:%M")

# print("df_gant(start) type"+ df["Start"].info())

gantt = ff.create_gantt(df_gantt)
# df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
#
table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i, "deletable":False} for i in df.columns],
    row_deletable=True,
    # editable=True,
    #data= [] #df.to_dict('records'),
)

horizontal_bar_graph =dcc.Graph(id='a_graph',
              figure={
        'data': [go.Bar(x=[1, 2, 3],
                        y=['A', 'B', 'C'],
                        orientation='h')]
    })


curr_year = int(dt.now().strftime("%Y"))
curr_month = int(dt.now().strftime("%m"))
curr_day = int(dt.now().strftime("%d"))
curr_hour = int(dt.now().strftime("%H"))
curr_minute = int(dt.now().strftime("%M"))
curr_second = int(dt.now().strftime("%S"))

page_1_layout = html.Div([
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
    html.Div([
        html.Br(),
        html.H1('Page 1'),
        html.Div([
            dcc.Graph(figure=gantt, id='gantt-id'),
        html.Div([
            table,
            html.Div([
            ], id = "table-output")
        ], className = "twelve columns"),
        html.Div([
            # table,
            html.Br(),
            html.Div([
                html.H6('Task Content'),
                # task_name
                dcc.Input(id='task_content', type='text', value=None),html.Br(),
                html.H6('Task Resource'),
                dcc.Dropdown(id='task_nature', value=None, options = [{"label":"---", "value" :"---"}, {"label":"---", "value" :"---"}, {"label":"---", "value" :"---"}]),
                html.H6('Deadline (Date)'),
                # deadline
                dcc.DatePickerSingle(
                    id='date-picker',
                    min_date_allowed=dt(curr_year, curr_month, curr_day),
                    max_date_allowed=dt(curr_year+1, 1, 1),
                    initial_visible_month=dt(2017, 8, 5),
                    date=str(dt(curr_year, curr_month, curr_day))
                )
                ,
                html.Div([
                    html.H6('Start Time'),
                    dcc.Input(id='start_task', type='text', value = datetime.now().strftime("%d/%m/%Y %H:%M")),
                    html.H6('End Time'),
                    dcc.Input(id='stop_task', type='text', value=(datetime.now()+ timedelta(hours=3)).strftime("%d/%m/%Y %H:%M")),

                ],className = "twelve columns"),
                # html.Div(id='output-container-date-picker-single'),
                html.Button(id='submit-button', n_clicks=0, children='Submit'),
                html.Div(id='output-state')
            ]),
        ], className = "twelve columns"),
        ], className = "container"),
        dcc.Dropdown(
            id='page-1-dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        ),
        html.Div(id='page-1-content'),
        html.Br(),
        dcc.Link('Go to Page 2', href='/app2'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ])

])
