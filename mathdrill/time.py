import colorama
import random
import shutil


from .correct_answer import correct_answer
from .wrong_answer import wrong_answer

def time(score : int):
    start_hour = random.randrange(1,12)
    end_hour = start_hour + 1
    current_hour = start_hour -1
    current_minutes = random.randrange(1,12) * 5
    terminal_width = shutil.get_terminal_size().columns-2

    class_time = f"Class: {colorama.Fore.YELLOW}{start_hour}:00 - {end_hour}:00{colorama.Style.RESET_ALL}"
    current_time = f"Current time: {colorama.Fore.YELLOW}{current_hour:2d}:{current_minutes:02d}{colorama.Style.RESET_ALL}".rjust(terminal_width)
    answer = 60-current_minutes
    while True:
        print(class_time)
        print(current_time)
        print(f"How many more minutes until class starts? ", end='')
        
        while True:
            try:
                response = int(input())
                break
            except ValueError:
                print("Enter a valid number!")

        if response == answer:
            score += 1
            correct_answer(score)
            return score
        else:
            wrong_answer()
