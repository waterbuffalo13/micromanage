import dash_html_components as html
from wms2B.graph import *

height_ind = 20
width_ind = 20
# user class
# user-controller class - handles all the main functions related to user (CRUD)
# session controller - logging in/out
index_page = html.Div([

    html.Div([
        html.H5(
            "Waterbuffalo Micromanagement v2.01 ~ Resilience in positions of uncertainity and resignation in the face of inevitability  "),
    ], className="banner", style={"textAlign": "center"}),


    html.Div([
        html.Div([
            html.Div([

            ],className="new"),
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
                dcc.Tab(className = "tabs-individual", label='Schedule', value='Schedule', style={'borderBottom': '1px solid #d6d6d6',
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

            dcc.Graph(figure=gantt_diagram, style={'height': "40vh"}),
            dcc.Graph(figure=fig, style={'height': "4vh"}),
        ], className="ganttchart"),

        html.Div([

dcc.Graph(figure=task_distribution, style={'height': "30vh"}),
        "gtest"
        ], className="sleepstats"),

        html.Div([
            html.Div([
                task_name,
                task_start,
                task_stop,
                html.Button('Submit', id='submit-val', n_clicks=0),
            ], className="addtoschedule"),
            zanzibar], className="schedulelist"),

        html.Div([
            html.Div([
                daq.LEDDisplay(
                    id='my-daq-leddisplay',
                    value="3.14159",
                    size=20
                )
            ],className = "six columns"),
            html.Div([
                daq.LEDDisplay(
                    id='my-daq-leddisplay',
                    value="3.14159",
                    size=20
                ),
            ], className="six columns"),

            html.Div(["n2 box", dcc.Graph(figure=sleep, style={'height': "5vh", "position": "bottom"}), html.Br(),], style={"text-align": "center"}),


        ], className="n2box"),
        html.Div([
            "n5 box",



        ], className="n5box"),
        #
        html.Div([
            # "n4 box",
            html.Div([
              zanzibar_todo
            ], className="test"),
            html.Div([
                "Box4",
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
                        ], style={"color": "white", "height":"2em"}),

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
        style={"color":"black", "background-color":"#ddd"},
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
            ], className="test")

        ], className="todolist"),
        html.Div([
            html.Div(["test"]),
            html.Div(["test"]),
            html.Div(["test"]),
            html.Div(["test"]),
            html.Div(["test"]),
        ], className="todolist"),

        html.Div([
                        # dcc.Graph(figure=fig, style={'height': "4vh"}),
            "take it easy"
        ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        #
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        #
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
        # html.Div([
        #     "n3 box",
        # ], className="n4box"),
    ], className="wrapper"),

], className="twelve columns")
