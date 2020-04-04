import datetime
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import plotly.graph_objects as go
import plotly
from plotly import __version__
print (__version__)
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from dash.dependencies import Input, Output
import random
from collections import deque
import apps



data_set_size = 10
productivity = np.random.randint(low=0, high=30, size=data_set_size)
date_list = [datetime.datetime.today() - datetime.timedelta(days=x) for x in range(data_set_size)]
dottedlines = {"background-color" : "#f7f7f7"}#{"border-style": "dotted"}
grey_color = {"paper_bgcolor": "#f7f7f7"}



productivity_time_series = dcc.Graph(
    id='line',
    figure={
        'data': [{'x': date_list, 'y': productivity, "line_color": "dimgray"} #"line": {"shape": "spline"}}
                 # 'mode': "markers", 'name': 'Trace 2'}

                 ],
        'layout': {
            'title': 'Actualization',
            "xaxis": {"title": "Week to Date"},
            "yaxis": {"title": "Productivity"},
            # "plot_bgcolor": "#f7f7f7",
           # "paper_bgcolor": "#f7f7f7",
            "height" : 400,
        }
    }
)

line_graph = dcc.Graph(id='live-graph', animate=False )
interval = dcc.Interval(id='graph-update',interval=1000,n_intervals=0)

newpie = dcc.Graph(
            id='graph',
            figure={
                'data': [{'values': [8, 10,2, 4], 'labels': ["sleep", "work", "recreation", "projects"], 'type': 'pie'}],
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    "height": 400,
                    "paper_bgcolor": "#f7f7f7", #mark
                    # 'legend': {'a': 0, 'y': 1}
                }
            }
        )

gauge = dcc.Graph(
    id = "gauge",
    figure = {
        "data" : [{'type': 'indicator','mode': 'gauge+number','value': 0.5}],
         "layout" : {'title': 'indicator', "height" : 150, "margin": {"t":0, "l":20,"r":20,"b":0}, "paper_bgcolor": "#f7f7f7",}#mark#,"font": {"font-size":"12px"}}
    }

)

indicator = dcc.Graph(
    id = "indicator",
    figure = {
        "data" : [{'type': 'indicator','mode': 'gauge+number+delta','value': 0.5, "gauge":{"shape":"bullet", "bar":{"color":"darkblue"}}}],
         "layout" : {'title': {"text": "mean", "font":{"size":"12"}, "x":"50%","y":"0.01%"}, "height" : "50", "margin": {"t":30, "l":80,"r":0,"b":0}, "paper_bgcolor": "#f7f7f7",}
    }

)






# pull is given as a fraction of the pie radius

# colorsettings = {"gradient":True,"ranges":{"red":[0,3],"yellow":[3,6],"green":[6,10]}}
productivity_gauge = daq.Gauge(id='prod', label="Productivity", value=8, showCurrentValue=True, units="Tasks/WEEK",
                               color="DodgerBlue", size=250, labelPosition="center")
integrity_gauge = daq.Gauge(id='intg', label="Integrity", value=4, showCurrentValue=True, units="completed:fail",
                            color="DodgerBlue", size=150, labelPosition="bottom")
ambition_gauge = daq.Gauge(id='amb', label="Ambition", value=6, showCurrentValue=True, units="start:end",
                           color="DodgerBlue", size=150, labelPosition="bottom")
selfrstr_gauge = daq.Gauge(id='selfrstr', label="Self-Restraint", value=2, showCurrentValue=True, units="metas",
                           color="DodgerBlue", size=150, labelPosition="bottom")
wellbeing_gauge = daq.Gauge(id='happy', label="Wellbeing", value=4, showCurrentValue=True, units="composite",
                            color="DodgerBlue", size=150, labelPosition="bottom")
wisdom_gauge = daq.Gauge(id='int', label="Wisdom", value=9, showCurrentValue=True, units="learn", color="DodgerBlue",
                         size=300, labelPosition="bottom")

