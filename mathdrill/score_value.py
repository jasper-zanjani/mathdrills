from .Classes import *


def score_value(problem : Equation):
    """
    Returns a number value to be added to score. Gauges the difficulty of the challenge 
    by various criteria, including operation type and difficulty of performing the operation
    on the given operands.
    """
    output = 1
    if problem.operation == Operations.ADDITION:
        # if (a >= 10 or b >= 10) and (a % 10 + b % 10 >=10):
        output = 1
    elif problem.operation == Operations.SUBTRACTION:
        # if (b % 10) < (a % 10):
        output = 1  # subtraction involves carrying one
    elif problem.operation == Operations.MULTIPLICATION:
        output = 1
    return output
