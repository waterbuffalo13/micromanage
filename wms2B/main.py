from dash.dependencies import Input, Output, State
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from wms2B.dashboard import index_page
import dash
import datetime
import plotly.figure_factory as ff
from wms2B.__init__ import app
import wms2B.functions
from wms2B.data.task import Task
from wms2B.db_conn import Database

if __name__ == '__main__':
    # p = Database(":memory:")
    # emp_1 = Employee('Jake', 'Williams', '80,000.00')
    # emp_2 = Employee('Django', 'Henry', '68,000.00')
    # p.cursor.execute("""CREATE TABLE employees (
    #             first text,
    #             last text,
    #             pay real
    #     )""")
    # p.execute("INSERT INTO employees VALUES (?, ? ,?)", (emp_1.first, emp_1.last, emp_1.pay))
    # p.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
    #           {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})


    app.run_server(debug=True, threaded =False)

