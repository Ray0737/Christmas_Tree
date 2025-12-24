import sys
import time
import os
import random

colors = {
    "R": "\033[31m",  
    "G": "\033[32m", 
    "Y": "\033[33m", 
    "B": "\033[34m",  
    "M": "\033[35m", 
    "C": "\033[36m"   
}
RESET_COLOR = "\033[0m"
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_tree():
    tree = [
        "      * ",
        "     *** ",
        "    ***** ",
        "   ******* ",
        "  ********* ",
        " *********** ",
        "*************",
        "      |  ", 
        "      |  "  
    ]
    for line in tree:
        output_line = ""
        for char in line:
            if char == '*':
                color = random.choice(list(colors.values()))
                output_line += color + char + RESET_COLOR
            else:
                output_line += char
        print(output_line) 
def main():
    try:
        while True:
            clear_console()
            print_tree()
            sys.stdout.flush() 
            time.sleep(0.5)
    except KeyboardInterrupt:
        clear_console()
        print(RESET_COLOR)
        sys.exit(0)
if __name__ == "__main__":
    main()