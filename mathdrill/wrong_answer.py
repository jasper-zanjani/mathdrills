import colorama

def wrong_answer():
    print(colorama.Fore.RED, 'Incorrect! ', end='')
    print(colorama.Style.RESET_ALL, 'Try again, Smellyana...', end='\n\n')
    return False