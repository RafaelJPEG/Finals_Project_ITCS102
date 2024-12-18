def c7():
    customer_status = input("Are you a customer? (yes/no): ")
    if customer_status.lower() == "yes":
        purchase_status = input("Did you buy a grocery? (yes/no): ")
        
        if purchase_status.lower() == "yes":
            item_name = input("Name of the item: ")
            item_price = float(input("Enter the price of the item: "))
            customer_age = int(input("Enter your age: "))
            amount_given = float(input("Amount Given: "))

            tax_amount = item_price * 0.123 if 18 <= customer_age < 60 else 0
            taxed_price = item_price + tax_amount
            
            discount_amount = taxed_price * 0.052 if customer_age >= 60 else 0
            total_cost = taxed_price - discount_amount
            change_due = amount_given - total_cost

            print(f"You bought: {item_name} for {item_price:.2f} Php.")
            if tax_amount:
                print(f"Tax: {tax_amount:.2f} Php.")
            if discount_amount:
                print(f"Discount: {discount_amount:.2f} Php.")
            print(f"Total: {total_cost:.2f} Php.")
            print(f"Change: {change_due:.2f} Php.")
            print("Thank you for shopping!")
        else:
            print("Thank you for visiting!")
c7()
