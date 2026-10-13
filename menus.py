from decks import createDeck, viewDecks, editDeck, studyDeck, removeDeck
from flashcards import viewFlashCards, addFlashCard, editFlashCard, removeFlashCard

def createMainMenu():
    print("~~~~~ Study Guide Creator ~~~~~")
    print("1) Create new flashcard deck")
    print("2) View flashcard decks")
    print("3) Select deck for editing")
    print("4) Select deck for studying")
    print("5) Remove a deck")
    print("6) Exit program")
    
def mainMenu():
    while True:
        createMainMenu()

        choice = input("Select an option: ")

        match choice:
            case "1":
                createDeck()
            case "2":
                viewDecks()
            case "3":
                deckID = editDeck()
                
                if deckID is not None:
                    editMenu(deckID)
            case "4":
                studyDeck()
            case "5":
                removeDeck()
            case "6":
                print("Goodbye!\n")
                break
            case _:
                print("Invalid input.  Please enter 1-6.\n")
    
def createEditMenu():
    print("~~~~~ Deck Editor ~~~~~")
    print("1) View Flashcards")
    print("2) Add Flashcard")
    print("3) Edit Flashcard")
    print("4) Remove Flashcard")
    print("5) Return to Main Menu")
    
def editMenu(deckID):
    while True:
            createEditMenu()
    
            choice = input("Select an option: ")
    
            match choice:
                case "1":
                    viewFlashCards(deckID)
                case "2":
                    addFlashCard(deckID)
                case "3":
                    editFlashCard(deckID)
                case "4":
                    removeFlashCard(deckID)
                case "5":
                    return
                case _:
                    print("Invalid input.  Please enter 1-5.\n")