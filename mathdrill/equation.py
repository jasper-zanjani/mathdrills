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
    Used to return a list of randomly generated operand values to instantiate
    an Equation object. Now is more of a frontend to the various equation classes.
    """
    if operation == Operations.ADDITION:
        return Addition()
    elif operation == Operations.SUBTRACTION:
        return Subtraction()
    elif operation == Operations.MULTIPLICATION:
        return Multiplication()
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

    # problem = get_equation(operation)

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
