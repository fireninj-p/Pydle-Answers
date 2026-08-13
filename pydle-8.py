for x in range(5):
    for y in range(5):
        pydle(x, y, "", "blue")
        if y > 3:
            pydle(x, y, "", "green")
        elif x == 2 or y == 1 and x%2==1:
            pydle(x, y, "", "brown")
