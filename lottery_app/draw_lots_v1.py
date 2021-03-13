import random

names=list()

def  ask_questions(questionType=1):
	if questionType==1:
		try:
			hmany=int(input("How many people will join the draw? --> "))
			print()
		except:
			hmany=0
		
	return hmany

def take_names(counter):
	names.append(input("{}.name : ".format(counter+1)))

def draw_lots():
	return random.sample(names,1)

question_answer=ask_questions()
if question_answer==0:
	print("!!! Please write number value !!!")
else:
	for i in range(question_answer):
		take_names(i)

	winner=draw_lots()

	print("\n Winning {} \n Congratulations :)".format(winner[0]))
