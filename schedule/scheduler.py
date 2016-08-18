import datetime, threading, subprocess
from db import db_aspects

class scheduler_exec:
    def __init__(self):
        threadEvent = threading.Event()
        def action():
            db_object = db_aspects()
            while not threadEvent.is_set():
                moment = datetime.datetime.today()
                schedules_for_moment = db_object.fetch_schedule_at_moment(moment)
                for eachSchedule in schedules_for_moment:
                    self.open_file(eachSchedule[1])
                threadEvent.wait(60)
        seconds_to_min = self.calculate_seconds_to_min()
        tObj = threading.Timer(seconds_to_min, action)
        tObj.start()
    
    def open_file(self, file_path):
        subprocess.Popen(file_path, shell=True, stdout=subprocess.PIPE)
        
    def calculate_seconds_to_min(self):
        current_moment = datetime.datetime.today()
        current_second = current_moment.second
        seconds_remaining = 60 - current_second
        return seconds_remaining