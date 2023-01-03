import calendar

def Show-Calendar(weekday=6, year=2015):
  '''
  Function to display entered year calendar starting with entered weekday.
  '''
  if weekday in range(7):
     print(calendar.TextCalendar(firstweekday=weekday).formatyear(year))
  else:
     print("Entered weekday is not in range 0 to 6.")

if __name__ == "__main__":
  weekday = int(input("Enter a weekday number[0 is Monday, 6 is Sunday]:"))
  year = int(input("Enter any year:"))
  Show-Calendar(weekday, year)
