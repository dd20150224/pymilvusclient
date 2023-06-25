# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.5 on Fri Jun 23 23:05:45 2023
#

import wx
# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode
from DialogConnections import DialogConnections
from milvus_service import connect_milvus, list_database, using_database, list_collections, get_collection
 
def refresh_collection_info(
  lbCollections,
  lblName,
  lblDescription,
  lblEntities,
  lcFields,
  lcIndexes,
  lcProperties):
  collection = get_collection(lbCollections.GetStringSelection())
  lblName.SetLabel(collection.name)
  lblDescription.SetLabel(collection.description)
  lblEntities.SetLabel(str(collection.num_entities))

def refresh_databases(lbDatabases):
  dbs = list_database()
  lbDatabases.Clear()
  lbDatabases.Append(dbs)
  select_database(lbDatabases)

def select_database(lbDatabases, index=0):
  if (index >= 0):
   dbs = lbDatabases.GetItems()
   if len(dbs) > index:
     lbDatabases.SetSelection(index)
     using_database(lbDatabases.GetStringSelection())
     return
  lbDatabases.SetSelection(-1)

def select_collection(lbCollections, index=0):
  if (index >= 0):
    collections = lbCollections.GetItems()
    if len(collections) > index:
      lbCollections.SetSelection(index)
      return
  lbCollections.SetSelection(-1)
  

def refresh_collections(lbCollections):
  collections = list_collections()
  lbCollections.Clear()
  print('collections', collections)
  lbCollections.Append(collections)
  select_collection(lbCollections)
# end wxGlade


