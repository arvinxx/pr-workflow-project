# PR Workflow Demo App

class Calculator:
    """简单计算器类"""
    
    def add(self, a, b):
        """加法运算"""
        return a + b
    
    def subtract(self, a, b):
        """减法运算"""
        return a - b
    
    def multiply(self, a, b):
        """乘法运算"""
        return a * b
    
    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

def main():
    calc = Calculator()
    print("PR Workflow Demo")
    print(f"2 + 3 = {calc.add(2, 3)}")
    return calc

if __name__ == "__main__":
    main()
