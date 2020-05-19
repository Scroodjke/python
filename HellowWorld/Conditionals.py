n=float(input("n = "))
if n // 100 + n % 10 == n // 10 % 10 * 2:
    print("true")
else:
    print("False")
#2
x = int(input("Enter x "))

y = int(input("Enter y "))

if (((x+3)**2)+((y+3)**2) < 9.0) and ((y > 2*x) or (y < x/2)):

   print("belong")

else:

print("not belong")