import calendar

def to_day(month, date, year):
    '''
    Function to convert input date to day.
    '''
    day = calendar.weekday(year, month, date)
    return calendar.day_name[day].upper()

if __name__ == '__main__':
    inputDate = input().split(" ") #input format: MM DD YYYY
    month = int(inputDate[0])
    date = int(inputDate[1])
    year = int(inputDate[2])
    print(to_day(month, date, year))
