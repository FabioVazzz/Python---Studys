# Python quiz game

questions = ("What is the largest ocean in the world?", "Who wrote Don Quixote?", "Which country has the largest population in the world?")

options = (("A) Atlantic Ocean", "B) Pacific Ocean", "C) Indian Ocean"), ("A) William Shakespeare", "B) Miguel de Cervantes", "C) Dante Alighieri"), ("A) India", "B) United States", "C) China"))

answers = ("B", "B", "A")
guesses = []
score = 0
question_num = 0

for x in questions:
    print(x)
    print()
    for y in options[question_num]:
        print(y)
    guessess = input("Enter your guess: ")
    if guessess == answers[question_num]:
        score += 1
    question_num += 1

print(score)