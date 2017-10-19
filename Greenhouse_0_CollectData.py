###
# Program to verify existence of databases on startup of pi and record DHT sensor data within SQLite database for later transfer to server
###

# import libraries
#import Adafruit_DHT
import time as t
import sqlite3
from random import randrange                                                                    ### DELETE AFTER TESTING

#create database and establish connection to write to DB
filepath='/Users/Apple/Documents/Programming/Python/Other Projects/Greenhouse/NEW/DHT.sqlite'   ### DELETE AFTER TESTING
#filepath='/Users/Apple/Adafruit_Python_DHT/tito/SQL_Log/DHT.sqlite'
connection = sqlite3.connect(filepath)
cur = connection.cursor()


# define database tables and column / data types and create table or verify table existence
# inside temp table
cur.execute('''CREATE TABLE IF NOT EXISTS {} (DateTime TEXT PRIMARY KEY NOT NULL,
               {} {} NOT NULL)'''.format('Temperature','Temperature','REAL'))
# inside humidity table
cur.execute('''CREATE TABLE IF NOT EXISTS {} (DateTime TEXT PRIMARY KEY NOT NULL,
               {} {} NOT NULL)'''.format('Humidity','Humidity','REAL'))

# collect datetime stamp and sensor readings
datetime = t.strftime("%m/%d/%Y %H:%M:%S", t.localtime())    # generate datetime stamp
#hi, ti = Adafruit_DHT.read_retry(22,4)                     # inside humidity / temp reading
hi, ti = randrange(40,80),randrange(1,4)                                                      ### DELETE AFTER TESTING
#ho, to = Adafruit_DHT.read_retry(22,17)                    # outside temp / humidity reading

# print live stream of values
value =(datetime,hi/100,ti)
print (value)

#add reading to database
cur.execute('''INSERT INTO {} (DateTime,{}) VALUES (?, ?)'''.format('Temperature','Temperature'), (datetime, ti))
cur.execute('''INSERT INTO {} (DateTime,{}) VALUES (?, ?)'''.format('Humidity','Humidity'), (datetime, hi))
connection.commit()