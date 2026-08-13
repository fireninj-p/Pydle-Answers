for x in range(5):
    for y in range(5):
        pydle(x, y, "", "green")
        if x%2==1 and y not in (0,2) or x == 2 and y in (2,3):
            pydle(x, y, "", "black")
