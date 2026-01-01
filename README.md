# 期末作業

## 著作狀態聲明

習題1到3自己完成，並依靠gemini加强理解其中的數學意義。

[期中作業](https://github.com/Dong-HuiYun/_cm/tree/main/%E6%9C%9F%E4%B8%AD%E4%BD%9C%E6%A5%AD)

[習題 1 : 請用程式驗證微積分基本定理](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%BF%92%E9%A1%8C1)

[習題 2 : 請寫程式求解二次多項式的根](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%BF%92%E9%A1%8C2)

[習題 3 : 請寫程式求解三次多項式的根](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%BF%92%E9%A1%8C3)

[習題 4 : 請寫一個函數 root(c) 求出 n 次多項式的根](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%BF%92%E9%A1%8C4)

[第二週習題：有限體](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%AC%AC%E4%BA%8C%E9%80%B1%E7%BF%92%E9%A1%8C)

[第三週習題：幾何學：（點，線，圓）世界的建構](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%AC%AC%E4%B8%89%E9%80%B1%E4%BD%9C%E6%A5%AD)

[第八週習題：機率統計 - 檢定背後的數學原理](https://gemini.google.com/share/5152a2870b84)

[第九週習題：資訊理論](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%AC%AC%E4%B9%9D%E9%80%B1%E7%BF%92%E9%A1%8C%EF%BC%9A%E8%B3%87%E8%A8%8A%E7%90%86%E8%AB%96)

[第十週習題：線性代數](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%AC%AC%E5%8D%81%E9%80%B1%E7%BF%92%E9%A1%8C%EF%BC%9A%E7%B7%9A%E6%80%A7%E4%BB%A3%E6%95%B8)

[第11週習題：請寫出傅立葉正轉換和逆轉換的函數](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%AC%AC11%E9%80%B1%E7%BF%92%E9%A1%8C)

[第13週習題：請寫程式求解常係數齊次常微分方程](https://github.com/Dong-HuiYun/_cm/tree/main/%E7%AC%AC13%E9%80%B1%E7%BF%92%E9%A1%8C)


## Gemini提示詞設定
```markdown
When I ask math questions, please respond in the following format:
1. First, confirm the problem and known conditions.
2. Use key steps for derivation, listing necessary formulas or equations, and can attach cutting-edge Python code for explanation.
3. Provide the final answer, with a brief explanation of the thought process.
If there are different solutions, you can provide the most intuitive or efficient one.
Please keep the response structure clear and the language concise.

```

## 期中作業

[csmaca碰撞機率模擬與分析](https://github.com/Dong-HuiYun/_cm/tree/main/%E6%9C%9F%E4%B8%AD%E4%BD%9C%E6%A5%AD)

### 功能介紹

主要用途：模擬無線網路中（如Wi-Fi）CSMA/CA機制的碰撞機率，並與理論公式進行比較。

- CSMA/CA：載波偵聽多重存取/碰撞避免，是Wi-Fi使用的通道存取協議

- Backoff機制：當節點要傳送資料時，會隨機選擇一個退避時間（0到CW之間）

- 碰撞發生：當多個節點選到相同的退避時間最小值時

![CSMA/CA示例圖](../image/csmaca.jpg)

- 模擬函數`simulate_collision_probability`

    - 每個節點隨機選擇一個退避值（0到CW）

    - 找出最小值

    - 檢查有多少節點選擇了這個最小值

    - 如果超過一個節點，則發生碰撞

- 主要分析：

    - 節點數從2到50（每隔2個節點）

    - 固定競爭窗口 CW = 31（即32個時槽）

    - 每個設定進行10,000次模擬

### 運用到的數學

#### 1. 離散均勻分配 (Discrete Uniform Distribution)
在模擬中，每個節點會從 $[0, CW]$ 的區間內隨機選擇一個整數作為倒數值。
*   **數學表達：** 設隨機變數 $X$ 為節點選擇的數值，則 $X \sim U(0, CW)$。
*   每個數值被選中的機率皆為 $P(X = k) = \frac{1}{CW+1} = \frac{1}{W}$（其中 $W$ 為窗口大小）。

#### 2. 獨立事件 (Independent Events)
程式假設 $N$ 個節點的行為是相互獨立的。這意味著一個節點選什麼數字，不會影響另一個節點。
*   在計算理論機率時，我們使用乘法原理：$P(A \cap B) = P(A) \cdot P(B)$。

#### 3. 互補事件機率 (Complementary Probability)
程式計算「碰撞機率」的方式是先計算「成功傳輸（不碰撞）的機率」，再用 1 減去它。
*   **公式：** $P(\text{Collision}) = 1 - P(\text{Success})$
*   **定義：** 「成功傳輸」是指在所有節點中，**恰好只有一個節點**選到了最小的倒數值。

#### 4. 組合數學與機率模型 (Combinatorics & Probability Model)
在 `theoretical_collision_probability` 函數中，使用了以下公式：
$$P(\text{Success}) = \sum_{k=0}^{CW} \left( N \cdot \frac{1}{W} \cdot \left( \frac{W-1-k}{W} \right)^{N-1} \right)$$
這個公式的組成包含了：
*   **恰好一者選中 $k$：** $C(N, 1) = N$。
*   **該節點選中 $k$ 的機率：** $\frac{1}{W}$。
*   **剩餘 $N-1$ 個節點都選中比 $k$ 大的數值的機率：** $\left( \frac{W-1-k}{W} \right)^{N-1}$。
*   **全機率定理 (Law of Total Probability)：** 因為最小值 $k$ 可能是 $0, 1, \dots, CW$ 中的任何一個，所以對所有 $k$ 進行累加。

#### 5. 蒙地卡羅模擬 (Monte Carlo Simulation)
`simulate_collision_probability` 函數運用了蒙地卡羅方法。
*   當理論模型太過複雜或難以推導時，我們通過大量重複隨機試驗（`trials=10000`），利用**大數法則 (Law of Large Numbers)** 來逼近真實的機率分佈。
*   模擬結果（藍點）會隨著試驗次數增加而收斂於理論曲線（紅線）。

#### 6. 統計分析與數據可視化
*   **變數依賴關係：** 探討節點數 $N$（自變數）與碰撞機率 $P$（應變數）之間的關係。
*   **趨勢分析：** 程式展示了隨著 $N$ 增加，碰撞機率呈非線性增長的特性（飽和曲線）。

### 參考資料

[google ai studio](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221OlOuVfRKeh85m68PjIrpe0cTiYxlxm8X%22%5D,%22action%22:%22open%22,%22userId%22:%22104108532823114063447%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)


## 習題 1 : 請用程式驗證微積分基本定理

![筆記](../image/ch1.jpg)

### 程式碼説明

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
### 延伸討論：計算積分的方式

1. **右黎曼和**

2. **梯形法**

3. **辛普森積分法**

4. **理查森外推法**

    利用兩個不同精度的估算值，透過特定的權重組合，將低階的誤差項完全抵消，從而獲得高階的精準度。

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/3ed135cc79ee)


## 習題 2 : 請寫程式求解二次多項式的根

![筆記](../image/ch2.jpg)

`root(a,b,c)`函數是利用一元二次方程式求根公式得出其多項式的根，判別式 $\Delta=b^2+4ac$。

- 當$\Delta$大於0時，方程式有兩解
- 當$\Delta$等於0時，方程式僅一解
- 當$\Delta$小於0時，方程式無實數解

```python
def root(a, b, c):
    judge = b ** 2 - 4 * a * c
    if judge > 0:
        ans1 = (-b + math.sqrt(judge)) / (2 * a)
        ans2 = (-b - math.sqrt(judge)) / (2 * a)
        print("answer: ", ans1, ans2)
    elif judge == 0:
        ans = -b / (2 * a)
        print("answer:", ans)
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-judge) / (2 * a)
        print("answer: ", f"{real}+{imag}i", f"{real}-{imag}i")
```

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/e01709e79717)

## 習題 3 : 請寫程式求解三次多項式的根

![筆記](../image/ch3.jpg)

`root3(a, b, c, d)`函數是利用一元二次方程式求根公式得出其多項式的根，判別式 $\Delta = \frac{q^2}{4} + \frac{p^3}{27}$。

- 當$\Delta$大於0時，有一實根、兩個共軛複數根
- 當$\Delta$等於0時，實數且有重根
- 當$\Delta$小於0時，三個不相等的實根

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/7ae678580a3f)

## 習題 4 : 請寫一個函數 root(c) 求出 n 次多項式的根
n>=5 的時候，數學上證明沒有公式 -- 伽羅瓦定理，因此對於高項多項式，可以運用：牛頓法、伴隨矩陣法來找出根。

伴隨矩陣:對於首項係數為 1 的多項式 $x^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0 = 0$，其伴隨矩陣 $C$ 定義如下

$$C = \begin{bmatrix}
0 & 0 & \dots & 0 & -a_0 \\
1 & 0 & \dots & 0 & -a_1 \\
0 & 1 & \dots & 0 & -a_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & 1 & -a_{n-1}
\end{bmatrix}$$

矩陣 $C$ 的特徵值即為該多項式的根。

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/23600b81945f)

