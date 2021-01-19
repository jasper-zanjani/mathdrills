import colorama

from .score_line import score_line


def correct_answer(score: int):
    print("\n", colorama.Fore.GREEN, "Correct!", end="")
    score_line(score)
