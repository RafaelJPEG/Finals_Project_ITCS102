name = str(input(f"What is your name?\n\n"))
ask = str(input(f"\nHello {name}! would you like to use this MENU PROGRAM? (yes/no):\n\n"))

if ask.lower() == 'yes':
    while True:
        print("Main Menu\n\n1.Pythong printing\n 2.back")
        ask2 = int(input("Enter the number of you choice here --->"))
        while True:
            if ask2 == 1:
                pass
            elif ask2 == 2:
                break
            else:
                print("Invalid answer!")
                # break
elif ask.lower() == "no":
    pass
# else:
#     print("invalid answer!")
