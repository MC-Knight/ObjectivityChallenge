import random
questions = {
    "What is the capital of France?": {
        "A": {"answer":"London", "status": False},
        "B": {"answer":"Paris", "status": True},
        "C": {"answer":"Rome", "status": False},
        "D": {"answer":"Madrid", "status": False},
    },
    "What is the largest continent?": {
        "A": {"answer":"Europe", "status": False},
        "B": {"answer":"Asia", "status": True},
        "C": {"answer":"Africa", "status": False},
        "D": {"answer":"North America", "status": False},
    },
    "What is the tallest mammal?": {
        "A": {"answer":"Elephant", "status": False},
        "B": {"answer":"Giraffe", "status": True},
        "C": {"answer":"Hippopotamus", "status": False},
        "D": {"answer":"Rhino", "status": False},
    },
    "What is the currency of Japan?": {
        "A": {"answer":"Yuan", "status": False},
        "B": {"answer":"Euro", "status": False},
        "C": {"answer":"Yen", "status": True},
        "D": {"answer":"Pound", "status": False}
    },
      "What is the capital of Rwanda?": {
        "A": {"answer":"Bujumbura", "status": False},
        "B": {"answer":"Cape Town", "status": False},
        "C": {"answer":"Rome", "status": False},
        "D": {"answer":"Kigali", "status": True},
    },
}


question_keys = list(questions.keys())
random_numbers = []

for i in range(0, 5):
    random_numbers.append(i)

random.shuffle(random_numbers)
score = 0


def check_choice(answers, choice):
    while choice.upper() not in answers:
        print(f"Invalid choice '{choice}'. Please choose one of the following: {answers}")
        choice = input("Enter your choice: ")
    return choice.upper()


    

print("""
    WELCOME TO SIMPLE QUIZ
    ----------------------
    """)
for i in random_numbers:
    answers = list(questions[question_keys[i]])
    print(f"{random_numbers.index(i)+1}.{question_keys[i]}")
    for answer in answers:
        print(f"\t{answer}: {questions[question_keys[i]][answer]['answer']}")

    user_answer = input("Enter Your Choice Here:")
    print()
    check_choice(answers, user_answer)

    if questions[question_keys[i]][check_choice(answers, user_answer)]['status'] == True:
        score = score + 1
    else:
        score = score + 0



print(f"""
    Quiz Results
    ------------
    Questions taken: {len(questions)}/{len(questions)}

    score: {score}/{len(questions)}
    ------------
    """)
