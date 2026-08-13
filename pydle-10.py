for x in range(5):
    for y in range(5):
        if abs(y-x)==1:
            pydle(x, y, "", "green")
            pydle(x, x+1, "", "purple")
            pydle(x, x, "", "white")
        if abs(y-x)==2:
            pydle(x, y, "", "yellow")
            pydle(x, x+2, "", "blue")
        if abs(y-x)==3:
            pydle(x, y, "", "orange")
            pydle(x, x+3, "", "red")
            pydle(x, x+4, "", "brown")
