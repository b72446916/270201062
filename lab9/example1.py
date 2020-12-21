
def harmonic(x):
  if x == 0:
    return 0
  else:  
    return 1/x + harmonic(x-1)
print(harmonic(5))