import sqlite3
import time

_connection = sqlite3.connect('People.db')
_connection.row_factory = sqlite3.Row


def add(nick, rfid):
    cursor = _connection.cursor()
    cursor.execute("INSERT INTO People (blipId, Nick, isHere, totalTime, lastLogin) VALUES (?,?,?,?,?);", (rfid, nick, 1, 0, time.time()))
    _connection.commit()
    return cursor.lastrowid


def logout(rfid):
    cursor = _connection.cursor()
    cursor.execute('UPDATE People SET totalTime=totalTime + (strftime("%s", "now") - lastLogin), isHere=0 WHERE blipId=?', [rfid])
    _connection.commit()


def login(rfid):
    cursor = _connection.cursor()
    cursor.execute('UPDATE People SET lastLogin=strftime("%s", "now"), isHere=1 WHERE blipId=?', [rfid])
    _connection.commit()


def fetch(rfid):
    cursor = _connection.cursor()
    cursor.execute("SELECT * FROM People WHERE blipId = ?", [rfid])
    return cursor.fetchone()

def update_nick(newNick, oldNick):
    cursor = _connection.cursor()
    cursor.execute("UPDATE People SET Nick = ? WHERE Nick = ?", (newNick, oldNick))
    _connection.commit()

def update_rfid(newRfid, oldRfid):
    cursor = _connection.cursor()
    cursor.execute("UPDATE People SET blipId = ? WHERE blipId = ?", (newRfid, oldRfid))
    _connection.commit()

def change_rfid(newRfid, nick):
    cursor = _connection.cursor()
    cursor.execute("UPDATE People SET blipId = ? WHERE Nick = ?", (newRfid, nick))
    _connection.commit()


def purge_inactive_users():
    cursor = _connection.cursor()
    cursor.execute("DELETE FROM People WHERE totalTime < 60")
    _connection.commit()

def logged_in():
	cursor = _connection.cursor()
	cursor.execute("SELECT * FROM People WHERE isHere = 1")
	return cursor.fetchall()


def highscore():
	cursor = _connection.cursor()
	cursor.execute("SELECT * FROM People WHERE totalTime > 600 ORDER BY totalTime DESC")
	return cursor.fetchall()


def logout_all():
    cursor = _connection.cursor()
    cursor.execute("UPDATE People SET isHere = 0")
    _connection.commit()

def remove(nick):
    cursor = _connection.cursor()
    cursor.execute("DELETE FROM People WHERE Nick = ?", (nick, ))
    _connection.commit()

def move_time(fromNick, toNick):
    cursor = _connection.cursor()

    cursor.execute("SELECT SUM(totalTime) FROM People WHERE Nick = ? OR Nick = ?", (fromNick, toNick))
    rows = cursor.fetchall()
    cursor.execute("UPDATE People SET totalTime = ? WHERE Nick = ?", (str(rows[0][0]), toNick))

    _connection.commit()


