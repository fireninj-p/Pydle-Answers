for x in range(5):
    for y in range(5):
        pydle(x, y, "", "yellow")
        pydle(2, 3, "", "black")
        if y in (0,4) and x in (0,4):
            pydle(x, y, "", "white")
        if x%2 == 1 and y%2 == 1:
            pydle(x, y, "", "black")
