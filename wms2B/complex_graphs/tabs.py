import dash_core_components as dcc
import dash_html_components as html
from wms2B.complex_graphs.gantt.ganttFigure import *
from wms2B.complex_graphs.other import fig
from datetime import datetime, timedelta
optionsList = {'Sleep': ['Sleep'], 'Work': ['Domestic', 'Paid', 'Job-Seeking'] , 'Study': ['Programming', 'Lectures', 'Books'], 'Exercise': ['Cardio', 'Resistance', "Stretch"], 'Routine': ['Breakfast', 'Lunch', 'Dinner', 'Commute'], 'Recreation': ['Travel', 'Socialize', 'Artistic & Creative'], 'Indulgence': ['YouTube & Music', 'Video games', 'Movies & TV shows', 'Music']}
names = list(optionsList.keys())
nestedOptions = optionsList[names[0]]

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

                        # dcc.Input(id='task_content', type='text', value="", style={"box-shadow": "0 0 2px 1px #666",'width': 100}),
                        # dcc.DatePickerSingle(
                        #     id='date-picker',
                        #     min_date_allowed=dt(curr_year, curr_month, curr_day),
                        #     max_date_allowed=dt(curr_year + 1, 1, 1),
                        #     initial_visible_month=dt(2017, 8, 5),
                        #     date=str(dt(curr_year, curr_month, curr_day))
                        # ),
                        dcc.Dropdown(
                            id='task_content',
                            options=[
                                {"label":name, "value":name} for name in names
                            ],
                            clearable=False,
                            value= list(optionsList.keys())[0],
                        style={'width': 120}),
                        dcc.Dropdown(
                            id='task_type',
                            options=[{'label': opt, 'value': opt} for opt in nestedOptions],
                            clearable=False,
                            value= nestedOptions[0],
                            # value= nestedOptions[0],
                            style={'width': 120}),
                        dcc.Input(id='task_start', type='text', value=datetime.now().strftime("%d/%m/%Y %H:%M"), style={'width': 100}),
                        dcc.Input(id='task_stop', type='text',
                                  value=(datetime.now() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M"), style={'width': 100}),
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