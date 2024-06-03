class Quizbrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)


    def new_questions(self):
        current_question = self.questions_list[self.question_number].text
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question} (True/False)?: ")


