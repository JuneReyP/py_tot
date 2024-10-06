import random

questions = {
    ("What is the color of banana?", "Yellow"),
    ("What is 2 + 2?", "4"),
    ("WHat is the color of the sky?", "Blue"),
    ("What programming language is this quiz written in?", "Python"),
    ("What is the capital of France?", "paris")
}

take = 0
def play_quiz():
    q = list(questions)
    random.shuffle(q)
    correct = 0
    global take

    for question, correct_ans in q:
        user = input(f"{question} ")
        if user.strip().lower() == correct_ans.lower():
            print("Correct!")
            correct+=1
        else:
            print(f"Incorrect. The answer is {correct_ans}")

    take += 1
    if correct < 3:
        print(f"You got {correct} out of {len(q)} and you need to take it again!")
        print("passing score is 3.")
        print(f"Takes: {take}")
        input("Press any key to continue...")
        play_quiz()
    else:
        print(f"You got {correct} out of {len(q)}")
        print("Congratulations. You Pass!")
        print(f"Takes: {take}")

play_quiz()