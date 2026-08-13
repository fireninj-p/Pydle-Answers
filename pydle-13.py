for x in range(5):
    for y in range(5):
        pydle(x, y, "", "black")
        pydle(2, 2, "", "red")
        if y < 3 and x in (0,4) or y==3 and x in (1,2,3) or x==2 and y==1:
            pydle(x, y, "", "white")
