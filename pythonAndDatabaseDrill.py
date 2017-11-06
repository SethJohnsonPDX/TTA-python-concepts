import sqlite3

rosterValues = (
    (1,'Jean-Baptiste Zorg','Human',122),
    (2,'Korben Dallas','Meat Popsicle',100),
    (3,'Ak''not','Mangalore',-5)
    )

with sqlite3.connect('roster_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Id INT, Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?,?,?,?)",
                  rosterValues)
    c.execute("UPDATE Roster SET Species='Human' WHERE Id == 2")
    c.execute("SELECT Name, IQ FROM Roster WHERE Species == 'Human'")


    for row in c.fetchall():
        print(row)

              



    
