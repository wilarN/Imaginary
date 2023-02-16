from src.headers import *


def realism_simulation():
    styled_coloured_print_centered(text="""
    ##############################################################################
    # All of the following simulations will affect and modify the stored data    #                      #
    # including database records of identities and ownerships of cars etc.       #
    # Please proceed with caution.                                               #
    ##############################################################################
    """, instant=True, colour="yellow")
    enter_to_continue()
    while True:
        clear()
        styled_coloured_print_centered(text=
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"-       [1]- Crime Simulation               -\n"
                                       f"+       [2]- Full Simulation                +\n"
                                       f"-                                           -\n"
                                       f"+                                           +\n"
                                       f"-                                           -\n"
                                       f"+          [ E/e(Exit) ]                    +\n"
                                       f"-                                           -\n"
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
        tab_down()
        usr_sel = input(" >> ")
        usr_sel = usr_sel.lower().strip(" ")
        if usr_sel.__contains__("1"):
            pass
        if usr_sel.__contains__("2"):
            # Full simulation --> Transactions, crime, car trade, property etc.
            pass

        elif usr_sel.__contains__("e"):
            break
