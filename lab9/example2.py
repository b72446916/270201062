def get_reversed(x):
  x = [1,2,3,4]
  for i in x:
    x[i]=x[-1]
  print(x)

get_reversed(x)