#evaluation function
#create patterns and assign them values
#board representation
#move generator

from src.algo_find import *

def search_play(map, pattern, play):
    pos =  patternSearch(map, pattern)
    if (pos and play == "p0"):
        x = pos[0][0]
        y = pos[0][1]
        return (x, y)
    if (pos and play == "p1"):
        x = pos[0][0] + pos[0][2][0]
        y = pos[0][1] + pos[0][2][1]
        return (x, y)
    if (pos and play == "p2"):
        x = pos[0][0] + (pos[0][2][0] * 2)
        y = pos[0][1] + (pos[0][2][1] * 2)
        return (x, y)
    return None

def where_to_play(map):
    to_check = [["00111", "p1"], ["01110", "p0"],
                ["01011", "p2"], ["10110", "p1"], ["11001", "p2"],
                ["10101", "p1"],
                ["01010", "p2"], ["00011", "p2"], ["00110", "p1"], ["10100", "p1"], ["10010", "p1"], ["10001", "p2"],
                ["02020", "p2"], ["00022", "p2"], ["00220", "p1"], ["20200", "p1"], ["20020", "p1"], ["20002", "p2"],
                ["01", "p0"], ["02", "p0"]]
    for elem in to_check:
        return_value = search_play(map, elem[0], elem[1])
        if (return_value != None):
            return return_value
    pos =  patternSearch(map, "0")
    x = pos[0][0]
    y = pos[0][1]
    return (x, y)

def defend_algo(map):
    to_check_def = [["02222", "p0"], ["20222", "p1"], ["22022", "p2"],
                    ["00222", "p1"], ["02220", "p0"],
                    ["02022", "p2"], ["20220", "p1"], ["22002", "p2"],
                    ["20202", "p1"]]
    for elem in to_check_def:
        return_value = search_play(map, elem[0], elem[1])
        if (return_value != None):
            return return_value
    return where_to_play(map)

def attack_algo(map):
    to_check_att = [["01111", "p0"], ["10111", "p1"], ["11011", "p2"]]
    for elem in to_check_att:
        return_value = search_play(map, elem[0], elem[1])
        if (return_value != None):
            return return_value
    else:
        return defend_algo(map)