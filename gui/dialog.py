# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from controller import controller

###########################################################################
## Class dialog_newsched
###########################################################################

class NewScheduleDialog (wx.Dialog):
    
    def __init__(self, parent):
        wx.Dialog.__init__ (self, parent, id = wx.ID_ANY,
            title = u"Add New Schedule",pos = wx.DefaultPosition,
            size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        gbSizer1.SetMinSize(wx.Size( 500,-1)) 
        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Date",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        gbSizer1.Add( self.m_staticText2, wx.GBPosition(0, 0),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.schedule_date = wx.DatePickerCtrl(self, wx.ID_ANY,
            wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
            wx.DP_DEFAULT|wx.DP_DROPDOWN)
        gbSizer1.Add(self.schedule_date, wx.GBPosition(0, 1),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Time",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gbSizer1.Add(self.m_staticText3, wx.GBPosition(1, 0),
            wx.GBSpan(1, 1), wx.ALL, 5 )
        
        self.schedule_time = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
            wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add( self.schedule_time, wx.GBPosition(1, 1),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.select_file = wx.Button(self, wx.ID_ANY, u"Select File",
            wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.select_file, wx.GBPosition(2, 0),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.label_file_dir = wx.StaticText(self, wx.ID_ANY,
            u"No file chosen", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_file_dir.Wrap(-1)
        gbSizer1.Add(self.label_file_dir, wx.GBPosition(2, 1),
            wx.GBSpan(1, 1), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        self.onttime = wx.RadioButton(self, wx.ID_ANY, u"One time",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.onttime.SetValue(True) 
        gbSizer1.Add( self.onttime, wx.GBPosition(3, 0),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.periodic = wx.RadioButton(self, wx.ID_ANY, u"Periodic",
            wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add( self.periodic, wx.GBPosition(3, 1),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Frequency",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        gbSizer1.Add(self.m_staticText4, wx.GBPosition(4, 0),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.interval_value = wx.TextCtrl(self, wx.ID_ANY,
            wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add( self.interval_value, wx.GBPosition(4, 1),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        frequency_typeChoices = [ u"Minute", u"Hour", u"Day", u"Week", u"Month" ]
        self.frequency_type = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition,
            wx.DefaultSize, frequency_typeChoices, 0)
        self.frequency_type.SetSelection(0)
        gbSizer1.Add( self.frequency_type, wx.GBPosition(4, 2),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Remark",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gbSizer1.Add( self.m_staticText5, wx.GBPosition(5, 0),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.schedule_remark = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
            wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.schedule_remark, wx.GBPosition(5, 1),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.add_btn = wx.Button(self, wx.ID_ANY, u"Add", wx.DefaultPosition,
            wx.DefaultSize, 0)
        gbSizer1.Add(self.add_btn, wx.GBPosition(6, 0), wx.GBSpan(1, 1 ), wx.ALL, 5)
        
        # Connect Events
	self.add_btn.Bind(wx.EVT_BUTTON, self.add_to_schedule)
	self.select_file.Bind(wx.EVT_BUTTON, self.choose_file)
	
        self.cancel_btn = wx.Button(self, wx.ID_ANY, u"Cancel",
            wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.cancel_btn, wx.GBPosition(6, 1),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancel)
        
        self.SetSizer(gbSizer1)
        self.Layout()
        gbSizer1.Fit(self)
        
        self.Centre(wx.BOTH)
    
    def __del__(self):
        pass
    
    def add_to_schedule(self, event):
        control = controller()
        date = self.schedule_date.GetValue().FormatISODate()
        time = self.schedule_time.GetValue()
        if len(time) == 4:
            time = '0'+time
        remark = self.schedule_remark.GetValue()
        file_dir = self.label_file_dir.GetLabel()
        interval = self.interval_value.GetValue()
        interval_type = self.frequency_type.GetString(self.frequency_type.GetCurrentSelection())
        control.add_to_schedule([file_dir,date,time,interval+'-'+interval_type,remark])
        #self.EndModal(wxdata.retCode)
    
    def choose_file(self, event):
        file_dialog = wx.FileDialog(None, 'Select file to schedule')
	if file_dialog.ShowModal() == wx.ID_OK:
	    self.label_file_dir.SetLabel(file_dialog.GetPath())

    def cancel(self, event):
        #self.EndModal(wxdata.retCode)