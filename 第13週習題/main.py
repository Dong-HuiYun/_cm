import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    # 1. 求特徵方程的根
    # np.roots 接收係數列表 [a_n, ..., a_0]
    roots = np.roots(coefficients)
    
    # 2. 處理數值精度問題
    # 將極小的項歸零，並將近乎相等的根合併
    # 使用 round 處理到小數點後 6 位，避免因精度問題導致 Counter 判斷重根失效
    refined_roots = []
    for r in roots:
        real_part = round(r.real, 6)
        imag_part = round(r.imag, 6)
        # 如果虛部極小，視為實根
        if abs(imag_part) < 1e-6:
            refined_roots.append(real_part + 0j)
        else:
            refined_roots.append(real_part + imag_part * 1j)
            
    # 3. 統計根的重數 (Multiplicity)
    # 這裡要注意共軛複根會成對出現，我們只需處理其中一個複根來生成 sin/cos
    root_counts = Counter(refined_roots)
    
    # 用於儲存處理過的複根，避免重複計算其共軛項
    processed_complex = set()
    terms = []
    c_idx = 1 # 積分常數 C_i 的計數器

    # 排序根，讓輸出較美觀 (實根優先，接著按大小排)
    sorted_unique_roots = sorted(root_counts.keys(), key=lambda r: (abs(r.imag) > 1e-6, r.real, r.imag))

    for r in sorted_unique_roots:
        if r in processed_complex:
            continue
            
        count = root_counts[r]
        alpha = r.real
        beta = r.imag
        
        # 情況 A: 實根 (虛部為 0)
        if abs(beta) < 1e-6:
            for m in range(count):
                x_pow = f"x^{m}" if m > 1 else ("x" if m == 1 else "")
                term = f"C_{c_idx}{x_pow}e^({alpha}x)"
                terms.append(term)
                c_idx += 1
        
        # 情況 B: 複數根 alpha + i*beta
        else:
            # 找到對應的共軛根 alpha - i*beta
            conjugate_r = alpha - 1j * beta
            # 複數根通常成對出現，且重數應該相同
            for m in range(count):
                x_pow = f"x^{m}" if m > 1 else ("x" if m == 1 else "")
                exp_part = f"e^({alpha}x)" if alpha != 0 else ""
                
                # Cosine 項
                terms.append(f"C_{c_idx}{x_pow}{exp_part}cos({abs(beta)}x)")
                c_idx += 1
                # Sine 項
                terms.append(f"C_{c_idx}{x_pow}{exp_part}sin({abs(beta)}x)")
                c_idx += 1
            
            processed_complex.add(r)
            processed_complex.add(conjugate_r)

    return "y(x) = " + " + ".join(terms)

print("--- 實數單根範例 ---")
coeffs1 = [1, -3, 2]
print(f"方程係數: {coeffs1}")
print(solve_ode_general(coeffs1))

# 範例測試 (2): 實數重根: y'' - 4y' + 4y = 0  特徵方程: lambda^2 - 4lambda + 4 = 0, 根: 2, 2
# 預期解: C_1e^(2x) + C_2xe^(2x)
print("\n--- 實數重根範例 ---")
coeffs2 = [1, -4, 4]
print(f"方程係數: {coeffs2}")
print(solve_ode_general(coeffs2))

# 範例測試 (3): 複數共軛根: y'' + 4y = 0  特徵方程: lambda^2 + 4 = 0, 根: 2i, -2i (alpha=0, beta=2)
# 預期解: C_1cos(2x) + C_2sin(2x)
print("\n--- 複數共軛根範例 ---")
coeffs3 = [1, 0, 4]
print(f"方程係數: {coeffs3}")
print(solve_ode_general(coeffs3))

# 範例測試 (4): 複數重根 (二重): (D^2 + 1)^2 y = 0  特徵方程: (lambda^2 + 1)^2 = 0, 根: i, i, -i, -i (alpha=0, beta=1, m=2)
# 預期解: C_1cos(1x) + C_2sin(1x) + C_3xcos(1x) + C_4xsin(1x)
print("\n--- 複數重根範例 ---")
coeffs4 = [1, 0, 2, 0, 1]
print(f"方程係數: {coeffs4}")
print(solve_ode_general(coeffs4))

# 範例測試 (5): 高階重根: y''' - 6y'' + 12y' - 8y = 0  特徵方程: (lambda - 2)^3 = 0, 根: 2, 2, 2
# 預期解: C_1e^(2x) + C_2xe^(2x) + C_3x^2e^(2x)
print("\n--- 高階重根範例 ---")
coeffs5 = [1, -6, 12, -8]
print(f"方程係數: {coeffs5}")
print(solve_ode_general(coeffs5))