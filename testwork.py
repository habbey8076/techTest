#!/usr/bin/env python
# coding: utf-8

#just to be in the right working directory
import os
print(os.getcwd())
import pandas as pd
import pyarrow as pa
import numpy as ny
import pyarrow.parquet as pq

#pyarrow libary was used to convert csv file into parquet
#Remember to run the file from right directory
# Test work were done with Jupyter Notebook

df = pd.read_csv('C:\\Users\habbe\\Documents\\jupyterNoteWok\\weather1.csv')
df.to_parquet('C:\\Users\\habbe\\Documents\\jupyterNoteWok\\weather1.parquet')
df = pd.read_csv('C:\\Users\habbe\\Documents\\jupyterNoteWok\\weather2.csv')
df.to_parquet('C:\\Users\\habbe\\Documents\\jupyterNoteWok\\weather2.parquet')

#parquet file was read into DataFrame
dataframe1 = pd.read_parquet('weather2.parquet')

#exploring the dataset to ensure that it was properly read into the DataFrame
dataframe1

dataframe = pd.read_parquet('weather1.parquet')

#DataFrame2 was read and expored

dataframe

# dataframe, dataframe1 was combined into single file
Workframes = [dataframe, dataframe1]

Workframes

#datsets in Workframes were concatenated into single file
datf_concat = pd.concat(Workframes)

datf_concat

#after exploring the dataset, I decided to keep only 9 rows that are relevant to keys questions associated with the data set

dat_2_kp = ['ScreenTemperature','ObservationTime','ObservationDate','ForecastSiteCode','SiteName','Latitude','Longitude','Region','Country']

#rows head to keep was explored further

dat_2_kp

#Inserted Data into empty rows that I decided to keep

data4Explore = datf_concat[dat_2_kp]

data4Explore

#the data were sorted and it was enough to answer the key questions namely:
#- Which date was the hottest day? - What was the temperature on that day? - In which region was the hottest day?

sortWork = data4Explore.sort_values('ScreenTemperature',ascending=False )

print(sortWork)

#sorted data answered the key questions asked:

#- Which date was the hottest day? - What was the temperature on that day? - In which region was the hottest day?
#Hottest day: Febraury 02, 2016
#Temp: 15.6 degree celcius - Assumption (ScreenTemperature was assumed to be the day temperature. The data set provided did not give further clarification)
#region: South west England
sortWork.head()
