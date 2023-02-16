import time
import pymongo
import os
import pystyle as ps
from src import searches
import src.misc
from src.generate import *
from src.simulation import realism_simulation

def tab_down():
    print()


def enter_to_continue():
    print("", flush=True)
    input("Press enter to continue...")


def styled_coloured_print_centered(text, cent=True, colour=None, instant=False):
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

