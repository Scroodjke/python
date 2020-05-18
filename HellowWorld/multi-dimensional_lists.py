from math import *
 
def f(k):
    return sin(k/3.12)+cos(k*k)-9.1*(sin(3*k))
 
def g(n):
    return cos(2*n)/1.12-cos(3*n-2)+6.15
 
a= []
h = 1
for k in range (1,5):
    a.append([])
    for n in range(1,5):
        element = n* f(k)+sin(k)*g(n)
        a[k-1].append(element)
 
        print('% 10.4f' % a[k-1][n-1], end=" ")
 
        if k < n:
            h *= a [k-1][n-1]
    print()
minimum =[]
for i in a:
    if i < 0:
        neg.append(i)
    elif i > 0:

        pos.append(i)
maximum = max(max(a))
result = minimum*maximum
print("\n""Min element",minimum)
print("Max element",maximum)
print("multiplication of min and max elements: ",result)
