import hashlib

salt = "AhBaik4auv3Seihu"

def toString(time):
    time = int(time)
    rest, sec = divmod(time, 60)
    hour, min = divmod(rest, 60)
    
    return str(hour).ljust(2, "0")+":"+str(min).ljust(2, "0")+":"+str(sec).ljust(2, "0")

def encode(clearString):
    return hashlib.sha512(str.encode(salt + clearString)).hexdigest()
