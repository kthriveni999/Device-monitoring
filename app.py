def calculate(expression):
    """calculator best the best"""
    Allowed = "+ - * /" 
    if not any(sing in expression for sing in allowed):
        raise ValueError(f"Invalid expression: {expression}")
    for sing in allowed:
        if sing in expression:
            try:
                left, right = expression.split(sing)
                left, right = int(left), int(right)
                return {
                    "+": lambda x, y: x + y,
                    "-": lambda x, y: x - y,
                    "*": lambda x, y: x * y,
                    "/": lambda x, y: x / y,
                }[sing](left, right)
            except (ValueError, TypeError):
                raise ValueError(f"Invalid expression: {expression}")

