import dash_html_components as html

index_page = html.Div([

        html.Div([
            html.H5("Waterbuffalo Micromanagement v2.01"),
        ], className="banner", style={"textAlign": "center"}),

        html.Div([
            html.Div(["Box1"], className = "box1"),
            html.Div(["Box2"], className = "box2"),
            html.Div(["Box3"], className = "box3"),
            html.Div(["Box4"], className = "box4"),
        ], className="wrapper")





    ],className = "twelve columns")