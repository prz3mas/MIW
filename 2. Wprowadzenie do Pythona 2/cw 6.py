class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def difference(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


class ScienceCalculator(Calculator):

    @staticmethod
    def power(a, b):
        return a ** b


print(ScienceCalculator.difference(5, 7))
print(Calculator.add(4, 5))
print(Calculator.difference(6, 8))
print(ScienceCalculator.power(4, 6))
