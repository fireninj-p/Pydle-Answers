for x in range(5):
    for y in range(5):
        pydle(x, y, "⊞", "black")
        if y<2 and x!=2:
            pydle(x, y, "", "blue")
            if y>0 and x>3:
                pydle(x-3, y+1, "", "blue")
                pydle(x, y, "⊞", "black")