## 第二週習題：有限體

![筆記](../image/week2.jpg)

有限體 (Finite Field)，又稱伽羅瓦體 (Galois Field)，是指包含有限個元素的代數結構。
一個集合 $F$ 若要稱為「有限體」，必須滿足：

- 加法與乘法的封閉性

- 結合律

- 交換律

- 單位元存在

- 反元素存在（乘法部分不含零）

- 分配律

- 集合中的元素數量為有限個

### 延伸討論：有限體的線性方程組求解

$ax + b \equiv c \pmod p$

**第一步：移項（利用加法反元素）**

$$ax \equiv c - b \pmod p$$

**第二步：係數歸一（利用乘法反元素）**

$$x \equiv a^{-1} \cdot (c - b) \pmod p$$

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/e4b4abbf4585)


## 第三週習題：幾何學：（點，線，圓）世界的建構

![筆記](../image/week3.jpg)

### 定義『點，線，圓』
 - **點**：點只有位置，沒有大小（寬度、長度或厚度）。坐標表示：在二維空間中，點 $P$ 表示為 $(x, y)$。
-  **線**：點的集合，具有無限的長度但沒有寬度與厚度。兩點可以決定唯一一條直線。
公式：斜截式 $y = mx + b$。
- **圓**：平面上到一固定點（圓心）之距離等於定長（半徑）的所有點的軌跡。公式：設圓心為 $(h, k)$，半徑為 $r$，則方程式為：

