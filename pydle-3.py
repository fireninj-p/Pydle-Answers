for x in range(5):
    for y in range(5):
        pydle(x, y, "", "white")
        if(x > 0 and y <= x-1):
            pydle(x, y, "+", "green")
        elif(y > x):
            pydle(x, y, "-", "red")
