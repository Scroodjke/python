import math
#1

a = float(input("Enter the number in radians:"))
b = math.sin(math.radians(a))*2 + math.sin(math.radians(a))*5 - math.sin(math.radians(a)) * 3 / math.cos(math.radians(a)) + 1 - 2 * (math.sin(math.radians(a)) * 2)**2
print(b)
z = 2 * math.sin(math.radians(a))
print(z)
a = float(input("cathetus 1: "))
b = float(input("cathetus 2: "))
c = math.hypot(a, b)
h = (a+b+c)/2
print(c)
print(h)

