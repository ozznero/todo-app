import json

with open("questions.json", "r") as file:
    content = file.read()

print(content)
data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index +1 , "-", alternative)
    user_choice = int(input("Enter your answer (just the corresponding number): "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["correct_answer"] == question["user_choice"]:
        score = score +1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = f"{index + 1} {result} - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']} "
    print(message)

print(f"You have answered right to {score} question")
print(f"Your success rate is {score}/{len(data)}")
