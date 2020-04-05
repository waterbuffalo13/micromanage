import dash_html_components as html

index_page = html.Div([

        html.Div([
            html.H5("Waterbuffalo Micromanagement v2.01"),
        ], className="banner", style={"textAlign": "center", "border-style": "dotted"}),

        # html.Div(["take it easy"],className = "four columns", style = {"background-color":"#f4f4f4"}),
        # html.Div(["take it easy"],className = "four columns", style = {"background-color":"#f4f4f4"}),
        # html.Div(["take it easy"],className = "four columns", style = {"background-color":"#f4f4f4"}),

        html.Div(["take it easy"], className="two columns", style={"background-color": "#f4f4f4"}),
        html.Div(["take it easy"], className="five columns", style={"background-color": "#f4f4f4"}),
        html.Div(["take it easy"], className="two columns", style={"background-color": "#f4f4f4"}),
        html.Div(["take it easy"], className="two columns", style={"background-color": "#f4f4f4"}),
        html.Div(["easy"], className="one columns", style={"background-color": "#f4f4f4"}),


    ],className = "twelve columns", style = {"border-style": "dotted"})