# 寫程式做 PCA 主成份分析
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. 產生模擬數據 (具有強線性相關的 2D 數據)
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = 2 * x + 1 + np.random.normal(0, 2, 50)
X = np.vstack((x, y)).T

# --- 手寫 PCA 流程 (利用 SVD) ---
# A. 標準化 (Standardization)
X_mean = np.mean(X, axis=0)
X_centered = X - X_mean

# B. SVD 分解
# X = U * S * Vt, 其中 Vt 的列 (V 的行) 即為主成分方向
U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

# C. 選擇前 k 個主成分 (這裡 k=1)
W = Vt[0, :] 

# D. 投影數據到新空間
X_pca_manual = X_centered @ W.T

# --- Scikit-learn 版本驗證 ---
pca = PCA(n_components=1)
X_pca_sklearn = pca.fit_transform(X)

# --- 結果驗證 ---
print(f"手寫 PCA 前 5 筆:\n{X_pca_manual[:5]}")
print(f"Sklearn PCA 前 5 筆:\n{X_pca_sklearn.flatten()[:5]}")
print(f"\n兩者是否一致: {np.allclose(np.abs(X_pca_manual), np.abs(X_pca_sklearn.flatten()))}")

# 繪圖視覺化
plt.figure(figsize=(8, 4))
plt.scatter(X[:, 0], X[:, 1], alpha=0.5, label='Original Data')
plt.quiver(X_mean[0], X_mean[1], Vt[0,0]*S[0]/5, Vt[0,1]*S[0]/5, color='r', scale=1, label='PC1 Direction')
plt.quiver(X_mean[0], X_mean[1], Vt[1,0]*S[1]/5, Vt[1,1]*S[1]/5, color='g', scale=1, label='PC2 Direction')
plt.title("PCA: Principal Components Visualization")
plt.axis('equal')
plt.legend()
plt.show()