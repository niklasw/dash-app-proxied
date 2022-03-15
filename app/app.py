
import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go
import plotly.express as px


app = dash.Dash('testing')   #initialising dash app
df = px.data.stocks() #reading stock price dataset

def stock_prices():
    # Function for creating line chart showing Google stock prices over time
    y=df['GOOG']
    fig = go.Figure([go.Scatter(x = df['date'], y = y,\
                     line = dict(color = 'firebrick', width = 4), name = 'Google')
                     ])
    fig.update_layout(title = 'Prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices')
    with open('/data/test.txt','a') as fp:
        fp.write(f'{y}\n')
    return fig


app.layout = html.Div(id = 'parent', children = [ \
    html.H1(id = 'h1', \
            children = 'Styling using html components and CSS', \
            className = 'title'), \
    dcc.Graph(id = 'line_plot', figure = stock_prices())])

if __name__ == '__main__': 
    app.run_server(host='0.0.0.0',debug=True, port=8080)
