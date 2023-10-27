from qcm import QCM
from questions import questions

if __name__ == "__main__":
    qcm = QCM(questions)
    qcm.start_quiz()
