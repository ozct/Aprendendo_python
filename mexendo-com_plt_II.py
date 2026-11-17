from sympy import symbols, sin, cos, plot

x1 = symbols('x')
x2 = symbols('x')

plot(sin(x1) + cos(x1), sin(x2), cos(x1))