import colorama


def wrong_answer():
    print(colorama.Fore.RED, "Incorrect! ",colorama.Style.RESET_ALL, "Try again, Smellyana...", end="\n\n")
    return False