class MyFrame(wx.Frame):
        def __init__(self, *args, **kwds):
                # begin wxGlade: MyFrame.__init__
                kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
                wx.Frame.__init__(self, *args, **kwds)
                self.SetSize((1066, 743))
                self.SetTitle("frame")

                # Menu Bar
                self.frame_menubar = wx.MenuBar()
                wxglade_tmp_menu = wx.Menu()
                self.frame_menubar.Append(wxglade_tmp_menu, "&File")
                wxglade_tmp_menu = wx.Menu()
                self.frame_menubar.Append(wxglade_tmp_menu, "&Edit")
                wxglade_tmp_menu = wx.Menu()
                self.frame_menubar.Append(wxglade_tmp_menu, "&Options")
                self.SetMenuBar(self.frame_menubar)
                # Menu Bar end

                self.panel_1 = wx.Panel(self, wx.ID_ANY)

                sizer_1 = wx.BoxSizer(wx.VERTICAL)

                sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
                sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)

                self.btnConnections = wx.Button(self.panel_1, wx.ID_ANY, "Connections")
                sizer_2.Add(self.btnConnections, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.FIXED_MINSIZE | wx.LEFT | wx.TOP, 5)

                self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "button_2")
                sizer_2.Add(self.button_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 5)

                self.window_1 = wx.SplitterWindow(self.panel_1, wx.ID_ANY)
                self.window_1.SetMinimumPaneSize(20)
                sizer_1.Add(self.window_1, 1, wx.ALL | wx.EXPAND, 0)

                self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)

                sizer_3 = wx.BoxSizer(wx.VERTICAL)

                sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
                sizer_3.Add(sizer_5, 0, wx.EXPAND, 0)

                label_1 = wx.StaticText(self.window_1_pane_1, wx.ID_ANY, "Databases")
                label_1.SetForegroundColour(wx.Colour(143, 143, 188))
                sizer_5.Add(label_1, 0, wx.ALIGN_BOTTOM | wx.LEFT | wx.RIGHT, 4)

                sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
                sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)

                self.panel_2 = wx.Panel(self.window_1_pane_1, wx.ID_ANY)
                sizer_6.Add(self.panel_2, 1, wx.EXPAND, 0)

                self.btnNewDatabase = wx.Button(self.window_1_pane_1, wx.ID_ANY, "New")
                sizer_6.Add(self.btnNewDatabase, 0, 0, 0)

                self.lbDatabases = wx.ListBox(self.window_1_pane_1, wx.ID_ANY, choices=[""])
                sizer_3.Add(self.lbDatabases, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 4)

                sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
                sizer_3.Add(sizer_7, 0, wx.EXPAND, 0)

                label_2 = wx.StaticText(self.window_1_pane_1, wx.ID_ANY, "Collections")
                label_2.SetForegroundColour(wx.Colour(143, 143, 188))
                sizer_7.Add(label_2, 0, wx.ALIGN_BOTTOM | wx.LEFT | wx.RIGHT, 4)

                sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
                sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)

                self.panel_3 = wx.Panel(self.window_1_pane_1, wx.ID_ANY)
                sizer_8.Add(self.panel_3, 1, wx.EXPAND, 0)

                self.btnNewCollection = wx.Button(self.window_1_pane_1, wx.ID_ANY, "New")
                sizer_8.Add(self.btnNewCollection, 0, 0, 0)

                self.connected = False
                self.lbCollections = wx.ListBox(self.window_1_pane_1, wx.ID_ANY, choices=[])
                sizer_3.Add(self.lbCollections, 3, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 4)

                self.window_1_pane_2 = wx.Panel(self.window_1, wx.ID_ANY)

                sizer_4 = wx.BoxSizer(wx.VERTICAL)

                sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
                sizer_4.Add(sizer_9, 0, wx.ALL | wx.EXPAND, 4)

                label_3 = wx.StaticText(self.window_1_pane_2, wx.ID_ANY, "Name")
                label_3.SetForegroundColour(wx.Colour(143, 143, 188))
                sizer_9.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 4)

                lblName = wx.StaticText(self.window_1_pane_2, wx.ID_ANY, "(Name)")
                self.lblName=lblName
                sizer_9.Add(lblName, 3, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

                label_4 = wx.StaticText(self.window_1_pane_2, wx.ID_ANY, "Description")
                label_4.SetForegroundColour(wx.Colour(143, 143, 188))
                sizer_9.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

                lblDescription = wx.StaticText(self.window_1_pane_2, wx.ID_ANY, "(description)")
                self.lblDescription=lblDescription
                sizer_9.Add(lblDescription, 5, wx.LEFT | wx.RIGHT, 4)

                label_5 = wx.StaticText(self.window_1_pane_2, wx.ID_ANY, "Entities")
                label_5.SetForegroundColour(wx.Colour(143, 143, 188))
                sizer_9.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

                lblEntities = wx.StaticText(self.window_1_pane_2, wx.ID_ANY, "(Entities)")
                self.lblEntities=lblEntities
                sizer_9.Add(lblEntities, 2, wx.LEFT | wx.RIGHT, 4)

                sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
                sizer_4.Add(sizer_10, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 4)

                sizer_11 = wx.BoxSizer(wx.VERTICAL)
                sizer_10.Add(sizer_11, 1, wx.EXPAND, 0)

                lblFields = wx.StaticText(self.window_1_pane_2, wx.ID_ANY, "Fields")
                lblFields.SetForegroundColour(wx.Colour(143, 143, 188))
                sizer_11.Add(lblFields, 0, 0, 0)

                self.lcFields = wx.ListCtrl(self.window_1_pane_2, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
                self.lcFields.SetMinSize((381, 200))
                self.lcFields.AppendColumn("Name", format=wx.LIST_FORMAT_LEFT, width=100)
                self.lcFields.AppendColumn("Description", format=wx.LIST_FORMAT_LEFT, width=180)
                self.lcFields.AppendColumn("Type", format=wx.LIST_FORMAT_LEFT, width=-1)
                self.lcFields.AppendColumn("Primary", format=wx.LIST_FORMAT_LEFT, width=-1)
                self.lcFields.AppendColumn("Auto-ID", format=wx.LIST_FORMAT_LEFT, width=-1)
                self.lcFields.AppendColumn("Params", format=wx.LIST_FORMAT_LEFT, width=-1)
                sizer_11.Add(self.lcFields, 1, wx.EXPAND, 0)

                sizer_12 = wx.BoxSizer(wx.VERTICAL)
                sizer_10.Add(sizer_12, 1, wx.EXPAND, 0)

                lblIndexes = wx.StaticText(self.window_1_pane_2, wx.ID_ANY, "Indexes")
                lblIndexes.SetForegroundColour(wx.Colour(143, 143, 188))
                sizer_12.Add(lblIndexes, 0, 0, 0)

                self.lcIndexes = wx.ListCtrl(self.window_1_pane_2, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
                self.lcIndexes.SetMinSize((381, 100))
                self.lcIndexes.AppendColumn("A", format=wx.LIST_FORMAT_LEFT, width=-1)
                self.lcIndexes.AppendColumn("B", format=wx.LIST_FORMAT_LEFT, width=-1)
                self.lcIndexes.AppendColumn("C", format=wx.LIST_FORMAT_LEFT, width=-1)
                sizer_12.Add(self.lcIndexes, 1, wx.EXPAND, 0)

                lblProperties = wx.StaticText(self.window_1_pane_2, wx.ID_ANY, "Properties")
                lblProperties.SetForegroundColour(wx.Colour(143, 143, 188))
                sizer_12.Add(lblProperties, 0, 0, 0)

                self.lcProperties = wx.ListCtrl(self.window_1_pane_2, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
                self.lcProperties.SetMinSize((381, 100))
                self.lcProperties.AppendColumn("A", format=wx.LIST_FORMAT_LEFT, width=-1)
                self.lcProperties.AppendColumn("B", format=wx.LIST_FORMAT_LEFT, width=-1)
                self.lcProperties.AppendColumn("C", format=wx.LIST_FORMAT_LEFT, width=-1)
                sizer_12.Add(self.lcProperties, 1, wx.EXPAND, 0)

                self.notebook_1 = wx.Notebook(self.window_1_pane_2, wx.ID_ANY)
                sizer_4.Add(self.notebook_1, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 4)

                self.grid_2 = wx.grid.Grid(self.notebook_1, wx.ID_ANY, size=(1, 1))
                self.grid_2.CreateGrid(10, 0)
                self.notebook_1.AddPage(self.grid_2, "notebook_1_pane_1")

                self.window_1_pane_2.SetSizer(sizer_4)

                self.window_1_pane_1.SetSizer(sizer_3)

                self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2, 163)

                self.panel_1.SetSizer(sizer_1)

                self.Layout()

                self.Bind(wx.EVT_BUTTON, self.onConnections, self.btnConnections)
                self.Bind(wx.EVT_LISTBOX, self.onCollectionSelected, self.lbCollections)
                # end wxGlade

        def onConnections(self, event):  # wxGlade: MyFrame.<event_handler>
            with DialogConnections(self) as dialogConnections:
              result = dialogConnections.ShowModal()
              if result == wx.ID_CANCEL:
                print('cancel')
              if result == wx.ID_OK:
                print('ok')
                selectedItemCount = dialogConnections.lcConnections.GetSelectedItemCount()
                print('selectedItemCount', selectedItemCount)
                selectedIndex = dialogConnections.lcConnections.GetFirstSelected()
                print('selectedIndex', selectedIndex)
                selectedHost = dialogConnections.lcConnections.GetItem(selectedIndex, 2).Text
                print('selectedHost', selectedHost)
                selectedPort = dialogConnections.lcConnections.GetItem(selectedIndex, 3).Text
                print('selectedPort', selectedPort)
                connect_milvus(host=selectedHost, port=selectedPort)

                refresh_databases(self.lbDatabases)
                refresh_collections(self.lbCollections)

                self.onCollectionSelected(self)

        def onCollectionSelected(self, event):  # wxGlade: MyFrame.<event_handler>
                refresh_collection_info(
                  self.lbCollections,
                  self.lblName,
                  self.lblDescription,
                  self.lblEntities,
                  self.lcFields,
                  self.lcIndexes,
                  self.lcProperties)
# end of class MyFrame