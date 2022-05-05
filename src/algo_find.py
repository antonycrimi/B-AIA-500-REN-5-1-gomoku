my_dir_check = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [0, -1]]
len_row = 0
len_column = 0

def search_in_map(map, row, col, find):
    global my_dir_check, len_row, len_column
    if map[row][col] != find[0]:
        return False, 0, 0
    for x, y in my_dir_check:
        row_to_check = row + x
        column_to_check = col + y
        flag = True
        for k in range(1, len(find)):
            if (0 <= row_to_check < len_row and
                0 <= column_to_check < len_column and
                find[k] == map[row_to_check][column_to_check]):
                row_to_check += x
                column_to_check += y
            else:
                flag = False
                break
        if flag:
            return True, x, y
    return False, 0, 0

def patternSearch(map, find):
    global my_dir_check, len_row, len_column
    len_row = len(map)
    len_column = len(map[0])
    res = []
    for row in range(len_row):
        for col in range(len_column):
            boole, x, y = search_in_map(map, row, col, find)
            if boole:
                res.append((row, col, (x, y)))
    return res