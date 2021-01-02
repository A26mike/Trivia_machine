from quiz_brain import QuizBrain
from typing import Text
from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

# for items in question_bank:
#     print(f' The question is {items.text}  the answer is {items.answer}')

quiz_brain = QuizBrain(question_bank)
print("\n\n")
while quiz_brain.still_has_questions():
    asked_question = quiz_brain.next_question()


print("\nYou have completed the quiz")
print(
    f"Your final score is {quiz_brain.score} out of {quiz_brain.question_number} questions "
)