$$(x - h)^2 + (y - k)^2 = r^2$$

### 定義一個三角形物件

組成要素：

- 三個頂點：$P_1, P_2, P_3$。
- 三條邊：$a, b, c$。
- 三個內角：$\angle A, \angle B, \angle C$。

存在條件（三角形不等式）：任意兩邊之和大於第三邊（例如 $a + b > c$）。

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/2bf2e368555e)

## 第八週習題：機率統計 - 檢定背後的數學原理

| 條件 | 選擇檢定 | 分布模型 |
|-------|-------|-------|
| 母體標準差 $\sigma$ 已知 | z 檢定 | 標準常態分布 $N(0, 1)$ |
| 母體標準差 $\sigma$ 未知 且 $n \ge 30$ | z 檢定 (可用 $s$ 代替) | 近似常態分布 |
| 母體標準差 $\sigma$ 未知 且 $n < 30$ | t 檢定 | $t$ 分布 (隨自由度變化) |

$$\text{檢定統計量} = \frac{\text{觀測值} - \text{假設值}}{\text{標準誤差}}$$

- z 檢定公式當我們知道母體標準差

 $\sigma$ 時：$$z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$$

- t 檢定公式當母體標準差未知，必須用樣本標準差 $s$ 來估計時：$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$$

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/6d02714c9a95)

## 第九週習題：資訊理論

![筆記](../image/week9.jpg)

1. **計算一公平銅板，連續投擲 10000 次，全部得到正面的機率。**
    ```python
    # 浮點數下溢
    prob = 0.5 ** 10000
    print(prob)
    ```
    僅用`float`來計算會造成浮點數下溢，因此需以對數機率的計算，將極小的乘法轉換為加法，避免下溢。

2. 用 $\log(P^N) = N \times \log(P)$ 計算  $\log(P^N)$ ，然後代入P=0.5，算出 $\log(0.5^10000)$

- $\log_e$ (自然對數, ln)：在 Python 中 math.log() 預設是這個。

    ```markdown
    自然對數 (log_e):
    10000 * log_e(0.5) = -6931.4718
    ```

- $\log_{10}$ (常用對數)：這最適合用來直觀地理解數字的數量級（即 $10$ 的幾次方）。

    ```markdown
    常用對數 (log_10):
    10000 * log_10(0.5) = -3010.3000
    ```

