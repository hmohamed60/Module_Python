from question import Question

questions = [
    Question("Quelle est la capitale de la France?", ["a) Londres", "b) Madrid", "c) Paris"], "c"),
    Question("Quelle est la capitale de l'Espagne?", ["a) Barcelone", "b) Séville", "c) Madrid"], "c"),
    Question("Quelle est la capitale de l'Allemagne?", ["a) Munich", "b) Hambourg", "c) Berlin"], "c"),
    Question("Quelle est la capitale de l'Italie?", ["a) Rome", "b) Milan", "c) Naples"], "a"),
    Question("Quelle est la capitale de la Chine?", ["a) Pékin", "b) Shanghai", "c) Canton"], "a"),
    Question("Quelle est la capitale de l'Inde?", ["a) Bombay", "b) New Delhi", "c) Bangalore"], "b"),
    Question("Quelle est la capitale de l'Australie?", ["a) Sydney", "b) Melbourne", "c) Canberra"], "c"),
    Question("Quelle est la capitale du Brésil?", ["a) São Paulo", "b) Rio de Janeiro", "c) Brasília"], "c"),
    Question("Quelle est la capitale de l'Égypte?", ["a) Alexandrie", "b) Le Caire", "c) Gizeh"], "b"),
    Question("Quelle est la capitale du Canada?", ["a) Toronto", "b) Montréal", "c) Ottawa"], "c"),
]

for question in questions:
    question.shuffle_options()
