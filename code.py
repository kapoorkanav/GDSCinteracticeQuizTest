question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class qna:
	def __init__(self, q, a):
		self.q = q
		self.a = a

class controller:
	def __int__(self, q_num, c_answer):
		self.q_num = q_num
		self.c_answer = c_answer

	def showans(self, c_answer):
		print(c_answer)

print("Lets play a quiz")
name=str(input("Enter name:	"))
print("Hello,",name," lets play a quiz")
print("You will get to know your score at the end:  ")
print("After each question fill the response:")
print("p= Show points")
print("a= Show answer")
print("l= Go back to last question")
print("e=End quiz")
print("Press any other key to move to next question")


current_question = 1
correct=0
points =0
while(current_question<=12):
	dictionary=question_data[current_question-1]
	qn=qna(dictionary["text"], dictionary["answer"])
	qn.q=dictionary["text"]
	qn.a=dictionary["answer"]
	print(qn.q)
	response =str(input())
	thispoints=0
	if(response.lower()==(qn.a).lower()):
		correct+=1
		points+=2
		thispoints=2
		print("correct")
	else:
		points-=1
		thispoints=-1
		print("incorrect")

	response2=str(input("Enter response  "))
	if(response2=="a"):
		aar=controller()
		aar.showans(qn.a)
	elif(response2=="p"):
		print(points)
	elif(response2=="l"):
		current_question-=1
		points=points-thispoints
	elif(response2=="h"):
		print(12-current_question, "question(s) remain")
	elif(response2=="e"):
	    current_question=13
	current_question+=1
print("Thanks for playing")
print("Your points are", points)
	
	
	
