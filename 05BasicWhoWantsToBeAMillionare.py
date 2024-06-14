# This is a basic version of the TV show, Who Wants to be a Millionaire.
# I've taken these questions and answers from the internet


print("Welcome to Who Wants to be a Millionaire!!!")

questions = [
    "What sort of animal is Walt Disney's Dumbo?",
    "What was the name of the Spanish waiter in the TV sitcom \"Fawlty Towers\"?",
    "Which battles took place between the Royal Houses of York and Lancaster?",
    "Which former Beatle narrated the TV adventures of Thomas the Tank Engine?",
    "Queen Anne was the daughter of which English Monarch?",
    "Who composed \"Rhapsody in Blue\"?",
    "What is the Celsius equivalent of 77 degrees Fahrenheit?",
    "What are Suffolk Punch and Hackney?",
    "Which Shakespeare play features the line \"Neither a borrower nor a lender be\"?",
    "Which is the largest city in the USA's largest state by area?",
    "The word \"aristocracy\" literally means power in the hands of ",
    "Where would a \"peruke\" be worn?",
    "In which palace was Queen Elizabeth I born?",
    "From which author's work did scientists take the word \"quark\"?",
    "Which of these islands was ruled by Britain from 1815 until 1864?"
]

money = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

options = [
    "Deer", "Rabbit", "Elephant", "Donkey",
    "Manuel", "Pedro", "Alfonso", "Javier",
    "Thirty Years War", "Hundred Years War", "Wars of the Roses", "English Civil War",
    "John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr",
    "James II", "Henry VIII", "Victoria", "William I",
    "Irving Blue", "George Gershwin", "Aaron Copland", "Cole Porter",
    "15", "20", "25", "27",
    "Carriage", "Wrestling Style", "Cocktail", "Horse",
    "Hamlet", "Macbeth", "Othello", "The Merchant of Venice",
    "Dallas", "Los Angeles", "New York", "Anchorage",
    "The few", "The best", "The barons", "The rich",
    "Around the neck", "On the head", "Around the waist", "On the wrist",
    "Greenwich", "Richmond", "Hampton Court", "Kensington",
    "Lewis Carrol", "Edward Lear", "James Joyce", "Aldous Huxley",
    "Crete", "Cyprus", "Corsica", "Corfu"
]

answers = [
    "Elephant", "Manuel", "Wars of the Roses", "Ringo Starr",
    "James II", "George Gershwin", "25", "Horse",
    "Hamlet", "Anchorage", "The barons", "On the head",
    "Greenwich", "James Joyce", "Corfu"
]

i = 0
j = 1

while True:
    print(f"The question for {money[i + 1]} Euros!")
    print(questions[i])
    print("A. ", options[j - 1], "\nB. ", options[j], "\nC. ", options[j + 1], "\nD. ", options[j + 2], "\n")

    quit = input("Would you like to continue(c) or quit(q): ")
    while True:
        if quit == "q":
            print(f"Thank you for playing the game, you've won {money[i]} Euros!")
            gameover = 1
            break
        elif quit == "c":
            gameover = -1
            break
        else:
            quit = input("Type: q to quit or c to continue: ")

    if gameover == 1:
        break

    reply = input("Please type the entire option: ")
    if reply == answers[i]:
        print(f"Correct answer! You've won {money[i + 1]} Euros\n")
    else:
        x = i // 5
        print(f"That's the wrong answer:(\nYou've won {money[5 * x]} Euros")
        break

    i = i + 1
    j = j + 4
