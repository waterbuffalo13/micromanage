import dash_html_components as html
from wms2B.graph import *

index_page = html.Div([

    html.Div([
        html.H5("Waterbuffalo Micromanagement v2.01"),
    ], className="banner", style={"textAlign": "center"}),

    html.Div([

        html.Div([
            "Box1",
            dcc.Graph(figure=pie, style={'height': "20vh"}),
            dcc.Graph(figure=horizontal_stats, style={'height': "9vh"})
        ], className="piechart"),

        html.Div([
            "Box2",
            dcc.Graph(figure=gantt_diagram, style={'height': "40vh"}),
        ], className="ganttchart"),

        html.Div([
            "To do list",
            zanzibar_todo
        ], className="todolist"),

        html.Div([
            "Box4",
            dcc.Graph(figure=sleep, style={'height': "3vh"}), html.Br(),
            dcc.Graph(figure=sleep, style={'height': "3vh"}), html.Br(),

        ], className="sleepstats"),

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
            # "next box",
html.Div([
            html.Div([mockup_gauge],className="three columns", style ={"border":"#333 1px solid"}),
            html.Div([mockup_gauge], className="three columns", style={"border": "#333 1px solid"}),
            html.Div([mockup_gauge], className="three columns", style={"border": "#333 1px solid"}),
            html.Div([mockup_gauge], className="three columns", style={"border": "#333 1px solid"}),
], className="twelve columns", style={"border": "#333 1px solid"}),
html.Div([
            html.Div([mockup_gauge], className="three columns", style={"border": "#333 1px solid"}),
            html.Div([mockup_gauge], className="three columns", style={"border": "#333 1px solid"}),
            html.Div([mockup_gauge], className="three columns", style={"border": "#333 1px solid"}),
            html.Div([mockup_gauge], className="three columns", style={"border": "#333 1px solid"}),
], className="twelve columns", style={"border": "#333 1px solid"}),
        ], className="nextbox"),
        html.Div([
            "n2 box"
        ], className="n2box"),
        html.Div([
            "n3 box",
        ], className="n3box"),

], className="wrapper"),




], className="twelve columns")
