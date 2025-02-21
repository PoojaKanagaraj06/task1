def display_instructions():
    print("Welcome to the Brainy Quiz!here you go")
    print("Here are the instructions to follow:")
    print("---------------------------")
    print("1. You will be asked a series of questions.")
    print("2. For each question, you will have multiple choices.")
    print("3. Type the letter corresponding to your chosen answer and press Enter.")
    print("4. Each correct answer will earn you points.")
    print("5. Try to answer all questions correctly to achieve the highest score.")
    print("6. If you are unsure about a question, take your best guess.")
    print("7. You can quit the quiz at any time by typing 'exit'.")
    print("8. Have fun and good luck!")
    
def ask_question(question, options, correct_answer):
    print("\n" + question)
    for option in options:
        print(option)
    answer = input("Your answer: ").strip().lower()
    if answer == 'exit':
        return False, 0
    elif answer == correct_answer:
        print("Correct!")
        return True, 1
    else:
        print("Incorrect! The correct answer was:", correct_answer)
        return True, 0

def brainy_quiz():
    display_instructions()
    
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
            "correct_answer": "c"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
            "correct_answer": "b"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["a) Atlantic Ocean", "b) Indian Ocean", "c) Arctic Ocean", "d) Pacific Ocean"],
            "correct_answer": "d"
        },
    ]

    score = 0
    for q in questions:
        continue_quiz, points = ask_question(q["question"], q["options"], q["correct_answer"])
        if not continue_quiz:
            break
        score += points

    print("\nQuiz Over!")
    print("Your final score is:", score)
