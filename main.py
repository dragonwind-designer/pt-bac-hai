import math
results = []

def solves(x, y, z):
    global results
    delta = y ** 2 - 4*x*z
    if delta >= 0:
        if delta == 0:
            x1 = x2 = -y/2*x
            results = results + [x1]
        elif delta > 0:
            x1 = (-y - math.sqrt(delta))/2*x
            x2 = (-y + math.sqrt(delta))/2*x
            results = results + [x1] + [x2]
    elif delta < 0:
        print("Phuong trinh vo nghiem")
        results = []
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
