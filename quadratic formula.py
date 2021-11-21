import math
a = int(input("what is a:"))
b = int(input("what is b:"))
c = int(input("what is c:"))

numerator1 = -1*b + math.sqrt((b**2)-4*a*c)
denominator1 = 2*a
y = str(numerator1/denominator1)

numerator2 = -1*b - math.sqrt((b**2)-4*a*c)
denominator2 = 2*a
z = str(numerator2/denominator2)

print("x="+ y + "x="+ z)
