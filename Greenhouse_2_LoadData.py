# Script to generate figures and widgets for plotting of temperature, humidity, pH, etc.

#import libraries
import time as t
import datetime as dt 
import pandas as pd
from pandas.tseries.offsets import *
import sqlite3
# from smb.SMBConnection import SMBConnection
from random import randrange
from scipy.signal import savgol_filter
from bokeh.plotting import figure, show
from bokeh.io import curdoc
from bokeh.layouts import column, widgetbox, row
from bokeh.models import *
from bokeh.models.widgets import Button, RadioButtonGroup, RadioGroup, Tabs, Panel, CheckboxGroup
from math import radians

# Function to capture data based on datetime range and distribution type
def load_data(datatype):
    '''
    The load_data function loads database data into a pandas dataframe, formats the date and passes the DF into a ColumnDataSource bokeh.models object to pass into the figure.

    datatype = The designation of the type of data being loaded. Designate by passing in one of the following ["Temp","Hum","pH"] as a string.
    '''
    # control tables names to be passed into the SQL query according to the datatype.  
    # define database table title by data type
    dbtdict = {'Temp':'????','Hum':'?????','pH':'??????'}
    
    # establish connection with database
    filepath='/Users/Apple/Documents/Programming/Python/Other Projects/Greenhouse/DHT_dummy_3.sqlite'
    conn = sqlite3.connect(filepath)

    # convert database to pandas dataframe and format / sort by datetime column
    df = pd.read_sql('SELECT * FROM {}'.format(dbtdict[datatype]),conn)
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    df.sort_values('DateTime',inplace=True)

    # Pass in DF to CDS bokeh.models object
    x = list(df['DateTime'])
    y_temp = list(df['Temperature'])
    y_hum = list(df['Humidity'])
    source=ColumnDataSource(dict(x=x,y=y_temp))
    source2=ColumnDataSource(dict(x=x,y=y_hum))
    return source, source2

# load original datasource
filepath='/Users/Apple/Documents/Programming/Python/Other Projects/Greenhouse/DHT_dummy_3.sqlite'
conn = sqlite3.connect(filepath)
df_original = pd.read_sql('SELECT * FROM LogData',conn)
df_original['DateTime'] = pd.to_datetime(df_original['DateTime'])
df_original.sort_values('DateTime',inplace=True)

distribution ='Discrete'
datetime_start = 8

