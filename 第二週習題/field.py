class FiniteField:
    """有限體 (Galois Field) 實作"""
    
    def __init__(self, value, modulus):
        if modulus <= 1:
            raise ValueError("Modulus must be a prime number greater than 1")
        if not self._is_prime(modulus):
            raise ValueError("Modulus must be a prime number")
        
        self.value = value % modulus
        self.modulus = modulus
    
    def _is_prime(self, n):
        """檢查是否為質數"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def __add__(self, other):
        """加法運算子重載"""
        if isinstance(other, FiniteField):
            if self.modulus != other.modulus:
                raise ValueError("Cannot add elements from different fields")
            return FiniteField((self.value + other.value) % self.modulus, self.modulus)
        elif isinstance(other, int):
            return FiniteField((self.value + other) % self.modulus, self.modulus)
        else:
            return NotImplemented
    
    def __sub__(self, other):
        """減法運算子重載"""
        if isinstance(other, FiniteField):
            if self.modulus != other.modulus:
                raise ValueError("Cannot subtract elements from different fields")
            return FiniteField((self.value - other.value) % self.modulus, self.modulus)
        elif isinstance(other, int):
            return FiniteField((self.value - other) % self.modulus, self.modulus)
        else:
            return NotImplemented
    
    def __mul__(self, other):
        """乘法運算子重載"""
        if isinstance(other, FiniteField):
            if self.modulus != other.modulus:
                raise ValueError("Cannot multiply elements from different fields")
            return FiniteField((self.value * other.value) % self.modulus, self.modulus)
        elif isinstance(other, int):
            return FiniteField((self.value * other) % self.modulus, self.modulus)
        else:
            return NotImplemented
    
    def __truediv__(self, other):
        """除法運算子重載"""
        if isinstance(other, FiniteField):
            if self.modulus != other.modulus:
                raise ValueError("Cannot divide elements from different fields")
            if other.value == 0:
                raise ZeroDivisionError("Division by zero in finite field")
            # 乘法反元素
            inverse = self._mod_inverse(other.value, self.modulus)
            return FiniteField((self.value * inverse) % self.modulus, self.modulus)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            inverse = self._mod_inverse(other % self.modulus, self.modulus)
            return FiniteField((self.value * inverse) % self.modulus, self.modulus)
        else:
            return NotImplemented
    
    def _mod_inverse(self, a, m):
        """使用擴展歐幾里得算法計算模反元素"""
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
        
        gcd, x, _ = extended_gcd(a, m)
        if gcd != 1:
            raise ValueError(f"{a} has no modular inverse modulo {m}")
        return x % m
    
    def __pow__(self, exponent):
        """冪運算"""
        if isinstance(exponent, int):
            if exponent < 0:
                # 負指數：先求反元素再正指數
                inverse = self._mod_inverse(self.value, self.modulus)
                base = inverse
                exponent = -exponent
            else:
                base = self.value
            
            result = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % self.modulus
                base = (base * base) % self.modulus
                exponent //= 2
            return FiniteField(result, self.modulus)
        else:
            return NotImplemented
    
    def __eq__(self, other):
        """等於運算子"""
        if isinstance(other, FiniteField):
            return self.value == other.value and self.modulus == other.modulus
        elif isinstance(other, int):
            return self.value == other % self.modulus
        else:
            return False
    
    def __neg__(self):
        """負號運算子（加法反元素）"""
        return FiniteField((-self.value) % self.modulus, self.modulus)
    
    def __str__(self):
        return f"{self.value} (mod {self.modulus})"
    
    def __repr__(self):
        return f"FiniteField({self.value}, {self.modulus})"

# 測試程式
def test_finite_field():
    """測試有限體功能"""
    print("=== 有限體測試 ===\n")
    
    # 創建有限體 GF(7) 的元素
    a = FiniteField(3, 7)
    b = FiniteField(5, 7)
    
    print(f"a = {a}")
    print(f"b = {b}\n")
    
    # 測試基本運算
    print("基本運算:")
    print(f"a + b = {a + b}")      # 3 + 5 = 8 ≡ 1 (mod 7)
    print(f"a - b = {a - b}")      # 3 - 5 = -2 ≡ 5 (mod 7)
    print(f"a * b = {a * b}")      # 3 * 5 = 15 ≡ 1 (mod 7)
    print(f"a / b = {a / b}")      # 3 / 5 = 3 * 3 = 9 ≡ 2 (mod 7)
    print(f"a² = {a ** 2}")        # 3² = 9 ≡ 2 (mod 7)
    print(f"-a = {-a}")            # -3 ≡ 4 (mod 7)
    
    # 測試分配律
    print("\n分配律驗證:")
    left = a * (b + FiniteField(2, 7))
    right = a * b + a * FiniteField(2, 7)
    print(f"a * (b + 2) = {left}")
    print(f"a * b + a * 2 = {right}")
    print(f"分配律成立: {left == right}")
    
    # 測試群性質
    print("\n群性質驗證:")
    zero = FiniteField(0, 7)
    one = FiniteField(1, 7)
    print(f"加法單位元素: {zero}")
    print(f"a + 0 = {a + zero} = {a}")
    print(f"乘法單位元素: {one}")
    print(f"a * 1 = {a * one} = {a}")
    print(f"加法反元素: a + (-a) = {a + (-a)} = {zero}")
    print(f"乘法反元素: a * a⁻¹ = {a * (a ** -1)} = {one}")

if __name__ == "__main__":
    test_finite_field()