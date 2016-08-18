from gui.startframe import MainFrame
#from controller import controller
#from scheduler import scheduler_exec
import wx


#sch = scheduler_exec()

class Application():
    def __init__(self):
        #my_control = controller()
        scheduler = wx.App()
        my_frame = MainFrame(None)
        #my_control.update_schedules()
        my_frame.Show()
        scheduler.MainLoop()
        #scheduler_object = scheduler_exec()
        
app = Application()