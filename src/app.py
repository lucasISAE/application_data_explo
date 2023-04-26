import pandas as pd
import random
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import numpy as np


#Cours bourse ################
randomlistAMAZON = []
for i in range(693):
    n = np.random.normal(105,15,1)
    randomlistAMAZON.append(n[0])
    
randomlistBOEING = []
for i in range(5602):
    n = np.random.normal(200,10,1)
    randomlistBOEING.append(n[0])
    
randomlistBP = []
for i in range(2136):
    n = np.random.normal(530,20,1)
    randomlistBP.append(n[0])
    
randomlistGAMESTOP = []
for i in range(12429):
    n = np.random.normal(19,10,1)
    randomlistGAMESTOP.append(n[0])
    
randomlistHSBC = []
for i in range(26298):
    n = np.random.normal(560,10,1)
    randomlistHSBC.append(n[0])
    
randomlistLVMH = []
for i in range(26290):
    n = np.random.normal(880,30,1)
    randomlistLVMH.append(n[0])
    
randomlistMICROSOFT = []
for i in range(3113):
    n = np.random.normal(280,15,1)
    randomlistMICROSOFT.append(n[0])
    
# randomlistMONSANTO = []
# for i in range(26303):
#     n = np.random.normal(150,30,1)
#     randomlistMONSANTO.append(n[0])
    
randomlistPFIZER = []
for i in range(8339):
    n = np.random.normal(40,5,1)
    randomlistPFIZER.append(n[0])
    
randomlistTESLA = []
for i in range(1034):
    n = np.random.normal(150,30,1)
    randomlistTESLA.append(n[0])
    
######################################################################
#vecteur date
# tAMAZON = pd.date_range('2022-11-18 22:00:00', periods=693, freq='H')
# tBOEING = pd.date_range('2022-11-18 22:00:00', periods=5602, freq='H')
# tBP = pd.date_range('2022-11-18 22:00:00', periods=2136, freq='H')
# tGAMESTOP = pd.date_range('2022-11-18 22:00:00', periods=12429, freq='H')
# tHSBC = pd.date_range('2022-11-18 22:00:00', periods=26298, freq='H')
# tLVMH = pd.date_range('2022-11-18 22:00:00', periods=26290, freq='H')
# tMICROSOFT = pd.date_range('2022-11-18 22:00:00', periods=3113, freq='H')
# tMONSANTO = pd.date_range('2022-11-18 22:00:00', periods=26303, freq='H')
# tPFIZER = pd.date_range('2022-11-18 22:00:00', periods=8339, freq='H')
# tTESLA = pd.date_range('2022-11-18 22:00:00', periods=1034, freq='H')
    
#Scores moyennes ###############
nom = "tesla"
tweetsTESLA = pd.read_csv(nom+'_moy')
tweetsTESLA.insert(2,"stock_value",randomlistTESLA)
nom = "amazon"
tweetsAMAZON = pd.read_csv(nom+'_moy')
tweetsAMAZON.insert(2,"stock_value",randomlistAMAZON)
nom = "boeing"
tweetsBOEING = pd.read_csv(nom+'_moy')
tweetsBOEING.insert(2,"stock_value",randomlistBOEING)
nom = "bp"
tweetsBP = pd.read_csv(nom+'_moy')
tweetsBP.insert(2,"stock_value",randomlistBP)
nom = "gamestop"
tweetsGAMESTOP = pd.read_csv(nom+'_moy')
tweetsGAMESTOP.insert(2,"stock_value",randomlistGAMESTOP)
nom = "hsbc"
tweetsHSBC = pd.read_csv(nom+'_moy')
tweetsHSBC.insert(2,"stock_value",randomlistHSBC)
nom = "lvmh"
tweetsLVMH = pd.read_csv(nom+'_moy')
tweetsLVMH.insert(2,"stock_value",randomlistLVMH)
nom = "microsoft"
tweetsMICROSOFT = pd.read_csv(nom+'_moy')
tweetsMICROSOFT.insert(2,"stock_value",randomlistMICROSOFT)
# nom = "monsanto"
# tweetsMONSANTO = pd.read_csv(nom+'_moy')
# tweetsMONSANTO.insert(2,"stock_value",randomlistMONSANTO)
nom = "pfizer"
tweetsPFIZER = pd.read_csv(nom+'_moy')
tweetsPFIZER.insert(2,"stock_value",randomlistPFIZER)

groups =["TESLA", "BOEING","AMAZON",
 "PFIZER","MICROSOFT","LVMH","HSBC",
 "GAMESTOP","BP"]

###################################################################
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H1("Sentiment analysis metrics"),
    html.Hr(),
    html.P("Choose company:"),
    html.Div(html.Div([
        dcc.Dropdown(id='animal-type', clearable=False,
                     value="DOG",
                     options=[{'label': x, 'value': x} for x in
                              groups]),
    ],className="two columns"),className="row"),

    html.Div(id="output-div", children=[]),
])

@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="animal-type", component_property="value"),
)

