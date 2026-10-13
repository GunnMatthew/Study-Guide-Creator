from database import getConnection

def viewFlashCards(deckID):
    connection = getConnection()
    cursor = connection.cursor()
    
    cursor.execute("""SELECT * FROM Flashcards
                        WHERE deckID = ?""", (deckID,))
    
    flashcards = cursor.fetchall()
    
    if not flashcards:
        print('\nThis deck has no flashcards.  Consider adding some!\n')
        connection.close()
        return
    
    for card in flashcards:
        print(card)
        
    connection.close()

def addFlashCard(deckID):
    pass

def editFlashCard(deckID):
    pass

def removeFlashCard(deckID):
    pass