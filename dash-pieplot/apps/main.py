#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from app import app
from datetime import datetime as dt

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_ebola.csv')
df = df.dropna(axis=0)

if 'DYNO' in os.environ:
    app_name = os.environ['DASH_APP_NAME']
else:
    app_name = 'dash-pieplot'


#mine
layout = html.Div([
    html.Div([html.H1("Ebola Cases Reported in Africa - 2014")], style={"textAlign": "center"}),
    dcc.Dropdown(id='month-selected',
        options=[
            {'label': "March", 'value': 3}, {'label': "April", 'value': 4},{'label': "May", 'value': 5},
            {'label': "June", 'value': 6},{'label': "July", 'value': 7},{'label': "August", 'value': 8},
            {'label': "September", 'value': 9},{'label': "October", 'value': 10},{'label': "November", 'value': 11},
            {'label': "December", 'value': 12}
        ],
        value=3,
    ),

    dcc.Graph(id="my-graph"),  
], className="container")



@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("month-selected", "value")]
)
def update_graph(selected):
    
    if df[df["Month"] == selected]["Value"].empty:
        return {
        "data": [go.Pie(labels=['Country Not Found'], values=[404],
                        marker={'colors': ['#000000']}, textinfo='none')],
        "layout": go.Layout(title="No Data to Display", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}
    
    else:
        return {
        "data": [go.Pie(labels=df["Country"].unique().tolist(), values=df[df["Month"] == selected]["Value"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title="Cases Reported Monthly", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}
        
