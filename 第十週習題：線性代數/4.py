# 寫程式用 特徵值分解來做 SVD
import numpy as np

def svd_via_evd(A):
    # 確保 A 是浮點數矩陣
    A = A.astype(float)
    m, n = A.shape
    
    # 1. 計算 V 和 奇異值 (透過 A^T * A)
    # AtA 是對稱矩陣，其特徵值必為非負實數
    AtA = A.T @ A
    eig_vals, V = np.linalg.eigh(AtA)
    
    # 特徵值排序 (eigh 是由小到大，我們需要由大到小)
    idx = np.argsort(eig_vals)[::-1]
    eig_vals = eig_vals[idx]
    V = V[:, idx]
    
    # 計算奇異值 sigma (特徵值的平方根)
    # 加上 clip 是為了避免極小負數(數值誤差)導致開根號出錯
    s = np.sqrt(np.clip(eig_vals, 0, None))
    
    # 2. 計算 U (透過 A * A^T)
    AAt = A @ A.T
    eig_vals_u, U = np.linalg.eigh(AAt)
    idx_u = np.argsort(eig_vals_u)[::-1]
    U = U[:, idx_u]
    
    # 3. 符號修正 (Sign Correction)
    # 由於 EVD 得到的 U 和 V 方向是獨立的，需滿足 Av = sigma * u
    # 我們通常固定 V，然後透過 u_i = A * v_i / sigma_i 來求得正確方向的 U
    # 這裡示範更嚴謹的修正法：
    for i in range(len(s)):
        if s[i] > 1e-10: # 奇異值不為 0 時
            actual_u = A @ V[:, i] / s[i]
            # 如果算出的方向與 EVD 的 U 方向相反，則翻轉 U 的該列
            if np.dot(actual_u, U[:, i]) < 0:
                U[:, i] = -U[:, i]

    return U, s, V.T

# --- 測試與驗證 ---
# 定義一個非方陣 (3x2)
A = np.array([[1, 2], 
              [3, 4], 
              [5, 6]])

U_custom, s_custom, Vt_custom = svd_via_evd(A)

# 官方 SVD 結果
U_np, s_np, Vt_np = np.linalg.svd(A)

print("自定義奇異值:", s_custom.round(4))
print("官方奇異值:  ", s_np.round(4))

# 驗證重建
Sigma = np.zeros(A.shape)
for i in range(len(s_custom)):
    Sigma[i, i] = s_custom[i]
A_reconstructed = U_custom @ Sigma @ Vt_custom

print("\n自定義 SVD 重建成功:", np.allclose(A, A_reconstructed))