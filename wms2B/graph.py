import dash_core_components as dcc
import plotly.figure_factory as ff

piechart = dcc.Graph(
    id="pie_chart",
    figure={
        'data': [
            {'values': [8, 10, 2, 4], 'labels': ["sleep", "work", "recreation", "projects"], 'type': 'pie'}],
    }
)

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

fig = ff.create_gantt(df)
fig["layout"].pop("height", None)
fig["layout"].pop("width", None)