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
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler(sys.stdout)
        hq_formatter = logging.Formatter(bcolors.ENDC + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
        handler.setFormatter(hq_formatter)
        self.logger.addHandler(handler)  # add handler to logger
        
        self.logger.propagate = False

    def info(self, message):
        self.logger.info("{}".format(message))
        
    def error(self, message):
        self.logger.error("{}".format(message))
        
    def debug(self, message):
        self.logger.debug("{}".format(message))
    
get_tiles_logger = ALogger("get tiles and save")
save_pic_logger = ALogger("save_pics")
high_alert_logger = ALogger("We found a BIG ONE!")
surprise_me_logger = ALogger("surprise_me")

# get_tiles_logger = logging.getLogger("get tiles and save")

# handler = logging.StreamHandler(sys.stdout)  # to console 
# hq_formatter = logging.Formatter(bcolors.ENDC + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
# handler.setFormatter(hq_formatter)

# get_tiles_logger.addHandler(handler)  # add handler to logger

# get_tiles_logger.setLevel(logging.INFO)



# save_pic_logger = logging.getLogger(__name__)
# high_alert_logger = logging.getLogger("We found a BIG ONE!")

# alert_handler = logging.StreamHandler(sys.stdout)  # to console 
# hq_formatter = logging.Formatter(bcolors.OKGREEN + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
# alert_handler.setFormatter(hq_formatter)

# high_alert_logger.addHandler(alert_handler)  # add handler to logger


# save_pic_logger.setLevel(logging.INFO)
# high_alert_logger.setLevel(logging.INFO)


# surprise_me_logger = logging.getLogger("surprise_me")

# surprise_handler = logging.StreamHandler(sys.stdout)  # to console 
# hq_formatter = logging.Formatter(bcolors.OKBLUE + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
# surprise_handler.setFormatter(hq_formatter)

# surprise_me_logger.addHandler(surprise_handler)  # add handler to logger
# surprise_me_logger.propagate = False

# surprise_me_logger.setLevel(logging.INFO)

