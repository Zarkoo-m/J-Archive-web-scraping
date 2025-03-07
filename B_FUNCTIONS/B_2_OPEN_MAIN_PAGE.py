from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------
from C_SUPPORTING_FILES.C_1_LOGS import CustomLogger
from C_SUPPORTING_FILES.C_2_EXCEPTION_HANDLERS import handle_exception
from C_SUPPORTING_FILES.C_4_REPEAT_MECHANISM import RepeatMechanism
#-------------------------------------------------------------------

class MainPageOpener:
    
    #----------------------------------------------------------------
    def __init__(self, driver):
        self.logger = CustomLogger().get_logger()  
        self.driver = driver
        self.retry = RepeatMechanism()
        self.open_main_page()
# (A) ------------------------- OPEN MAIN PAGE --------------------------------------------------------------
    def open_main_page(self):

        print("\n[OPEN MAIN PAGE]\n")
        #----------------------------------------------------------------
        try:
            wait = WebDriverWait(self.driver, 5)

            # -------LOCATE - ELEMENT-------
            logo_locator = (By.XPATH, "//img[@src='j-archive.gif' and @alt='Enter the J! Archive']")
            clickable_logo = self.retry.repeat_action(lambda: wait.until(EC.element_to_be_clickable(logo_locator)), ) 

            # ------- ACTION -------
            self.retry.repeat_action(lambda: clickable_logo.click(), "CLICKING MAIN PAGE LOGO")

            # ------- ACTION - LOGGER -------
            self.logger.info("[ACTION - SUCCESSFUL]: Clicked on the main page logo.")
        
        # ------- EXCEPTION HANDLER -------
        except Exception as e:  
            handle_exception("CLICKING MAIN PAGE LOGO", e)
        #-------------------------------------------------------------------    
