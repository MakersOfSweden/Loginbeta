import hashlib
import settings

salt = "AhBaik4auv3Seihu"

def encode(clearString):
    return hashlib.sha512(str.encode(salt + clearString)).hexdigest()
    
def formatTime(time):
    if settings.TIME_FORMAT == "MakersLink":
        time = int(time)
        rest, sec = divmod(time, 60)
        hour, min = divmod(rest, 60)
    
        return str(hour).rjust(2, "0")+":"+str(min).rjust(2, "0")+":"+str(sec).rjust(2, "0")
    else:
        return time
