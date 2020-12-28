def f(x):
  if x == 1:
    return 1
  elif x % 2 == 0:
      return f(x//2)
  else:
    return f(3*x+1)   
