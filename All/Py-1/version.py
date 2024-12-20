import sys
import datetime
print(sys.version_info)
print(sys.version)
now=datetime.datetime.now()
print(now.strftime("%y-%m-%d %H:%M:%S"))
 
from datetime import datetime
current = datetime.now()
formatted_datetime = current.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", formatted_datetime)
