import os 
import sqlite3
import pandas as pd 

data_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv'
headers = ['first_name','last_name','address','city','state','zip']
data_table = pd.read_csv(data_url, header=None, names=headers, converters={'zip': str})

# if the DB exists, remove it 
if os.path.exists('inventory.db'):
    os.remove('inventory.db')

#  create a new Db
dbConn = sqlite3.connect('inventory.db')

# Add data to our db 
data_table.to_sql('data_table', dbConn, dtype={
    'first_name':'VARCHAR(256)',
    'last_name':'VARCHAR(256)',
    'address':'VARCHAR(256)',
    'city':'VARCHAR(256)',
	'state':'VARCHAR(2)',
	'zip':'VARCHAR(5)',
})

dbConn.row_factory = sqlite3.Row

# query functions 
def getAll(query):
    cur = dbConn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def insertOne(query,var):
    cur = dbConn.cursor()
    cur.execute(query,var)
    dbConn.commit()

def deleteOne(query,var):
    cur = dbConn.cursor()
    cur.execute(query,var)

def getOne(query,var):
    cur = dbConn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows
