for x in range(5):
    for y in range(5):
        if x in (1,2,3) and y in (1,2,3):
            pydle(x, y, "", "green")
        if x in (0,4) and y in (0,4):
            pydle(x, y, "", "white")
        pydle(2, 2, "", "red")
