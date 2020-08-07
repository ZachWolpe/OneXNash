# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
from os import listdir

from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



# ----- Import Data -----x
path = '../data/'
dirs = listdir(path)

tyger = pd.read_csv(path + dirs[0])




sub = tyger['BudgetLOB'].value_counts()
pd.DataFrame(sub,)
frame = {'group': sub.index, 'freq': sub.values}
sub = pd.DataFrame(frame)



# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


fig = px.bar(sub, x="group", y="freq", color="group", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Nashua'),

    html.Div(children='''
        Nashua: Line of Business Analysis
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
