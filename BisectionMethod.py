def f(x):
    return x**3 - 4


a = int(input())
b = int(input())
mid = (a + b) / 2

tolerance = 0.0001

while abs(f(mid)) > tolerance:
    mid = (a + b) / 2

    if f(mid) * f(a) < 0:
        b = mid
    
    else:
        a = mid

print("The root is: ", mid)