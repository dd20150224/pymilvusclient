import sqlite3
from dotenv import load_dotenv
load_dotenv()

import os
# from pymilvus import connections, utility

def getRows(dbConn, tableName):
  sql_query = """SELECT name, host, port FROM 'config';"""
  cursor = dbConn.cursor()
  cursor.execute(sql_query)
  return cursor.fetchall()
  
def getTableNames(dbConn):
  sql_query = """SELECT name from sqlite_master WHERE type='table';"""
  cursor = dbConn.cursor()
  cursor.execute(sql_query)
  return cursor.fetchall()

def ensureTable(dbConn, tableName):
  tableNames=getTableNames(dbConn)
  print('tableNames', tableNames)
  if not 'config' in tableNames:
    cur = dbConn.cursor()
    cur.execute('''CREATE TABLE config
      (ID INT PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      host TEXT NOT NULL,
      port INT);''')
    dbConn.commit()


# conn = connections.connect(
#     host=os.getenv("HOST"),
#     port=os.getenv("PORT")    
# )
# print(conn)

# print(connections.list_connections())

dbConn = sqlite3.connect('config.db')
print('Opened databse successfully')


ensureTable(dbConn, 'config')
rows = getRows(dbConn, 'config')
print('get rows:', rows)
