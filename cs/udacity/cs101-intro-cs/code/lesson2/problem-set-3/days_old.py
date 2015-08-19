def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  assert not dateisBefore(year2, month2, day2, year1, month1, day1)
  days = 0
  while dateisBefore(year1, month1, day1, year2, month2, day2):
    year1, month1, day1 = nextDay(year1, month1, day1)
    days += 1
  return days

def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      return False
    return True
  return False
    
def daysInMonth(year, month):
  if month in (1,3,5,7,8,10,12):
    return 31
  if month == 2:
    if is_leap_year(year):
      return 29
    return 28
  return 30

def nextDay(year, month, day):
  if day == daysInMonth(year, month):
    if month == 12:
      year = year + 1
      month = 1
      day = 1
      return (year, month, day)
    month = month + 1
    day = 1
    return (year, month, day)
  day = day + 1
  return (year, month, day)
        
def dateisBefore(year1, month1, day1, year2, month2, day2):
  if year1 < year2:
    return True
  if year1 == year2:
    if month1 < month2:
      return True
    if month1 == month2:
      if day1 < day2:
        return True
  return False

def test():
  test_cases = [((2012,1,1,2012,2,28), 58), 
                ((2012,1,1,2012,3,1), 60),
                ((2011,6,30,2012,6,30), 366),
                ((2011,1,1,2012,8,8), 585 ),
                ((1900,1,1,1999,12,31), 36523)]
  for (args, answer) in test_cases:
    result = daysBetweenDates(*args)
    if result != answer:
      print "Test with data:", args, "failed"
    else:
      print "Test case passed!"

test()