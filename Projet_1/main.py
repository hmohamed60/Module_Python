from qcm import QCM
from questions import questions

if __name__ == "__main__":
    while True:
        qcm = QCM(questions)
        qcm.start_quiz()

        replay = input("Voulez-vous recommencer le QCM? (o/n) : ")
        if replay.lower() != 'o':
            break
