from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in (question_data):
    text=i['text']
    answer=i['answer']
    question=Question(text,answer)  #here "question" is the object we created for the class "Question" in question_model
    question_bank.append(question)
quiz=QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")