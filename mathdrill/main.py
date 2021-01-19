import random
import colorama
import sys
import argparse

from .time import time
from .equation import equation
from .Operations import Operations
from .score_line import score_line
from .correct_answer import correct_answer
from .score_value import score_value

def get_args():
    parser = argparse.ArgumentParser()
    operations = parser.add_mutually_exclusive_group()
    operations.add_argument("-a", dest="add", help="Addition", action="store_true")
    operations.add_argument("-m", dest="minus", help="Subtraction", action="store_true")
    operations.add_argument("-t", dest="time", help="Time", action="store_true")

    return parser.parse_args()


def main():
    score = 0
    args = get_args()
    try:
        correct = True

        while True:
            if correct == True:

                if args.time:
                    op = Operations.TIME
                    score = time(score)
                elif args.add:
                    op = Operations.ADDITION
                    score = equation(op, score)
                elif args.minus:
                    op = Operations.SUBTRACTION
                    score = equation(op, score)
                else:
                    op = random.choice(list(Operations))
                    if op in [Operations.ADDITION, Operations.SUBTRACTION]:
                        score = equation(op, score)
                    elif op in [Operations.TIME]:
                        score = time(score)
            elif correct == False:
                pass

    except KeyboardInterrupt:
        print("\n")
        sys.exit()
    except EOFError:
        print("\n")
        sys.exit()
