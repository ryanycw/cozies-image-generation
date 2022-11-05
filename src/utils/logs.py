import os
import numpy as np
from datetime import datetime

def mkdir(directory):
    if not os.path.exists(directory):
        try: 
            os.mkdir(directory) 
        except OSError as error:
            print(error)
    return directory

def getNameWithTime(fileName):
    now = datetime.now()
    return f"{fileName}-{now.strftime('%Y-%m-%d-%H-%M')}"

def saveLog(record, fileName):
    np.savetxt(fileName, record, delimiter=",", fmt="% s")