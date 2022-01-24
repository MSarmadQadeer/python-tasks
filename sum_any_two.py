print("Dear User You Are Going To Sum Any Two")
x = input("Enter Data 01: ")
y = input("Enter Data 02: ")
if x.lstrip("+,-").replace(".", "").isdigit() and y.lstrip("+,-").replace(".", "").isdigit():
    a = float(x)
    b = float(y)
    c = float(a+b)
    print(a, " + ", b, " = ", c)
else:
    a = str(x)
    b = str(y)
    c = str(a+b)
    print(a+" + "+b+" = "+c)
