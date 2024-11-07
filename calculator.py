class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, abs(a))

        if (a < 0) ^ (b < 0):
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        quotient = 0
        abs_a = abs(a)
        abs_b = abs(b)
        while abs_a >= abs_b:
            abs_a -= abs_b
            quotient += 1
        # Determine the sign of the result
        if (a < 0) ^ (b < 0):
            quotient = -quotient
        return quotient
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")
        abs_a = abs(a)
        abs_b = abs(b)
        while abs_a >= abs_b:
            abs_a -= abs_b
        return abs_a if a >= 0 else -abs_a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))