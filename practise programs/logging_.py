import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s -  %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

logging.debug("this is a debug massage")
logging.info("this is a info massage")
logging.warning("this is a warning massage")
logging.error("this is an error massage")
logging.critical("this is a critical massage")