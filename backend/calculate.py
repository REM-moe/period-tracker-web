from datetime import datetime
from datetime import timedelta, datetime

class Calculate_date:
    """Date
        year-month-day
        returns date
    """ 
    format = "%Y-%m-%d"

    def __init__(self, first_day_of_last_period, avg_cycle_length):
        self.first_day_of_last_period = datetime.strptime(first_day_of_last_period, "%Y-%m-%d")
        self.avg_cycle_length = int(avg_cycle_length)

    def fertile_window_start_day(self):
        start_day = self.first_day_of_last_period + timedelta(days = 10)
        return start_day.strftime(format = self.format)
    
    def fertile_window_end_day(self):
        start_day = self.first_day_of_last_period + timedelta(days = 10)
        end_day = start_day + timedelta(days = 5)
        return end_day.strftime(format = self.format)


    def next_period_date(self):
        next_period_date = self.first_day_of_last_period + timedelta(days = self.avg_cycle_length)
        return next_period_date.strftime(format= self.format)

    
    def ovulation_date(self):
        ovulation_date = self.first_day_of_last_period + timedelta(days = 14)
        return ovulation_date.strftime(format = self.format)
    
    def take_pregnancy_test(self):
        next_period_date = self.first_day_of_last_period + timedelta(days = self.avg_cycle_length)
        result = next_period_date + timedelta(days = 1)
        return result.strftime(format = self.format)
    