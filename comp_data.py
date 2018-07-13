#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:19:22 2018

@author: a_swart
"""
from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#df = pd.read_csv("~/Documents/Data/ISTIdata/TrinityData/SEDC_FILES/BC_ARIES_ENV_log-20160209t14"
 #                , low_memory=False)

#s_df = df.loc[df["service id"] == "c2-3c2s11"]


def read_data(csv_string, id_subset = "none",time_index = "none"):
    df = pd.read_csv(csv_string, low_memory=False)
    if id_subset != "none":
        df = df.loc[df["service id"] == id_subset]
    df = df[df["service id"] != "service id"]
    if time_index != "none":
        # time_index is a string of what column the time index
        #Problem is that most timestamps are dups
        # Call convert time and remove time column from df
        df[time_index] = pd.to_datetime(df[time_index])
        df.index = df[time_index]
        del df[time_index]
    
    #return df
    labels = [i for i in df.dtypes.axes[0]]
    maps = dict([ (i,np.float64) for i in labels[1:] ])
    return df.astype(maps)
  
    



"""    
a = pd.to_datetime(df["time"])    




#print(s_df.dtypes)
x = s_df.dtypes.axes[0]
labels = [i for i in s_df.dtypes.axes[0]]
maps = dict([ (i,np.float64) for i in labels[2:] ])

s1_df = s_df.astype(maps)

print(s1_df.dtypes)

times = s1_df["time"].tolist()

#print(times[-1])

"""
"""
Converts time string to seconds from earliest datapoint
"""
def convert_time(time_string_array, return_datetime = False, tstamp = False):
    # Im just gonna be lazy here and assume times are sorted
    #datetime_array = [datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
    #for t in time_string_array]
    datetime_array = []
    for t in time_string_array:
        dt = datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
        if tstamp == True:
            dt = pd.Timestamp(dt.timestamp(),unit="s")
        if return_datetime == True:
            #datetime_array.append(dt)
            return pd.to_datetime(time_string_array)
        else:
            datetime_array.append((dt.time().hour*60+dt.time().minute)*60+dt.time().second)
    #if return_datetime == True:
        #return datetime_array
    normed_seconds = [t-datetime_array[0] for t in datetime_array]
    return normed_seconds

def plot_dataframe_time(df):
    # Dataframe should be indexed by time
    #times = df["time"].tolist()
    #ts = convert_time(times)
    #new_df["time"] = ts
    
    df.plot.scatter(x=df.index,y="BC_T_ARIES_TEMP")
    
    return

filename = "~/Documents/Data/ISTIdata/TrinityData/SEDC_FILES/BC_ARIES_ENV_log-20160209t14"
#id_subset = "service id"
id_subset = 'none'
df = read_data(filename,id_subset,"time")
#print(df.head())


plot_dataframe_time(df)
#k = plot_dataframe_time(s1_df)
#print(k.dtypes)
