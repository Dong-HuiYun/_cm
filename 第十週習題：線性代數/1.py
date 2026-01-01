# 寫程式用遞迴的方式計算行列式
import numpy as np

def calculate_determinant(matrix):
    """
    使用遞迴法計算矩陣的行列式
    """
    # 轉換為 numpy array 以方便切片操作
    matrix = np.array(matrix)
    n = matrix.shape[0]

    # 1. 終止條件：1x1 矩陣
    if n == 1:
        return matrix[0, 0]
    
    # 2. 終止條件：2x2 矩陣 (為了提升效率可直接計算)
    if n == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    det = 0
    # 3. 沿著第一列 (Row 0) 進行展開
    for j in range(n):
        # 取得餘子矩陣：劃去第 0 列與第 j 行
        # np.delete(arr, index, axis) 用於刪除指定行列
        minor = np.delete(np.delete(matrix, 0, axis=0), j, axis=1)
        
        # 正負號因子: (-1)^(i+j) -> 這裡 i 永遠是 0
        sign = (-1) ** j
        
        # 遞迴呼叫
        det += sign * matrix[0, j] * calculate_determinant(minor)
        
    return det

# --- 測試代碼 ---
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [3, 2, 0],
    [1, -1, 4],
    [0, 5, 2]
]

print(f"矩陣 A 的行列式: {calculate_determinant(A)}") # 預期為 0 (線性相關)
print(f"矩陣 B 的行列式: {calculate_determinant(B)}") # 預期為 -50
print(f"NumPy 內建驗證: {np.linalg.det(B):.0f}")