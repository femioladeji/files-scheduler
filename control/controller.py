import wxdata
import datetime
from db import db_aspects
class controller():
    
    def __init__(self):
        self.db_instance = db_aspects()
        
    def add_to_schedule(self, schedule_details):
        #frameObj = sched_frame()
        #schedule_data = ["x.txt", '12/04/2016', '12:00:00', '5 minutes', 'just playing']
        #start.add_to_display(schedule_details)
        interval = schedule_details[3].split('-')
        data_to_insert = schedule_details[0], schedule_details[1], schedule_details[2], int(interval[0]), interval[1], schedule_details[4]
        self.db_instance.insert_into_db(data_to_insert)
        wxdata.display_schedule.AppendItem(schedule_details)
        
    def update_schedules(self):
        all_scheds = self.db_instance.fetch_all_schedules()
        for each_sched in all_scheds:
            sched_details = [each_sched[1], each_sched[2], each_sched[3], str(each_sched[4])+'-'+each_sched[5], each_sched[6]]
            wxdata.display_schedule.AppendItem(sched_details)
                    