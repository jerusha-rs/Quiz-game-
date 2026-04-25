print("Welcome to Quiz Game 🎯")

score = 0

answer = input("1. What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. What is 5 + 3? ")
if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. Who is the father of Computer? ")
if answer.lower() == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your score is:", score)
