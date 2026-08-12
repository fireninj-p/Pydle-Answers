for x in range(5):
    for y in range(5):
        pydle(x, y, "", "yellow")
        pydle(2, 3, "^", "yellow")
        if x%2==1 and y in (0,2):
            pydle(x, y, "", "white")
            if y == 2:
                pydle(x, y, "o", "white")
        elif y > 3 and x in (1,2,3):
            pydle(x, y, "=", "yellow")
