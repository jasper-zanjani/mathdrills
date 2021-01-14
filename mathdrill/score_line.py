import colorama

def score_line(score: int):    
    print(colorama.Fore.CYAN, colorama.Style.BRIGHT,f' SCORE: {score} ',colorama.Style.RESET_ALL, end='')
    if score >= 20:
        print('🦄', end='')

    print(end='\n\n')