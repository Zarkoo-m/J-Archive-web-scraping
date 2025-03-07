from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#-------------------------------------------------------------------
from C_SUPPORTING_FILES.C_1_LOGS import CustomLogger
from C_SUPPORTING_FILES.C_2_EXCEPTION_HANDLERS import handle_exception
from C_SUPPORTING_FILES.C_4_REPEAT_MECHANISM import RepeatMechanism
#-------------------------------------------------------------------
class WebsiteOpener:
    #-------------------------------------------------------------------
    def __init__(self, driver, url="https://j-archive.com/"): 
        self.logger = CustomLogger().get_logger()  
        self.driver = driver  
        self.url = url
        self.retry = RepeatMechanism()
        self.open_website()
# (A) ------------------------- OPEN WEB SITE --------------------------------------------------------------
    def open_website(self):
        
        print("\n[OPEN WEB SITE]\n")
        #-------------------------------------------------------------------
        try:
            # ------- ACTION -------
            self.retry.repeat_action(lambda: self.driver.get(self.url), "OPENING WEB SITE") 
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            # ------- ACTION - LOGGER -------
            self.logger.info(f"[ACTION - SUCCESSFUL]: {self.url}")
            
        # ------- EXCEPTION HANDLER -------    
        except Exception as e:
            handle_exception("OPENING WEB SITE", e)
        #-------------------------------------------------------------------
