import time
#-------------------------------------------------------------------
class RepeatProcess:
    def __init__(self, main_function, driver):
 
        self.main_function = main_function  
        self.driver = driver
        
        
# (A) ------------------------- USER INPUT - REPEAT PROCESS --------------------------------------------------------------
    def ask_user(self):

        while True:
            print("\n🔄 [REPEAT PROCESS] 🔄")
            print("1️⃣ - YES (Repeat the process)")
            print("2️⃣ - QUIT (Exit the script)")

            choice = input("\n👉 Enter your choice (1/2): ").strip()
            #------------------------CHOICE 1-------------------------------------------
            if choice == "1":
                print("\n✅ Restarting the process...\n")
                self.driver.quit()  # CLOSE PREVIOUS BROWSER
                time.sleep(2)
                self.main_function()  # START NEW BROWSER
                break
            #------------------------CHOICE 2-------------------------------------------
            elif choice == "2":
                print("\n👋 Exiting the script. Goodbye!\n")
                self.driver.quit() 
                time.sleep(2)
                exit()  

            else:
                print("\n❌ Invalid input! Please enter '1' to repeat or '2' to quit.")
