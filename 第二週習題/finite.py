class FiniteFieldElement:
    def __init__(self, value, p):
        if p <= 1:
            raise ValueError("模數 p 必須是質數且大於 1")
        self.p = p
        self.value = value % p  # 元素值永遠落在 0..p-1

    def __repr__(self):
        return f"{self.value} (mod {self.p})"

    # 加法
    def __add__(self, other):
        self._check_same_field(other)
        return FiniteFieldElement(self.value + other.value, self.p)

    # 減法
    def __sub__(self, other):
        self._check_same_field(other)
        return FiniteFieldElement(self.value - other.value, self.p)

    # 乘法
    def __mul__(self, other):
        self._check_same_field(other)
        return FiniteFieldElement(self.value * other.value, self.p)

    # 除法（需要乘上逆元）
    def __truediv__(self, other):
        self._check_same_field(other)
        if other.value == 0:
            raise ZeroDivisionError("在有限體中，不能除以 0")
        return self * other.inverse()

    # 求逆元（利用擴展歐幾里得演算法）
    def inverse(self):
        if self.value == 0:
            raise ZeroDivisionError("0 在有限體中沒有逆元")
        return FiniteFieldElement(pow(self.value, -1, self.p), self.p)

    # 等於判斷
    def __eq__(self, other):
        return isinstance(other, FiniteFieldElement) and self.value == other.value and self.p == other.p

    # 輔助函式：檢查是否在同一個有限體
    def _check_same_field(self, other):
        if self.p != other.p:
            raise ValueError("兩個元素必須屬於同一個有限體")
        
if __name__ == "__main__":
    # 建立有限體 F_5 = Z/5Z
    a = FiniteFieldElement(2, 5)
    b = FiniteFieldElement(3, 5)

    print("a =", a)
    print("b =", b)

    print("a + b =", a + b)  # 2 + 3 = 0 mod 5
    print("a - b =", a - b)  # 2 - 3 = 4 mod 5
    print("a * b =", a * b)  # 2 * 3 = 1 mod 5
    print("a / b =", a / b)  # 2 * 3⁻¹ = 2 * 2 = 4 mod 5

