class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(x, y):
        return x + y
    
    @classmethod
    def multiply(cls, x, y):
        print(f"Calculation type: {cls.calculation_type}")
        return x * y
    

from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()