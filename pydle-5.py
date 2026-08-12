for x in range(5):
    for y in range(5):
        pydle(x, y, "", "red")
        if((y < 1 and x % 2 == 0) 
           or (y >2 and x in (0,4))
           or (y > 3 and x != 2)):
            pydle(x, y, "", "black")
