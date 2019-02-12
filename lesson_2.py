a = float(input(" Enter a>"))
b = float(input(" Enter b>"))
c = float(input(" Enter c>"))

D = b**2-4*a*c
if D >= 0:
    x1 = (-b+D**(1/2))/(2*a)
    x2 = (-b-D**(1/2))/(2*a)
    print(f"X1= {x1:.5f}")
    print(f"X2= {x2:.5}")

else:
    print("error")