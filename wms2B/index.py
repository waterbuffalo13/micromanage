import dash_html_components as html
from wms2B.graph import *

index_page = html.Div([

    html.Div([
        html.H5("Waterbuffalo Micromanagement v2.01"),
    ], className="banner", style={"textAlign": "center"}),

    html.Div([

        html.Div([
            "Box1"
            , dcc.Graph(figure=pie, style={'height': "20vh"}, ),
            dcc.Graph(figure=horizontal_stats, style={'height': "9vh"})
            # dcc.Graph(figure=sleep, style={'height': "4vh"}),
            # dcc.Graph(figure=sleep, style={'height': "4vh"}),
            # dcc.Graph(figure=sleep, style={'height': "4vh"})
            # horizontal_stats

        ], className="box1"),

        html.Div([
            "Box2", dcc.Graph(figure=gantt_diagram, style={'height': "40vh"}),

        ], className="box2"),

        html.Div([
                zanzibar_todo
        ], className="box4"),



        html.Div([
            "Box7",
            dcc.Graph(figure=sleep, style={'height': "3vh"}), html.Br(),
            dcc.Graph(figure=sleep, style={'height': "3vh"}), html.Br(),

            # slider2,
            # slider1, html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),html.Br(),html.Br(),html.Br(),
            # slider1, html.Br(), html.Br(), html.Br(), html.Br(),
            # slider1,
        ], className="box7"),
        # html.Div(["Box8"], className="box8"),
        # html.Div(["Box9"], className="box9"),
        # html.Div(["Box10"], className="box10"),

        # html.Div([
        #     "Box11",
        #     todo_name
        #     # "Box11", dcc.Graph(figure =  wellbeing, style={'height': "20vh"})
        # ], className="box11"),


        html.Div([
            "wellbeing index",
                html.Div([

                    interpolation_strats,

                    interpolation_strats,

                ],className = "nested"),
                html.Br(),  html.Br(), html.Br(), html.Br(),



                dcc.Graph(figure=wellbeing, style={'height': "20vh"}),

                  ], className="box15"),

        # html.Div(["Box16"], className="box16"),
        html.Div([
html.Div([
            task_name, task_start, task_stop, html.Button('Submit', id='submit-val', n_clicks=0),
            ],className="nested4"),
            zanzibar], className="box17"),

# html.Div(["Box16"]),
#     html.Div(["Box16"]),
#     html.Div(["Box16"]),
#     html.Div(["Box16"]),
#     html.Div(["Box16"]),
#     html.Div(["Box16"]),
#     html.Div(["Box16"]),
#




    ], className="wrapper")

], className="twelve columns")
