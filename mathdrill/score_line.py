import colorama
import sys

def score_line(score: int):
    print(
        colorama.Fore.CYAN,
        colorama.Style.BRIGHT,
        f" SCORE: {score} ",
        colorama.Style.RESET_ALL,
        end="",
    )
    if score >= 30:
        print("🦄", end="\n\n")
        print(
            colorama.Fore.MAGENTA,
            "💜💙💚💛🧡💖💘 You're all done! Go have fun!! 💜💙💚💛🧡💖💘", 
            colorama.Style.RESET_ALL, 
            end="\n\n")
        sys.exit()

    print(end="\n\n")
