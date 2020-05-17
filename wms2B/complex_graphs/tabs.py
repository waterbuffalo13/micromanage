import dash_core_components as dcc
import dash_html_components as html
from wms2B.complex_graphs.gantt.ganttFigure import *
from wms2B.complex_graphs.other import fig
from datetime import datetime, timedelta

tabs = html.Div([
    dcc.Tabs(id='tabs-example', value='Schedule', children=[

        dcc.Tab(className="tabs-individual", label='Schedule', value='Schedule',
                style={'borderBottom': '1px solid #d6d6d6', 'padding': '6px', 'fontWeight': 'bold'},
                selected_style={'borderBottom': '1px solid #d6d6d6',
                                'padding': '6px',
                                'fontWeight': 'bold'},
                children = [
                    html.Div(
                        ["Today's Schedule"],
                        style={"text-align": "center", "font-size": "150%"}),
                    dcc.Graph(id="gantt_chart", figure=gantt_diagram, style={'height': "35vh"}),
                    dcc.Graph(figure=fig, style={'height': "4vh"}),
                    html.Br(),
                    html.Div([

                        dcc.Input(id='task_content', type='text', value="", style={"box-shadow": "0 0 2px 1px #666"}),
                        # dcc.DatePickerSingle(
                        #     id='date-picker',
                        #     min_date_allowed=dt(curr_year, curr_month, curr_day),
                        #     max_date_allowed=dt(curr_year + 1, 1, 1),
                        #     initial_visible_month=dt(2017, 8, 5),
                        #     date=str(dt(curr_year, curr_month, curr_day))
                        # ),
                        # dcc.Dropdown(
                        #     id='demo-dropdown',
                        #     options=[
                        #         {'label': '1', 'value': 1},
                        #         {'label': '2', 'value': 2},
                        #         {'label': '3', 'value': 3},
                        #         {'label': '4', 'value': 4},
                        #         {'label': '5', 'value': 5},
                        #         {'label': '6', 'value': 6},
                        #         {'label': '7', 'value': 7},
                        #         {'label': '8', 'value': 8},
                        #         {'label': '9', 'value': 9},
                        #         {'label': '10', 'value': 10},
                        #         {'label': '11', 'value': 11},
                        #         {'label': '12', 'value': 12},
                        #         {'label': '13', 'value': 13},
                        #         {'label': '14', 'value': 14},
                        #         {'label': '15', 'value': 15},
                        #         {'label': '16', 'value': 16},
                        #         {'label': '17', 'value': 17},
                        #         {'label': '18', 'value': 18},
                        #         {'label': '19', 'value': 19},
                        #         {'label': '20', 'value': 20},
                        #         {'label': '21', 'value': 21},
                        #         {'label': '22', 'value': 22},
                        #         {'label': '23', 'value': 23},
                        #         {'label': '24', 'value': 24}
                        #     ],
                        #     value=''
                        # ),
                        dcc.Input(id='task_start', type='text', value=datetime.now().strftime("%d/%m/%Y %H:%M"), ),
                        dcc.Input(id='task_stop', type='text',
                                  value=(datetime.now() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")),
                        html.Button('Submit', id='submit-schedule', n_clicks=0),
                    ], className="addtoschedule"),



            ]),
        dcc.Tab(label='Retro-Schedule', value='Performance', style={'borderBottom': '1px solid #d6d6d6',
                                                                    'padding': '6px',
                                                                    'fontWeight': 'bold'},
                selected_style={'borderBottom': '1px solid #d6d6d6',
                                'padding': '6px',
                                'fontWeight': 'bold'}),
        dcc.Tab(label='Mood and Energy', value='Wisdom', style={'borderBottom': '1px solid #d6d6d6',
                                                                'padding': '6px',
                                                                'fontWeight': 'bold'},
                selected_style={'borderBottom': '1px solid #d6d6d6',
                                'padding': '6px',
                                'fontWeight': 'bold'}),
        dcc.Tab(label='Journal', value='Energy', style={'borderBottom': '1px solid #d6d6d6',
                                                        'padding': '6px',
                                                        'fontWeight': 'bold'},
                selected_style={'borderBottom': '1px solid #d6d6d6',
                                'padding': '6px',
                                'fontWeight': 'bold'}),
        dcc.Tab(label='Diet Planner', value='Weight', style={'borderBottom': '1px solid #d6d6d6',
                                                             'padding': '6px',
                                                             'fontWeight': 'bold'},
                selected_style={'borderBottom': '1px solid #d6d6d6',
                                'padding': '6px',
                                'fontWeight': 'bold'}),

    ]),

])