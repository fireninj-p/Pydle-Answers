for x in range(5):
    for y in range(5):
        if x == 1:
            pydle(x, y, "", "green")
        if y == 1:
            pydle(x, y, "", "blue")
        if x == 3:
            pydle(x, y, "", "purple")
        if y == 3 and x!= 1:
            pydle(x, y, "", "yellow")
