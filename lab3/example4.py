age = float(input("Please enter your age :"))
normal_bus_ticket = 3
discount = 0.5
discount_price = normal_bus_ticket * discount
if 6 <= age <= 60   :
  if 6 <= age <= 18 :
   print(discount_price)
  else:
     print(normal_bus_ticket)
  else:
     print("You don't have to pay.")

   