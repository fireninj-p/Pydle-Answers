for x in range(5):
    for y in range(5):
        if y in (0,3) and x != 2 or y in (1,4) and x in (0,4):
            pydle(x, y, "", "white")
        else:
            pydle(x, y, "", "black")
