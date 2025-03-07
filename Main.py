from A_DRIVERS.A_1_DRIVER_SETUP import setup_driver 
#----------------------------------------------------------------------------------------------- 
from B_FUNCTIONS.B_1_OPEN_WEB_SITE import WebsiteOpener
from B_FUNCTIONS.B_2_OPEN_MAIN_PAGE import MainPageOpener
from B_FUNCTIONS.B_3_SEARCH_ENTRY import SearchEntry
from B_FUNCTIONS.B_4_RESULT_SCANNER import ResultScanner
from B_FUNCTIONS.B_5_SEPARATE_GAME import SeparateGame
from B_FUNCTIONS.B_6_ANALYSIS import DataAnalyzer  
from B_FUNCTIONS.B_7_REPEAT_PROCESS import RepeatProcess
#-----------------------------------------------------------------------------------------------
from C_SUPPORTING_FILES.C_3_CLEAR_CACHE_MEMORY import BrowserCacheCleaner
#-----------------------------------------------------------------------------------------------
# (1) - LAUNCHING THE WEBDRIVER
driver = setup_driver()  
print("---------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
# (2) - CLEARING BROWSER CACHE MEMORY
BrowserCacheCleaner.clear_cache(driver) 
print("---------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
# (3) - OPENING THE WEBSITE
website = WebsiteOpener(driver, "https://j-archive.com/") 
print("---------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
# (4) - OPENING THE MAIN PAGE
main_page = MainPageOpener(driver)  
print("---------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
# (5) - SEARCH ENTRY
search_entry = SearchEntry(driver)
print("---------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
# (6) - SCAN SEARCH RESULTS
result_scanner = ResultScanner(driver)
print("---------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
# (7) - EXTRACTING AND PROCESS GAME LINKS
SeparateGame(driver, result_scanner.get_game_links())
#-----------------------------------------------------------------------------------------------
# (8) -  DATA ANALYSIS
print("---------------------------------------------------------------------------------------")
print("\n📊 STARTING DATA ANALYSIS")

analyzer = DataAnalyzer() 
analyzer.analyze_scraped_data()  
print("---------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
# (9) -  REPEAT SKRIPT PROCESS
repeat_process = RepeatProcess(main_function=lambda: exec(open("main.py").read()), driver=driver)  
repeat_process.ask_user()
print("---------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
driver.quit()

