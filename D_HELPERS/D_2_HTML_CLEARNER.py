from bs4 import BeautifulSoup
#----------------------------------------------------------------
class HtmlCleaner:
   
    #----------------------------------------------------------------
    @staticmethod
    def clean_html(raw_html):
        
        soup = BeautifulSoup(raw_html, "html.parser")
        return soup.get_text(separator=" ").strip()
