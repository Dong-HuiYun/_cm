# 有限體與程式實作

## 1. 有限體的數學觀念
有限體 (Finite Field) 是一種「元素數量有限」的體 (Field)。  
它的運算規則是：
- **加法形成一個群**  
- **乘法（去掉 0）形成一個群**  
- **加法與乘法之間滿足分配律**  


## 2. 程式設計的思路
`FiniteFieldElement` 類別，主要功能有：
- **加法、減法、乘法、除法**（運算子重載 `+ - * /`）  
- **求逆元**（利用 Python 內建的 `pow(value, -1, p)`）  
- **自動檢查是否在同一個有限體**  


## 3. 數學與程式的連結
- 「**加法形成群**」 → 在程式裡對應到 `__add__` 和 `__sub__`。  
- 「**乘法形成群**」 → 在程式裡對應到 `__mul__` 和 `inverse()`。  
- 「**分配律**」 → 自然由模運算實現，因為 `(a+b)*c mod p = (a*c + b*c) mod p`。  


## 4. 執行範例
```python
a = FiniteFieldElement(2, 5)
b = FiniteFieldElement(3, 5)

print(a + b)  # 0 (mod 5)
print(a * b)  # 1 (mod 5)
print(a / b)  # 4 (mod 5) 
```

 ## 6. AI對話連結
 [ChatGPT](https://chatgpt.com/share/68d5ff5c-23a8-8005-aa36-f8f4de82566a)
