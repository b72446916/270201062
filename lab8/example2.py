def is_prime(i):
  i = int(input("type a number: \n"))
  while i > 2 : 
    if i % 2 == 0:
      print(i,"is a prime number")
def print_primes_between(j,k):
  j = int(input("type a number:\n"))
  k = int(input("type a number:\n"))
  if j > k :
    print("invalid value.type a smaller value.")
  for i in range(j,k):
    while i > 2 :
      if i % 2 != 0  :
        print(i,"is a prime number.")
        break
print(print_primes_between("",""))      
print(is_prime(i))