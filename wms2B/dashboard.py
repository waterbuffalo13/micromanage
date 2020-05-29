from wms2B.complex_graphs.other import *
from wms2B.complex_graphs.habitsmonitor import habitsmonitor
from wms2B.complex_graphs.gantt.ganttFigure import *
from datetime import datetime as dt, datetime, timedelta
from wms2B.complex_graphs.tabs import tabs
from pytimeparse.timeparse import timeparse

# from wms2B.app import app


# user class
# user-controller class - handles all the main functions related to user (CRUD)
# session controller - logging in/out

suggested_data = {'Index': ['1', '2','3','4','5','6'],
             'content': ['Draw a picture', 'Listen to a podcast','Watch a movie','Read a book','Work on game design', 'write papers'],
             }

suggested_df = pd.DataFrame(suggested_data)


todo_df = pd.read_csv("data/todolist.csv")
schedule_df = pd.read_csv("data/gantt.csv")

curr_year = int(dt.now().strftime("%Y"))
curr_month = int(dt.now().strftime("%m"))
curr_day = int(dt.now().strftime("%d"))
curr_hour = int(dt.now().strftime("%H"))
curr_minute = int(dt.now().strftime("%M"))
curr_second = int(dt.now().strftime("%S"))

index_page = html.Div([

    html.Div([
        html.H5("Waterbuffalo Micromanagement v2.01 ~ Success is commemorated; Failure merely remembered.  "),
        # html.Img(src="/assets/test.png"),
    ], className="banner", style={"textAlign": "center"}),
    html.Div([

        html.Div([

            html.Div([
                html.Div([], className="new"),
                html.Div(
                    ["Activity Breakdown"],
                    style={"text-align": "center", "font-size": "150%"}),

                dcc.Graph(id ="pie-chart", figure=pie,style={'height': "20vh"} ),

                # dcc.Graph(figure=personality, style={'height': "25vh"}),
                dcc.Graph(figure=horizontal_stats, style={'height': "9vh"}),
                html.Br(),
                html.Div([
                ]
                    # , style={"position": "relative", "bottom": "-2vh"}
                ),
                # dcc.Graph(figure=sleep, style={'height': "3vh", "position": "bottom"}), html.Br(),
                # dcc.Graph(figure=sleep, style={'height': "3vh", "position": "bottom"}), html.Br(),

            ], className="piechart", style={"position": "relative"}),

            html.Div([
                # "Box2",
                # html.Div([
                # dcc.Tabs(id='tabs-example', value='tab-1', children=[
                #
                #     dcc.Tab(className="tabs-individual", label='Schedule', value='Schedule', style={'borderBottom': '1px solid #d6d6d6','padding': '6px','fontWeight': 'bold'},
                #             selected_style={'borderBottom': '1px solid #d6d6d6',
                #                             'padding': '6px',
                #                             'fontWeight': 'bold'}),
                #     dcc.Tab(label='Retro-Schedule', value='Performance', style={'borderBottom': '1px solid #d6d6d6',
                #                                                                 'padding': '6px',
                #                                                                 'fontWeight': 'bold'},
                #             selected_style={'borderBottom': '1px solid #d6d6d6',
                #                             'padding': '6px',
                #                             'fontWeight': 'bold'}),
                #     dcc.Tab(label='Mood and Energy', value='Wisdom', style={'borderBottom': '1px solid #d6d6d6',
                #                                                             'padding': '6px',
                #                                                             'fontWeight': 'bold'},
                #             selected_style={'borderBottom': '1px solid #d6d6d6',
                #                             'padding': '6px',
                #                             'fontWeight': 'bold'}),
                #     dcc.Tab(label='Journal', value='Energy', style={'borderBottom': '1px solid #d6d6d6',
                #                                                     'padding': '6px',
                #                                                     'fontWeight': 'bold'},
                #             selected_style={'borderBottom': '1px solid #d6d6d6',
                #                             'padding': '6px',
                #                             'fontWeight': 'bold'}),
                #     dcc.Tab(label='Diet Planner', value='Weight', style={'borderBottom': '1px solid #d6d6d6',
                #                                                          'padding': '6px',
                #                                                          'fontWeight': 'bold'},
                #             selected_style={'borderBottom': '1px solid #d6d6d6',
                #                             'padding': '6px',
                #                             'fontWeight': 'bold'}),
                #
                # ]),
                #
                # ]),
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
                        columns=[{"name": i, "id": i} for i in schedule_df.columns],
                        row_deletable=True,
                        page_size=7,
                    )
                ], className="schedulelist"),

            # ], className="schedulelist-flex"),

            html.Div([
                html.Div([
                    html.Div([
                        daq.LEDDisplay(
                            label="SLEEP",
                            labelPosition='bottom',
                            id='my-daq-leddisplay',
                            value="6.43",
                            size=10,
                            backgroundColor="#f5f5f5",
                            color="red"
                        ),

                    ], className="three columns"),
                    html.Div([
                        daq.LEDDisplay(
                            label="EAT",
                            labelPosition='bottom',
                            id='my-daq-leddisplay',
                            value="3000",
                            size=10,
                            backgroundColor="#f5f5f5",
                            color="green"
                        ),

                    ], className="three columns"),
                    html.Div([
                        daq.LEDDisplay(
                            label="WORK",
                            labelPosition='bottom',
                            id='my-daq-leddisplay',
                            value="5.14",
                            size=10,
                            backgroundColor="#f5f5f5",
                            color="green"
                        ),

                    ], className="three columns"),
                    html.Div([
                        daq.LEDDisplay(
                            label="",
                            labelPosition='bottom',
                            id='my-daq-leddisplay',
                            value="3.14159",
                            size=10,
                            backgroundColor="#f5f5f5",
                            color="green"
                        ),

                    ], className="three columns"),

                ], className="twelve columns"),

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
                        # data=todo_df.to_dict('records'),
                        editable=True,
                        row_deletable=True,
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
