age = float(input("Please enter your age :"))
normal_bus_ticket = 3
discount = 0.5
discount_price = normal_bus_ticket * discount
 if age < 6  :
   print("You don't have to pay.")
 if age > 60 :
   print("You don't have to pay.") 
 if age < 18 :
   print(discount_price)
 else : 
   print(normal_bus_ticket)