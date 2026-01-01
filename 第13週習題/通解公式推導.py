import sympy as sp

# 定義符號
x = sp.Symbol('x')
y = sp.Function('y')(x)
a, b, c = sp.symbols('a b c')

# 定義微分方程: a*y'' + b*y' + c*y = 0
ode = a*sp.diff(y, x, 2) + b*sp.diff(y, x) + c*y

# 求解 ODE
solution = sp.dsolve(ode, y)
print(f"通解公式為: {solution}")