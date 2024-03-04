import random

def display_question(question, choices):
    print(question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    return int(input("Enter the number of your answer: "))

def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    random.shuffle(questions)  # Shuffle the order of questions

    for question in questions:
        user_answer = display_question(question["question"], question["choices"])
        correct_answer = question["answer"]

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['choices'][correct_answer - 1]}\n")

    print(f"You scored {score} out of {total_questions}.")

def main():
    print("Welcome to the Quiz Application!")

    # Define your questions, choices, and correct answers
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["Berlin", "Paris", "Rome", "Madrid"],
            "answer": 2,
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": 2,
        },
        {
            "question": "What is the largest mammal in the world?",
            "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "answer": 2,
        },
        # Add more questions as needed
    ]

    run_quiz(questions)

if __name__ == "__main__":
    main()
