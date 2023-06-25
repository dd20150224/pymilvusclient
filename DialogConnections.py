# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.5 on Fri Jun 23 23:05:45 2023
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import sqlite3
from config_service import create_config, get_rows, ensure_config_table
from dotenv import load_dotenv
load_dotenv()
import os
from DialogNewConnection import DialogNewConnection


def refreshConnections(lcConnections):
  lcConnections.DeleteAllItems()
  rows = get_rows(dbConn, 'config')

  for i, row in enumerate(rows):
    print('row:',row)
    lcConnections.InsertItem(i, str(row[0]))
    lcConnections.SetItem(i, 1, row[1])
    lcConnections.SetItem(i, 2, row[2])
    lcConnections.SetItem(i, 3, row[3])

dbConn = sqlite3.connect('config.db')
ensure_config_table(dbConn)
# end wxGlade


class DialogConnections(wx.Dialog):
        selected: int

        def __init__(self, *args, **kwds):
                # begin wxGlade: DialogConnections.__init__
                kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
                wx.Dialog.__init__(self, *args, **kwds)
                self.SetTitle("Connections")

                sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

                self.lcConnections = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
                self.lcConnections.AppendColumn("#", format=wx.LIST_FORMAT_LEFT, width=80)
                self.lcConnections.AppendColumn("Name", format=wx.LIST_FORMAT_LEFT, width=160)
                self.lcConnections.AppendColumn("Host", format=wx.LIST_FORMAT_LEFT, width=160)
                self.lcConnections.AppendColumn("Port", format=wx.LIST_FORMAT_LEFT, width=80)
                sizer_1.Add(self.lcConnections, 1, wx.ALL | wx.EXPAND, 4)

                sizer_2 = wx.BoxSizer(wx.VERTICAL)
                sizer_1.Add(sizer_2, 0, wx.ALL, 4)

                self.btnOk = wx.Button(self, wx.ID_OK, "")
                self.btnOk.SetDefault()
                sizer_2.Add(self.btnOk, 0, wx.BOTTOM, 4)

                self.btnCancel = wx.Button(self, wx.ID_CANCEL, "")
                sizer_2.Add(self.btnCancel, 0, wx.BOTTOM, 4)

                self.btnNew = wx.Button(self, wx.ID_ADD, "")
                sizer_2.Add(self.btnNew, 0, wx.BOTTOM, 4)

                self.SetSizer(sizer_1)
                sizer_1.Fit(self)

                self.SetAffirmativeId(self.btnOk.GetId())
                self.SetEscapeId(self.btnCancel.GetId())

                self.Layout()
                refreshConnections(self.lcConnections)

                self.Bind(wx.EVT_BUTTON, self.onNewClicked, self.btnNew)
                # end wxGlade

        def onNewClicked(self, event):  # wxGlade: DialogConnections.<event_handler>
                with DialogNewConnection(self) as dialogNewConnection:
                    result = dialogNewConnection.ShowModal()
                    if result == wx.ID_OK:
                      config = (
                        self.lcConnections.GetItemCount(),                        
                        dialogNewConnection.txtName.GetValue(),
                        dialogNewConnection.txtHost.GetValue(),
                        dialogNewConnection.txtPort.GetValue()
                      )
                      configId = create_config(dbConn, config)                          
                      print('configId', configId)
                    refresh_connections(self.lcConnections)

                # print("Event handler 'onNewClicked' not implemented!")
                # event.Skip()

        # def onItemSelected(self, event):  # wxGlade: DialogConnections.<event_handler>
        #         itemIndex = self.lcConnections.GetFirstSelected()
        #         item = self.lcConnections.GetItem(itemIndex)
        #         print('selectedItem', item)
# end of class DialogConnections
