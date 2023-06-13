import math


print("Phuong trinh bac hai co dang: ")
i = input("Nhap a: ")
o = input("Nhap b: ")
p = input("Nhap c: ")
a = int(i)
b = int(o)
c = int(p)
if a == 0:
    print("Vo so nghiem")
delta = b ** 2 - 4*a*b
if a + b + c == 0:
    x1 = 1
    x2 = c/a
elif a - b + c == 0:
    x1 = -1
    x2 = -c/a
elif delta >= 0:
    if delta == 0:
        x1 = x2 = -b/2*a
    elif delta > 0:
        sqrts = math.sqrt(delta)
        x1 = (-b - sqrts)/2*a
        x2 = (-b + sqrts)/2*a


print(x1, x2)
