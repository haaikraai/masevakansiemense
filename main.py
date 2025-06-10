import os
import datetime
import time
from datetime import datetime, date, timedelta
import dateutil as datediff
import calendar
from pandas import date_range
import pandas

from rich.pretty import pprint as pp
from rich import print
import holidays
# import holidays.countries

# holdies = holidays.SA()

holy_holies = holidays.country_holidays('ZA')

holy_holies.weekends = {1,4,5,6}

class VacationRange:
    def __init__(self):
        self.start_date: date
        self.end_date: date
        self.daterange: list[date]
        self.actual_leave_days: list[date]

class EmployeeLeave:
    def __init__(self):
        self.startDate: date
        self.allowed_anual_leave: int
        self.total_leave_received: int
        self.vacations: list[VacationRange]

    

# 1. Get test vacation range date range. Call it vacation_dates.
def get_vacation_range(start: date, end: date) -> list[date]:
    '''
    Using a list rather than proposed set, because sets do not support subscription.
    Will change to set for arithmetic.
    Ideally, should be a class containing both...hmm
    '''
    daterange = list()
    
    # note here the +1. normal people count with dates inclusive
    for day in range((end-start).days+1):
        daterange.append(start+timedelta(days=day))
    
    return daterange

def get_actual_leave_days(daterange: list[date]) -> list[date]:
    actual_days = [day for day in daterange if not holy_holies.is_working_day(day)]
    return actual_days

def total_leave_accrued(start_date: date, annual_leave: int) -> int:
    '''
    Get the leave an employee has right NOW, base on the date of starting to work and the leave given per year.

    This method (tobe, not in a class yet) works in montly units. Therefore, it converts anual leave to montly leave (anual_leave/12) and also automatically conciders pro-rate leave days for partially worked years.
    '''
    monthly_leave = annual_leave/12
    
    employed_range = (date.today().year - 1) - (start_date().year + 1)*12 + date.today().month + start_date.month()

beginday = date(2024,5,26)
endday = date(2024,6,20)
vacation_range = get_vacation_range(beginday,endday)
print(vacation_range)
print(get_actual_leave_days(vacation_range))
