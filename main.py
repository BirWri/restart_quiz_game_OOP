from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    text = question['text']
    answer = question['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz_brain = Quizbrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.new_questions()


