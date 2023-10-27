import random

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_option.lower()

    def shuffle_options(self):
        random.shuffle(self.options)
