class questions():

    def __init__(self , question , option_1 , option_2 ):
        self.question = question
        self.option_1 = option_1
        self.option_2 = option_2




question_1 = questions( question='hey bro ' ,option_1='hi' , option_2='hey')
question_2 = questions( question='are u ok ?' ,option_1='yes' , option_2='no')
question_3 = questions( question='u like her' ,option_1='yes' , option_2='no')
question_4 = questions( question='i know you do' ,option_1='yes' , option_2='no')

def print_question(question):
    print(question.question + question.option_1 + question.option_2)
    message = input("enter")
    if question == question_1:
        reply(question , question_2 , question_2 , message)
    elif question == question_2:
        reply(question, question_3, question_3, message)
    elif question == question_3:
        reply(question, question_4, question_1, message)
    print_question()


def reply(question , reply_1 , reply_2 , message ):
    if  message == question.option_1 :
        print_question(reply_1)
    else:
        print_question(reply_2)


print_question(question_1)