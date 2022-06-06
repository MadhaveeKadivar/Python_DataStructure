import logging
# Logging

def func():
    """ 
        Description: 
            This function is used for maintain log file and print log message to file and console
        Parameter:
            None
        Return:
            returns name of logger 
    """
    logging.basicConfig(filename = 'file.log',format = '%(asctime)s | %(levelname)s | %(lineno)d: %(message)s')
    logger = logging.getLogger("root_logger")
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    log_format = '%(message)s'
    console_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(console_handler)
    return logger
