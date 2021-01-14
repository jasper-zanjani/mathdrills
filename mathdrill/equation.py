import colorama
import random
from .Operations import Operations
from .correct_answer import correct_answer
from .wrong_answer import wrong_answer

def addition(a: int, b: int):
    operands=[a,b]
    formatted_operands = [f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} " for i in operands]
    formatted_operator = f"{colorama.Fore.GREEN} + {colorama.Style.RESET_ALL}"
    output = formatted_operator.join( formatted_operands)
    answer = sum(operands)
    return output, answer

def subtraction(a:int, b:int):
    operands=[a,b]
    formatted_operands = [f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} " for i in reversed(operands)]
    formatted_operator = f"{colorama.Fore.RED} - {colorama.Style.RESET_ALL}"
    output = formatted_operator.join( formatted_operands)
    answer = operands[1] - operands[0]
    return output, answer



def equation(operation : Operations, score: int):
    a = random.randrange(10)
    b = random.randrange(10,50)
    operands = [a, b]
    output : str = ""
    response = ""
    while True:
        if operation == Operations.ADDITION:
            output, answer = addition(a,b)
        elif operation == Operations.SUBTRACTION:
            output, answer = subtraction(a,b)
        else:
            print(colorama.Fore.RED, "Unknown operation!")
        print(f"{output} = ", end='')
     
        while True:    
            try:
                response = int(input())
                break
            except ValueError:
                print(f"{colorama.Fore.RED}Enter a number{colorama.Style.RESET_ALL}")

        if response == answer:
            score += 1
            correct_answer(score)
            return score
            break
        else:
            wrong_answer()
