#Code Challenge 9 - for loop
def c9():
    for r in range(0 , 11):
        print(r, end = " ")
        for y in range(0 , r): 
            print("*" , end= " ")
        print()
c9()