index_page = html.Div([

    html.Div([
        html.Div([
            html.H2("Waterbuffalo Micromanagement v2.01"),
            html.Img(src="/assets/stock-icon.png"),
        ], className="banner", style={"textAlign": "center"}
        ),

        # , "box-shadow": "5px 0px 2px grey"}),
        html.Div([
            html.A(html.Button('Home', className='three columns button-primary'),
                   href='/'),
            html.A(html.Button('Todo list', className='three columns'),
                   href='/app1'),
            html.A(html.Button('Journal', className='three columns'),
                   href='/app2'),
            html.A(html.Button('New Page', className='three columns'),
                   href='/app3'),
        ], className="container", style={"textAlign": "center"}) ]),

        html.Br(),

        html.Div([

            html.Div([
                newpie
                #productivity_gauge
            ], className="four columns", style=dottedlines),
            html.Div([
                # productivity_time_series
                line_graph, interval
            ], className="eight columns", style=dottedlines),

            html.Div([
                html.Div([
                    html.H4("SECTOR 1"),
                    # productivity_gauge
                ], className="four columns", style=dottedlines),
                html.Div([
                    # html.Br(),
                    indicator,
                ], className="eight columns", style=dottedlines),
            ], className="twelve columns", style=dottedlines),

            # html.Div([
            #     gauge
            # ], className="three columns", style=dottedlines),#, style={'vertical-align': 'top'} ),

        ], className = "containerforward", style=dottedlines),
        html.Div([
            html.Div([
                "Productivity:",
                gauge,
                "Working ceaselessly to create ones values"
            ], className="two columns", style=dottedlines),
            html.Div([
                "Integrity:",
                gauge,
                "Consistent application of reason"
            ], className="two columns", style=dottedlines),
            html.Div([
                "Ambition:",
                gauge,
                "Pursuing one's own goals and desires"
            ], className="two columns", style=dottedlines),
            html.Div([
                "Self Restraint",
                gauge,
                "Moderation or voluntary self-control"
            ], className="two columns", style=dottedlines),
            html.Div([
                gauge
            ], className="two columns", style=dottedlines),
            html.Div([
                gauge
            ], className="two columns", style=dottedlines),

        ], className="containerforward", style=dottedlines),

        html.Div([],style=dottedlines)
])

#, style = {"background-color" : "#f7f7f7"})
        # html.Div([
        #     html.Div([productivity_gauge], style={"border-style": "dotted", "margin-bottom": "-75px"}),
        #     html.Div(["Working ceaselessly to create ones values"], className="body")
        # ], className="two columns", style={"border-style": "dotted"}),
        # html.Div([
        #     html.Div([integrity_gauge], style={"border-style": "dotted", "margin-bottom": "-75px"}),
        #     html.Div(["Consistent application of reason"], className="body")
        # ], className="two columns", style={"border-style": "dotted"}),
        # html.Div([
        #     html.Div([ambition_gauge], style={"border-style": "dotted", "margin-bottom": "-75px"}),
        #     html.Div(["Pursuing one's own goals and desires"], className="body")
        # ], className="two columns", style={"border-style": "dotted"}),
        # html.Div([
        #     html.Div([selfrstr_gauge], style={"border-style": "dotted", "margin-bottom": "-75px"}),
        #     html.Div(["Moderation or voluntary self-control"], className="body")
        # ], className="two columns", style={"border-style": "dotted"}),
        # html.Div([
        #     html.Div([wellbeing_gauge], style={"border-style": "dotted", "margin-bottom": "-75px"}),
        #     html.Div(["The basis of all virtue"], className="body")
        # ], className="two columns", style={"border-style": "dotted"}),
        # ], style={"background-color": "#f5f5f5"})  # , className = "container")#,style = {"border-style": "dotted" })
        #
        #


    # dcc.Link('Go to Page 1', href='/app1'),
    # html.Br(),
    # dcc.Link('Go to Page 2', href='/app2'),


