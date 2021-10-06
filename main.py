import platform
import time
import random
import os
import sys
import datetime

from os import system, name
from typing import Dict, Any

with open(os.devnull, 'w') as f:
    # disable stdout
    oldstdout = sys.stdout
    sys.stdout = f

    from pygame import mixer

    # enable stdout
    sys.stdout = oldstdout

# ===============================================================================================
# ========================================Game_Inports===========================================
# ===============================================================================================

from ascii_art import *
from colors import bcolors
from character import Character

# ===============================================================================================
# =========================================Functions=============================================
# ===============================================================================================

def get_input(string: str, valid_options: list) -> str:
    """
    Deals with error checking for inputs
    """
    while True:
        user_input = input(string)
        if user_input in valid_options:
            return user_input
        print("    incorrect input ^")

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

def character_generator():
    """
    Generates a character determined by user input and saves it in
    a pickle database.
    """
    character_style_menu = {
        "\n > We have reached the first crucial part of your journey: We must choose the path that you will take! The decision\n": 0.5,
        " > is up to you my friend! Whether you choose to be a bloodthirsty warrior or a cunning and strategic fighter,\n": 0.8,
        " > the choice is up to you!\n": 0.5,
        "\n > Now then, lets get right into it!": 0.8,
        " Are you more of a tanky player[1] or a strategic player[2]?": 0.0
    }
    print_block(character_style_menu)
    player_t_choice_1 = get_input('\n > ', ['1', '2'])

    if player_t_choice_1 == '1':
        total_health = 100
        damage = 75

    elif player_t_choice_1 == '2':
        total_health = 75
        damage = 50

    attack_style_menu = {
        "\n > So, we have that out of the way, Let's carry on! ": 0.8,
        "Oh of course! Sorry to forget! Another quick question: ": 0.5,
        "Do you like \n": 0.5,
        " > to use magic from great distances[1] or run in to the thick of battle wielding a deadly blade[2]?\n": 0.5,
    }
    print_block(attack_style_menu)
    player_t_choice_2 = get_input('\n > ', ['1', '2'])

    if player_t_choice_2 == '1':
        shield = 50
        magic = 75

    elif player_t_choice_2 == '2':
        shield = 75
        magic = 45

    luck_menu = {
        "\n > Good good! We have decided your play style and your preferred ways of attacking the enemy!\n": 0.5,
        " > Now, we must see what luck we are able to bestow upon you. Be warned: it is entirely random!\n": 0.8
    }
    print_block(luck_menu)
    print_text('\n > Press enter to roll a dice...')
    input()
    time.sleep(0.3)
    print_text(' > Rolling dice...\n')
    luck = random.randint(0, 10)
    time.sleep(1)
    print_text(f' > Your hero has {luck} luck out of 10!\n', 0.8)

    name_menu = {
        "\n > At last! We have reached the most important part of creating your character! The naming!\n": 0.0,
        " > Choose wisely my friend. Your hero will be named this for the rest of their lives...\n": 1,
        "\n > What should your hero be named?\n": 0.0
    }
    print_block(name_menu)

    name = ''
    while not name:
        name = input(' > ')

    time.sleep(1)

    menu_wrap = {
        f"\n > Welcome mighty hero! You shall henceforth be known as: {name} !!!\n ": 0.3,
        "> A perfect choice!\n": 0.0,
        " \n > Now then. I guess you should be on your way! You have a journey to start and a belly to fill!\n": 0.0
    }
    print_block(menu_wrap)

    parting_text = {
        " > I have to say, I have rather enjoyed your company! Feel free to come by at any time!\n": 0.0,
        " > Goodbye and god speed!\n": 1,
        " > Your starting stats are as follows:\n": 0.3,
        f" > [ health: {total_health}, damage: {damage}, shield: {shield}, magic: {magic}, luck: {luck}, name: {name} ]": 0.0,
        "\n > We should now save your character if you want to come back to it later - character file name:\n": 0.0
    }
    print_block(parting_text)


def new_character(CLEAR_SCREEN='cls'):
    # print_text(
    #     "\n > You have chosen to create a new game: Redirecting...", 2)

    redirect = {
        "\n > You have chosen to create a new game: ": 2,
        "Redirecting...": 2
    }

    print_block(redirect)
    system(CLEAR_SCREEN)
    # print('  \n  We will begin with creating your character:                                        Quick tip: Choose wisely')
    line1 = '  \n  We will begin with creating your character:'
    line2 = 'Choose wisely'
    print(line1 + line2.rjust(118-(len(line1[3:])), " "))
    screen_line()
    time.sleep(0.5)
    sword()
    screen_line()
    time.sleep(0.3)
    return character_generator()

def main_menu(CLEAR_SCREEN='cls'):
    """
    This is where everything to do with the main game is. This includes all functions in one
    way or another.
    """

    __version__ = 0.2
    time.sleep(0.5)
    time.sleep(0.5)
    show_date_and_time = datetime.datetime.now().strftime("%d %H:%M")
    # print('\n  <Adventure Colossus>     session:', session_count, '| version:', __version__,
    # '| current date:', show_date_and_time, '| date of creation: 9.2.2021')

    title1 = f"\n  <Adventure Colossus>"

    a = len(title1)
    title2 = f"s~{session_count} | v{__version__} "
    print(title1 + title2.rjust(118-a, " "))
    screen_line()
    time.sleep(0.5)
    logo2()
    mountain_range()
    screen_line()
    print("\n")

    create_load_menu = {
        " > [1] Create new game\n": 0.5,
        " > [2] Load existing game\n": 0.5,
        " > [3] End game\n": 0.5,
        " > [4] Credits\n": 0.5
    }
    print_block(create_load_menu)
    while True:

        choice = get_input("\n  > ", ['1', '2', '3', '4'])

        if choice == '1':
            new_character()

        elif choice == '4':
            credits = {
            "   Numens\n":0.3,
            "   r0nnyn\n":0.3
            }

            print_block(credits)
            print()
            logo()

if __name__ == '__main__':
    song = "C:/Users/sbenf/Desktop/Text RPG/magic-forest-kevin-macleod-main-version-04-20-8004.mp3"
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
    main_menu()
