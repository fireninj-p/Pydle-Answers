for x in range(5):
    for y in range(5):
        pydle(x, y, "", "white")
        if y in (0,2) or y < 3 and x%2==1:
            pydle(x, y, "", "red")
        if y > 2 and x in (1,2,3):
            pydle(x, y, "", "orange")
            if y < 4 and x%2==1:
                pydle(x, y, "", "black")
