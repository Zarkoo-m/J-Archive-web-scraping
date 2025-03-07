import os
import csv
#----------------------------------------------------------------
class CsvSaver:
    """ Utility class for saving scraped data to a CSV file. """
    #----------------------------------------------------------------
    @staticmethod
    def save_data_to_csv(scraped_data):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        csv_file_path = os.path.join(desktop_path, "scraped_data.csv")

        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Category", "Clue", "Answer"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(scraped_data)

        print(f"\n✅ Scraped data successfully saved to: {csv_file_path}")
