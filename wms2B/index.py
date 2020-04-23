import dash_html_components as html
from wms2B.graph import *

# user class
# user-controller class - handles all the main functions related to user (CRUD)
# session controller - logging in/out
index_page = html.Div([

    html.Div([
        html.H5("Waterbuffalo Micromanagement v2.01"),
    ], className="banner", style={"textAlign": "center"}),

    html.Div([

        html.Div([
            "Box1",
            dcc.Graph(figure=pie, style={'height': "20vh"}),
            dcc.Graph(figure=horizontal_stats, style={'height': "9vh"}),
            html.Br(),
            html.Div([
                dcc.Graph(figure=sleep, style={'height': "3vh", "position": "bottom"}), html.Br(),
                dcc.Graph(figure=sleep, style={'height': "3vh", "position": "bottom"}), html.Br(),
            ], style={"position": "relative", "bottom": "-2vh"})

        ], className="piechart", style={"position": "relative"}),

        html.Div([
            "Box2",
            dcc.Graph(figure=gantt_diagram, style={'height': "40vh"}),
        ], className="ganttchart"),

        html.Div([
            # "To do list",
            # zanzibar_todo,
            html.Div(["Todolist ", zanzibar], className="test"),
            html.Div(["Habits monitor",
                      html.Div([
                          html.Div([
                              ""
                          ]),
                          html.Div([
                              "MON"
                          ]),

                          html.Div([
                              "TUES"
                          ]),
                          html.Div([
                              "WED"
                          ]),
                          html.Div([
                              "THURS"
                          ]),

                          html.Div([
                              "FRI"
                          ]),
                          html.Div([
                              "CARD"
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )

                          ]),

                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )

                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),

                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              "MIND"
                          ]),

                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              "STRETCH"
                          ]),

                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              "RESIST"
                          ]),

                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                          html.Div([
                              daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=10,
                                  height=10
                                  ,
                              )
                          ]),
                      ], className="habitsmonitor")

                      ], className="test"),
            html.Div([zanzibar], className="test"),
            html.Div([zanzibar], className="test"),

        ], className="todolist"),

        # html.Div([
        #     "Box4",
        #     dcc.Graph(figure=sleep, style={'height': "3vh"}), html.Br(),
        #     dcc.Graph(figure=sleep, style={'height': "3vh"}), html.Br(),
        #
        # ], className="sleepstats"),

        html.Div([
            "wellbeing index",
            html.Div([
                interpolation_strats,
                interpolation_strats,
            ], className="nested"),
            html.Br(), html.Br(), html.Br(), html.Br(),
            dcc.Graph(figure=wellbeing, style={'height': "20vh"}),
        ], className="wellbeing"),

        html.Div([
            html.Div([
                task_name,
                task_start,
                task_stop,
                html.Button('Submit', id='submit-val', n_clicks=0),
            ], className="addtoschedule"),
            zanzibar], className="schedulelist"),
        html.Div([
            virtue_table,
        ], className="nextbox"),
        # html.Div([
        #     "n2 box"
        # ], className="n2box"),
        # html.Div([
        #     "n3 box",
        # ], className="n3box"),
        # html.Div([
        #     "n3 box",
        # ], className="n3box"),
        #
        # html.Div([
        #     "n3 box",
        # ], className="n3box"),
        # html.Div([
        #     "n3 box",
        # ], className="n3box"),
        # html.Div([
        #     "n3 box",
        # ], className="n3box"),
        # html.Div([
        #     "n3 box",
        # ], className="n3box"),

    ], className="wrapper"),

], className="twelve columns")
