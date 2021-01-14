import colorama

from .score_line import score_line

def correct_answer(score: int):
    print('\n',colorama.Fore.GREEN, 'Correct!',end='')
    if score > 4:
        score_line(score)
    else:
        print(end='\n\n')
