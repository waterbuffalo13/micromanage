import wms2B.complex_graphs.gantt_schedule as import_gantt_callbacks
from wms2B.app import app
from dash.dependencies import Input, Output, State
import pandas as pd
import dash
import datetime
from wms2B.dashboard import index_page
from wms2B import progress
from wms2B.db_conn import Database
from wms2B.data.task import Task

################################################
###TO-DO LIST
################################################


import_gantt_callbacks

p = Database(":memory:")

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/':
        return index_page
    if pathname == '/progress':
            return progress.progress_layout
    else:
        return '404'

@app.callback(Output("table", "data"),
              [Input('todo_submit', 'n_clicks')],
              [State('todo_content', 'value')])
def update_output(n_clicks, task_contents):

    # if n_clicks is  None and n_clicks <= 0:
    if (task_contents == ""):
        dash.exceptions.PreventUpdate()
        base = pd.read_sql("SELECT * FROM tasks", p.connection)
        return base.to_dict('records')
    else:

        # base = base.loc[:, ~base.columns.str.contains('^Unnamed')]
        created = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # task_data = [[created, task_contents]]

        p.execute("INSERT INTO tasks VALUES (?, ? ,?)", (created, task_contents, created))
        updated = pd.read_sql("SELECT * FROM tasks", p.connection)
        # updated = pd.read_sql("SELECT * FROM employees", p.connection)
        # updated.to_sql()
        # updated = pd.DataFrame(task_data, columns=['created_date', "task_contents"])
        # updated = base.append(updated, sort=False)
        # updated = updated[pd.notnull(updated["task_contents"])]
        # updated.to_csv("data/todolist.csv", index=False)

        return updated.to_dict('records')


@app.callback(Output("hidden_div", "figure"),
              [Input('table', 'data_previous'), Input("table", "data")],
              [State('table', 'data')])
def delete_from_todo(previous, data, current):
    current_df = pd.read_csv("data/todolist.csv")
    if previous is None:
        dash.exceptions.PreventUpdate()
        base = pd.read_sql("SELECT * FROM tasks", p.connection)
        return base.to_dict('records')
    else:
        for row in previous:
            if row not in current:
                x_row = row
                x_row_id = row["first"]
                p.execute("DELETE FROM tasks WHERE first = (:first)",{"first": x_row_id})
                current = pd.read_sql("SELECT * FROM tasks", p.connection)
                return current.to_dict('records')

@app.callback(
    [dash.dependencies.Output('task_type', 'options'), dash.dependencies.Output('task_type', 'value'),],
    [dash.dependencies.Input('task_content', 'value')]
)
def update_date_dropdown(name):
    optionsList = {'Sleep': ['Sleep'], 'Work': ['Domestic', 'Paid', 'Job-Seeking'],
                   'Study': ['Programming', 'Lectures', 'Books'], 'Exercise': ['Cardio', 'Resistance', "Stretch"],
                   'Routine': ['Morning', 'Lunchtime', 'Dinner', 'Commute'],
                   'Recreation': ['Travel', 'Socialize', 'Artistic & Creative'],
                   'Indulgence': ['YouTube & Music', 'Video games', 'Movies & TV shows', 'Music']}
    # names = list(optionsList.keys())
    # nestedOptions = optionsList[names[0]]

    return [{'label': i, 'value': i} for i in optionsList[name]], optionsList[name][0]
