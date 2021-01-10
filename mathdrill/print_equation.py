import colorama
# import emoji
from .Operations import Operations

def print_equation(*operands, operation=Operations.ADDITION, score=0):
    output : str = ""
    if operation == Operations.ADDITION:
        formatted_operands = [f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} " for i in operands]
        formatted_operator = f"{colorama.Fore.GREEN} + {colorama.Style.RESET_ALL}"
        output = formatted_operator.join( formatted_operands)
        answer = sum(operands)
    elif operation == Operations.SUBTRACTION:
        formatted_operands = [f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} " for i in reversed(operands)]
        formatted_operator = f"{colorama.Fore.RED} - {colorama.Style.RESET_ALL}"
        output = formatted_operator.join( formatted_operands)
        answer = operands[1] - operands[0]
    else:
        print(colorama.Fore.RED, "Unknown operation!")
    print(f"{output} = ", end='')
    c = int(input())
    if c == answer:
        print(colorama.Fore.GREEN, 'Correct!',end='')
        if score > 1:
            print(colorama.Fore.CYAN, colorama.Style.BRIGHT,f' SCORE: {score} ', end='')
            if score > 19: print('🦄')
        print(colorama.Style.RESET_ALL, end='\n\n')
        return True
    else:
        print(colorama.Fore.RED, 'Incorrect! ', end='')
        print(colorama.Style.RESET_ALL, 'Try again, Smellyana...', end='\n\n')
        return False
