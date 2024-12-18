def act15():
    #for loop complete range
    for e in range(0 , 11): 
        print(e, end = " ")
        for y in range(0, e):
            print("*", end = " ")
        print()
        
    for e in reversed(range(0 , 12)): 
        print(e, end = " ")
        for y in range(0, e):
            print("*", end = " ")
        print()
act15()