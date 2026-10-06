import sqlite3

def initializeDatabase():
    connection = sqlite3.connect("studyGuide.db")  # Create database if it doesn't exist, open if it does.
    
    # Create cursor to send queries, create intial decks table
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Decks (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT NOT NULL)""")
    
    connection.commit()
    connection.close() # close database

def mainMenu():
    print("~~~~~ Study Guide Creator ~~~~~")
    print("1) Create new flashcard deck")
    print("2) View flashcard decks")
    print("3) Select deck for editing")
    print("4) Select deck for studying")
    print("5) Remove a deck")
    print("6) Exit program")
    
def createDeck():
    deckName = input("What is the name of this deck? ")
    
    connection = sqlite3.connect("studyGuide.db")  # Create database if it doesn't exist, open if it does.
        
    # Create cursor to send queries, create intial decks table
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Decks (Name)
                        Values (?)""", (deckName,))
        
    connection.commit()
    
    print(f"Created deck: {deckName}\n")
    
    connection.close() # close database

def viewDecks():
    pass

def editDeck():
    pass

def studyDeck():
    pass

def removeDeck():
    connection = sqlite3.connect("studyGuide.db")
    
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Decks")
    decks = cursor.fetchall()
    print(f'\n{decks}')
    
    deckSelection = input('Enter the ID # of the deck you wish to remove: ')
    
    cursor.execute("""SELECT Name FROM Decks
                        WHERE ID = ?""", (deckSelection,))
    removedDeck = cursor.fetchone()
    
    cursor.execute("""DELETE FROM Decks
                        WHERE ID = ?""", (deckSelection,))
    
    connection.commit()
    
    print(f'\nRemoved "{removedDeck[0]}"!\n')
    
    connection.close()

# Run logic below
initializeDatabase()
    
while True:
    mainMenu()

    choice = input("Select an option: ")

    match choice:
        case "1":
            createDeck()
        case "2":
            viewDecks()
        case "3":
            editDeck()
        case "4":
            studyDeck()
        case "5":
            removeDeck()
        case "6":
            print("Goodbye!")
            break
        case _:
            print("Invalid input.  Please enter 1-5.")