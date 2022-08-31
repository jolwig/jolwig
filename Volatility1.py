import numpy as np
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf
import statistics

#Import and clean data
df = yf.download("BTC-USD", start='2014-07-10', interval='1D')
df.dropna(inplace=True)
df.index.name = 'Date'

    #price change (%)
price_change_pct = pd.Series(abs(df['Open'].pct_change()*100))

    #Standard Deviation
stdeviation = price_change_pct.std(skipna= True)
stdeviation_series = pd.Series(stdeviation, index=price_change_pct.index)

    #New DataFrame (Price change% + Standard Dev)
df2 = pd.concat([price_change_pct, stdeviation_series], axis= 1)
df2.rename(columns= {'Open': '% Change', 0: 'Standard Dev'}, inplace= True)

    #Add 'Volatility' column
df2.loc[df2['% Change'] >= stdeviation, 'Volatility'] = 'High'
df2.loc[df2['% Change'] < stdeviation, 'Volatility'] = 'Normal'
high_v = df2[df2['Volatility'] == 'High']

#Plotly Chart
fig = px.scatter(df2, x= df2.index, y= '% Change', color= 'Volatility', log_y= True, range_y= [.001,50])
fig.show()


