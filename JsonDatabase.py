'''
#Read Json
import pandas as pd

df = pd.read_json('/Users/thomas/Documents/Programmierung/GitHub/TournamentAdministrator/GruempeliDB.json')
for columnName,columnData in df.iteritems():  
  print(columnName)
'''
#Impots
import pandas as pd

#Read CSV-File
csvfile = pd.read_csv('/Users/thomas/Documents/Programmierung/GitHub/TournamentAdministrator/GruempeliImport.csv', encoding='utf-8')

#create Dataframe
data = {}

for columnName,columnData in csvfile.iteritems(): 
  print(columnName)
  if columnName == 'Mannschaftsname':
      print(columnData)






