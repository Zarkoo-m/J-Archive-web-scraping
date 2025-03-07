import threading
#------------------------------------------------------------
class UserInputHandler1:
    """ Class to handle user input with a timeout mechanism. """
    
    #------------------------------------------------------------
    @staticmethod
    def get_user_input(timeout=300):
        """ Waits for user input for up to `timeout` seconds. """
        user_input = [None]  
        input_thread = threading.Thread(target=UserInputHandler1._input_with_timeout, args=(user_input,))
        input_thread.start()
        input_thread.join(timeout=timeout)  

        return user_input[0]  
    
    #------------------------------------------------------------
    @staticmethod
    def _input_with_timeout(user_input):
        """ Helper method to get input within the given time limit. """
        try:
            user_input[0] = input("[INPUT REQUIRED] Enter search value (Timeout: 5 min): ")
        except:
            pass  
