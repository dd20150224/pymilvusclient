import sqlite3

def create_config(dbConn, config):
    sql = '''INSERT INTO config(id, name, host, port) VALUES(?,?,?,?)'''
    cur = dbConn.cursor()
    print("config:",config)
    cur.execute(sql, config)
    dbConn.commit()
    return cur.lastrowid

def ensure_config_table(dbConn):
  tableNames=get_table_names(dbConn)
  print('tableNames', tableNames)
  if not 'config' in tableNames:
    cur = dbConn.cursor()
    cur.execute('''CREATE TABLE config
      (id INT PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      host TEXT NOT NULL,
      port TEXT NOT NULL);''')
    dbConn.commit()

def get_table_names(dbConn):
  sql_query = """SELECT name from sqlite_master WHERE type='table';"""
  cursor = dbConn.cursor()
  cursor.execute(sql_query)
  rows = cursor.fetchall()
  result = [row[0] for row in rows]
  return result

def get_rows(dbConn, tableName):
  sql_query = """SELECT id, name, host, port FROM 'config';"""
  cursor = dbConn.cursor()
  cursor.execute(sql_query)
  rows = cursor.fetchall()
  for row in rows:
    print(tableName, row)
  return rows