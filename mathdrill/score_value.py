from .Operations import Operations

def score_value(op: Operations, a: int = 0, b: int = 0):
    """
    Returns a number value to be added to score. Gauges the difficulty of the challenge 
    by various criteria, including operation type and difficulty of performing the operation
    on the given operands.
    """
    output = 1
    if op == Operations.ADDITION:
        if (a >= 10 or b >= 10) and (a % 10 + b % 10 >= 10):
            output = 2
    elif op == Operations.SUBTRACTION:
        if (b % 10) < (a % 10):
            output = 2  # subtraction involves carrying one
    elif op == Operations.TIME:
        output = 3
    return output
