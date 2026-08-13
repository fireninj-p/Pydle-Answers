for x in range(5):
    for y in range(5):
        pydle(x, y, "", "brown")
        pydle(2, 3, "", "red")
        pydle(2, 2, "", "orange")
        if y==2 and x%2==1:
            pydle(x, y, "", "blue")
        if y > 1 and x in (0,4):
            pydle(x, y, "", "orange")
            pydle(y-1, x-3, "", "orange")
