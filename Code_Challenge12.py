def c12():
    for e in range(6, 0, -1):
        for r in range(1, e):
            print(" ", end= " ")
        for t in range(6, e , -1):
            print("*", end=" ")
        for y in range(6, e, -1):
            print("*", end=" ")
        print()

    for u in range(4):
        print("        * *")
c12()