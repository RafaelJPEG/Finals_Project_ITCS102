# Main Program
name = str(input("What's your name?: "))

def main():
    # Ask if the user wants to use the program
    user_response = input(f"Hello {name}! Would you like to use this program? (yes/no): ").strip().lower()

    if user_response == 'yes':
        # Main program loop
        while True:
            # Main Menu
            print("\nThis Main Menu are composed of activities and code challenges that we've created on our subject ITCS102 during our first semester")
            print("\n=====Main Menu=====")
            print("1. Activities")
            print("2. Code Challenges")
            print("3. Exit Program")
            print("")
            choice = input("Choose an option (1, 2, or 3): ")

            if choice == '1':
                # Activities Submenu
                while True:
                    print("\nActivities Submenu")
                    print("Choose an activity (1-26):")
                    activity_choice = input("Enter a number (1-26): ")
                    if activity_choice == '1':
                        from Metran_Activity1 import act1
                    elif activity_choice == '2':
                        from Metran_Activity2 import act2
                    elif activity_choice == '3':
                         from Metran_Activity3 import act3
                    elif activity_choice == '4':
                        from Metran_Activity4 import act4
                    elif activity_choice == '5':
                        from Metran_Activity5 import act5
                    elif activity_choice == '6':
                        from Metran_Activity6 import act6
                    elif activity_choice == '7':
                        from Metran_Activity7 import act7
                    elif activity_choice == '8':
                        from Metran_Activity8 import act8
                    elif activity_choice == '9':
                        from Metran_Activity9 import act9
                    elif activity_choice == '10':
                        from Metran_Activity10 import act10
                    elif activity_choice == '11':
                        from Metran_Activity11 import act11
                    elif activity_choice == '12':
                        from Metran_Activity12 import act12
                    elif activity_choice == '13':
                        from Metran_Activity13 import act13
                    elif activity_choice == '14':
                        from Metran_Activity14 import act14
                    elif activity_choice == '15':
                        from Metran_Activity15 import act15
                    elif activity_choice == '16':
                        from Metran_Activity16 import act16
                    elif activity_choice == '17':
                        from Metran_Activity17 import act17
                    elif activity_choice == '18':
                        from Metran_Activity18 import act18
                    elif activity_choice == '19':
                        from Metran_Activity19 import act19
                    elif activity_choice == '20':
                        from Metran_Activity20 import act20
                    elif activity_choice == '21':
                        from Metran_Activity21 import act21
                    elif activity_choice == '22':
                        from Metran_Activity22 import act22
                    elif activity_choice == '23':
                        from Metran_Activity23 import act23
                    elif activity_choice == '24':
                        from Metran_Activity24 import act24
                    elif activity_choice == '25':
                        from Metran_Activity25 import act25
                    elif activity_choice == '26':
                        from Metran_Activity26 import act26
                    else:
                        print("Invalid choice. Please select a valid activity (1-26).")
                        continue

                    # Ask if the user wants to choose another activity
                    continue_activities = input("Do you want to choose another activity? (yes/no): ").lower()
                    if continue_activities != 'yes':
                        break

            elif choice == '2':
                # Code Challenges Submenu
                while True:
                    print("\nCode Challenges Submenu")
                    print("Choose a code challenge (1-16):")
                    challenge_choice = input("Enter a number (1-16): ")

                    if challenge_choice == '1':
                        from Code_Challenge1 import c1
                    elif challenge_choice == '2':
                        from Code_Challenge2 import c2
                    elif challenge_choice == '3':
                        from Code_Challenge3 import c3
                    elif challenge_choice == '4':
                        from Code_Challenge4 import c4
                    elif challenge_choice == '5':
                        from Code_Challenge5 import c5
                    elif challenge_choice == '6':
                        from Code_Challenge6 import c6
                    elif challenge_choice == '7':
                        from Code_Challenge7 import c7
                    elif challenge_choice == '8':
                        from Code_Challenge8 import c8
                    elif challenge_choice == '9':
                        from Code_Challenge9 import c9
                    elif challenge_choice == '10':
                        from Code_Challenge10 import c10
                    elif challenge_choice == '11':
                        from Code_Challenge11 import c11
                    elif challenge_choice == '12':
                        from Code_Challenge12 import c12
                    elif challenge_choice == '13':
                        from Code_Challenge13 import c13
                    elif challenge_choice == '14':
                        from Code_Challenge14 import c14
                    elif challenge_choice == '15':
                        from Code_Challenge15 import c15
                    elif challenge_choice == '16':
                        from Code_Challenge16 import c16
                    else:
                        print("Invalid choice. Please select a valid code challenge (1-16).")
                        continue

                    # Ask if the user wants to choose another code challenge
                    continue_challenges = input("Do you want to choose another code challenge? (yes/no): ").strip().lower()
                    if continue_challenges != 'yes':
                        break

            elif choice == '3':
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option (1, 2, or 3).")

    else:
        print("Goodbye!")

main()
