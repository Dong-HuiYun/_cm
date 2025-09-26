import cmath, random

def eval_poly(coeffs, x):
    """Horner 法計算多項式值"""
    result = 0
    for coeff in reversed(coeffs):
        result = result * x + coeff
    return result

def eval_poly_derivative(coeffs, x):
    """計算多項式在 x 的導數"""
    n = len(coeffs) - 1
    result = 0
    for coeff in reversed(coeffs[1:]):
        result = result * x + coeff * n
        n -= 1
    return result

def newton_root(coeffs, max_iter=2000, tol=1e-12):
    """用 Newton–Raphson 找一個根（可能是複數）"""
    x = complex(random.uniform(-1,1), random.uniform(-1,1))  # 隨機初始值
    for _ in range(max_iter):
        fx = eval_poly(coeffs, x)
        dfx = eval_poly_derivative(coeffs, x)
        if abs(dfx) < 1e-14:  # 避免除以 0
            x += (random.random() + random.random()*1j) * 0.1
            continue
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def deflate(coeffs, root):
    """多項式除法，把 (x - root) 除掉"""
    n = len(coeffs) - 1
    new_coeffs = [coeffs[-1]]  # 最高次
    for i in range(n-1, -1, -1):
        new_coeffs.append(coeffs[i] + root * new_coeffs[-1])
    remainder = new_coeffs.pop()  # 最後一項是餘數
    if abs(remainder) > 1e-6:
        raise RuntimeError("Deflation error, remainder not ~0")
    return list(reversed(new_coeffs))

def all_roots(coeffs):
    """逐步找所有根"""
    roots = []
    poly = coeffs[:]
    while len(poly) > 2:
        r = newton_root(poly)
        roots.append(r)
        poly = deflate(poly, r)
    # 最後剩下 ax + b
    if len(poly) == 2:
        roots.append(-poly[0]/poly[1])
    return roots

# 測試
coeffs = [-6, 11, -6, 1, 9, 11]  # 11x^5 + 9x^4 + x^3 - 6x^2 + 11x -6
roots = all_roots(coeffs)

for i, r in enumerate(roots):
    print(f"Root {i+1}: {r.real:.6f} + {r.imag:.6f}j")
