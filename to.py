#!/bin/python3

import core
import sys

try:
    sys.argv[1] == "-s"
except IndexError:
    raise SystemExit(core.menu())

command = str()

while(command != "q" or command != "quit"):
    command = input("command (m for menu): ")
    if(command == 'a'):
        core.menu()
    elif(command == 'i'):
        pass
    elif(command == 'e'):
        pass
    elif(command == 'c'):
        pass
    elif(command == 'd'):
        pass
    elif(command == 'p'):
        core.printTask()
    elif(command == 's'):
        core.printDone()
    elif(command == 'clear'):
        core.clear()
    elif(command == 'q'):
        quit()
    else:
        pass