'''
import os, sys, sqlite3
from sqlite3 import Error   
import Parameter

def CreateDB():
    #Angaben Teammates
    #-> hier fehlen noch die restlichen 7 möglichen Anmeldenamen

    connection = sqlite3.connect(Parameter.dbPfad)
    cursor = connection.cursor()
    # Tabelle erzeugen
    sql = """
        CREATE TABLE personen (
        TimeStampAnmeldung DATE, 
        EMailadresseCapitain STRING, 
        Anrede STRING,
        Name STRING,
        Vorname STRING, 
        Adresse STRING,
        Postleitzahl INT,
        Ort STRING, 
        Telefonnummer STRING,
        TournamentCategory STRING, 
        TeamName STRING,
        player1name = STRING,
        player1vorname = STRING,
        player1geschlecht = STRING,
        player1jahrgang = STRING,
        player1fussballspieler = STRING,
        player2name = STRING,
        player2vorname = STRING,
        player2geschlecht = STRING,
        player2jahrgang = STRING,
        player2fussballspieler = STRING,
        player3name = STRING,
        player3vorname = STRING,
        player3geschlecht = STRING,
        player3jahrgang = STRING,
        player3fussballspieler = STRING,
    );"""

    cursor.execute(sql)
    connection.close()


# Existenz der Datenbank überprüfen und ggf. diese anlegen
if not os.path.exists(Parameter.dbName):
    print("Datenbank " + Parameter.dbName + ".db nicht vorhanden - Datenbank wird anglegt.")
    #CreateDB()


  

    def CreateConnection(dbPfad):
        try:
            conn = sqlite3.connect(dbPfad)
        except Error as e:
            print(e)
        return conn

    def SaveData():
        connection = create_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO tempWerte VALUES(" + timestamp + ", " \
            + str(maxTempSensor) + ", " \
            + str(minTempUser) + ", " + str(maxTempUser) + ")"
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("Datenbank tempdata.db mit " + sql + " Inhalt angelegt")


    def ReadData(dbPfad):
        """
         Query all rows in the tasks table
         :param conn: the Connection object
         :return:
         """
         conn = CreateConnection()
         conn.execute("SELECT * FROM tasks")

         rows = conn.fetchall()

        for row in rows:
            print(row)

Databaseinstanz = Database()

Database.ReadData()
'''
