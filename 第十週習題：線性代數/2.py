# 寫程式做 LU 分解後，再計算行列式
import numpy as np

def lu_determinant(A):
    """
    透過手寫 LU 分解 (Doolittle Algorithm) 計算行列式
    """
    n = len(A)
    # 初始化 L 和 U
    L = np.eye(n)
    U = np.zeros((n, n))
    A = A.astype(float) # 確保浮點數運算
    
    # 進行 LU 分解
    for i in range(n):
        # 1. 計算 U 的第 i 列
        for k in range(i, n):
            sum_val = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_val
        
        # 2. 計算 L 的第 i 行
        for k in range(i + 1, n):
            if U[i][i] == 0:
                raise ValueError("矩陣奇異（對角線出現0），無法完成基礎 LU 分解")
            sum_val = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - sum_val) / U[i][i]
            
    # 行列式 = U 的對角線乘積
    det_U = 1.0
    for i in range(n):
        det_U *= U[i][i]
        
    return det_U, L, U

# --- 測試代碼 ---
B = np.array([
    [3, 2, 0],
    [1, -1, 4],
    [0, 5, 2]
])

try:
    det_val, L_mat, U_mat = lu_determinant(B)
    print("下三角矩陣 L:\n", L_mat)
    print("上三角矩陣 U:\n", U_mat)
    print(f"\n透過 LU 分解計算的行列式: {det_val:.2f}")
    print(f"NumPy 內建驗證: {np.linalg.det(B):.2f}")
except Exception as e:
    print(f"錯誤: {e}")