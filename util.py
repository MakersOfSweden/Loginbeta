import hashlib
import settings
import time

salt = "AhBaik4auv3Seihu"

def encode(clearString):
    return hashlib.sha512(str.encode(salt + clearString)).hexdigest()
    
def formatTime(totalTime):
    if settings.TIME_FORMAT:
        return time.strftime(settings.TIME_FORMAT, time.gmtime(totalTime))
    else:
        return totalTime
