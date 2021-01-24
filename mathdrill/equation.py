from time import sleep
import colorama
import random
import os
from .Classes import Operations, Addition, Subtraction, Multiplication
from .correct_answer import correct_answer
from .wrong_answer import wrong_answer
from .score_value import score_value


def get_equation(operation : Operations = Operations.ADDITION):
    """
    Return a list of randomly generated operand values to instantiate
    an Equation object.
    """
    if operation == Operations.ADDITION:
        operands = random.randrange(20,60), random.randrange(20,60)
        return Addition(*operands)
    elif operation == Operations.SUBTRACTION:
        operands = random.randrange(10,60), random.randrange(10) 
        return Subtraction(*operands)
    elif operation == Operations.MULTIPLICATION:
        operand_a = random.randrange(1,6)
        if operand_a >= 4:
            operand_b = random.randrange(1,3)
        else:
            operand_b = random.randrange(2,5)
        # operands = random.randrange(1,4), random.randrange(1,5)
        return Multiplication(operand_a, operand_b)
    else: 
        raise Exception

def equation(operation: Operations, score: int):
    """
    Generate Equation objects, handling user input
    """
    try:
        problem = get_equation(operation)
    except Exception as ex:
        print(colorama.Fore.RED, "Unknown operation!", colorama.Style.RESET_ALL)
        print(ex)
        sleep(1)
        return False

    problem = get_equation(operation)

    response = ""
    while True:
        print(problem.output, end="")
        while True: 
            try:
                response = int(input())
                break
            except ValueError:
                print(f"{colorama.Fore.RED}Enter a number{colorama.Style.RESET_ALL}")

        if response == problem.result:
            points_earned = score_value(problem)
            score += points_earned
            correct_answer(score)
            del(problem)
            return score
        else:
            wrong_answer()
