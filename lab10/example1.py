def f(n):
  if n == 0:
    return 0 
  else:
    return f(n) + f(n) + f(n)