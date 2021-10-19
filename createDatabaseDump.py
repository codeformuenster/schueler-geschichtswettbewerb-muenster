import time
import sys 
import os
import pipes 

# Change into settings dir and import settings 
sys.path.append(os.path.abspath("Website/geschichtswettbewerb/geschichtswettbewerb"))
from settings import *

# Set local variables 
MY_DB = DATABASES['default']
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = DATETIME

def write_sql_dump(db, DB_HOST, DB_USER, DB_USER_PASSWORD):
	dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + db + ".sql"
	os.system(dumpcmd)
	gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + db + ".sql"
	os.system(gzipcmd)


write_sql_dump(MY_DB['NAME'], MY_DB['HOST'], MY_DB['USER'], MY_DB['PASSWORD']);
