from wms2B.complex_graphs.indicators import indicators
from wms2B.complex_graphs.z_misc_graphs import *
from wms2B.complex_graphs.habits_monitor import habitsmonitor
from datetime import datetime as dt, datetime, timedelta
from wms2B.complex_graphs.tabs import tabs
from pytimeparse.timeparse import timeparse

from wms2B.data.task import Task
from wms2B.db_conn import Database

# from wms2B.app import app


# user class
# user-controller class - handles all the main functions related to user (CRUD)
# session controller - logging in/out
# p = Database(":memory:")
p = Database(":memory:")

# emp_1 = Employee('Jake', 'Williams', '80,000.00')
# emp_2 = Employee('Django', 'Henry', '68,000.00')
# p.cursor.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay real
#     )""")
# p.execute("INSERT INTO employees VALUES (?, ? ,?)", (emp_1.first, emp_1.last, emp_1.pay))
# p.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
#           {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})

suggested_data = {'Index': ['1', '2','3','4','5','6'], 'content': ['Draw a picture', 'Listen to a podcast','Watch a movie','Read a book','Work on game design', 'write papers'],}

suggested_df = pd.DataFrame(suggested_data)


# todo_df = pd.read_csv("data/todolist.csv")
todo_df = pd.read_sql("SELECT * FROM Task", p.connection)

# schedule_df = pd.read_csv("data/gantt.csv")
schedule_df = pd.read_sql("SELECT * FROM Activity", p.connection)

test = schedule_df.columns

curr_year = int(dt.now().strftime("%Y"))
curr_month = int(dt.now().strftime("%m"))
curr_day = int(dt.now().strftime("%d"))
curr_hour = int(dt.now().strftime("%H"))
curr_minute = int(dt.now().strftime("%M"))
curr_second = int(dt.now().strftime("%S"))