- $\log_2$ (二進位對數)：在這個 $P=0.5$ 的情況下，這個會特別整齊。

    ```markdown
    二進位對數 (log_2):
    10000 * log_2(0.5) = -10000.0
    ```
3. 計算『熵，交叉熵，KL 散度，互熵（互資訊）』
- 熵 (Entropy)：衡量「自己」有多亂。
- KL 散度 (KL Divergence)：衡量「兩者」的差異距離。
- 交叉熵 (Cross Entropy)：等於「自己的亂」+「兩者的差異」。
- 互資訊 (Mutual Information)：衡量「關聯性」。

4. 驗證 cross_entropy(p,p) > cross_entropy(p,q), 當 q != p 時
5. 『7-4 漢明碼』的編碼
是一種前向錯誤更正碼，能將 4 位元的資料 (data) 編碼成 7 位元的碼字。
 (7, 4) 代表總碼長（Code length）為 7 位元，其中有效數據位元（Data bits）為 4 位元，因此校驗位元（Parity bits）為 3 位元（$7 - 4 = 3$）。
6. 夏農兩大定理
- 夏農信道編碼定理：如何有效地編碼
- 夏農-哈特利定理：一個通道究竟能傳多快

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/f06e78b92837)

[gemini對話記錄](https://gemini.google.com/share/c117c27bb0e8)

[計算機概論_偵錯碼_1.漢明碼(hamming Code)](https://youtu.be/yslPYECVWzI?si=Aw_-C1eL_VCFXIuu)

## 第十週習題：線性代數

- 縮放，旋轉，平移

    - 2D

        縮放：
        $$S(s_x, s_y) = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
        旋轉：
        $$R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
        平移
        $$T(t_x, t_y) = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix}$$

    - 3D

        平移： $T(t_x, t_y, t_z)$ 在矩陣最右側一列填入偏移量。

        縮放： $S(s_x, s_y, s_z)$ 在對角線填入縮放倍率。

        旋轉 (以繞 $z$ 軸為例)：
        $$R_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

- PCA 主成份分析

![圖表](../image/PCA主成份分析.png)

**PCA 在高相關性數據上的有效性。由於 PC1 捕獲了數據的絕大部分變異，這組二維數據非常適合進行降維處理。**

### 參考資料

[manus圖表分析](https://manus.im/share/uGqflUyzYUZ0KpAi39uuIV)

[chatgpt套件安裝問題](https://chatgpt.com/share/69566f5b-e340-8000-a01b-30bbfaa60c27
)

[gemini對話記錄](https://gemini.google.com/share/871e8f2781fd)

## 第11週習題：請寫出傅立葉正轉換和逆轉換的函數

- 傅立葉正轉換）（Forward FT）：從「時域 (Time Domain)」轉換到「頻域 (Frequency Domain)」。

- 傅立葉逆轉換 (Inverse FT)：從「頻域」還原回「時域」。

### 延伸討論

- 狄里赫利條件

要滿足狄里赫利條件，函數 $f(t)$ 在一個週期內（或全時域內）必須滿足以下三點：

**條件一：絕對可積**

**條件二：有限個極值點**

- $f(t) = \sin(1/t)$ 在 $t=0$ 附近有無窮多個震盪，不滿足此條件

![震蕩聚集](../image/震蕩聚集.png)

**條件三：有限個間斷點**

方波在每個半週期處都有一個間斷點，但數量是有限的，因此滿足條件三

![有限個間斷點](../image/有限個間斷點.png)


- 吉布斯現象

    當使用有限項傅立葉級數來重新建構（合成）一個包含不連續點（間斷點）的訊號時，在間斷點附近會出現明顯的震盪（Ringing）與過衝（Overshoot）

- 使用「窗函數」來有效抑制這些重建時產生的震盪波紋

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/be1b2598fbcb)

## 第13週習題：請寫程式求解常係數齊次常微分方程

![筆記](../image/week13.jpg)

方程形式：$ay'' + by' + cy = 0$

已知條件：其中 $a, b, c$ 為常數，且 $a \neq 0$。

目標：尋找通解 $y(x)$。

- Step 1: 特徵方程

- Step 2: 求解特徵根

- Step 3: 根據判別式 $\Delta = b^2 - 4ac$ 分類討論

### 參考資料

[gemini對話記錄](https://gemini.google.com/share/f89b2579f824)