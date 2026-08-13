for x in range(5):
    for y in range(5):
        if y in (0,4) and x != 2 or y%2 == 1 and (x <1 or x > 3):
            pydle(x, y, "", "white")
        else:
            pydle(x, y, "", "red")
