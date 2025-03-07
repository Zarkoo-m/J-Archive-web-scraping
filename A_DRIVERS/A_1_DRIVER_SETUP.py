from selenium import webdriver  
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
#-------------------------------------------------------------------
import logging
#-------------------------------------------------------------------
logging.getLogger('selenium').setLevel(logging.ERROR)
#-------------------------------------------------------------------

def setup_driver():
    
    service = ChromeService(ChromeDriverManager().install())
    options = ChromeOptions()
    
    
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu") 
    options.add_argument("--window-size=1920,1080")  
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage") 
    
    driver = webdriver.Chrome(service=service, options=options)
    return driver
#-------------------------------------------------------------------
