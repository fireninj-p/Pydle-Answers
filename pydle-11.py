for x in range(5):
    for y in range(5):
        pydle(3, 1, "🕊️", "blue")
        pydle(x, y, "", "blue")
        if x == 2 and y < 3 or x%2 == 1 and (y < 4 and y > 1) or y >3 and x in (0,4):
            pydle(x, y, "", "black")
