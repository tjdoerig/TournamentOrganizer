'''
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
'''

class Player:
    '''
    def __init__(self, firstname, surname, gender, birthday, footballer):
        self.firstname = firstname
        self.surname = surname
        self.gender = gender
        self.birthday = birthday
        self.footballer = footballer
    '''

    def print(self):
        print("player")

class Capitain:
    '''
    def __init__(self, salutation, firstname, surname, adress , zipCode, place, email, phoneNumber):
        self.salutation = salutation
        self.firstname = firstname
        self.surname = surname
        self.adress = adress
        self.zipCode = zipCode
        self.place = place
        self.email = email
        self.phoneNumber = phoneNumber
    '''
    def print(self):
        print("capitain")


class Team(Player, Capitain):
    
    def print(self):
        print("team")
        Player.print(self)
        Capitain.print(self)

t = Team()
print(t.print())
