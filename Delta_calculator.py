import math
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
print("-----------------------")
delta = (B*B) - 4*(A*C)
print("Delta: ")
print(delta)

if delta > 0:
    pzd = math.sqrt(delta)
    x1 = (-B - pzd)/(2*A)
    x2 = (-B + pzd)/(2*A)
    print("X1: ")
    print(x1)
    print("X2: ")
    print(x2)
elif delta == 0:
    x0 = -B/(2*A)
    print("X0: ")
    print(x0)
else:
    print("no solutions/only imaginary solution")