index_page = html.Div([

    html.Div([
        # html.H5("Waterbuffalo Micromanagement v2.01 ~ Success is commemorated; Failure merely remembered.  "),
        # html.Img(src="/assets/test.png"),
        html.Button('Personal Dashboard', id='btn-nclicks-1', n_clicks=0),
        html.A(html.Button('Progress Monitor', id='btn-nclicks-2', n_clicks=0), href='/progress'),
        html.Button('Predictive Analytics', id='btn-nclicks-3', n_clicks=0),
        html.Button('Retrieval', id='btn-nclicks-4', n_clicks=0),


    ], className="banner", style={"textAlign": "center"}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([], className="new"),
                html.Div(["Activity Breakdown"], style={"text-align": "center", "font-size": "150%"}),
                dcc.Graph(id ="pie-chart", figure=pie,style={'height': "20vh"} ),
                dcc.Graph(id="horizontal-stats", figure=horizontal_stats, style={'height': "9vh"}),
                html.Br(),
                html.Div([
                ]
                ),

            ], className="piechart", style={"position": "relative"}),

            html.Div([
                tabs,
                html.Div(id='tabs-example-content'),

            ], className="ganttchart"),

            html.Div([
                html.Div(
                    ["Wellbeing & Energy Distribution"],
                    style={"text-align": "center", "font-size": "150%"}),
                dcc.Graph(figure=task_distribution, style={'height': "30vh"}),
                "gtest"
            ], className="sleepstats"),
            # html.Div([
                html.Div([
                    html.Div(
                        ["Schedule Log"],
                        style={"text-align": "center", "font-size": "150%"}),
                    dash_table.DataTable(
                        id='schedule-table',
                        # columns=[{"name": i, "id": i} for i in schedule_df.columns[3:] ],
                        columns=[{"name": i, "id": i} for i in schedule_df.columns],
                        row_deletable=True,
                        style_cell={'fontSize': 12, 'font-family': 'Helvetica'}



                    )
                ], className="schedulelist"),

            # ], className="schedulelist-flex"),

            html.Div([
                indicators,
                html.Div(
                    ["-", dcc.Graph(figure=sleep, style={'height': "5vh", "position": "bottom"}), html.Br(), ],
                    style={"text-align": "center"}),

            ], className="n2box"),
            html.Div([
                html.Div([
                    tank1,
                ], className="three columns"),
                html.Div([
                    tank2,
                ], className="three columns"),
                html.Div([
                    tank3,
                ], className="three columns"),
                html.Div([
                    tank4,
                ], className="three columns"),
                # dcc.Graph(figure=pie, style={'height': "10vh"}),

            ], className="n5box twelve columns"),

            # html.Div([
            html.Div([
                # "n4 box",
                # html.Div(["\"Resilience in Uncertainity, Resignation in Inevitability\""], className="test"),
                html.Div([
                    html.Div(
                        ["To-do list"],
                        style={"text-align": "center", "font-size": "150%"}),
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in todo_df.columns],
                        style_cell={'fontSize': 12, 'font-family': 'Helvetica'},
                        # data=todo_df.to_dict('records'),
                        editable=True,
                        row_deletable=True,

                        # style_cell_conditional=[
                        #     {
                        #         'if': {'column_id': i},
                        #         'textAlign': 'left'
                        #     } for i in ['Date', 'Region']
                        # ],
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'odd'},
                                'backgroundColor': 'rgb(248, 248, 248)'
                            }
                        ],
                        style_header={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'fontWeight': 'bold'
                        }

                    ),
                    html.Div(id="hidden_div", style={"display": "none"}),
                    html.Div([
                        html.Div([
                            dcc.Input(id='todo_content', type='text', value="",
                                      style={"width": "90%"}),
                        ], className="six columns"),
                        html.Div([
                            html.Button('Submit', id='todo_submit', n_clicks=0)
                        ], className="six columns")
                    ], className="twelve columns")

                ], className="test"),

                html.Div([
                    html.Div([

                        habitsmonitor
                    ], className="test"),
                ], className="test"),
                html.Div([
                    daq.GraduatedBar(
                        id='my-daq-graduatedbar',
                        color={"ranges": {piecolours[3]: [0, 2], piecolours[1]: [2, 5], piecolours[2]: [5, 10]}},
                        label=dict(
                            label="Overall Performance",
                            style={"color": "black", "background-color": "#ddd"},
                        ),

                        value=10,

                    ),

                ], className="test"),

                html.Div([
                    html.Div(
                        ["Virtue Radar"],
                        style={"text-align": "center", "font-size": "150%"}),
                    dcc.Graph(figure=personality, style={'height': "25vh"}),
                ], className="test"),
                html.Div([

                          ], className="test"),

            ], className="todolist"), html.Div([
                html.Div([html.Img(src="/assets/test.png", style={"height": "13vh"}), "Waterbuffalo says", html.Br(),
                          "The question isn't who is going to let me; it's who is going to stop me. ~ Howard Roark",

                          ], className="test"),
                html.Div([
                    dcc.Graph(
                        id='example-graph-2',
                        figure=line_chart,
                        style={
                            # "width": "25vh,"
                            "height": "20vh"},
                    ),

                    "test",

                ], className="test"),
                html.Div([
                    "SUGGESTED ACTIVITIES", html.Br(),
                    dash_table.DataTable(
                        id='suggested',
                        columns=[{"name": i, "id": i} for i in suggested_df.columns],
                        data=suggested_df.to_dict('records'),
                        style_cell={'fontSize':15, 'font-family':'sans-serif'}
                    )

                    , html.Br(),
                    # dcc.Graph(
                    #     id='example-graph-2',
                    #     figure=sankey,
                    #     style={"width": "25vh", "height": "20vh"},
                    # ),
                ],
                    className="test"),
                html.Div(
                    ["LONG TERM STRATEGY", html.Br(), " - Develop Waterbuffalo Micromanagement", html.Br(),
                     " - Create Waterbuffalo Analytics",
                     html.Br(), " - Become a Data Analyst", html.Br(), " - WRI", html.Br(),

                     "RECENT ACHIEVEMENTS", html.Br(), "- Implemented fourth column", html.Br(),
                     "- Watched a lecture on statistics", html.Br(), "- Maintained a google schedule"
                     ],
                    className="test"),
                # html.Div([dcc.Graph(figure=sankey, style={'height': "20vh"}),
                #           ], className="test"),
                html.Div([
                    "KPI REPORT", html.Br(), "SLEEP : CONSISTENT GOOD", html.Br(), "NUTRITION : GOOD", html.Br(),
                          "SCHEDULE QUALITY : CONSISTENT LOW", html.Br(), "VIRTUE SCORE : HIGH", html.Br(),
                          "OVERALL WELLBEING: FLUCTUATING HIGH"
                          ], className="test"),

            ], className="todolist"),

            # ],className="listoftodo"),

            # html.Div([
            #     # dcc.Graph(figure=fig, style={'height': "4vh"}),
            #     "take it easy"
            # ]),
            # html.Div([
            #     "n3 box",
            # ], className="rightbar"),
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box1",
            # ], className="rightbar1"),
            #
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box",
            # ]),
            #
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box",
            # ]),
            # html.Div([
            #     "n3 box",
            # ]),

        ], className="wrapper"),
    ], className="centerdiv"),

], className="twelve columns")
