import datetime
import sqlite3
import os.path

class db_aspects:
    
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.realpath(__file__)), "schedule.db"))
        self.con_handle = self.conn.cursor()
        
        
        # Create table
        self.con_handle.execute(
        '''create table if not exists schedule
        (schedule_id INTEGER PRIMARY KEY AUTOINCREMENT, filedir text, date text, time text,
        interval_value INTEGER, interval_unit TEXT, remark TEXT)''')
        
        # Insert a row of data
        
        # Save (commit) the changes
        self.conn.commit()
        
        # We can also close the cursor if we are done with it
        #self.con_handle.close()
        
    def insert_into_db(self, data_to_insert):
        self.con_handle.execute('insert into schedule (filedir, date, time, interval_value, interval_unit, remark) values(?,?,?,?,?,?)', data_to_insert)
        
        self.conn.commit()
    
    def fetch_all_schedules(self):
        self.con_handle.execute('select * from schedule')
        return self.con_handle
        
    def fetch_schedule_at_moment(self, moment):
        date, time = self.change_datetime_format(moment)
        self.con_handle.execute('select * from schedule where date = ? AND time = ?', [date, time])
        return self.con_handle
    
    def change_datetime_format(self, moment):
        date = str(datetime.date(moment.year, moment.month, moment.day))
        time = str(datetime.time(moment.hour, moment.minute))
        time = time[:(len(time)-3)]
        datetimetuple = date, time
        return datetimetuple