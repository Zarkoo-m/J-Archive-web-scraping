from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------
from C_SUPPORTING_FILES.C_1_LOGS import CustomLogger
from C_SUPPORTING_FILES.C_2_EXCEPTION_HANDLERS import handle_exception
from C_SUPPORTING_FILES.C_4_REPEAT_MECHANISM import RepeatMechanism
from D_HELPERS.D_2_HTML_CLEARNER import HtmlCleaner
#-------------------------------------------------------------------

class ResultScanner:
    #----------------------------------------------------------------
    def __init__(self, driver):
        self.logger = CustomLogger().get_logger()  
        self.driver = driver
        self.retry = RepeatMechanism()
        self.game_links = [] 
        self.scan_results()
# (A) ------------------------- SCAN RESULT --------------------------------------------------------------
    def scan_results(self):

        print("\n[SCANNING SEARCH RESULTS]\n")
        separator = "-" * 100  
        #----------------------------------------------------------------
        try:
            wait = WebDriverWait(self.driver, 10)

            # ------- LOCATE - ALL RESULT ROWS -------
            rows_locator = (By.XPATH, "//tbody/tr")
            result_rows = self.retry.repeat_action(lambda: wait.until(EC.presence_of_all_elements_located(rows_locator)),"LOCATING ALL SEARCH RESULT ROWS" ) 

            total_results = len(result_rows)
            print(f"\nTOTAL NUMBER OF RESULTS: {total_results}\n")
            print(separator)  
            self.logger.info(f"[ACTION - SUCCESSFUL]: Found {total_results} results.")

            valid_results_count = 0  

            # ------- ITERATE & FILTER RESULTS -------
            for index, row in enumerate(result_rows, start=1):
                try:
                    # LOCATE ALL `<td>` ELEMENTS WITHIN `tr`
                    td_elements = row.find_elements(By.TAG_NAME, "td")
                    
                    # FIND `<a>` INSIDE THE FIRST `<td>` (SHOULD CONTAIN showgame.php?game_id)
                    first_td = td_elements[0]
                    a_element = first_td.find_element(By.TAG_NAME, "a") if first_td else None

                    # CHECK IF IT'S A VALID RESULT (CONTAINS showgame.php?game_id)
                    if not a_element or "showgame.php?game_id" not in a_element.get_attribute("href"):
                        continue  

                    game_url = a_element.get_attribute("href").strip()  
                    self.game_links.append(game_url)  

                    valid_results_count += 1

                    # EXTRACT CONTENT FROM `<td>` ELEMENTS
                    td_contents = [td.get_attribute("innerHTML").strip() for td in td_elements]

                    # PROCESS CONTENT (REMOVE HTML TAGS)
                    clean_contents = [HtmlCleaner.clean_html(td) for td in td_contents]

                    # CREATE FORMATTED RESULT
                    formatted_result = f"{valid_results_count}. " + " | ".join(clean_contents)

                    # ------- PRINT FORMATTED RESULT -------
                    print(f"\n{formatted_result}")
                    print(separator)  

                    # ------- ACTION - LOGGER -------
                    self.logger.info(f"[ACTION - SUCCESSFUL]: Processed result {valid_results_count}")
                    print(separator)  
                    
                # ------- EXCEPTION HANDLER ------- 
                except Exception as e:
                    handle_exception(f"PROCESSING RESULT {index}", e)

            # IF NO VALID RESULTS WERE FOUND
            if valid_results_count == 0:
                print("\n NO VALID RESULTS FOUND!")
                self.logger.warning("[ACTION - FAILED]: No valid results found.")

        # ------- EXCEPTION HANDLER -------
        except Exception as e:  
            handle_exception("SCANNING SEARCH RESULTS", e)
        #-------------------------------------------------------------------

# (B) ------------------------- GAME LINKS --------------------------------------------------------------
    def get_game_links(self):
        """ Now correctly returns a populated list of all found game links. """
        
        return self.game_links  
