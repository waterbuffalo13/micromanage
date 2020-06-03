import plotly.figure_factory as ff
import dash_html_components as html
import dash_core_components as dcc

df = [dict(Task="Employment Seeking", Start='2020-06-03', Finish='2020-09-03'),
      dict(Task="Startup", Start='2020-02-26', Finish='2021-03-24'),
      dict(Task="Campervan Dream", Start='2020-03-01', Finish='2021-01-01'),
      dict(Task="stress test", Start='2020-02-24', Finish='2021-02-29')]

fig = ff.create_gantt(df)


# "border-style": "dotted",233
progress_layout = html.Div([
    html.Div([
        dcc.Graph(id="gantt_future", figure = fig#, style={'height': "35vh"}
                  ),

    ])



])