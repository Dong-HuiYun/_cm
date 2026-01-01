# 習題 1 : 請用程式驗證微積分基本定理

- `h`是每一段的寬度，將函數圖形切分成0.00001的細小寬度。

- `df(f, x)`算出了函數的微分（寬度為h時，該區域間線段的斜率）。

- `integral(f, a, b)`用左黎曼和求出了函數的積分。

    - 目的在於計算函數$f(x)$在區間[a,b]下方的總面積近似值。因此先從左端點開始（$x_0$），將x設爲左端點。初始面積設爲0。
    - 當x未達到右端點b時，計算以$f(x)$為高、以$h$為寬度的矩形面積，計算完後移動到下一個左端點。

```python

    x = a # 從左端點開始
    area = 0
    while x<b:
        area += f(x)*h
        x+=h
    return area

```
## 延伸討論：計算積分的方式
1. **右黎曼和**

```python

def integral(f, a, b):
    x = a
    area = 0
    while x < b:
        # 關鍵：計算面積時使用 (x + h) 作為自變量
        area += f(x + h) * h 
        x += h
    return area

```
2. **梯形法**

```python

def integral_trapezoid(f, a, b):
    h = 0.00001
    x = a
    area = 0
    while x < b:
        # 計算當前區間的梯形面積
        # (左端點高度 + 右端點高度) * 寬度 / 2
        area += (f(x) + f(x + h)) * h / 2
        x += h
    return area

```

3. **辛普森積分法**

```python

def integral_simpson(f, a, b):
    h = 0.00001
    x = a
    area = 0
    while x < b:
        mid = x + h/2  # 找到區間中點
        # 辛普森公式：(左端 + 4*中點 + 右端) * 寬度 / 6
        area += (f(x) + 4*f(mid) + f(x+h)) * (h / 6)
        x += h
    return area

```
4. **理查森外推法**

    利用兩個不同精度的估算值，透過特定的權重組合，將低階的誤差項完全抵消，從而獲得高階的精準度。

```python

def romberg(f, a, b, steps):
    # 第一列：基礎梯形法
    R = [[0] * (steps + 1) for _ in range(steps + 1)]
    h = b - a
    R[0][0] = 0.5 * h * (f(a) + f(b))
    
    for i in range(1, steps + 1):
        h /= 2
        # 計算新的梯形法結果
        sum_f = sum(f(a + (2*j - 1) * h) for j in range(1, 2**(i-1) + 1))
        R[i][0] = 0.5 * R[i-1][0] + h * sum_f
        
        # 進行權重調整（理查森外推）
        for k in range(1, i + 1):
            weight = 4**k
            R[i][k] = (weight * R[i][k-1] - R[i-1][k-1]) / (weight - 1)
            
    return R[steps][steps]

# 測試
print(f"龍貝格積分結果: {romberg(lambda x: x**3, 0, 2, 4)}")

```