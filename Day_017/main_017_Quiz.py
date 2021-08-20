from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list()

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    user_answer = quiz.next_question()
    score = quiz.check_answer(user_answer)

print("You've completed the quiz.")
print(f"You've scored: {score}/{len(question_bank)}")
