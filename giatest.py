import random 
import time
import string
import sys


def report(section, quiz):
	score = 0
	q = 0
	for r in quiz[0]:
		q+=1
		print (f"  {q}) [{r[0]} = {r[1][0]} - your answer: {r[1][1]}")
		if (str(r[1][0])==r[1][1]):
			score+=1
	print("")
	print(f"Report: {section}")
	t = round(quiz[1])
	print (f"Time: {t} secs. - average per question: {round (t/len(quiz))}")
	print (f"Total score: {score} out of {len(quiz)} = {round(score/len(quiz)*100)}%")
	print("")

 
def test_number_distance(section_length):
	quiz = []
	print(f"Number Distance Test..")
	input ("Hit any key to start..")
	time_stamp = time.time()
	for x in range(section_length):
		# generate s (small number) random no. 1-5
		s = random.randint(1,10)	
		# add an odd no. 3,5,7,9 to it, to generate b (big number)
		b = s + random.choice([3,5,7]) 
		# subtract s from b, generate random no. in that range, add to s to get m (middle no) 
		m = random.choice(range(s+1,b-1))	
		# work out which is closer (b-m) > (m-s)? store as a (answer)
		a = b if b-m > m-s else s 
		rec = [s,m,b]
		# randomise into an array 
		random.shuffle(rec)
		print (f"[{rec[0]} {rec[1]} {rec[2]}]")
		u = input ("? ")
		#store tuple of record plus answer
		hist = (rec, [a,u])
		# get user input, store in set, put set in array
		# when loop is done, print report and score.
		quiz.append(hist)
	return (quiz, time.time()-time_stamp)

def test_letter_match(length):
	print(f"Letter Match Test..")
	input ("Hit any key to start..")
	time_stamp = time.time()
	quiz = []
	for x in range(section_length):
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
	return (quiz, time.time()-time_stamp)

# do both tests to specified length or default 10, then dump report
section_length = 10
if len(sys.argv) > 1:
	section_length = int(sys.argv[1])
result = test_number_distance(section_length)
report("Number Distance", result)
result = test_letter_match(section_length)
report("Letter Match", result)
