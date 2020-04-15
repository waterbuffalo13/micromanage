import dash_html_components as html
from wms2B.graph import *


index_page = html.Div([

        html.Div([
            html.H5("Waterbuffalo Micromanagement v2.01"),
        ], className="banner", style={"textAlign": "center"}),

        html.Div([

            html.Div([
                "Box1"
                , dcc.Graph(figure=pie, style={'height': "30vh"}, ),
                dcc.Graph(figure=horizontal_stats, style={'height': "10vh"})
                # dcc.Graph(figure=sleep, style={'height': "4vh"}),
                # dcc.Graph(figure=sleep, style={'height': "4vh"}),
                # dcc.Graph(figure=sleep, style={'height': "4vh"})
                # horizontal_stats

            ], className = "box1"),

            html.Div([
                  "Box2", dcc.Graph(figure = gantt_diagram, style={'height': "40vh"}),


            ], className = "box2"),

            html.Div(["Box3 - Todo list",
                      zanzibar
                      ], className = "box3"),
            html.Div(["Box4"], className = "box4"),
            html.Div(["Box5"], className = "box5"),

            html.Div([
                "Box6",
            ],className="box6", ),
            html.Div([
                # "Box7",

                 dcc.Graph(figure = horizontal_stats, style={'height': "10vh"})
            ], className="box7"),
            # html.Div(["Box8"], className="box8"),
            # html.Div(["Box9"], className="box9"),
            # html.Div(["Box10"], className="box10"),

            html.Div([
                "Box11"
                # "Box11", dcc.Graph(figure =  wellbeing, style={'height': "20vh"})
            ], className="box11"),
            html.Div(["Box12"], className="box12"),
            html.Div(["Box13"], className="box13"),
            html.Div(["Box14"], className="box14"),
            html.Div(["Box15"], className="box15"),

            html.Div(["Box16"], className="box16"),
            html.Div(["Box17"], className="box17"),
            html.Div(["Box18"], className="box18"),
            html.Div(["Box19", journal_content], className="box19"),
            html.Div(["Box20",zanzibar], className="box20"),

            html.Div([
               # "Box21", html.P(children = "", id="rolex"),
               #  task_name, task_start, task_stop
task_name, task_start, task_stop
            ], className="box21"),
            html.Div(["Box22",
                      # zanzibar

                      ], className="box22"),
            html.Div(["Box23"], className="box23"),
            html.Div(["Box24"], className="box24"),
            html.Div(["Box25"], className="box25"),


            html.Div(["Box26"], className="box26"),
            html.Div(["Box27"], className="box27"),
            html.Div(["Box28"], className="box28"),
            html.Div(["Box29"], className="box29"),
            html.Div(["Box30"], className="box30"),

            html.Div(["Box31"], className="box31"),
            html.Div(["Box32"], className="box32"),
            html.Div(["Box33"], className="box33"),
            html.Div(["Box34"], className="box34"),
            html.Div(["Box35"], className="box35"),

            html.Div(["Box36"], className="box36"),
            html.Div(["Box37"], className="box37"),
            html.Div(["Box38"], className="box38"),
            html.Div(["Box39"], className="box39"),
            html.Div(["Box40"], className="box40"),

            html.Div(["Box41"], className="box41"),
            html.Div(["Box42"], className="box42"),
            html.Div(["Box43"], className="box43"),
            html.Div(["Box44"], className="box44"),
            html.Div(["Box45"], className="box45"),

            html.Div(["Box46"], className="box46"),
            html.Div(["Box47"], className="box47"),
            html.Div(["Box48"], className="box48"),
            html.Div(["Box49"], className="box49"),
            html.Div(["Box50"], className="box50"),

        ], className="wrapper")





    ],className = "twelve columns")