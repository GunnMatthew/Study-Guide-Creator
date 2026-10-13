from database import getConnection

# Function to create a new deck
def createDeck():
    deckName = input("What is the name of this deck? ")
    
    connection = getConnection()
        
    # Create cursor to send queries, create intial decks table
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Decks (Name)
                        Values (?)""", (deckName,))
        
    connection.commit()
    
    print(f"Created deck: {deckName}\n")
    
    connection.close() # close database

# Function shows decks
def viewDecks():
    connection = getConnection()
    
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
    # Doesn't do anything now.  Later, renaming?
    connection = getConnection()
    
    cursor = connection.cursor()
    
    viewDecks()
    
    deckSelection = input('Enter the ID # of the deck you wish to edit: ')
    
    cursor.execute("""SELECT Name FROM Decks
                            WHERE ID = ?""", (deckSelection,))
    
    selectedDeck = cursor.fetchone()
    
    if selectedDeck is None:
        print('\nDeck not found.\n')
        connection.close()
        return
    
    print(f'\nEditing deck: {selectedDeck[0]}\n')
    
    connection.close()
    
    return deckSelection
    
def studyDeck():
    pass

# Function shows decks, takes user input for which deck to delete, and gives confirmation of deletion
## Need to revisit later to fix logic with fk enforcement, I believe.
def removeDeck():
    connection = getConnection()
    
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