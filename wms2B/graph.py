import dash_core_components as dcc
import plotly.figure_factory as ff
import plotly.graph_objects as go
import dash_table
import pandas as pd
import numpy as np

solar_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]



x = np.arange(10)

wellbeing = go.Figure(data=go.Scatter(x=x, y=x**2))
wellbeing.update_layout(
    autosize=True,
    # width=500,
    margin=dict(
        l=0,
        r=10,
        b=0,
        t=10,
    ))

zanzibar = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in solar_df.columns],
    data=solar_df.to_dict('records'),
)

def wrapiefigure(labels, values, holes):
    return go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])

pie = wrapiefigure(labels, values, .4)
pie.update_layout(
    autosize=True,
    # width=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
    ),
    # paper_bgcolor="#ddd",
    showlegend=False,


)
# pie.update_layout(legend=dict(x=0, y=0))
pie.update_yaxes(automargin=True)

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

gantt_diagram = ff.create_gantt(df)
gantt_diagram.update_layout(autosize=True)
gantt_diagram["layout"].pop("height", None)
gantt_diagram["layout"].pop("width", None)

sleep = go.Figure()
sleep.add_trace(go.Bar(
    y=['sleep'],
    x=[3],
    name='SF Zoo',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
sleep.add_trace(go.Bar(
    y=['sleep'],
    x=[4],
    name='LA Zoo',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    ),
))
sleep.add_trace(go.Bar(
    y=['sleep'],
    x=[3],
    name='LA Zoo',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    ),
))
sleep.update_layout(barmode='stack', autosize=True,     margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
    ), showlegend=False,)


fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta", value = 220,
    domain = {'x': [0.1, 1], 'y': [0, 1]},
    title = {'text' :"<b>Profit</b>"},
    delta = {'reference': 200},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 300]},
        'threshold': {
            'line': {'color': "red", 'width': 2},
            'thickness': 0.75,
            'value': 280},
        'steps': [
            {'range': [0, 150], 'color': "lightgray"},
            {'range': [150, 250], 'color': "gray"}]}))
# fig.update_layout(height = 250)
# fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})


