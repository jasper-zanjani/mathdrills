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
        self.result = sum(self.operands)
        self.output = \
            f"{colorama.Fore.GREEN}{self.operation.value}{colorama.Style.RESET_ALL}".join( \
            [f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} " for i in self.operands])
        self.output += "= "


class Subtraction(Equation):
    def __init__(self, *operands: int):
        super().__init__(operands)
        self.operation = Operations.SUBTRACTION
        self.result = self.operands[0] - sum(self.operands[1:])
        self.output = \
            f"{colorama.Fore.RED}{self.operation.value}{colorama.Style.RESET_ALL}".join( \
            [f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} " for i in self.operands])
        self.output += "= "


class Multiplication(Equation):
    def __init__(self, *operands: int):
        super().__init__(operands)
        self.operation = Operations.MULTIPLICATION
        self.result = prod(self.operands)
        self.output = \
            f"{colorama.Fore.CYAN}{self.operation.value}{colorama.Style.RESET_ALL}".join( \
            [f" {colorama.Fore.YELLOW}{i}{colorama.Style.RESET_ALL} " for i in self.operands])
        self.output += "= "