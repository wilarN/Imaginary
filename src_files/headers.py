import platform
import subprocess
import time
import pymongo
import os
import pystyle as ps
from src_files import searches
import src_files.misc
import logging
from src_files.misc import ANNOTATIONS_AND_CRIMES
from src_files.simulation import realism_simulation
import random
import src_files.globals


logo_ascii = """
8888888                                 d8b                                    
  888                                   Y8P                                    
  888                                                                          
  888   88888b.d88b.   8888b.   .d88b.  888 88888b.   8888b.  888d888 888  888 
  888   888 "888 "88b     "88b d88P"88b 888 888 "88b     "88b 888P"   888  888 
  888   888  888  888 .d888888 888  888 888 888  888 .d888888 888     888  888 
  888   888  888  888 888  888 Y88b 888 888 888  888 888  888 888     Y88b 888 
8888888 888  888  888 "Y888888  "Y88888 888 888  888 "Y888888 888      "Y88888 
                                    888                                    888 
                               Y8b d88P                               Y8b d88P 
                                "Y88P"                                 "Y88P"      [  ~$ ©William. Johnsson - 2023  ]
[ EXPERIMENTAL BRANCH ]
"""

def tab_down():
    print()


def enter_to_continue():
    print("", flush=True)
    input("Press enter to continue...\n")


def styled_coloured_print_centered(text, cent=False, colour=None, instant=False):
    if colour is not None:
        col = colour
    else:
        col = None
    if instant:
        time_delay = 0
    else:
        time_delay = 0.01
    '''
    Default colour "None" --> cyan_to_green
    red --> red
    blue --> cyan
    orange --> orange
    pink --> pink
    yellow --> yellow
    bluegreen --> bluegreen
    purpleblue --> purple to blue gradient
    greenyellow --> greenyellow
    green --> green
    Default instant --> False
    '''
    if colour is None:
        if cent:
            ps.Write.Print(text=ps.Center.XCenter(text), color=ps.Colors.cyan, interval=time_delay)
        else:
            ps.Write.Print(text=text, color=ps.Colors.cyan, interval=time_delay)
    else:
        if colour == "red":
            col = ps.Colors.red
        elif colour == "orange":
            col = ps.Colors.orange
        elif colour == "blue":
            col = ps.Colors.cyan
        elif colour == "pink":
            col = ps.Colors.pink
        elif colour == "greenwhite":
            col = ps.Colors.green_to_white
        elif colour == "purpleblue":
            col = ps.Colors.purple_to_blue
        elif colour == "yellow":
            col = ps.Colors.yellow
        elif colour == "bluegreen":
            col = ps.Colors.blue_to_green
        elif colour == "greenyellow":
            col = ps.Colors.green_to_yellow
        elif colour == "green":
            col = ps.Colors.green
        if cent:
            ps.Write.Print(text=ps.Center.XCenter(text), color=col, interval=time_delay)
        else:
            ps.Write.Print(text=text, color=col, interval=time_delay)
    print("", flush=True)


def write_to_file(text_to_write, path_to_file, typeOfWrite):
    try:
        if os.path.exists(path_to_file):
            write_file = open(path_to_file, typeOfWrite)
            write_file.write(text_to_write)
            write_file.close()
    except Exception as e:
        print(e)
        enter_to_continue()

def yes_no(text):
    usr_answ = input(f"{text} (y/n) >> ").strip(" ")
    if usr_answ.__contains__("y"):
        return True
    else:
        return False


def is_ascii(text):
    try:
        # Valid ascii input
        mynewstring = text.encode('ascii')
        return True
    except UnicodeEncodeError:
        # Invalid ascii input
        return False


def styled_input(text):
    """
    center? TRUE || FALSE

    """
    return ps.Write.Input(color=ps.Colors.yellow_to_red, text=text, interval=0.001)

def open_file_in_editor(file_path):
    # Get the operating system
    os_name = platform.system()

    # Determine the command to open the file in the default editor
    if os_name == 'Windows':
        command = ['cmd', '/c', 'start', '', file_path]
    elif os_name == 'Darwin':  # Mac OS
        command = ['open', file_path]
    else:  # Assume Linux or other Unix-based OS
        command = ['xdg-open', file_path]

    # Run the command
    subprocess.run(command, check=True)

def save_results_to_file(list_of_items):
    usr_res = input("Save results to file?(y/n) (Enter to continue...)")
    if usr_res.strip(" ").lower() == "y":
        if not os.path.exists("./output"):
            os.mkdir("./output")

        for item in list_of_items:
            write_to_file(text_to_write=str(item), path_to_file=("./output/"+"latest_logged.txt"), typeOfWrite="w+")
    else:
        pass

def line():
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

