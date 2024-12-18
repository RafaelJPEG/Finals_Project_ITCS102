def c16():
    def W_D():
        wt = balance//1000
        wt2 = balance%1000

        fh = wt2//500
        fh2 = wt2%500

        th = fh2//200
        th2 = fh2%200

        y = th2//100
        y2 = th2%100

        u = y2//50
        u2 = y2%50

        i = u2//20
        i2 = u2%20

        o = i2//10
        o2 = i2%10  

        p = o2//5
        p2 = o2%5

        print(f"{wt} - ₱1000 \n{fh} - ₱500 \n{th} - ₱200\n{y} - ₱100 \n{u} - ₱50\n{i} - ₱20 \n{o} - ₱10\n{p} - ₱5")
    
    ask = str(input(f"HELLO DEAR COSTUMER! WELCOME TO RLM BANK! \nWOULD YOU LIKE TO OPEN A BANK ACCOUNT? (yes or no): "))

    if ask.lower() == "yes":
        name = str(input("Enter your name : "))
        balance = float(input("Enter your Innitial deposit : "))

        print(f"\nAccount Details: \n\n\nAccount name: {name}\nBalance: ₱{round(balance,2)} \nBalance Denomination Breakdown:\n")
        W_D()
        
        while True:
            ask2 = str(input("\nBank Services:\n(1)deposit  (2)withdraw  (3)Check Balance  (4)Denomination Breakdown  (5)Termination \nChoose service: "))

            if ask2.lower() == "1":
                ID = int(input("Deposit amount: "))
                balance += ID
                print(f"Hello {name} you deposited an amount of ₱{ID}, your current balance now is ₱{balance}")
                continue
            elif ask2.lower() == "2":
                WI = int(input("Withdrawal amount: "))
                balance -= WI
                print(f"Hello {name} you withdrawn an amount of ₱{WI}, your current balance now is ₱{balance}")
                continue
            elif ask2.lower() == "3":
                print(f"Hello {name} your current balance is ₱{balance}")
                continue
            elif ask2.lower() == "4":
                print(f"Your Balance Breakdown denomination is:")
                W_D()
                continue
            elif ask2.lower() == "5":
                print("Your account has been terminated!")
                break        
            else:
                print('Invalid answer!')
    elif ask.lower() == "no":
            print('Alright, have a nice day!')
    else:
        print('Invalid answer!')
c16()