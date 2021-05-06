#!/bin/python3

import core
import sys

command = str()

while(command != "q" or command != "quit"):
    command = input(core.tcolor.NORMAL+"command (m for menu): ")
    if(command == 'm'):
        core.Menu()
    elif(command == 'a'):
        pass
    elif(command == 'i'):
        pass
    elif(command == 'e'):
        pass
    elif(command == 'c'):
        pass
    elif(command == 'd'):
        core.DoneTask()
    elif(command == 'p'):
        core.PrintTask()
    elif(command == 's'):
        core.PrintDone()
    elif(command == 'clear'):
        core.Clear()
    elif(command == 'q'):
        quit()
    else:
        pass