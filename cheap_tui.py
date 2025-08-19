import cutie
from datetime import date
from main import Employee

sandra = Employee('sandra', starting_date=date(2023,3,1), anual_leave=15)
print(sandra.vacations)

sandra.weekends = {1,4,5,6}
print('past breakpoint now')

sandra.add_vaccation(date(2025,6,10), date(2025,6,20))
print(sandra.leave_days_remaining)
pass
