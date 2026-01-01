import math

# 1. dft(f) 正轉換
def dft(f):
    N = len(f)
    F = []
    for k in range(N):
        sum_val = complex(0, 0)
        for n in range(N):
            # 尤拉公式 e^(-ix) = cos(x) - i*sin(x)
            angle = -2 * math.pi * k * n / N
            exp_val = complex(math.cos(angle), math.sin(angle))
            sum_val += f[n] * exp_val
        F.append(sum_val)
    return F

# 2. idft(F) 逆轉換
def idft(F):
    N = len(F)
    f = []
    for n in range(N):
        sum_val = complex(0, 0)
        for k in range(N):
            # 逆轉換角度為正 e^(ix) = cos(x) + i*sin(x)
            angle = 2 * math.pi * k * n / N
            exp_val = complex(math.cos(angle), math.sin(angle))
            sum_val += F[k] * exp_val
        # 進行正規化 (除以 N)
        f.append(sum_val / N)
    return f

# 3. 驗證某函數 f
original_f = [1.0, 2.0, 3.0, 4.0]
print(f"原始訊號: {original_f}")

# 執行正轉換
F_omega = dft(original_f)
# 執行逆轉換
recovered_f = idft(F_omega)

# 格式化輸出結果 (取實部)
print(f"還原訊號: {[round(x.real, 2) for x in recovered_f]}")