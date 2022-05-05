#!/usr/bin/env python3
from src.pbrain_algo import *

MAP_size = 20
folder = ''
board_array = [ [ '0' for i in range(20)] for j in range (20)]

def add_board(x, y, j, bool):
    global board_array
    if (board_array[x][y] != '0'):
        print("ERROR invalid move", flush=True)
        return
    board_array[x][y] = j
    if (bool):
        print(x, ",", y, sep = "", flush=True)

def turn(arg):
    valid = True
    try :
        tmp = arg[1].split(",")
        tmp_arg = [int(tmp[0]), int(tmp[1])]
        for elem in tmp_arg:
            if (elem < 0 or elem >= MAP_size):
                print("ERROR arguments not supported, must be > 0 and <= ", MAP_size, "(MAP_size)", flush=True)
                valid = False
                break
        add_board(tmp_arg[0], tmp_arg[1], '2', False)
    except Exception as e:
        print("ERROR unsupported arguments", flush=True)
    if (valid):
        pos = attack_algo(board_array)
        add_board(pos[0], pos[1], '1', True)

def start(arg):
    global MAP_size, board_array
    valid = True
    if (len(arg) != 2):
        print("ERROR, need a size", flush=True)
        return
    try :
        tmp = int(arg[1])
        if (tmp < 5):
            print("ERROR unsupported size, must be >= 0", flush=True)
            valid = False
    except Exception as e:
        print("ERROR unsupported type size", flush=True)
    if (valid):
        print("OK", flush=True)
        MAP_size = int(arg[1])
        board_array = []
        board_array = [ [ '0' for i in range(MAP_size)] for j in range(MAP_size)]

def begin():
    global MAP_size
    middle = int(MAP_size/2)
    add_board(middle, middle, '1', True)

def board(arg):
    global MAP_size, board_array
    cmd = ''
    while (1):
        cmd = input()
        arg = cmd.split(',')
        try:
            if (arg[0] == "DONE"):
                break
            if (len(arg) != 3):
                print("ERROR need 3 args", flush=True)
            if (arg[2] != "1" and arg[2] != "2"):
                print("ERROR 3rd arg need to be 1 or 2", flush=True)
            if (int(arg[0]) < 0 or int(arg[0]) >= MAP_size):
                print("ERROR 1st arg need to be > 0 and <= ", MAP_size, "(MAP_size)", flush=True)
            if (int(arg[1]) < 0 or int(arg[1]) >= MAP_size):
                print("ERROR 2nd arg need to be > 0 and <= ", MAP_size, "(MAP_size)", flush=True)
            if (board_array[int(arg[0])][int(arg[1])] != '0'):
                print("Error, invalid move, spot already occupied", flush=True)
            else:
                add_board(int(arg[0]), int(arg[1]), (arg[2]), False)
        except Exception as e:
            print("ERROR unsupported type arg", flush=True)
    pos = attack_algo(board_array)
    add_board(pos[0], pos[1], '1', True)

def end():
    exit(0)

def about():
    print('name="LittleApple", version="1.0", author="Utuje, Crimi, Oger", country="BZH"', flush=True)

def mainalgo():
    global MAP_size, board_array
    cmd = " "
    while (cmd != ""):
        cmd = input()
        arg = cmd.split(' ')
        if (arg[0] == "START"): 
           start(arg)
        elif (arg[0] == "TURN"):
            turn(arg)
        elif (arg[0] == "BEGIN"):
            begin()
        elif (arg[0] == "BOARD"):
            board(arg)
        elif (arg[0] == "END"):
            end()
        elif (arg[0] == "ABOUT"):
            about()
        else:
            print("Unknown command", flush=True)

def main():
    mainalgo()

if __name__ == "__main__":
    main()