year = int(input("Please enter a year."))
if year % 4 == 0 and year % 400 == 0 :
  print(year , "is a leap year")
else :
  print("This year isn't a leap year.")