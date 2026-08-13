for x in range(5):
    for y in range(5):
        pydle(x, y, "", "blue")
        if x == 2 or y == 2:
            pydle(x, y, "", "white")
        elif x<2 and y < 2 or x > 2 and y > 2 :
            pydle(x, y, "", "green")
