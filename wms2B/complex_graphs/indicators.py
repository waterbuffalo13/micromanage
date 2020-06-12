import dash_html_components as html
import dash_daq as daq

indicators=                html.Div([
                    html.Div([
                        daq.LEDDisplay(
                            label="SLEEP",
                            labelPosition='bottom',
                            id='my-daq-leddisplay',
                            value="6.43",
                            size=10,
                            backgroundColor="#f5f5f5",
                            color="red"
                        ),

                    ], className="three columns"),
                    html.Div([
                        daq.LEDDisplay(
                            label="EAT",
                            labelPosition='bottom',
                            id='my-daq-leddisplay',
                            value="3000",
                            size=10,
                            backgroundColor="#f5f5f5",
                            color="green"
                        ),

                    ], className="three columns"),
                    html.Div([
                        daq.LEDDisplay(
                            label="WORK",
                            labelPosition='bottom',
                            id='my-daq-leddisplay',
                            value="5.14",
                            size=10,
                            backgroundColor="#f5f5f5",
                            color="green"
                        ),

                    ], className="three columns"),
                    html.Div([
                        daq.LEDDisplay(
                            label="",
                            labelPosition='bottom',
                            id='my-daq-leddisplay',
                            value="3.14159",
                            size=10,
                            backgroundColor="#f5f5f5",
                            color="green"
                        ),

                    ], className="three columns"),

                ], className="twelve columns")