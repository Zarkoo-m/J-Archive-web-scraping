import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#-------------------------------------------------------------------
from C_SUPPORTING_FILES.C_1_LOGS import CustomLogger
from C_SUPPORTING_FILES.C_2_EXCEPTION_HANDLERS import handle_exception
from C_SUPPORTING_FILES.C_4_REPEAT_MECHANISM import RepeatMechanism
from D_HELPERS.D_3_CONVERT_TO_BINARY import BinaryConverter
from D_HELPERS.D_4_USER_INPUT2_CHOICE import UserChoice
from D_HELPERS.D_5_CSV_SAVER import CsvSaver
#-------------------------------------------------------------------
class SeparateGame:
    
    #----------------------------------------------------------------
    def __init__(self, driver, game_links):
        self.logger = CustomLogger().get_logger()  
        self.driver = driver
        self.retry = RepeatMechanism()
        self.actions = ActionChains(self.driver)  
        self.scraped_data = [] 

# (A) ------------------------- CHECK LINKS OF GAMES --------------------------------------------------------------
        if not game_links:
            print("\n NO GAME LINKS FOUND! Skipping game analysis.")
            self.logger.warning("[ACTION - SKIPPED]: No game links provided.")
            return  

        self.game_links = game_links  
        print(f"✅ {len(self.game_links)} game links found!")
        print("---------------------------------------------------------------------------------------")
        
        # ------- USER CHOICE -------
        self.num_games_to_process = UserChoice.get_user_choice(self.game_links)
        # ------- PROCESS GAME -------
        self.process_games()
        # ------- CSV SAVER -------
        CsvSaver.save_data_to_csv(self.scraped_data)

