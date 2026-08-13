for x in range(5):
    for y in range(5):
        if x<2:
            pydle(x, y, "", "yellow")
        if y<2:
            pydle(x, y, "", "blue")
        if x>2:
            pydle(x, y, "", "purple")
        if y>2 and x>1:
            pydle(x, y, "", "green")
        if x % 2 == 1 and y == 2 or y in (1,2,3) and x == 2:
            pydle(x, y, "", "red")
