def c8():
    total_sum = 0  

    print("Please enter 10 random numbers:")

    for i in range(10):
        while True:
            try:
                number = float(input(f"Enter number {i + 1}: "))
                total_sum += number  
                break  
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    print(f"The sum of the provided numbers is: {total_sum}")
c8():