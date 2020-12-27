import os, sys, sqlite3
from sqlite3 import Error   

dbName = "chinook.ds"
dbSpeicherpfad = "/Users/thomas/Documents/Programmierung/GitHub/TournamentAdministrator/"
dbPfad = dbSpeicherpfad + dbName

def CreateConnection(dbPfad):
    try:
        conn = sqlite3.connect(dbPfad)
    except Error as e:
        print(e)
    return conn

CreateConnection(dbPfad)
