import logging
import time
#-------------------------------------------------------------------
class CustomLogger:
    #-------------------------------------------------------------------
    def __init__(self, level=logging.DEBUG):
        self.logger = logging.getLogger("CustomLogger")
        self.logger.setLevel(level)

        #-------------------------------------------------------------------
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            formatter.converter = time.gmtime 
            formatter.formatTime = self.custom_time_format  

            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
            
    #-------------------------------------------------------------------
    @staticmethod
    def custom_time_format(record, datefmt=None):
        log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(record.created)) 
        elapsed_time = f"{record.relativeCreated / 1000:.1f} sec"
        return f"{log_time} - {elapsed_time}"
    #-------------------------------------------------------------------
    def get_logger(self):
        return self.logger