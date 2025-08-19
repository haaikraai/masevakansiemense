import datetime
from dataclasses import dataclass
from functools import cache

@dataclass(frozen=True, order=True)
class DateRange:
    """
    Represents a range of dates, from a start date to an end date (inclusive).
    """
    start_date: datetime.date
    end_date: datetime.date

    @property
    @cache
    def dates(self) -> list[datetime.date]:
        """
        Returns a list with all the dates from start_date to end_date.
        The result is calculated on the first access and cached for subsequent calls.
        """
        date_list: list[datetime.date] = []
        current_date = self.start_date
        while current_date <= self.end_date:
            date_list.append(current_date)
            current_date += datetime.timedelta(days=1)
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
    @cache
    def nr_of_working_days(self) -> int:





class Employee:
    """
    Represents an employee with vacation days and remaining leave days.
    """
    vacations: list[DateRange]
    leave_days_remaining: int | None

    def __init__(self):
        self.vacations = []
        self.leave_days_remaining = None

# Example Usage:
if __name__ == "__main__":
    employee = Employee()
    today = datetime.date.today()
    seven_days_from_now = today + datetime.timedelta(days=7)
    employee.vacations.append(DateRange(today, seven_days_from_now))
    print(employee.vacations[0].dates)
    print(f"Employee vacations: {employee.vacations}")
    print(f"Start Date: {employee.vacations[0].start_date}, End Date: {employee.vacations[0].end_date}")
    print(f"All dates in range: {employee.vacations[0].dates}")
