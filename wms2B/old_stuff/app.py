import dash
from dash.dependencies import Input, Output

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index_page
    # if pathname == '/app1':
    #     return financials.page_1_layout
    # elif pathname == '/app2':
    #     return data_analysis.page_2_layout
    # elif pathname == '/app3':
    #     return correlations.page_3_layout
    else:
        return '404'



# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])