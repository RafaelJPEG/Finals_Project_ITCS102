def c14():
    num = True
    sum = 0

    while num == True:
        sk = eval(input("Please enter a number ---> "))

        if sk== 0 :
            print("Loop Terminated")
            print(f"The sum of all the numbers is {sum}")
            break
        else:
            print("Please continue entering a number")
            sum += sk
            continue
c14()