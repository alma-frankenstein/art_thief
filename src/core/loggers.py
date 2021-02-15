import sys
import logging

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
class ALogger:
    def __init__(self, name, color):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler(sys.stdout)
        hq_formatter = logging.Formatter(color + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
        handler.setFormatter(hq_formatter)
        self.logger.addHandler(handler)  # add handler to logger
        
        self.logger.propagate = False

    def info(self, message):
        self.logger.info("{}".format(message))
        
    def error(self, message):
        self.logger.error("{}".format(message))
        
    def debug(self, message):
        self.logger.debug("{}".format(message))
        
    def warning(self, message):
        self.logger.warning("{}".format(message))
        
        
    
get_tiles_logger = ALogger("get tiles", bcolors.OKCYAN)
save_pic_logger = ALogger("save_pics", bcolors.ENDC)
high_alert_logger = ALogger("We found a BIG ONE!", bcolors.FAIL)
surprise_me_logger = ALogger("surprise_me", bcolors.OKBLUE)
