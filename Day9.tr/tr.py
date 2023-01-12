class Calculator:
    def calculator(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def add(self):
        result = self.number1 + self.number2
        return result
    def sub(self):
        result = self.number1 - self.number2
        return result
    def mul(self):
        result = self.number1 * self.number2
        return result
    def div(self):
        result = self.number1 // self.number2
        return result

a = Calculator()
a.calculator(10, 5)
b = Calculator()
b.calculator(2, -2)

print(f'# number1 = 10, number2 = 5')
print(f'# 합 : {a.add()}')
print(f'# 빼기 : {a.sub()}')
print(f'# 곱 : {a.mul()}')
print(f'# 몫 : {a.div()}')
print(f'# number1 = -2, number2 = 2')
print(f'# 합 : {b.add()}')
print(f'# 빼기 : {b.sub()}')
print(f'# 곱 : {b.mul()}')
print(f'# 몫 : {b.div()}')