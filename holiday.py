from datetime import date
import holidays

uk_holidays= holidays.UnitedStates()

for ptr in holidays.UnitedStates(years= 2019).items():
    print(ptr)

