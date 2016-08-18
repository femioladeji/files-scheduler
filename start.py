from schedule import sched_frame
from dialog import dialog_newsched
from controller import controller
from scheduler import scheduler_exec
import wx


sch = scheduler_exec()

class gui_transformation():
    def __init__(self):
        my_control = controller()
        mysched = wx.App()
        my_frame = sched_frame(None)
        my_control.update_schedules()
        my_frame.Show()
        mysched.MainLoop()
        #scheduler_object = scheduler_exec()
        
        
gui = gui_transformation()