for x in range(5):
    for y in range(5):
        pydle(2, 2, "", "orange")
        pydle(x, y, "", "yellow")
        if x in (0,4) and y in (0,4):
            pydle(x, y, "", "white")
        if y > 1 and x%2==1:
            pydle(x, y, "", "blue")
        if y ==1  and x%2==1:
            pydle(x, y, "", "black")
