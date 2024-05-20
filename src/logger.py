import logging
import os
from datetime import datetime

# Define the log file name with the current timestamp
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up the logging configuration with line number and function name
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s',
)


# if __name__=="__main__":
#     logging.info("logging has started")


