#General Knowledge Quiz
score = 0

print("===== GENERAL KNOWLEDGE QUIZ =====")

# Question 1
print("\n1. What is the capital of India?")
print("A. Mumbai")
print("B. Delhi")
print("C. Chennai")
print("D. Hyderabad")

answer = input("Enter your answer (A/B/C/D): ").upper()

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is B.")

# Question 2
print("\n2. Which planet is called the Red Planet?")
print("A. Mars")
print("B. Venus")
print("C. Earth")
print("D. Jupiter")

answer = input("Enter your answer (A/B/C/D): ").upper()

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is A.")

# Question 3
print("\n3. Who is known as the Father of Computers?")
print("A. Charles Babbage")
print("B. Bill Gates")
print("C. Steve Jobs")
print("D. Alan Turing")

answer = input("Enter your answer (A/B/C/D): ").upper()

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is A.")

print("\n========================")
print("Quiz Completed!")
print("Your Score:", score, "/3")