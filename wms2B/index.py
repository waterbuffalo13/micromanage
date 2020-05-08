import dash_html_components as html
from wms2B.graph import *

height_ind = 18
width_ind = 18
# user class
# user-controller class - handles all the main functions related to user (CRUD)
# session controller - logging in/out
todo_df = pd.read_csv("todolist.csv")
schedule_df = pd.read_csv("gantt.csv")


df = pd.read_csv("gantt.csv")
df_gantt = df[["task_name", "start_task", "stop_task", "task_nature"]].copy()
df_gantt.columns = ["Task", "Start", "Finish", "Resource"]

df_gantt["Start"] = pd.to_datetime(df_gantt["Start"], format = "%d/%m/%Y %H:%M")
df_gantt["Finish"] = pd.to_datetime(df_gantt["Finish"], format = "%d/%m/%Y %H:%M")


gantt_diagram = ff.create_gantt(df_gantt, group_tasks=True)
gantt_diagram.update_layout(autosize=True,
                            margin=dict(
    l=10,
    r=10,
    b=10,
    t=0,)
)

gantt_diagram["layout"].pop("height", None)
gantt_diagram["layout"].pop("width", None)


index_page = html.Div([

    html.Div([
        html.H5(
            "Waterbuffalo Micromanagement v2.01 ~ Success is commemorated; Failure merely remembered.  "),
    ], className="banner", style={"textAlign": "center"}),
    html.Div([

        html.Div([

            html.Div([
                html.Div([

                ], className="new"),
                "Box1",
                dcc.Graph(figure=pie, style={'height': "20vh"}),
                # dcc.Graph(figure=personality, style={'height': "25vh"}),
                dcc.Graph(figure=horizontal_stats, style={'height': "9vh"}),
                html.Br(),
                html.Div([
                ], style={"position": "relative", "bottom": "-2vh"}),
                # dcc.Graph(figure=sleep, style={'height': "3vh", "position": "bottom"}), html.Br(),
                # dcc.Graph(figure=sleep, style={'height': "3vh", "position": "bottom"}), html.Br(),

            ], className="piechart", style={"position": "relative"}),

            html.Div([
                # "Box2",
                dcc.Tabs(id='tabs-example', value='tab-1', children=[
                    dcc.Tab(className="tabs-individual", label='Schedule', value='Schedule',
                            style={'borderBottom': '1px solid #d6d6d6',
                                   'padding': '6px',
                                   'fontWeight': 'bold'},
                            selected_style={'borderBottom': '1px solid #d6d6d6',
                                            'padding': '6px',
                                            'fontWeight': 'bold'}),
                    dcc.Tab(label='Retro-Schedule', value='Performance', style={'borderBottom': '1px solid #d6d6d6',
                                                                                'padding': '6px',
                                                                                'fontWeight': 'bold'},
                            selected_style={'borderBottom': '1px solid #d6d6d6',
                                            'padding': '6px',
                                            'fontWeight': 'bold'}),
                    dcc.Tab(label='Mood and Energy', value='Wisdom', style={'borderBottom': '1px solid #d6d6d6',
                                                                            'padding': '6px',
                                                                            'fontWeight': 'bold'},
                            selected_style={'borderBottom': '1px solid #d6d6d6',
                                            'padding': '6px',
                                            'fontWeight': 'bold'}),
                    dcc.Tab(label='Journal', value='Energy', style={'borderBottom': '1px solid #d6d6d6',
                                                                    'padding': '6px',
                                                                    'fontWeight': 'bold'},
                            selected_style={'borderBottom': '1px solid #d6d6d6',
                                            'padding': '6px',
                                            'fontWeight': 'bold'}),
                    dcc.Tab(label='Diet Planner', value='Weight', style={'borderBottom': '1px solid #d6d6d6',
                                                                         'padding': '6px',
                                                                         'fontWeight': 'bold'},
                            selected_style={'borderBottom': '1px solid #d6d6d6',
                                            'padding': '6px',
                                            'fontWeight': 'bold'}),
                ]),
                html.Div(id='tabs-example-content'),


                dcc.Graph(id = "gantt_chart",figure=gantt_diagram, style={'height': "35vh"}),
                dcc.Graph(figure=fig, style={'height': "4vh"}),
                html.Br(),
                html.Div([

                    dcc.Input(id='task_content', type='text', value= "", style = {"box-shadow":"0 0 2px 1px #666"}),
                    dcc.Input(id='task_start', type='text', value=datetime.now().strftime("%d/%m/%Y %H:%M"), style = {"box-shadow":"0 0 2px 1px #666"}),
                    dcc.Input(id='task_stop', type='text',value=(datetime.now() + timedelta(hours=3)).strftime("%d/%m/%Y %H:%M"),style={"box-shadow": "0 0 2px 1px #666"}),
                    html.Button('Submit', id='submit-schedule', n_clicks=0),
                ], className="addtoschedule"),
            ], className="ganttchart"),

            html.Div([

                dcc.Graph(figure=task_distribution, style={'height': "30vh"}),
                "gtest"
            ], className="sleepstats"),

            html.Div([
                # html.Div([
                #     task_name,
                #     task_start,
                #     task_stop,
                #     html.Button('Submit', id='submit-val', n_clicks=0),
                # ], className="addtoschedule"),
                dash_table.DataTable(
                    id='schedule-table',
                    columns=[{"name": i, "id": i} for i in schedule_df.columns],
                    # data=schedule_df.to_dict('records'),
                    row_deletable=True,
                )





            ], className="schedulelist"),

            html.Div([
                html.Div([
                    daq.LEDDisplay(
                        id='my-daq-leddisplay',
                        value="3.14159",
                        size=15
                    )
                ], className="six columns"),
                html.Div([
                    daq.LEDDisplay(
                        id='my-daq-leddisplay',
                        value="3.14159",

                        size=15
                    ),
                ], className="six columns"),

                html.Div(
                    ["n2 box", dcc.Graph(figure=sleep, style={'height': "5vh", "position": "bottom"}), html.Br(), ],
                    style={"text-align": "center"}),

            ], className="n2box"),
            html.Div([

                # html.Div([dcc.Graph(figure=sleep, style={'height': "5vh", "position": "bottom"})],className="twelve columns"),
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
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in todo_df.columns],
                        # data=todo_df.to_dict('records'),
                        row_deletable=True,
                    ),
                    html.Div(id="hidden_div", style={"display":"none"}),
                    html.Div([
                        html.Div([
                            dcc.Input(id='todo_content', type='text', value="",
                                      style={"width":"90%"}),
                        ], className="six columns"),
                        html.Div([
                            html.Button('Submit', id='todo_submit', n_clicks=0)
                        ], className="six columns")
                    ], className="twelve columns")


                ], className="test"),

                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                "HABITS MONITOR"
                            ], style={"grid-column": "1/9"}),
                            html.Div([
                                ""
                            ]),
                            html.Div([
                                "MON"
                            ]),

                            html.Div([
                                "TUE"
                            ]),
                            html.Div([
                                "WED"
                            ]),
                            html.Div([
                                "THU"
                            ]),

                            html.Div([
                                "FRI"
                            ]),
                            html.Div([
                                "SAT"
                            ]),
                            html.Div([
                                "SUN"
                            ]),
                            html.Div([
                                "MIND"
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="yellow",
                                    value=True,
                                    # width=width_ind,
                                    # height=height_ind

                                )
                            ], style={"color": "white", "height": "2em"}),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind,
                                    # style={"width": "100%", "height":"100%"}
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )

                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                "GYM"
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                "CARDIO"
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                "GYM"
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                "CARDIO"
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),

                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                            html.Div([
                                daq.Indicator(
                                    color="green",
                                    value=True,
                                    width=width_ind,
                                    height=height_ind
                                    ,
                                )
                            ]),
                        ], className="habitsmonitor")
                    ], className="test"),

                ], className="test"),
                html.Div([
                    # dcc.Graph(figure=personality, style={'height': "25vh"}),
                    daq.GraduatedBar(
                        id='my-daq-graduatedbar',
                        label=dict(
                            label="Overall Performance",
                            style={"color": "black", "background-color": "#ddd"},
                        ),
                        value=4
                    ),
                    # html.Br(),
                    #                 daq.GraduatedBar(
                    #                   id='my-daq-graduatedbar',
                    #                   value=4
                    # )
                ], className="test"),

                html.Div([
                    dcc.Graph(figure=personality, style={'height': "25vh"}),
                ], className="test"),
                html.Div([                     "RECENT ACHIEVEMENTS", html.Br(), "- Implemented fourth column", html.Br(),
                                               ], className="test"),

            ], className="todolist"), html.Div([
                html.Div(["takeiteasy"], className="test"),
                html.Div([
                    dcc.Graph(
                        id='example-graph-2',
                        figure=line_chart,
                        style={"width": "25vh", "height": "20vh"},
                    ),

                    "test",

                ], className="test"),
                html.Div([

                    dcc.Graph(
                        id='example-graph-2',
                        figure=sankey,
                        style={"width": "25vh", "height": "20vh"},
                    ),
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
                html.Div(["KPI REPORT", html.Br(), "SLEEP : CONSISTENT GOOD", html.Br(), "NUTRITION : GOOD", html.Br(),
                          "SCHEDULE QUALITY : CONSISTENT LOW", html.Br(), "VIRTUE SCORE : HIGH", html.Br(),
                          "OVERALL WELLBEING: FLUCTUATING HIGH"], className="test"),

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
