import random
from question import Question
from reponse import Reponse

class QCM:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.shuffle_options()
            print(question.text)
            for option in question.options:
                print(option)
            user_answer = input("Votre réponse (a, b, c) : ").lower()
            if user_answer in ['a', 'b', 'c'] and question.is_correct(user_answer):
                print("\n")
                self.score += 1
            else:
                print("\n")

        self.display_score()

    def display_score(self):
        print(f"Votre score final est de {self.score}/{len(self.questions)}")


        
        # Ajouter l'affichage des réponses correctes
        for question in self.questions:
            print(f"Question: {question.text}")
            print(f"Réponse correcte : {question.correct_option}")
            print()

