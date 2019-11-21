import math

#1
a = math.sqrt(1+math.sqrt(1+math.sqrt(1+math.sqrt(1))))
print(a)
b = (1+math.sqrt(5)/2)
print(b)
print(a < b)
#2
a=math.pi**math.e
print(a)
b=math.e**math.pi
print(b)
print(a<b)
#3
a=math.log(6,5)
print(a)
b=math.log(7,6)
print(b)
print(a<b)
#4
a=(math.tan (math.radians(10)) ** 6) + (math.tan (math.radians(50)) **6) + (math.tan (math.radians(70)) ** 6)
print(a)        
b=433
print(b)
print(a==b)

#5
a = (16 * (math.cos(3600) / 17))
print(a)
b = math.sqrt(34 - 2 * math.sqrt(17))\
     + \
math.sqrt(17) - 1 + \
2 * math.sqrt(17 + 3*math.sqrt(17) - math.sqrt(170 + 38 * math.sqrt(17)))
print(b)
print(a==b) 