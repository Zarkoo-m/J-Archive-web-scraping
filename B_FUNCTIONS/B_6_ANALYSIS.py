import csv
import collections
import os
import datetime
#-------------------------------------------------------------------
from D_HELPERS.D_6__CONVERT_TO_BINARY2 import BinaryConverter
from D_HELPERS.D_7_EXCEL_REPORT import ExcelReport
from D_HELPERS.D_9_HTML_REPORT import HtmlReport
#-------------------------------------------------------------------
class DataAnalyzer:
    
    def __init__(self):
        
        self.data_file = os.path.join(os.path.expanduser("~"), "Desktop", "scraped_data.csv")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.excel_file = os.path.join(os.path.expanduser("~"), "Desktop", f"scraped_analysis_{timestamp}.xlsx")
        self.html_file = os.path.join(os.path.expanduser("~"), "Desktop", f"scraped_analysis_{timestamp}.html")
        self.scraped_data = self.load_scraped_data()
           
# (A) ------------------------- LOADING SCRAPED DATA --------------------------------------------------------------
    def load_scraped_data(self):
       
        try:
            data = []
            with open(self.data_file, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append({
                        "Category": BinaryConverter.from_binary(row["Category"]),
                        "Clue": BinaryConverter.from_binary(row["Clue"]),
                        "Answer": BinaryConverter.from_binary(row["Answer"])
                    })
            return data
        
        # ------- EXCEPTION HANDLER ------- 
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
# (B) ------------------------- ANALYZE --------------------------------------------------------------
    def analyze_scraped_data(self):
       
        if not self.scraped_data:
            print("No data available for analysis!")
            return

        print(f" Number of loaded records: {len(self.scraped_data)}")

        # 📌 Analysis of the most frequently occurring Clue values
        clue_counter = collections.Counter([(entry["Clue"], entry["Category"], entry["Answer"]) for entry in self.scraped_data])
        sorted_clues = clue_counter.most_common()

        # 📌 Analysis of the most frequently occurring categories
        category_counter = collections.Counter([entry["Category"] for entry in self.scraped_data])
        sorted_categories = category_counter.most_common()

        # 📌 Analysis of the most frequently occurring answers
        answer_counter = collections.Counter([entry["Answer"] for entry in self.scraped_data])
        sorted_answers = answer_counter.most_common()

        # 📌 Print results in the terminal
        print("\n🔹 THE MOST COMMON CLUE VALUES 🔹\n")
        for (clue, category, answer), count in sorted_clues:
            print(f"📌 {clue} | Category: {category} | Answer: {answer} | Occurrences: {count}")

        print("\n🔹 THE MOST COMMON CATEGORIES 🔹\n")
        for category, count in sorted_categories:
            print(f"📌 Category: {category} | Occurrences: {count}")

        print("\n🔹 THE MOST COMMON ANSWERS🔹\n")
        for answer, count in sorted_answers:
            print(f"📌 Answer: {answer} | Occurrences: {count}")

# (C) ------------------------- EXPORT TO EXCEL --------------------------------------------------------------
        ExcelReport.create_excel_report(self.excel_file, sorted_clues, sorted_categories, sorted_answers)
        
# (D) ------------------------- EXPORT TO HTML --------------------------------------------------------------        
        HtmlReport.generate_html_report(self.html_file, sorted_clues, sorted_categories, sorted_answers) 

        
