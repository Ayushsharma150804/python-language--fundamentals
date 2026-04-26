##main.py

class User:
    pass

user_1 =User()  #object
user_1.id = "44" #incide object we can add this attribute
user_1.name ="ayush"

user_2 =User()
user_2.id = "43"
user_2.name = "gupta"

print(user_1.id)
print(user_2.name)

#write this same code in shorter way
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers =0   #we can also initialize attribute inside class
                            # as a instagram example followers not always 0 but id and name is always same
                            # create a attribute inside class can be updatable
        self.following = 0

    def follow(self, user):       #method
        user.followers +=1
        self.following +=1




user_1 = User("44", "ayush")
user_2 = User("43", "gupta")
print(user_1.id)         #derect access from User class or User class attribute
print(user_2.username)   #derect access from User class or User class attribute
print(user_1.followers)  #derect access from User class or User class attribute
print(user_2.followers)  #derect access from User class or User class attribute

user_1.follow(user_2) # from these line user can send following to another user_2

print(user_1.followers)
print(user_2.following)
print(user_1.following)
print(user_2.followers)

var=user_1.followers
print(var)
vari=user_1.following
print(vari)

##quizmain.py

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

que_ans = []            #initilaz list
for question in question_data:
    question_text = question["question"]            #insert answer
    question_answer = question["correct_answer"]        #insert question
    show =Question(question_text,question_answer)  #Question class call
    que_ans.append(show)                         #add question to list

quiz = QuizBrain(que_ans)    #call Question class
while quiz.still_has_question():
    quiz.next_question()

print("you're complete the quiz")
print(f"your final scor was {quiz.score}/{quiz.question_number}")



##data.py

question_data = [{"type": "boolean", "difficulty": "easy",
                  "category": "Science: Computers",
                  "question": "The Windows 7 operating system has six main editions.",
                  "correct_answer": "True", "incorrect_answers": ["False"]},
                 {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                  "question": "The first IBM PC was released in 1981.", "correct_answer": "True",
                  "incorrect_answers": ["False"]},
                 {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                  "question": "The name of the programming language AWK is abbreviated from the names of the developers &ndash; Aho, Weinberger, and Kernighan.",
                  "correct_answer": "True", "incorrect_answers": ["False"]},
                 {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                  "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
                  "correct_answer": "True", "incorrect_answers": ["False"]},
                 {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                  "question": "The logo for Snapchat is a Bell.", "correct_answer": "False",
                  "incorrect_answers": ["True"]},
                 {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                  "question": "The Windows ME operating system was released in the year 2000.",
                  "correct_answer": "True", "incorrect_answers": ["False"]},
                 {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                  "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True",
                  "incorrect_answers": ["False"]},
                 {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                  "question": "JavaScript derives from a later version of Java",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                  "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"type": "boolean", "difficulty": "easy",
                  "category": "Science: Computers",
                  "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
                  "correct_answer": "False", "incorrect_answers": ["True"]}]

##question_model.py

import random
from data import question_data

class Question:
    def __init__(self, question, answers):
        """separate the question and answer from dictionary """
        self.question= question
        self.answer=answers


##quiz_brain.py

class QuizBrain:

    def __init__(self,q_list):
        """contain a list of question answers and initialize attributes """
        self.question_number = 0
        self.question_list=q_list
        self.score=0

    def still_has_question(self):
        """ chck the question remain in list"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """print only the question and ask for true/false  """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number}: {current_question.question} (True/False):")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """check th user answer is correct or not"""
        if user_answer.lower()== correct_answer.lower():
            print("Corrct answer")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"correct answer was {correct_answer}.\n you score is {self.score}/{self.question_number}")
        print("\n")


