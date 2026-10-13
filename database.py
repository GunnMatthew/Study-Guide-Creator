import sqlite3

def getConnection():
    connection = sqlite3.connect("studyGuide.db")
    connection.execute("PRAGMA foreign_keys = ON") # Enables fk enforcement
    return connection

def initializeDatabase():
    connection = getConnection()
    
    # Create cursor to send queries, create intial decks table
    cursor = connection.cursor()
    
    # Create Decks table
    cursor.execute("""CREATE TABLE IF NOT EXISTS Decks (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT NOT NULL)""")
    
     # Create Flashcards table
    cursor.execute("""CREATE TABLE IF NOT EXISTS Flashcards (
                        ID INTEGER PRIMARY KEY,
                        DeckID INTEGER NOT NULL,
                        Question TEXT NOT NULL,
                        Answer TEXT NOT NULL,
                        FOREIGN KEY (DeckID) REFERENCES Decks(ID))""")
    
    connection.commit()
    connection.close() # close database
    