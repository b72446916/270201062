import random
def get_rand_list(N):
  b = int(input("type the first number>>"))
  e = int(input("type the second number>>"))
  random.sample(range(b, e), N)