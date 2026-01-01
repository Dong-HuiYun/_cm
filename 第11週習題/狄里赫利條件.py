# 檢查數值上的積分收斂性或偵測極值點數量
import numpy as np
from scipy.integrate import quad

# 定義一個函數 f(t)
def f(t):
    return np.exp(-abs(t)) * np.cos(5*t)

# 1. 檢查絕對可積性 (條件一)
integral, error = quad(lambda t: np.abs(f(t)), -np.inf, np.inf)

if integral < np.inf:
    print(f"條件一通過：絕對積分值為 {integral:.4f}")

# 2. 數值尋找極值點 (條件二的模擬檢查)
t_points = np.linspace(-10, 10, 1000)
f_values = f(t_points)
extrema_count = np.sum(np.diff(np.sign(np.diff(f_values))) != 0)
print(f"在區間內偵測到約 {extrema_count} 個極值點")