import math
results = []

def solves(x, y, z):
    global results
    delta = y**2 - 4 * x * z
    if delta >= 0:
        if x + y + z == 0:
            x1 = 1
            x2 = z/x
        elif x - y + z == 0:
            x1 = -1
            x2 = -z/x
        elif delta > 0:
            sqrts = math.sqrt(delta)
            x1 = (- (y) - sqrts ) / (2*x)
            x2 = (- (y) + sqrts ) / (2*x)
    results = results + [x1] + [x2]
    print(results)

print("Phuong trinh bac hai co dang: ")
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
if a == 0:
    print("Khong the nhap so nay, vui long khoi dong lai chuong trinh")
    a = int(input("Nhap b: "))
if b == 0:
    print("Phuong trinh vo nghiem")

solves(a, b, c)
