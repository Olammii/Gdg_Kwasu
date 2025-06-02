quiz_questions = [
    {
        "question": "1. What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Port Harcourt"],
        "answer": "B"
    },
    {
        "question": "2. Who is the first president of Nigeria?",
        "options": ["A. Nnamdi Azikiwe", "B. Obafemi Awolowo", "C. Tafawa Balewa", "D. Goodluck Jonathan"],
        "answer": "A"
    },
    {
        "question": "3. What year did Nigeria gain independence?",
        "options": ["A. 1960", "B. 1963", "C. 1957", "D. 1975"],
        "answer": "A"
    },
    {
        "question": "4. Which river is the longest in Nigeria?",
        "options": ["A. River Niger", "B. River Benue", "C. Ogun River", "D. Osun River"],
        "answer": "A"
    },
    {
        "question": "5. What is the official currency of Nigeria?",
        "options": ["A. Dollar", "B. Cedi", "C. Naira", "D. Pound"],
        "answer": "C"
    }
]

def run_quiz():
    score = 0
    total_questions = len(quiz_questions)

    for question in quiz_questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        while True:
            user_answer = input("Enter your answer: ").strip().upper()
            if user_answer == "EXIT":
                print("\nExiting the quiz.")
                return
            elif user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")


        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"wrong answer, correct answer: {question['answer']}\n")

    print("=" *40)
    print(f"You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    run_quiz()
