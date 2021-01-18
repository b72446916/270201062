sort_list = [55,25,78,2,17,98,13,5]

def sel_sort(sort_list):
  for i in range(len(sort_list)):
    a = sort_list[0]
    b = sort_list[1]
  
  if a < b :
    a,b = sort_list
  elif a > b :
    a,b = b,a 
  elif a or b == sort_list[-1]:
    return -1