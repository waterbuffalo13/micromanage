import dash_core_components as dcc
import plotly.figure_factory as ff
import plotly.graph_objects as go
import dash_html_components as html
import dash_daq as daq
import dash_table
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Use `y` argument instead of `x` for horizontal histogram

line_chart = go.Figure(data=[go.Scatter(x=[1, 2, 3,4,5,6,7,8,9,10,11,12], y=[1, 2, 5,8,10,11,13,16,18,19,20,19], mode='lines',  line=dict(color='royalblue', width=1))])
line_chart.update_layout(
    margin = dict(
        l=0,
        r=0,
        b=0,
        t=40,

    ),
    autosize=True,
    title="Actualization Index",
    # mode="lines",
)


task_distribution = go.Figure(data=[go.Histogram(y=np.random.randn(500))])
task_distribution.update_layout(

    margin = dict(
        l=0,
        r=0,
        b=0,
        t=0,
    ),
    autosize=True,
)

personality = go.Figure(data=go.Scatterpolar(
  r=[6, 3, 2, 3, 1],
  theta=['PROD','INTGR','SELF_R', 'AMB', 'WIS'],
  fill='toself'
))

personality.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False,
    margin = dict(
        l=40,
        r=40,
        b=0,
        t=0,
    ),
    autosize=True,
)

schedule_data = {'Index': ['timestamp', 'Second value', "third value", "fourth value"], #, "third value", "fourth value",  "third value", "fourth value"],
                 'content': ['First value', 'Second value',  "third value", "fourth value"],#"third value", "fourth value",  "third value", "fourth value"],
                 'start': ['First value', 'Second value',  "third value", "fourth value"],  #"third value", "fourth value",  "third value", "fourth value"],
                 'stop': ['First value', 'Second value',  "third value", "fourth value"]  #"third value", "fourth value",  "third value", "fourth value"],
                 }
#
schedule_data = {'Index': ['timestamp', 'Second value', "third value", "fourth value", "third value", "fourth value",  "third value", "fourth value"],
                 'content': ['First value', 'Second value',  "third value", "fourth value","third value", "fourth value",  "third value", "fourth value"],
                 'start': ['First value', 'Second value',  "third value", "fourth value", "third value", "fourth value",  "third value", "fourth value"],
                 'stop': ['First value', 'Second value',  "third value", "fourth value", "third value", "fourth value",  "third value", "fourth value"],
                 }

schedule_df = pd.DataFrame(schedule_data)

todo_data = {'Index': ['1', '2','3','4','5','6'],
             'content': ['Finish up waterbuffalo micromanagement', 'take up yoga','go to the clubs','have a good time','develop relationships', 'write papers'],
             }

todo_df = pd.DataFrame(todo_data)

virtue_data = {
    'Index': ["timestamp",    'wellbeing avg',  'wellbeing_stdv', 'prod_cap','rel-inter', 'domain', 'relex'], #, "third value", "fourth value",  "third value", "fourth value"],
    'row1': ['3.81','2.42','213','431','clunker','strat','dawg'], #, '2.61',  "3.2", "fourth value"],#"third value", "fourth value",  "third value", "fourth value"],
                 }

virtue_df = pd.DataFrame(virtue_data)

auto_data = {
    'Index': ["SLEEP",    'DIET',  'wellbeing_stdv', 'prod_cap','rel-inter', 'domain', 'relex'], #, "third value", "fourth value",  "third value", "fourth value"],
    'row1': ['3.81','2.42','213','431','clunker','strat','dawg'], #, '2.61',  "3.2", "fourth value"],#"third value", "fourth value",  "third value", "fourth value"],
                 }

labels = ['Sleep', 'Recr', 'Work', 'Waste']
values = [8*60, 4*60, 3*60, 9*60]

x = np.arange(10)

wellbeing = go.Figure(data=go.Scatter(x=x, y=x ** 2))
wellbeing.update_layout(
    autosize=True,
    # width=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
    ))

zanzibar = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in schedule_df.columns],
    data=schedule_df.to_dict('records'),
    row_deletable=True,
)

zanzibar_todo = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in todo_df.columns],
    data=todo_df.to_dict('records'),
    row_deletable=True,
)

virtue_table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in virtue_df.columns],
    data=virtue_df.to_dict('records'),
    # row_deletable=True,
)


def wrapiefigure(labels, values, holes):
    return go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4, textinfo='label+percent',  automargin=False)])


pie = wrapiefigure(labels, values, .4)
pie.update_layout(
    autosize=True,
    # width=500,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=10,
    ),
    # paper_bgcolor="#ddd",
    paper_bgcolor="white",
    showlegend=False,

)
# pie.update_layout(legend=dict(x=0, y=0))
pie.update_yaxes(automargin=True)

