for x in range(5):
    for y in range(5):
        pydle(x, y, "", "green")
        if(x == 0 and y == 0):
            pydle(x, y, "", "black")
        if((y == 0 and x > 1) or (y == 1 and x > 0) or (y == 4 and ((x > 1 and x < 4) or x == 0))):
            pydle(x, y, "", "white")
        if(x == 0 and y > 1 and y < 4):
            pydle(x, y, "", "yellow")
