import platform
import time
import random
import os
import sys
import datetime

from os import system, name
from typing import Dict, Any

from ascii_art import *
from colors import bcolors

def get_input(string: str, valid_options: list) -> str:
    """
    Deals with error checking for inputs
    """
    while True:
        user_input = input(string)
        if user_input in valid_options:
            return user_input

def session_counter(filename="adventure_colussus_session_counter.dat"):
    """
    Determines the version of the last played game, either in the {VERSION_FILENAME}
    file, or generating a new file if none is found.
    """
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

session_count = session_counter()

def print_text(text: str, sleep_time: float = 0.0) -> None:
    """
    Prints the text to the console character by character. RPG style.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.021)
    if sleep_time != 0.0:
        time.sleep(sleep_time)


def print_block(lines: dict) -> None:
    """
    Takes dictionary where -
    keys = string to print
    values = float wait time
    """
    for key in lines.keys():
        print_text(key, lines[key])


def main_menu(CLEAR_SCREEN='clear'):
    """
    This is where everything to do with the main game is. This includes all functions in one
    way or another.
    """
    __version__ = 0.2
    time.sleep(0.5)
    time.sleep(0.5)
    show_date_and_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    screen_line()
    # print('\n  <Adventure Colossus>     session:', session_count, '| version:', __version__,
    # '| current date:', show_date_and_time, '| date of creation: 9.2.2021')

    title1 = "\n  <Adventure Colossus>"

    a = len(title1)
    title2 = f"session: {session_count} | current date: {show_date_and_time} | date of creation: 9.2.2021 | version: {__version__} "
    print(title1 + title2.rjust(118-a, " "))
    screen_line()
    time.sleep(0.5)
    mountain_range()
    screen_line()
    print("\n")

    create_load_menu = {
        f" > [{bcolors.Green}1{bcolors.ResetAll}] Create new game\n": 0.5,
        f" > [{bcolors.Green}2{bcolors.ResetAll}] Load existing game\n": 0.5,
        f" > [{bcolors.Green}3{bcolors.ResetAll}] End game\n": 0.5,
        f" > [{bcolors.Green}4{bcolors.ResetAll}] Credits\n": 0.5
    }
    print_block(create_load_menu)
    choice = get_input("\n  > ", ['1', '2', '3', '4'])

    if choice == '4':
        print_text('   Hey')

if __name__ == '__main__':
    main_menu()
