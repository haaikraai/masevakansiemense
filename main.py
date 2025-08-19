import os
from datetime import date, timedelta
from dataclasses import dataclass
import holidays
from functools import cache


@dataclass(frozen=True)
class DateRange:
    """
    Represents a range of dates, from a start date to an end date (inclusive).
    """
    start_date: date
    end_date: date
    holies = holidays.country_holidays('SouthAfrica')
    weekends: set[int]| None
    # def __post_init__(self, weekends: set[int]|None = {5,6}):
    #     print('running post init mewthod')
    #     if not weekends:
    #         self.weekends = {5,6}
    #     else:
    #         self.weekends = weekends


    @property
    @cache
    def dates(self) -> list[date]:
        """
        Returns a list with all the dates from start_date to end_date.
        The result is calculated on the first access and cached for subsequent calls.
        """
        date_list: list[date] = []
        current_date = self.start_date
        while current_date <= self.end_date:
            date_list.append(current_date)
            current_date += timedelta(days=1)
        return date_list
    
    @property
    @cache
    def nr_of_days(self) -> int:
        """
        Returns the number of days in the date range.
        Note the +1 because normal people count with dates inclusive.
        """
        return (self.end_date - self.start_date).days + 1

    @property
    def nr_of_working_days(self) -> int:
        '''
        The actual days leave will be taken in a requested date range.
        This returns all the days which do not fall on a public holiday, weekend or any such burdens to this industrialistic civilization
        '''
        # breakpoint()
        actual_working_days = [day for day in self.dates if self.holies.is_working_day(day)]
        
        return len(actual_working_days)


    @property
    def weekends(self) -> set[int]:
        return self.holies.weekend

    @weekends.setter
    def weekends(self, new_weekends: set[int]):
        self.holies.weekend = new_weekends
        

class Employee:
    def __init__(self, name: str, starting_date: date, anual_leave: int):
        self.name = name
        self.starting_date = starting_date
        self.anual_leave = anual_leave
        self.vacations: list[DateRange] = []
        self.weekends = {5,6}
        
    @property
    def months_employed(self) -> int:
        months = ((date.today().year - 1) - (self.starting_date.year + 1))*12 + date.today().month + (12-self.starting_date.month)
        return(months)
    
    @property
    def total_leave_acrued(self) -> int:
        days = self.months_employed*(self.anual_leave/12)
        return days
    
    @property
    def leave_days_remaining(self) -> int:
        days = self.total_leave_acrued - self.leave_days_taken
        return days

    @property
    def leave_days_taken(self) -> int:
        days = 0
        for vacation in self.vacations:
            days += vacation.nr_of_working_days
        return days

    def add_vaccation(self, start: date, end: date) -> int:
        
        vacation = DateRange(start_date=start, end_date=end, weekends=frozenset(self.weekends))
        self.vacations.append(vacation)


