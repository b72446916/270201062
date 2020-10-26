number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter a number: "))
number3 = float(input("Please enter a number: "))

if number1 < number2 < number3 :
  print(number1)
elif number2 < number1 < number3 :
  print(number2)
elif number3 < number2 < number1 :
  print(number3)
elif number3 < number1 < number2 :
  print(number3)