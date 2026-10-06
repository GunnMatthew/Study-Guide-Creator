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

# Function to create a new deck
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

# Function shows decks
def viewDecks():
    connection = sqlite3.connect("studyGuide.db")
    
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Decks")
    decks = cursor.fetchall()
    
    if not decks:
        print('There are no created decks.\n')
        connection.close()
        return
    
    for deck in decks:
        print(f'\nID:{deck[0]} Name:{deck[1]}')
    
    connection.close()

def editDeck():
    pass

def studyDeck():
    pass

# Function shows decks, takes user input for which deck to delete, and gives confirmation of deletion
def removeDeck():
    connection = sqlite3.connect("studyGuide.db")
    
    cursor = connection.cursor()
    
    viewDecks()
    
    deckSelection = input('Enter the ID # of the deck you wish to remove: ')
    
    cursor.execute("""SELECT Name FROM Decks
                        WHERE ID = ?""", (deckSelection,))
    removedDeck = cursor.fetchone()
    
    if removedDeck is None:
        print('\nDeck not found.\n')
        connection.close()
        return
    
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
            print("Goodbye!\n")
            break
        case _:
            print("Invalid input.  Please enter 1-6.\n")