def make_graphs(group):

    # LINE CHART
    
    if group == "TESLA":
        fig_line = px.line(tweetsTESLA, x="date_created", y="score", title="reputation indicator for TESLA")
        fig_line2 = px.line(tweetsTESLA, x="date_created", y="stock_value", title="Stock value for TESLA")
        fiability = 85
        
    if group == "BOEING":
        fig_line = px.line(tweetsBOEING, x="date_created", y="score", title="reputation indicator for BOEING")
        fig_line2 = px.line(tweetsBOEING, x="date_created", y="stock_value", title="Stock value for BOEING")
        fiability = 25
        
    if group == "AMAZON":
        fig_line = px.line(tweetsAMAZON, x="date_created", y="score", title="reputation indicator for AMAZON")
        fig_line2 = px.line(tweetsAMAZON, x="date_created", y="stock_value", title="Stock value for AMAZON")
        fiability = 55
        
    if group == "BP":
        fig_line = px.line(tweetsBP, x="date_created", y="score", title="reputation indicator for BP")
        fig_line2 = px.line(tweetsBP, x="date_created", y="stock_value", title="Stock value for BP")
        fiability = 15
        
    if group == "GAMESTOP":
        fig_line = px.line(tweetsGAMESTOP, x="date_created", y="score", title="reputation indicator for GAMESTOP")
        fig_line2 = px.line(tweetsGAMESTOP, x="date_created", y="stock_value", title="Stock value for GAMESTOP")
        fiability = 60
        
    if group == "HSBC":
        fig_line = px.line(tweetsHSBC, x="date_created", y="score", title="reputation indicator for HSBC")
        fig_line2 = px.line(tweetsHSBC, x="date_created", y="stock_value", title="Stock value for HSBC")
        fiability = 15
        
    if group == "LVMH":
        fig_line = px.line(tweetsLVMH, x="date_created", y="score", title="reputation indicator for LVMH")
        fig_line2 = px.line(tweetsLVMH, x="date_created", y="stock_value", title="Stock value for LVMH")
        fiability = 90
        
    if group == "MICROSOFT":
        fig_line = px.line(tweetsMICROSOFT, x="date_created", y="score", title="reputation indicator for MICROSOFT")
        fig_line2 = px.line(tweetsMICROSOFT, x="date_created", y="stock_value", title="Stock value for MICROSOFT")
        fiability = 70
        
    if group == "PFIZER":
        fig_line = px.line(tweetsPFIZER, x="date_created", y="score", title="reputation indicator for PFIZER")
        fig_line2 = px.line(tweetsPFIZER, x="date_created", y="stock_value", title="Stock value for PFIZER")
        fiability = 20
        
    # if group == "MONSANTO":
    #     fig_line = px.line(tweetsTESLA, x="date_created", y="score", title="reputation indicator for MONSANTO")
    #     fig_line2 = px.line(tweetsTESLA, x="date_created", y="stock_value", title="Stock value for MONSANTO")
    #     fiability = 30

    return [
        html.Div([
            html.Div([dcc.Graph(figure=fig_line)], className="twelve columns"),
            html.Div([dcc.Graph(figure=fig_line2)], className="twelve columns"),
        ], className="row"),
        html.Table([
                html.Tr([html.Td(["fiability score = "+str(fiability)+" %"]), html.Td(id='square')])
                ]),
    ]

if __name__ == '__main__':
    app.run(debug=False)




















# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.server

# app.layout = html.Div([
#     dcc.Graph(
#         figure=dict(
#             data=[
#                 dict(
#                     x=tweetsBOEING["date_created"],
#                     y=tweetsBOEING["score"],
#                     name='Mean sentiment analysis',
#                     marker=dict(
#                         color='rgb(55, 83, 109)'
#                     )
#                 ),
#             ],
#             layout=dict(
#                 title='Sentiment analysis for '+nom,
#                 showlegend=True,
#                 legend=dict(
#                     x=0,
#                     y=1.0
#                 ),
#                 margin=dict(l=40, r=0, t=40, b=30)
#             )
#         ),
        
#         style={'height': 300},
#         id='my-graph-example'
#     ),
    
#     dcc.Graph(
#         figure=dict(
#             data=[
#                 dict(
#                     x=tweetsBOEING["date_created"],
#                     y=randomlistBOEING,
#                     name=nom+ ' stock value($)',
#                     marker=dict(
#                         color='rgb(200, 0, 0)'
#                     )
#                 ),
#             ],
#             layout=dict(
#                 title='',
#                 showlegend=True,
#                 legend=dict(
#                     x=0,
#                     y=1.0
#                 ),
#                 margin=dict(l=40, r=0, t=40, b=30)
#             )
#         ),
        
#         style={'height': 300},
#         id='my-graph-example'
#     ),
    
#     html.Table([
#         html.Tr([html.Td(['Fiability indicator : 85%']), html.Td(id='square')])
#         ]),
        
# ])

# if __name__ == "__main__":
#     app.run_server(debug=True)