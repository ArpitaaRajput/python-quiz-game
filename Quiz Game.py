questions = ("How many elemsnts are in the periodic table? :",
              "Which animal lays the largest eggs?:",
              "What is the most abundant gas in Earth's atnosphere?:",
              "Which planet in the solar system is hottest?:")

options = (("A. 116" , "B. 117", "C. 118", "D. 119") , 
           ("A. Whale" , "B. Crocodile", "C. Elephant", "D. Ostrich") , 
           ("A. Nitrogen" , "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen") ,
            ("A. Mercury" , "B. Venus", "C. Earth", "D. Mars") )

answers = ("C","D","A","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("✅ Correct!")
        score+=1
    else:
        print("❌ Wrong!")
        print(f"Correct Answer: {answers[question_num]}")
    question_num += 1

print("-----------------------------------------------------------")
print("                        RESULT                             ")
print("-----------------------------------------------------------")
print("Answers: ", answers)
print("Guesses: ", guesses)
print(f"Your score: {score}/{len(questions)}")