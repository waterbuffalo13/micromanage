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

            ], style={"position": "relative", "bottom": "-2vh"})

        ], className="piechart", style={"position": "relative"}),

        html.Div([
            # "Box2",
            dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Retro-Schedule',  value='Schedule', style = {"height":"1vh", "vertical-align":"10px"}, selected_style={"height":"1vh"}),
        dcc.Tab(label='Mood and Energy', value='Performance', style = {"height":"1vh"}, selected_style={"height":"1vh"}),
        dcc.Tab(label='Journal', value='Wisdom', style = {"height":"1vh"}, selected_style={"height":"1vh"}),
        dcc.Tab(label='Wellbeing', value='Energy', style = {"height":"1vh"}, selected_style={"height":"1vh"}),
    ]),
    html.Div(id='tabs-example-content'),

            dcc.Graph(figure=gantt_diagram, style={'height': "40vh"}),
            dcc.Graph(figure=fig, style={'height': "3vh"}),
        ], className="ganttchart"),

        html.Div([
            # "To do list",
            # zanzibar_todo,
            html.Div(["Todolist ", zanzibar], className="test"),
            html.Div([
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
                                  width=15,
                                  height=15
                                  ,
                              )

                          ]),

                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15,
                                  # style={"width": "100%", "height":"100%"}
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )

                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),

                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
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
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
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
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
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
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                          html.Div([
                                                  daq.Indicator(
                                  color="green",
                                  value=True,
                                  width=15,
                                  height=15
                                  ,
                              )
                          ]),
                      ], className="habitsmonitor")

                      ], className="test"),
            html.Div(["Automated Feedback",zanzibar], className="test"),
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
        html.Div([
            html.Div(["n2 box"], style={"text-align":"center"}),
            dcc.Graph(figure=sleep, style={'height': "3vh", "position": "bottom"}), html.Br(),
            dcc.Graph(figure=sleep, style={'height': "3vh", "position": "bottom"}), html.Br(),
        ], className="n2box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),

        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),

        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),

        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
        html.Div([
            "n3 box",
        ], className="n3box"),
    ], className="wrapper"),

], className="twelve columns")
