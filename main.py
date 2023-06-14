import math
results = []

def solves(x, y, z):
    global results
    delta = y ** 2 - 4*x*z
    if delta >= 0:
        if x + y + z == 0:
            x1 = 1
            x2 = z/x
        elif x - y + z == 0:
            x1 = -1
            x2 = -z/x
        elif delta > 0:
            sqrts = math.sqrt(delta)
            x1 = (- y - sqrts ) / 2*x
            x2 = (- y + sqrts ) / 2*x
    results = results + [x1] + [x2]
    print(results)

print("Phuong trinh bac hai co dang: ")
i = input("Nhap a: ")
o = input("Nhap b: ")
p = input("Nhap c: ")
a = int(i)
b = int(o)
c = int(p)
if a == 0:
    print("Vo so nghiem")
solves(a, b, c)
