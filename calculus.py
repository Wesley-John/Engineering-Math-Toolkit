import math

def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def integrate(f, a, b, n):
    h = (b - a) / float(n)

    integral_sum = 0.5 * h * (f(a) + f(b))

    for i in range(1, int(n)):
        integral_sum += f(a + i * h)

    return h * integral_sum