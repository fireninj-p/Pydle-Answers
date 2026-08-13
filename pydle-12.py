for x in range(5):
    for y in range(5):
        pydle(x, y, "", "white")
        if x in (0,4) and y in (0,4):
            pydle(x, y, "", "black")
        elif x in (1,3) and y in (1,3):
            pydle(x, y, "⚫", "white")
