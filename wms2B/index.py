import dash_html_components as html
from wms2B.graph import *

index_page = html.Div([

        html.Div([
            html.H5("Waterbuffalo Micromanagement v2.01"),
        ], className="banner", style={"textAlign": "center"}),

        html.Div([

            html.Div([
                dcc.Graph(figure=pie)
            ], className = "box1"),

            html.Div([
                 dcc.Graph(figure = gantt_diagram)
            ], className = "box2"),

            html.Div(["Box3"], className = "box3"),
            html.Div(["Box4"], className = "box4"),
            html.Div(["Box5"], className = "box5"),

            html.Div(["Box6"], className="box6"),
            html.Div([
               # dcc.Graph(figure=sleep)
            ], className="box7"),
            html.Div(["Box8"], className="box8"),
            html.Div(["Box9"], className="box9"),
            html.Div(["Box10"], className="box10"),

            html.Div([
                # dcc.Graph(figure=fig)
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


        ], className="wrapper")





    ],className = "twelve columns")