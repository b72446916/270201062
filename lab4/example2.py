year = int(input("Please enter a year : "))
if year % 4 == 0 and year % 400 == 0 :
  print(year , "is a leap year")
elif year % 4 == 0 :
  print(year, "is a century year.")

else :
  print("This year isn't a leap year.")