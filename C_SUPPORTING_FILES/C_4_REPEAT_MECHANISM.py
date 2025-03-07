import time
from C_SUPPORTING_FILES.C_1_LOGS import CustomLogger
from C_SUPPORTING_FILES.C_2_EXCEPTION_HANDLERS import handle_exception
#----------------------------------------------------------------
class RepeatMechanism:
    
    #----------------------------------------------------------------
    def __init__(self, retries=3, delay=2):
        self.retries = retries  
        self.delay = delay  
        self.logger = CustomLogger().get_logger()
    #----------------------------------------------------------------
    def repeat_action(self, action, action_name="ACTION"):
        "Attempts to perform the action up to 3 times before reporting an error."
        for attempt in range(1, self.retries + 1):
            try:
                # ------- ACTION -------
                return action()
            
            # ------- EXCEPTION HANDLER -------
            except Exception as e:
                self.logger.warning(f"[{action_name} - FAILED] Attempt {attempt}/{self.retries} - Retrying in {self.delay} sec")
                handle_exception(action_name, e)
                time.sleep(self.delay)  
                
                
       
        self.logger.error(f"[{action_name} - FAILED] All {self.retries} attempts exhausted.")
        return None
