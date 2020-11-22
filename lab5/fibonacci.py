n = int(input("How many fibonacci numbers do you want ?"))
n1 = 0
n2 = 1
if n == 1 :
    print(0)
else:
 print(n1)
 print(n2)
for i in range(2,n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)
