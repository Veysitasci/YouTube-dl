import sys, os
from datetime import datetime

year = datetime.now().year
lstupdt = "2021-03-20" #Well not that it's a separete file I should be updating it more.
spath = sys.path[0]+os.path.sep #path of the yt-dl dir
settigui5 = spath+"gui5_settings.json"
setticli = spath+"cli_settings.json"
curb = "testing"
ver = "2.1.8"