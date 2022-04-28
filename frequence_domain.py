from cmath import sin
from math import acos
import random

# declare variables
dt = 0.002
pi = acos(-1)
f1 = 8
f2 = 10
f3 = 40
t = 0

x = 4*sin(2*pi*f1*t) + 8*sin(2*pi*f2*t) + 2*sin(2*pi*f3*t)
# print("{:.4f}".format(t), "{:.4f}".format(x)) #4 decimal places

y = x + random.randint(t, dt)

print(y)
