# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from dialog import dialog_newsched
import wxdata
import os.path

###########################################################################
## Class sched_frame
###########################################################################

class sched_frame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Scheduler", pos = wx.DefaultPosition, size = wx.Size( 900,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( 900,400 ), wx.Size( 900,700 ) )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
        
        self.menubar_main = wx.MenuBar( 0 )
        self.menubar_main.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
        
        self.menu_task = wx.Menu()
        self.menu_addsched = wx.MenuItem( self.menu_task, wx.ID_ANY, u"Add Schedule", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_task.AppendItem( self.menu_addsched )
        
        self.menubar_main.Append( self.menu_task, u"Task" ) 
        
        self.menu_view = wx.Menu()
        self.menubar_main.Append( self.menu_view, u"View" ) 
        
        self.menu_help = wx.Menu()
        self.menubar_main.Append( self.menu_help, u"Help" ) 
        
        self.SetMenuBar( self.menubar_main )
        
        self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
        
        self.tool_addschedule = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Add New Schedule", wx.Bitmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "circle.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
        
        self.m_toolBar1.Realize() 
        
        fgSizer1 = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.display_split = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 900,400 ), wx.SP_3D )
        self.display_split.Bind( wx.EVT_IDLE, self.display_splitOnIdle )
        
        self.display_split.SetMinSize( wx.Size( 900,400 ) )
        
        self.m_panel5 = wx.Panel( self.display_split, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel5.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
        
        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_button5 = wx.Button( self.m_panel5, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_button5, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( fgSizer2 )
        self.m_panel5.Layout()
        fgSizer2.Fit( self.m_panel5 )
        self.m_panel6 = wx.Panel( self.display_split, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel6.SetMinSize( wx.Size( 700,-1 ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.display_schedule = wx.dataview.DataViewListCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,300 ), wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_VERT_RULES )
        bSizer1.Add( self.display_schedule, 0, wx.ALL, 5 )
        self.display_schedule.AppendTextColumn("Filename")
        self.display_schedule.AppendTextColumn("Date")
        self.display_schedule.AppendTextColumn("Time")
        self.display_schedule.AppendTextColumn("Interval")
        self.display_schedule.AppendTextColumn("Remark")
        
        
        wxdata.display_schedule = self.display_schedule

        self.m_panel6.SetSizer( bSizer1 )
        self.m_panel6.Layout()
        self.display_split.SplitVertically( self.m_panel5, self.m_panel6, 0 )
        fgSizer1.Add( self.display_split, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( fgSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_TOOL, self.show_add_dialog, id = self.tool_addschedule.GetId() )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def show_add_dialog( self, event ):
        dialog = dialog_newsched(self)
        wxdata.retCode = dialog.ShowModal()
        #event.Skip()
    
    def display_splitOnIdle( self, event ):
        self.display_split.SetSashPosition( 0 )
        self.display_split.Unbind( wx.EVT_IDLE )
    
