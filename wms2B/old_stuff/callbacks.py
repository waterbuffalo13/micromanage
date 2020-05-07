from datetime import datetime
from dash.dependencies import Input, Output, State
from wms2B.index import index_page
from wms2B.main import app
import pandas as pd
from wms2B.main import *


# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/':
#         return index_page
#     # if pathname == '/app1':
#     #     return financials.page_1_layout
#     # elif pathname == '/app2':
#     #     return data_analysis.page_2_layout
#     # elif pathname == '/app3':
#     #     return correlations.page_3_layout
#     else:
#         return '404'

@app.callback(Output("table", "data"),
                [Input('todo_submit', 'n_clicks')],
                [State('todo_content', 'value')])

def update_output(n_clicks, task_contents):
    # read from database
    base = pd.read_csv("../todolist.csv")
    # remove all redundant columns
    base = base.loc[:, ~base.columns.str.contains('^Unnamed')]
    # convert the created data from the input into a specific datetime format
    created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # attempt to parse the date picker as an input
    # stor
    task_data = [[created, task_contents]]
    updated = pd.DataFrame(task_data, columns=['created_date', "task_contents"])
    updated = base.append(updated, sort=False)
    # updated = updated.dropna()
    updated = updated[pd.notnull(updated["task_contents"])]
    updated.to_csv("todolist.csv", index=False)
    return updated.to_dict('records')