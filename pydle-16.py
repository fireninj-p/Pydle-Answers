for x in range(5):
    for y in range(5):
        pydle(x, y, "", "red")
        pydle(2, 4, "", "brown")
        if y == 0 and x!= 2 or y ==1 and x in (0,4):
            pydle(x, y, "", "white")
        if y>2:
            pydle(x, y, "", "yellow")
