# code challenge 10
def c10():
    for e in range(6):
        for r in range(5 - e):
            print(" ", end=" ")
        for z in range(e + 1):
            print("*", end=" ")
        for w in range(e):
            print("*", end=" ")
        print()

    for e in range(4, -1, -1):
        for r in range(5 - e):
            print(" ", end=" ")
        for z in range(e + 1):
            print("*", end=" ")
        for w in range(e):
            print("*", end=" ")
        print()
c10()