###
# Program to write sensor readings to local DB on rasberry pi for batch transmissions
# Note: reading collection is controlled by cron
###

# import libraries
#import Adafruit_DHT
from time import strftime, localtime
import sqlite3
from random import randrange  ## TO BE DELETED

#create database
filepath='/Users/Apple/Documents/Programming/Python/Other Projects/Greenhouse/NEW/RPiDB.sqlite'  ## TO DELETE
#filepath='/Users/Apple/Adafruit_Python_DHT/tito/SQL_Log/DHT.sqlite'
conn = sqlite3.connect(filepath)
cur = conn.cursor()

#### DOES IT MAKE MORE SENSE TO CREATE A STANDARD STRING AND THEN PASS IN STRING FORMATTING VALUES??

cur.execute('''
            CREATE TABLE IF NOT EXISTS DateTime 
            (RecordID INT PRIMARY KEY AUTO_INCREMENT, 
            DateTime TEXT NOT NULL UNIQUE)

            CREATE TABLE IF NOT EXISTS Temp_Inside 
            (RecordID INT PRIMARY KEY AUTO_INCREMENT, 
            Temperature_Inside REAL NOT NULL)
            
            CREATE TABLE IF NOT EXISTS Hum_Inside
            (RecordID INT PRIMARY KEY AUTO_INCREMENT, 
            Humidity_Inside REAL NOT NULL)
            
            ''')

# take readings from sensors

#ti, hi = Adafruit_DHT.read_retry(4,22) 
ti, hi = randrange(1,4),randrange(40,80)                                        ### TO DELETE
#to, ho = Adafruit_DHT.read_retry(17,22) --for 2 sensors
datetime = strftime("%m/%d/%Y %H:%M:%S", localtime())  
value =(datetime,hi/100,ti)
print (value)

#add reading to database
cur.execute('INSERT INTO DateTime (DateTime) VALUES (?)', (datetime))
cur.execute('INSERT INTO Temp_Inside (Temperature_Inside) VALUES (?)', (ti))
cur.execute('INSERT INTO Hum_Inside (Humidity_Inside) VALUES (?)', (hi))

conn.commit()