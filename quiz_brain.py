class Quizbrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list

    def new_questions(self):
        current_question = self.questions_list[self.question_number].text
        user_answer = input(f"Q.{self.question_number + 1}: {current_question} (True/False)?: ")
        return user_answer


