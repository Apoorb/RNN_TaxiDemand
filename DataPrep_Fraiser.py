# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:52:19 2018

@author: A-Bibeka
"""


import os
import pandas as pd
from datetime import datetime
from datetime import date, timedelta # to get 1st Sunday of an year
import matplotlib.pyplot as plt # this is used for the plot the graph 

def parse(x):
	return datetime.strptime(x, '%Y %m %d %H')
print('Current working directory ',os.getcwd())
#os.chdir("/Users/Apoorb/Documents/GitHub/RNN_TaxiDemand")
os.chdir("C:\\Users\\a-bibeka\\Documents\\GitHub\\RNN_TaxiDemand")
print('Current working directory ',os.getcwd())

# load data
df = pd.read_csv('TTB.csv',  usecols = ["totaltrips","TIME1"])

#df["dt"]=pd.to_datetime(dict(year=df.year, month=df.month, day=df.day,hour=df.time))
#df=df.drop(['year', 'month', 'day', 'time'],axis=1)

df["dt"]=pd.to_datetime(df.TIME1)
df=df.set_index('dt')
df=df.drop(columns="TIME1")
df=df[df.index.year==2016]
df=df.rename(columns={"totaltrips":"NumTrips"})


# Get 8th day from the new year
d = date(2016, 1, 1)                    # January 8th
df=df[(df.index>=str(d))]
d2=date(2016,12,31)
# Fill missing dates
idx = pd.date_range(str(d),str(d2),freq='H')
df=df.reindex(idx,fill_value=0)
df[df.NumTrips==0]

df.to_csv("RNN_data_Fraiser.csv")

