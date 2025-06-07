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
# import holidays
# import holidays.countries

# holdies = holidays.SA()

# 1. Get test vacation range date range. Call it vacation_dates.
def get_vacation_range(start: datetime, end: datetime) -> list[datetime]:
    
    daterange = []
    # note here the +1. normal people count with dates inclusive
    for day in range((end-start).days+1):
        daterange.append(start+timedelta(days=day))
        print(daterange)
    return daterange
    


beginday = datetime(2025,6,1)
endday = datetime.today()
vacation = get_vacation_range(beginday,endday)
