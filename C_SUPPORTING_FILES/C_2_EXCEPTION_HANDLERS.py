import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#-------------------------------------------------------------------
logger = logging.getLogger("ExceptionHandler")
#-------------------------------------------------------------------

def handle_exception(context, e):
    """General exception handler for Selenium automation."""
    #-------------------------------------------------------------------
    # TIMEOUT
    if isinstance(e, TimeoutException):
        logger.error(f"[EXCEPTION - TIMEOUT] | ({context}) - Element not detected within timeframe!")
    #-------------------------------------------------------------------
    # NO SUCH ELEMENT
    elif isinstance(e, NoSuchElementException):
        logger.error(f"[EXCEPTION - NOT FOUND] | ({context}) - No such element found.")
    #-------------------------------------------------------------------
    # OTHER ERRORS
    else:
        logger.critical(f"[EXCEPTION - ERROR] | ({context}) - Unexpected error: {e}")
