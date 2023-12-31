# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.5 on Fri Jun 23 09:59:42 2023
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import sqlite3
from dotenv import load_dotenv
load_dotenv()
import os

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

dbConn = sqlite3.connect('config.db')
ensureTable(dbConn, 'config')
rows=getRows(dbConn, 'config')
# end wxGlade


class DialogConnections(wx.Dialog):
        def __init__(self, *args, **kwds):
                # begin wxGlade: DialogConnections.__init__
                kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
                wx.Dialog.__init__(self, *args, **kwds)
                self.SetTitle("dialog")

                sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

                self.lcConnections = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
                self.lcConnections.AppendColumn("Name", format=wx.LIST_FORMAT_LEFT, width=160)
                self.lcConnections.AppendColumn("Host", format=wx.LIST_FORMAT_LEFT, width=160)
                self.lcConnections.AppendColumn("Port", format=wx.LIST_FORMAT_LEFT, width=80)
                sizer_1.Add(self.lcConnections, 1, wx.ALL | wx.EXPAND, 4)

                sizer_2 = wx.BoxSizer(wx.VERTICAL)
                sizer_1.Add(sizer_2, 0, wx.ALL, 4)

                self.btnNew = wx.Button(self, wx.ID_ANY, "New")
                sizer_2.Add(self.btnNew, 0, wx.BOTTOM, 4)

                self.btnOk = wx.Button(self, wx.ID_ANY, "OK")
                self.btnOk.SetDefault()
                sizer_2.Add(self.btnOk, 0, wx.BOTTOM, 4)

                self.btnCancel = wx.Button(self, wx.ID_CANCEL, "")
                sizer_2.Add(self.btnCancel, 0, wx.BOTTOM, 4)

                self.SetSizer(sizer_1)
                sizer_1.Fit(self)

                self.SetAffirmativeId(self.btnOk.GetId())
                self.SetEscapeId(self.btnCancel.GetId())

                self.Layout()
                # end wxGlade

# end of class DialogConnections
