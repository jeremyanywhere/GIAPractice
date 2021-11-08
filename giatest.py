import random 
import time
import string
import sys


def report(section, quiz, seconds):
	score = 0
	q = 0
	for r in quiz:
		q+=1
		mark = ""
		if (str(r[1][0])==r[1][1]):
			score+=1
		else:
			mark = '*'
		
	print (f"  {q}) [{r[0]} = {r[1][0]} - your answer: {r[1][1]} {mark}")
	print("")
	print(f"Report: {section}")
	print(f"Time : {seconds} secs. ")
	print(f"Questions Answered: {len(quiz)}")
	print(f"Average time per question: {round(seconds/len(quiz),1)} secs.")
	print(f"Correct Answers: {score} out of {len(quiz)} - {round(score/len(quiz)*100)}%")
	print(f"Average time per correct answer: {round(seconds/score,1)}")
	print("")

 
def test_number_distance(seconds):
	quiz = []
	print(f"Number Distance Test..")
	input ("Hit any key to start..")
	time_stamp = round(time.time())
	while time.time()-time_stamp < seconds:
		# generate s (small number) random no. 1-5
		s = random.randint(1,12)	
		# add an odd no. 3,5,7,9 to it, to generate b (big number)
		b = s + random.choice([3,5,7,9,11]) 
		# generate random no. in that range, to get m (middle no) 
		m = random.choice(range(s+1,b-1))	
		# work out which is closer (b-m) > (m-s)? store as a (answer)
		a = b if b-m > m-s else s 
		rec = [s,m,b]
		# shuffle the 3 numbers 
		random.shuffle(rec)
		print (f"[{rec[0]} {rec[1]} {rec[2]}]")
		# get user input
		u = input ("? ")
		#store tuple of question record plus answer
		quest = (rec, [a,u])
		#add to quiz
		quiz.append(quest)
	#return quiz with the time. 
	return quiz

def test_letter_match(seconds):
	print(f"Letter Match Test..")
	input ("Hit any key to start..")
	time_stamp = round(time.time())
	quiz = []
	while time.time()-time_stamp < seconds:
		l = ""+string.ascii_lowercase
		top = ""
		bot = ""
		a = 0
		for p in range (0,4):
			tl = random.choice(l)
			l=l.replace(tl,'')
			top += tl
			if random.random() < 0.55:
				bl =tl.upper()
			else:
				bl = random.choice(l).upper()
				l=l.replace(bl,'')
			bot += bl
			if (tl.upper()==bl):
				a+=1
		print (f"{top[0]} {top[1]} {top[2]} {top[3]}")
		print (f"{bot[0]} {bot[1]} {bot[2]} {bot[3]}")
		u = input ("? ")
		quiz.append(([top,bot], [a,u]))
	return quiz

# do both tests to specified length or default 10, then dump report
timing = 60
if len(sys.argv) > 1:
	timing = int(sys.argv[1])
else:
	print(f"Defaulting to {timing} seconds. Specify no. seconds at command prompt if required")
result = test_number_distance(timing)
report("Number Distance", result, timing)
result = test_letter_match(timing)
report("Letter Match", result, timing)