# (C) ------------------------- PROCESS GMAES - INDIVIDUALLY --------------------------------------------------------------
    def process_games(self):

        print("\n[PROCESSING INDIVIDUAL GAMES]\n")
        separator = "-" * 100  

        for index, game_link in enumerate(self.game_links[:self.num_games_to_process], start=1):  
            try:
                start_time = time.time()  

                print(f"\n➡️ OPENING GAME {index}: {game_link}")
                
                # ------- OPEN GAME PAGE -------
                self.retry.repeat_action(lambda: self.driver.get(game_link), f"OPENING GAME PAGE {index}")

                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

                wait = WebDriverWait(self.driver, 10)

                #------- (TABLES) LOCATE ALL TABLES PER GAME------- 
                table_round_locator = (By.XPATH, "//table[contains(@class, 'round')]")
                table_round_elements = self.retry.repeat_action(
                    lambda: wait.until(EC.presence_of_all_elements_located(table_round_locator)),
                    f"LOCATING TABLE ELEMENTS WITH CLASS 'round' ON GAME PAGE {index}"
                )

                end_time = time.time()  
                elapsed_time = end_time - start_time  

                print(f"\n✅ (GAME)) {index} SCANNED SUCCESSFULLY IN : {elapsed_time:.2f} seconds.")
                print(f"📌 NUMBER OF ROUNDS : {len(table_round_elements)}")

                #------- (CATEGORIES) LOCATE AND EXTRACT CATEGORIES PER TABLE-------
                table_categories = []
                for table_index, table in enumerate(table_round_elements, start=1):
                    category_elements = table.find_elements(By.XPATH, ".//td[contains(@class, 'category')]//td[contains(@class, 'category_name')]")
                    categories = [category.text.strip() for category in category_elements if category.text.strip()]
                    
                    if categories:
                        table_categories.append(categories)
                        print(f"📌 -CATEGORIES FOR ROUND - {table_index}: {', '.join(categories)}")
                    else:
                        table_categories.append([])
                        print(f"📌 -CATEGORIES FOR ROUND - {table_index}: No categories found.")
                        
                # ----------------- SCROLL SECTION -------------------------
                
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

                self.driver.execute_script("window.scrollTo(0, 0);")
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

                # ------------- (EACH CLUE) OPEN CLUE DETAILS IN NEW TAB -------------

                print("\n[OPENING CLUE DETAILS TO EXTRACT CLUE TEXT & ANSWERS]\n")

                for table_index, table in enumerate(table_round_elements, start=1):
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", table)
                    WebDriverWait(self.driver, 5).until(EC.visibility_of(table))

                    categories = table_categories[table_index - 1]  

                    if table_index == 3:  # Final Jeopardy round
                        print(f"\n📌-- EXTRACTING CLUE & ANSWER IN ROUND -- {table_index}:\n")

                        try:
                            fj_clue_element = WebDriverWait(table, 5).until(
                                EC.presence_of_element_located((By.XPATH, ".//td[@id='clue_FJ' and contains(@class, 'clue_text')]"))
                            )
                            fj_clue_text = fj_clue_element.text.strip()

                            hover_element = WebDriverWait(table, 5).until(
                                EC.presence_of_element_located((By.XPATH, ".//div[contains(@onmouseover, 'toggle')]"))
                            )
                            self.actions.move_to_element(hover_element).perform()

                            answer_element = WebDriverWait(table, 3).until(
                                EC.presence_of_element_located((By.XPATH, ".//em[@class='correct_response']"))
                            )
                            answer_text = re.sub(r"<.*?>", "", answer_element.text.strip()) 

                            # save data in binday format
                            self.scraped_data.append({
                                "Category": BinaryConverter.to_binary(categories[0]),
                                "Clue": BinaryConverter.to_binary(fj_clue_text),
                                "Answer": BinaryConverter.to_binary(answer_text)
                            })

                            print(f"✅ Saved Data: {self.scraped_data[-1]}")  
                            
                        # ------- EXCEPTION HANDLER ------- 
                        except Exception as e:
                            print(f" Failed to extract Final Jeopardy clue & answer: {e}")
                    #--------------------------------------------------------------------------------------------------------
                    else:
                        clue_links = table.find_elements(By.XPATH, ".//td[contains(@class, 'clue_order_number')]/a")

                        print(f"\n📌 -- EXTRACTING CLUES & ANSWERS IN TABLE -- {table_index}:\n")

                        for clue_number, clue_link in enumerate(clue_links, start=1):
                            try:
                                category_index = (clue_number - 1) % 6  
                                category = categories[category_index] if category_index < len(categories) else "Unknown"

                                # Open link in new tab
                                clue_url = clue_link.get_attribute("href")
                                self.driver.execute_script(f"window.open('{clue_url}', '_blank');")

                                WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
                                self.driver.switch_to.window(self.driver.window_handles[-1])

                                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

                                # Locate clue text in textarea
                                clue_textarea = WebDriverWait(self.driver, 5).until(
                                    EC.presence_of_element_located((By.XPATH, "//textarea[contains(@class, 'clue_text_input')]"))
                                )
                                raw_clue_text = clue_textarea.get_attribute("value").strip()  
                                clue_text = re.sub(r"<.*?>", "", raw_clue_text)

                                answer_input = WebDriverWait(self.driver, 5).until(
                                    EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'clue_correct_response_input')]"))
                                )
                                answer_text = re.sub(r"<.*?>", "", answer_input.get_attribute("value").strip())
                                
                                # ------- ACTION -------
                                # save data in binday format
                                self.scraped_data.append({
                                    "Category": BinaryConverter.to_binary(category),
                                    "Clue": BinaryConverter.to_binary(clue_text),
                                    "Answer": BinaryConverter.to_binary(answer_text)
                                })

                                print(f"✅ Saved Data: {self.scraped_data[-1]}")  

                                self.driver.close()
                                self.driver.switch_to.window(self.driver.window_handles[0])
                                
                            # ------- EXCEPTION HANDLER ------- 
                            except Exception as e:
                                print(f"⚠️ Failed to extract clue details: {e}")
                                self.driver.switch_to.window(self.driver.window_handles[0])

                print(separator)
            # ------- EXCEPTION HANDLER ------- 
            except Exception as e:
                handle_exception(f"PROCESSING GAME PAGE {index}", e)

