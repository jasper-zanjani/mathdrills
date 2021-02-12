import random
import enum
import colorama
from math import prod


class Operations(enum.Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "x"
    TIME = enum.auto()


class Equation:
    def __init__(self, *operands: int):
        self.operands = tuple(*operands)


class Addition(Equation):
    def __init__(self, *operands: int):
        super().__init__(operands)
        self.operation = Operations.ADDITION
        
        self.operands = random.choice([                                                 \
            (random.randrange(20,60), random.randrange(20,60), random.randrange(10,20)),   \
            (random.randrange(100, 1000), random.randrange(100, 1000))  \
        ])

        self.result = sum(self.operands)
        self.output = f"{colorama.Fore.GREEN}{self.operation.value}{colorama.Style.RESET_ALL}".join(
            [
                f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} "
                for i in self.operands
            ]
        )
        self.output += "= "

    @property
    def score(self):
        output = 1
        if self.result > 1000: output += 1
        return output



class Subtraction(Equation):
    def __init__(self, *operands: int):
        super().__init__(operands)
        self.operation = Operations.SUBTRACTION
        if self.operands == ():
            a = random.randrange(20, 60)
            self.operands = a, random.randrange(10, a - 10), random.randrange(10)
        self.result = self.operands[0] - sum(self.operands[1:])
        self.output = (
            f"{colorama.Fore.RED}{self.operation.value}{colorama.Style.RESET_ALL}".join(
                [
                    f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} "
                    for i in self.operands
                ]
            )
        )
        self.output += "= "
    
    @property
    def score(self):
        output = 1
        return output


class Multiplication(Equation):
    def __init__(self, *operands: int):
        super().__init__(operands)
        self.operation = Operations.MULTIPLICATION
        if operands == ():
            a = random.randrange(1, 20)
            if a >= 10:
                b = random.randrange(4)
            else:
                b = random.randrange(2, 5)
            self.operands = a, b
        self.result = prod(self.operands)
        self.output = f"{colorama.Fore.CYAN}{self.operation.value}{colorama.Style.RESET_ALL}".join(
            [
                f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} "
                for i in self.operands
            ]
        )
        self.output += "= "

    @property
    def score(self):
        output = 1
        if a > 2 and b > 2: output += 1
        return output
