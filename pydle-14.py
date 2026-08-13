for x in range(5):
    for y in range(5):
        pydle(x, y, "", "white")
        if x in (1,2) and y < 4 or y in (1,2) and x < 4:
            pydle(x, y, "", "red")
        if y > 2 and y == x:
            pydle(x, y, "", "black")
