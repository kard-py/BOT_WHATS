import pywhatkit
from datetime import datetime
pywhatkit.sendwhatmsg("+55999348031", "teste", datetime.now().hour, datetime.now().minutes)