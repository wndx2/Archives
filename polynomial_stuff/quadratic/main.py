from imports import *
from lib.clear import clear


clear()

while True:
    try:
        clear()

        print("Polynomial (Degree 2)\n")
        a = float(input("\na : "))
        b = float(input("\nb : "))
        c = float(input("\nc : "))

        if a == 0:
            print("\nMa ERROR.\n")
            input("Press any button to continue.")
            continue
            # resets loop

        d = b**2 - 4 * a * c  # discriminant (** = ^)

        if d > 0:
            # '**0.5' = '√', squaring it to half (same as rooting)
            x1 = round((-b + d**0.5) / (2 * a), 4)
            x2 = round((-b - d**0.5) / (2 * a), 4)
            print(f"\nTwo Real Solutions, as {Fore.GREEN}D = {d}{Fore.RESET} (D > 0):")
            print(f"    X1 [{Fore.GREEN}{x1}{Fore.RESET}]")
            print(f"    X2 [{Fore.GREEN}{x2}{Fore.RESET}]\n")

        elif d == 0:
            x = round(-b / (2 * a), 4)
            print(f"\nOne Real Solution, as {Fore.YELLOW}D = {d}{Fore.RESET} (D = 0):")
            print(f"    X1 [{Fore.YELLOW}{x}{Fore.RESET}] * 2\n")

        else:
            print(f"\nNo Real Solution(s), as {Fore.RED}D = {d}{Fore.RESET} (D < 0).\n")

        input("Press any button to continue.")

    except ValueError:
        print("Invalid Input.\n")
