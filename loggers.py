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

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
get_tiles_logger = logging.getLogger("get tiles and save")

handler = logging.StreamHandler(sys.stdout)  # to console 
hq_formatter = logging.Formatter(bcolors.ENDC + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
handler.setFormatter(hq_formatter)

get_tiles_logger.addHandler(handler)  # add handler to logger


# logger.setLevel(logging.INFO)
get_tiles_logger.setLevel(logging.INFO)



save_pic_logger = logging.getLogger(__name__)
high_alert_logger = logging.getLogger("We found a BIG ONE!")

alert_handler = logging.StreamHandler(sys.stdout)  # to console 
hq_formatter = logging.Formatter(bcolors.OKGREEN + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
alert_handler.setFormatter(hq_formatter)

high_alert_logger.addHandler(alert_handler)  # add handler to logger


# save_pic_logger.setLevel(logging.DEBUG)
# high_alert_logger.setLevel(logging.DEBUG)
save_pic_logger.setLevel(logging.INFO)
high_alert_logger.setLevel(logging.INFO)




# logging.basicConfig(level=logging.INFO)

surprise_me_logger = logging.getLogger("surprise_me")
# high_alert_logger = logging.getLogger("We found a BIG ONE!")

surprise_handler = logging.StreamHandler(sys.stdout)  # to console 
hq_formatter = logging.Formatter(bcolors.OKBLUE + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
surprise_handler.setFormatter(hq_formatter)

surprise_me_logger.addHandler(surprise_handler)  # add handler to logger
surprise_me_logger.propagate = False


# surprise_me_logger.setLevel(logging.DEBUG)
surprise_me_logger.setLevel(logging.INFO)

# high_alert_logger.setLevel(logging.DEBUG)