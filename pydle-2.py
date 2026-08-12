for x in range(5):
    for y in range(5):
        pydle(x, y, "", "green")
        if((x % 2 == 1) and (y % 2 == 1)):
            pydle(x, y, "", "red")
