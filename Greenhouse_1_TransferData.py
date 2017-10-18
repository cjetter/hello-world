###
# Program to record DHT sensor data within SQLite database
###

#import Adafruit_DHT
import time as t
import sqlite3
from random import randrange  ## TO BE DELETED

#create database
filepath0='/Users/Apple/Documents/Programming/Python/Other Projects/Greenhouse/DHT.sqlite'
#filepath='/Users/Apple/Adafruit_Python_DHT/tito/SQL_Log/DHT.sqlite'
connection = sqlite3.connect(filepath0)
cur = connection.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS LogData (DateTime TEXT PRIMARY KEY NOT NULL UNIQUE,
Humidity REAL NOT NULL,
Temperature REAL NOT NULL)''')

#loop to record temp and humidity every min
while True:
    #hi, ti = Adafruit_DHT.read_retry(22,4) 
    hi, ti = randrange(40,80),randrange(1,4)  ### TO DELETE
    #ho, to = Adafruit_DHT.read_retry(22,17) --for 2 sensors
    datetime = t.strftime("%m/%d/%Y %H:%M:%S", t.localtime())  
    #hora = "%d/%d/%d,%d:%d:%d" %(date[1],date[2],date[0],date[3],date[4],date[5])
    #value =(hora,hi/100,ti,ho/100,to) -- for 2 sensors
    value =(datetime,hi/100,ti)
    print (value)

    #add reading to database
    cur.execute('''
    INSERT INTO LogData (DateTime, Temperature, Humidity)
    VALUES ( ?, ?, ?)''', (datetime, ti, hi/100))
    connection.commit()
    t.sleep(5)