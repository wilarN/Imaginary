import time
import pymongo
import os
import pystyle as ps
from src import searches
from src.misc import carMaster

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["imaginaryMaster"]
global mycol
mycol = mydb["people"]
global dbCurs
dbCurs = mycol.find({})

def enter_to_continue():
    print("", flush=True)
    input("Press enter to continue...")


def styled_coloured_print_centered(text, colour=None, instant=False):
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
        ps.Write.Print(text=ps.Center.XCenter(text), color=ps.Colors.cyan, interval=time_delay)
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

        ps.Write.Print(text=ps.Center.XCenter(text), color=col, interval=time_delay)
    print("", flush=True)

def line():
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def tab_down():
    print()
