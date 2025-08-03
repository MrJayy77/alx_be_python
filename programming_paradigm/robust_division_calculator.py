def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator
        return f"Your result is: {result}"
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
    
