import pywhatkit
from datetime import datetime

def send_notice(no, msg, th, tm):
    pywhatkit.sendwhatmsg('+91'+no, msg, th, tm)

#now = datetime.now()
#th = now.hour        # current hour (0–23)
#tm = now.minute + 1  # schedule for the next minute (pywhatkit needs future time)
#send_notice("", "There will be water outage", th, tm)

