from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------
from C_SUPPORTING_FILES.C_1_LOGS import CustomLogger
from C_SUPPORTING_FILES.C_2_EXCEPTION_HANDLERS import handle_exception
from C_SUPPORTING_FILES.C_4_REPEAT_MECHANISM import RepeatMechanism
from D_HELPERS.D_1_USER_INPUT_1 import UserInputHandler1
#-------------------------------------------------------------------

class SearchEntry:
    
    #----------------------------------------------------------------
    def __init__(self, driver):
        self.logger = CustomLogger().get_logger()  
        self.driver = driver
        self.retry = RepeatMechanism() 
        self.search_entry()
# (A) ------------------------- SEARCH FILED --------------------------------------------------------------
    def search_entry(self):

        print("\n[SEARCH ENTRY]\n")
        #-------------------------------------------------------------------
        try:
            wait = WebDriverWait(self.driver, 20)

            # -------LOCATE - INPUT FIELD-------
            search_input_locator = (By.ID, "search")
            search_input = self.retry.repeat_action(lambda: wait.until(EC.presence_of_element_located(search_input_locator)), "LOCATING SEARCH INPUT FIELD") 

            # ------- WAIT FOR USER INPUT -------
            search_value = UserInputHandler1.get_user_input()

            if search_value:
                # ------- ENTER VALUE -------
                search_input.clear()
                search_input.send_keys(search_value)
                self.logger.info(f"[ACTION - SUCCESSFUL]: Entered search value: {search_value}")

                # ------- LOCATE & CLICK SEARCH BUTTON -------
                search_button_locator = (By.CLASS_NAME, "search_button")
                search_button = self.retry.repeat_action(lambda: wait.until(EC.element_to_be_clickable(search_button_locator)), "LOCATING SEARCH BUTTON") 
                
                # ------- ACTION -------
                self.retry.repeat_action(lambda: search_button.click(), "CLICKING SEARCH BUTTON")  
                
                # ------- ACTION - LOGGER -------
                self.logger.info("[ACTION - SUCCESSFUL]: Clicked the search button.")
            else:
                self.logger.warning("[ACTION - FAILED]: No input received. Search aborted.")

        # ------- EXCEPTION HANDLER -------
        except Exception as e:  
            handle_exception("SEARCH ENTRY", e)

