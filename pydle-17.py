for x in range(5):
    for y in range(5):
        if x==2 or y == 2 or x==3 and y in (1,3):
            pydle(x, y, ">", "red")
        else:
            pydle(x, y, "", "white")
