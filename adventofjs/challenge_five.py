def in_box(box):
    rows = len(box)
    cols = len(box[0])

    for i in box:
        if "*" not in i:
            return False

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if box[i][j] == "*":
                if (box[i - 1][j] == '#' and  # Top
                        box[i + 1][j] == '#' and  # Bottom
                        box[i][j - 1] == '#' and  # Left
                        box[i][j + 1] == '#'):
                    return True


in_box([
    "*####",
    "#   #",
    "#  #*",
    "####"
])
