class UserChoice:
    """ Handles user input for selecting the number of game links to process. """
    #----------------------------------------------------------------
    
    @staticmethod
    def get_user_choice(game_links):
        """ Ask the user whether to process all links or a specific number """
        while True:
            print("\n🔹 CHOOSE PROCESSING OPTION:")
            print("1 - PROCESS (ALL) LINKS")
            print("2 - PROCESS (SPECIFIC NUMBER) OF LINKS")
            choice = input("ENTER CHOICE - (1 or 2): ").strip()
            #----------------------------------------------------------------
            if choice == "1":
                return len(game_links)
            #----------------------------------------------------------------
            elif choice == "2":
                while True:
                    try:
                        num_links = int(input(f"Enter number of links to process (max {len(game_links)}): ").strip())
                        if 1 <= num_links <= len(game_links):
                            return num_links
                        else:
                            print(f" Please enter a number between 1 and {len(game_links)}.")
                    # ------- EXCEPTION HANDLER -------
                    except ValueError:
                        print(" Invalid input. Please enter a valid number.")

            else:
                print(" Invalid choice. Please enter 1 or 2.")
