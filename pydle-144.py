for x in range(5):
    for y in range(5):
        if x in (2,4) and y<2:
            pydle(x, y, "", "yellow")
        if x == 3 and y in (2,3):
            pydle(x, y, "", "brown")
        if y > 3 and x in (1,2) or x < 1 and y in (1,2,3):
            pydle(x, y, "", "orange")
