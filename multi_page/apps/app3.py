import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt, datetime, timedelta
import plotly.figure_factory as ff


df = [dict(Task="Fasanara", Start='2020-01-26', Finish='2020-02-24'),
      dict(Task="Method", Start='2020-02-26', Finish='2021-03-24'),
      dict(Task="WMS", Start='2020-03-01', Finish='2021-01-01'),
      dict(Task="stress test", Start='2020-02-24', Finish='2021-02-29')]

fig = ff.create_gantt(df)

#"border-style": "dotted",
page_3_layout = html.Div([
    html.Div([
    ], className = "two columns", style = { "border-style": "dotted", "background": "green", "height": "100%", "position":"absolute", "background-image" : "url(assets/sidebar.png)", "width":"15%"}),
    html.Div([
        "Howdy ho"
    ], className="ten columns", style={"border-style": "dotted", "background": "blue", "height": "100%"})

#     html.Div([
#         html.Div([
#             html.H2("Waterbuffalo Micromanagement v2.01"),
#             html.Img(src="/assets/stock-icon.png")], className="banner", style={"textAlign": "center"}),
#         # , "box-shadow": "5px 0px 2px grey"}),
#         html.Div([
#             html.A(html.Button('Home', className='three columns'),
#                    href='/'),
#             html.A(html.Button('Todo list', className='three columns'),
#                    href='/app1'),
#             html.A(html.Button('Journal', className='three columns'),
#                    href='/app2'),
#             html.A(html.Button('EXT2', className='three columns'),
#                    href='/app3'),
#         ], className="container", style={"textAlign": "center"})
#
#     ], style={"background-color": "#f5f5f5"}),
# html.Br(),
# html.Br(),
#         html.H1('Achievements Panel'),
# html.Div([
#         html.Div([
#             dcc.Graph(figure=fig, id='gantt-id'),
#             html.Div([html.H6('An ideal future')],style={"textAlign": "center"}),
#             "In the future I would like to be a person who lives the best life he can every day. "
#             "He would be deeply productive and creative, focusing on pursuits such as programming over television and games. "
#             "This person would be successful in the world in his personal career and in my work life."
#             "In the short-term, I would like to get my bases in check namely completing university and "
#             "getting a job as a data analyst. This allows me to be self-sufficient and affords me the "
#             "opportunity to make new friends, go on adventures and eventually work towards buying a house. \n"
#             "After gaining these essentials, the next stage is to place emphasis on making friends at work "
#             "and going on adventures. After that I would want to focus on building my skills in data analysis "
#             "which would include Python, R, SQL etc.",
#             "Alongside building my career skills, I would like to improve my knowledge of web/software development and Skyrim modding."
#             "I would like to continue working on WaterBuffalo Micromanagement "
#             "and making lots of important tools that I can use in my everyday life. "
#             "I would also like to be popular on social media."
#          ], className = "container"),
#         dcc.RadioItems(
#             id='page-2-radios',
#             options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
#             value='Orange'
#         ),
#         html.Div(id='page-2-content'),
#         html.Br(),
#         dcc.Link('Go to Page 1', href='/app1'),
#         html.Br(),
#         dcc.Link('Go back to home', href='/')
#         ])
])