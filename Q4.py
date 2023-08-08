def get_season(month,day):
            if month in range(2,4):
                 return "Spring"
            elif month in range(5,8):
                 return "Summer"
            elif month in range(8,10):
                 return "Autum"
            else:
                 return "Winter"

def is_leap_year(year):
    # Check if the year is a leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def next_leap_year(year):
    # Find the next leap year after the given year
    while True:
        year += 1
        if is_leap_year(year):
            return year


year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day: "))

season = get_season(month,day)
print("Season:", season)

if is_leap_year(year):
    print(f"{year} is a leap year.")
    days_in_year = 366
    print(f"Number of days in the year {year}: {days_in_year}")
else:
    next_leap = next_leap_year(year)
    print(f"{year} is not a leap year.")
    print(f"The next leap year is: {next_leap}")



