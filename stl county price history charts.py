import pandas as pd
import numpy as np
import plotly.express as px

#Import and clean data

df = pd.read_csv(r"C:\Users\13148\Desktop\DataSets\zillow real estate.csv")
#drop columns (only want to see st louis metro area)
df = df.drop(columns=["RegionID","SizeRank", "RegionType","StateName", "State"])
df = df.rename(columns={"RegionName" : "Zip Code", "CountyName" : "County"})
df = df[df["Metro"] == "St. Louis"]
df = df.sort_values(by="City")
df = df.drop(columns=["Metro", "Zip Code","County"])
#transpose df and reset index
df = df.T.reset_index()
df.rename(columns= df.iloc[0], inplace=True)
df.rename(columns= {"City" : "Date"}, inplace=True)
df.drop([0], inplace=True)

for i in df:
    fig = px.line(df, x=df["Date"], y=df[i])
    fig.show()



