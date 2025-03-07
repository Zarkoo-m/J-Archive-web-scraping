from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
#-------------------------------------------------------------------

class BrowserCacheCleaner:
    @staticmethod
    #-------------------------------------------------------------------

    def clear_cache(driver):
        
        print("[CLEARING CACHE MEMORY - STARTED]")

        #-------------------------------------------------------------------

        ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('i').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
        time.sleep(2)  

       
        ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('DELETE').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
        time.sleep(2) 

       
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(3)  
        #-------------------------------------------------------------------

        print("[CACHE MEMORY - CLEARED SUCCESSFULLY!]")