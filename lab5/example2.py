x = int(input("How many numbers are there :"))
even_numbers = 0
for i in range (x):
  num = int(input("Enter a number."))
  if not num % 2 == 0:
    even_numbers += num
print(even_numbers * x / 100)


  


