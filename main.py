import os
from datetime import datetime

def createDir(dir):
  if not os.path.isdir(dir):
	try:
	    os.makedirs(dir)
	except OSError as e:
	    if e.errno != errno.EEXIST:
	        raise  # not "directory exist" error.

def getDateDir(baseDir):
	dir = os.path.join(
#         # os.getcwd(), 
        baseDir, 
        datetime.now().strftime('%Y/%m/%d/'))
	return dir

dir = getDateDir(baseBackupDir);
createDir(dir)
