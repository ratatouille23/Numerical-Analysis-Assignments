def f(x):
    return x**3-5*x-9

a = float(input())
b = float(input())
mid = (a + b) / 2

tolerance = 0.001

while abs(f(mid)) > tolerance:
    mid = a - (b-a) * f(a)/( f(b) - f(a))

    if f(a) * f(mid) < 0:
        b = mid

    else:
        a = mid

print("The root is: ", mid)