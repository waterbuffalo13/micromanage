import plotly.figure_factory as ff
import dash_html_components as html
import dash_core_components as dcc

#Overall Gantt
df = [dict(Task="Gain Employment", Start='2020-06-03', Finish='2020-09-03'),

      dict(Task="MVP Development", Start='2020-06-03', Finish='2020-12-31'),
      dict(Task="MVP Deployment", Start='2021-01-01', Finish='2021-04-30'),

      dict(Task="Rent Accommodation", Start='2021-04-30', Finish='2021-12-31'),


      ]

#Waterbuffalo Gantt
df_new = [
    dict(Task="MVP Development", Start='2020-06-03', Finish='2020-12-31'),
]

fig = ff.create_gantt(df)


# "border-style": "dotted",233
progress_layout = html.Div([
    html.Div([
        dcc.Graph(id="gantt_future", figure = fig, style={'width': "100vh"}
                  ),

    ])



])