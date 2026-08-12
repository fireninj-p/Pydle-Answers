for x in range(5):
    for y in range(5):
        pydle(2, 0, "", "green")
        if y in (1,2) and x in (1,2,3):
            pydle(x, y, "🍒", "green")
        elif(x == 2 and y > 2):
            pydle(x, y, "", "brown")
