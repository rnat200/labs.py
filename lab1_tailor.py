import math


def taylor_exp(x: float, eps: float) -> float:
    sum = 1.0
    total_sum = sum
    step = 1

    while abs(sum) >= eps:
        sum *= x / step
        total_sum += sum
        step += 1

    return total_sum

eps = float(input("Enter the acuracy"))
x = float(input("Enter the x"))
print (f"e^{x} = {taylor_exp(5,eps)} , with acuracy = {eps}")
