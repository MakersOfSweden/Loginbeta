import sqlite3 as lite

con = lite.connect('People.db')
con.row_factory = lite.Row

with con:
    
    cur = con.cursor()
    
    cur.execute("BEGIN TRANSACTION;")
    cur.execute("ALTER TABLE People RENAME TO People_old;")
    
    cur.execute("CREATE TABLE People(Id INTEGER PRIMARY KEY AUTOINCREMENT, blipId INTEGER, Nick TEXT, isHere INTEGER, totalTime FLOAT, lastLogin FLOAT);")
    
    cur.execute("INSERT INTO People (blipId, Nick, isHere, totalTime, lastLogin) SELECT blipId, Nick, isHere, totalTime, lastLogin FROM People_old;")    

    cur.execute("COMMIT;")
        
