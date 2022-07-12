from utils import load_ques, build_statistics

import random

filename = 'ques.json'
questions = load_ques(filename)

random.shuffle(questions)

for question in questions:
    print(question.build_question())
    answer = input('Ваш ответ')
    question.answer = answer
    print(question.build_feedback())


print(build_statistics(questions))
