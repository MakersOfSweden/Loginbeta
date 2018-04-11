import hasher
import sqlite3 as lite

con = lite.connect('People.db')
con.row_factory = lite.Row

salt = b"AhBaik4auv3Seihu"

with con:
    
    cur = con.cursor()
    
    cur.execute("SELECT * FROM People;")
    
    rows = cur.fetchall()
    
    hashed = []
    
    for row in rows:
        #hashedId = hashlib.sha512(salt+str.encode(str(row["blipId"]))).hexdigest()
        hashedId = hasher.encode(str(row["blipId"]))
        hashedRow = [hashedId, row["blipId"]]
        hashed.append(hashedRow)
    
    cur.executemany("UPDATE People SET blipId =? WHERE blipId =?", hashed)
        
