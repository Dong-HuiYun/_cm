# 寫程式驗證 LU 分解，特徵值分解，SVD 分解後，可以相乘得到原矩陣
import numpy as np
from scipy.linalg import lu, eig, svd

# 定義一個 3x3 的隨機矩陣 A (確保其可對角化以便測試 EVD)
A = np.array([[4, 2, 1],
              [2, 5, 2],
              [1, 2, 4]], dtype=float)

def verify_reconstruction(name, original, reconstructed):
    # 使用 np.allclose 檢查數值是否在誤差範圍內相等
    success = np.allclose(original, reconstructed)
    print(f"[{name}] 重建成功: {success}")
    if not success:
        print(f"最大誤差: {np.max(np.abs(original - reconstructed))}")

# --- 1. LU 分解驗證 ---
# P 是置換矩陣, L 是下三角, U 是上三角
P, L, U = lu(A)
# 重組 A = P @ L @ U (注意：scipy 的 lu 返回的 P 是 P*A = L*U，故 A = P.T @ L @ U)
A_lu = P @ L @ U 
verify_reconstruction("LU Decomposition", A, A_lu)

# --- 2. 特徵值分解 (EVD) 驗證 ---
# vals 是特徵值, vecs 是特徵向量矩陣 Q
vals, vecs = eig(A)
# 重組 A = Q @ Lambda @ Q_inv
Lambda = np.diag(vals)
A_evd = vecs @ Lambda @ np.linalg.inv(vecs)
verify_reconstruction("Eigenvalue Decomposition", A, A_evd.real) # 取實部排除極小虛部誤差

# --- 3. 奇異值分解 (SVD) 驗證 ---
# U 是左奇異向量, s 是奇異值向量, Vt 是 V 的轉置
U_svd, s, Vt = svd(A)
# 重組 A = U @ Sigma @ Vt
Sigma = np.zeros(A.shape)
np.fill_diagonal(Sigma, s)
A_svd = U_svd @ Sigma @ Vt
verify_reconstruction("SVD Decomposition", A, A_svd)

# 打印結果觀察
print("\n原始矩陣 A:\n", A)
print("SVD 重建矩陣:\n", A_svd.round(2))