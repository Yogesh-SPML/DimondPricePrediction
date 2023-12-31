import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"         # It will give current datetime 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)                    # This will join cwd/logs/LOG_FILE
os.makedirs(logs_path,exist_ok=True)                                   # this will create folder with logs and inside this LOG_FILE file

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)                         

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
