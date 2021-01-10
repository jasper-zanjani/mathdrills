import random
import colorama
import sys
import argparse

from .print_equation import print_equation
from .Operations import Operations

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest="add", help='Addition',action='store_true')
    parser.add_argument('-m', dest='minus', help="Subtraction", action='store_true')
    return parser.parse_args()

def main():
    args = get_args()
    try:
        correct = True
        score=0
        while True:
            if correct == True:
                score += 1
                b = random.randrange(10)
                a = random.randrange(10,20)
                if args.add:
                    op = Operations.ADDITION
                elif args.minus:
                    op = Operations.SUBTRACTION
                else:
                    op = random.sample(list(Operations), 1)[0]
            elif correct == False:
                pass
            correct = print_equation(b,a,operation=op, score=score)
    except KeyboardInterrupt:
        print('\n')
        sys.exit()
