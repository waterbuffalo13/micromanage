import dash_html_components as html
from wms2B.graph import *

index_page = html.Div([

        html.Div([
            html.H5("Waterbuffalo Micromanagement v2.01"),
        ], className="banner", style={"textAlign": "center"}),

        html.Div([

            html.Div([
                "Box1"
                # "Box1", dcc.Graph(figure=pie, style={'height': "17.5vh"})
            ], className = "box1"),

            html.Div([
                "Box2"
                 # "Boax2", dcc.Graph(figure = gantt_diagram, style={'height': "40vh"})
            ], className = "box2"),

            html.Div(["Box3"], className = "box3"),
            html.Div(["Box4"], className = "box4"),
            html.Div(["Box5"], className = "box5"),

            html.Div([
                "Box6"
                # dcc.Graph(figure=sleep, style={'height': "2vh"}), "Box 6"
            ],className="box6"),
            html.Div([
               "Box7",# dcc.Graph(figure=sleep)
            ], className="box7"),
            html.Div(["Box8"], className="box8"),
            html.Div(["Box9"], className="box9"),
            html.Div(["Box10"], className="box10"),

            html.Div([
                "Box11"# dcc.Graph(figure=fig)
            ], className="box11"),
            html.Div(["Box12"], className="box12"),
            html.Div(["Box13"], className="box13"),
            html.Div(["Box14"], className="box14"),
            html.Div(["Box15"], className="box15"),

            html.Div(["Box16"], className="box16"),
            html.Div(["Box17"], className="box17"),
            html.Div(["Box18"], className="box18"),
            html.Div(["Box19"], className="box19"),
            html.Div(["Box20"], className="box20"),

            html.Div(["Box21"], className="box21"),
            html.Div(["Box22"], className="box22"),
            html.Div(["Box23"], className="box23"),
            html.Div(["Box24"], className="box24"),
            html.Div(["Box25"], className="box25"),

            html.Div(["Box26"], className="box26"),
            html.Div(["Box27"], className="box27"),
            html.Div(["Box28"], className="box28"),
            html.Div(["Box29"], className="box29"),
            html.Div(["Box30"], className="box30"),


        ], className="wrapper")





    ],className = "twelve columns")