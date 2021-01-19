import colorama
import random
from .Operations import Operations
from .correct_answer import correct_answer
from .wrong_answer import wrong_answer

def addition(a: int, b: int):
    operands = [a, b]
    formatted_operands = [
        f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} " for i in operands
    ]
    formatted_operator = f"{colorama.Fore.GREEN} + {colorama.Style.RESET_ALL}"
    output = formatted_operator.join(formatted_operands)
    answer = sum(operands)
    return output, answer


def subtraction(a: int, b: int):
    operands = [a, b]
    formatted_operands = [
        f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} "
        for i in reversed(operands)
    ]
    formatted_operator = f"{colorama.Fore.RED} - {colorama.Style.RESET_ALL}"
    output = formatted_operator.join(formatted_operands)
    answer = operands[1] - operands[0]
    return output, answer


def score_value(a: int, b: int, op: Operations):
    output = 1
    if op == Operations.ADDITION:
        if (a >= 10 or b >= 10) and (a % 10 + b % 10 >= 10):
            output = 2
    elif op == Operations.SUBTRACTION:
        if (b % 10) < (a % 10):
            output = 2  # subtraction involves carrying one
    elif op == Operations.TIME:
        output = 3
    else:
        pass
    return output


def equation(operation: Operations, score: int):
    a = random.randrange(10)
    b = random.randrange(10, 50)
    operands = [a, b]
    output: str = ""
    response = ""
    while True:
        if operation == Operations.ADDITION:
            output, answer = addition(a, b)
        elif operation == Operations.SUBTRACTION:
            output, answer = subtraction(a, b)
        else:
            print(colorama.Fore.RED, "Unknown operation!")
        print(f"{output} = ", end="")

        while True:
            try:
                response = int(input())
                break
            except ValueError:
                print(f"{colorama.Fore.RED}Enter a number{colorama.Style.RESET_ALL}")

        if response == answer:
            points_earned = score_value(a, b, operation)
            score += points_earned
            correct_answer(score)
            return score
        else:
            wrong_answer()
