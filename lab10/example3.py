def f(x):
  if not f(x,list):
    return x
  else:
    sum = 0
    for i in x:
      sum += f(i)
      return i  