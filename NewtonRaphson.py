def f(x):
    return x**3 - 4

def derivative_f(x):
    return 3*x**2


x = int(input())

tolerance = 0.001

while abs(f(x)) > tolerance:
    x = x - f(x)/derivative_f(x)


print("The root is: ", x)