x = int(input("input x: ")) 
n = int(input("input n: "))
k=3
s = a = f =  1
c=2
b=1/2
g = x+x**3/3*b

for f in range(1,n):
    a += 2
    c += 2
    k += 2
    b=float(b*(a/c))
    s=b*x**k/k
    g=g+s
    
print("Answer 1 = ",g)

k=3
s = a = f =  1
c=2
b=1/2
g = x+x**3/3*b

while f < n:
    a += 2
    c += 2
    k += 2
    b=b*(a/c)
    s=b*x**k/k
    g=g+s
    f+=1
print("Answer 2 = ",g)
