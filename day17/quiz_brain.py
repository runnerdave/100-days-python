import random
from data import question_data
from question_model import Question


class Brain:
    def __init__(self):
        self.total_answers = 0
        self.right_answers = 0
        self.questions = self._load_questions()

    def _load_questions(self):
        questions = []
        for item in question_data:
            # questions.append((item['text'], item['answer'])) IF NOT USING CLASS
            questions.append(Question(item['text'], item['answer']))
        random.shuffle(questions)
        return questions

    def __repr__(self):
        return f"Your current score is: {self.right_answers}/{self.total_answers}"

    def present_question(self):
        while self.total_answers < len(self.questions):
            # question, answer = self.questions[self.total_answers] IF NOT USING CLASS
            question = self.questions[self.total_answers].text
            answer = self.questions[self.total_answers].answer
            response = input(
                f"Q.{self.total_answers + 1}: {question} (True/False):")
            if response == answer:
                print("You got it right!")
                self.right_answers += 1
            else:
                print("That's wrong.")
            print(f"The correct answer was: {answer}.")
            self.total_answers += 1
            print(self)
            print("")
        print(
            f"Those are all the questions I had, thanks for playing. Final score: {self.right_answers}/{self.total_answers}")