df = [
    # dict(Task="Sleep", Start='2020-04-01 ', Finish='2020-04-01 09:30'),
    dict(Task="Break", Start='2020-04-01 09:30', Finish='2020-04-01 10:30'),
    dict(Task="Program", Start='2020-04-01 10:30', Finish='2020-04-01 12:30'),
    dict(Task="Break", Start='2020-04-01 12:30', Finish='2020-04-01 13:30'),
    dict(Task="Timex", Start='2020-04-01 13:30', Finish='2020-04-01 15:30'),
    dict(Task="Netflix", Start='2020-04-01 15:30', Finish='2020-04-01 18:00'),
    dict(Task="Program", Start='2020-04-01 18:30', Finish='2020-04-01 20:00'),
    dict(Task="Treat", Start='2020-04-01 20:00', Finish='2020-04-01 23:00'),


      ]
# df_new = pd.read_csv(r"C:\Users\Patrick\Desktop\wms2\wms2A\apps\todolist.csv")

gantt_diagram = ff.create_gantt(df, group_tasks=True)
gantt_diagram.update_layout(autosize=True, margin=dict(
    l=10,
    r=10,
    b=10,
    t=0,
), )
gantt_diagram["layout"].pop("height", None)
gantt_diagram["layout"].pop("width", None)

sleep = go.Figure()
sleep.add_trace(go.Bar(
    y=[''],
    x=[8],
    name='SF Zoo',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 1)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
sleep.add_trace(go.Bar(
    y=[''],
    x=[8],
    name='LA Zoo',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 1)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    ),
))
sleep.add_trace(go.Bar(
    y=[''],
    x=[8],
    name='SF Zoo',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 1)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))

sleep.update_layout(barmode='stack', autosize=True, margin=dict(
    l=0,
    r=0,
    b=0,
    t=0,
), showlegend=False, title="test",
                 paper_bgcolor="#ddd",

                    )

fig = go.Figure(go.Indicator(
    mode="gauge", value=7,
    domain={'x': [0.1, 1], 'y': [0.5, 1]},
    title={'text': "Day"},
    # delta={'reference': 200},
    gauge={
        'shape': "bullet",
        'axis': {'range': [None, 24]}
        # 'threshold': {
        #     'line': {'color': "red", 'width': 2},
        #     'thickness': 0.75,
        #     'value': 280}
        ,
        # 'steps': [
        #     {'range': [0, 150], 'color': "lightgray"},
        #     {'range': [150, 250], 'color': "gray"}]
    }))

fig.update_layout(
    autosize=True, margin=dict(
    l=0,
    r=0,
    b=10,
    t=0,
)

                    )

task_name = dcc.Input(id='task_content', type='text', value="name")
task_start = dcc.Input(id='task_start', type='text', value="start")
task_stop = dcc.Input(id='task_stop', type='text', value="stop")
task_group = dcc.Input(id='task_stop', type='text', value="group")
submit_tasks = html.Button('Submit', id='submit-val', n_clicks=0),

todo_name = dcc.Input(id='task_content', type='text', value="name")
submit_todo = html.Button('Submit', id='submit-val', n_clicks=0),

journal_content = dcc.Textarea(
    id="journal_content",
    placeholder="What's on your mind?",
    # value='This is a TextArea component',
    style={'width': '100%', 'height': '300px'}
)

horizontal_stats = go.Figure(go.Bar(
    x=[20, 14, 23],
    y=['work', 'sleep', 'recr'],
    orientation='h',

))
horizontal_stats.update_layout(
    margin=dict(
        l=0,
        r=10,
        b=10,
        t=10,
    ),
    paper_bgcolor="#ddd",

)

slider1 = daq.Slider(
    id='my-daq-slider',
    value=40,
    min=0,
    max=100,
    step=10,
    color=dict(default="grey"),
    size=100
    # targets={"25": {"label": "TARGET"}}
)

slider2 = daq.Gauge(
    id='my-daq-gauge',
    min=0,
    max=10,
    value=6,
    size=100
)

interpolation_strats = dcc.Dropdown(
    id='demo-dropdown',
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='NYC'
)

mockup_gauge= daq.Gauge(
    color="#9B51E0",
    value=2,
    label='Default2',
    max=10,
    min=0,
    size=60,

)


tank = daq.Tank(
    value=3,
    width=20,
    height= 200,
    label='Index',
    labelPosition='bottom',
    style={'margin-left': '5%', "margin-top":"10%"},
    color="red",
)

# fig.update_layout(height = 250)
# fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})
