def tupled():
    for k in range(4):
        for ij in ((0, k), (3-1, k), (k, 0), (k, 5-1)):
            print ij
print tupled()