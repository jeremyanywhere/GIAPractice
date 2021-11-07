import random 
import time
import string


def report(section, quiz, timestamp):
	score = 0
	q = 0
	for r in quiz:
		q+=1
		print (f"  {q}) [{r[0]} = {r[1][0]} - your answer: {r[1][1]}")
		if (str(r[1][0])==r[1][1]):
			score+=1
	print("")
	print(f"{section}")
	t = round(time.time()-timestamp)
	print (f"Time: {t} secs. - average per question: {round (t/len(quiz))}")
	print (f"Total score: {score} out of {len(quiz)} = {round(score/len(quiz)*100)}%")
	print("")

 
def test_number_distance(section_length):
	quiz = []
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
		#make tuple to store question / answer (where a is actual answer and u is user answer)
		hist = (rec, [a,u])
		# get user input, store in set, put set in array
		# when loop is done, print report and score.
		quiz.append(hist)
	return quiz

def test_letter_match(length):
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
			if random.random() < 0.6:
				bl =tl.upper()
			else:
				bl = random.choice(l).upper()
				l=l.replace(bl,'')
				print(f"after bot, L is now {l}")
			bot += bl
			if (tl.upper()==bl):
				a+=1
		print (f"    {top[0]} {top[1]} {top[2]} {top[3]}")
		print (f"    {bot[0]} {bot[1]} {bot[2]} {bot[3]}")
		u = input ("? ")
		quiz.append(([top,bot], [a,u]))
	return quiz

section_length = 10
print("Report: ")
#timestamp = time.time()
#quiz = test_number_distance(section_length)
#report("Numbers", quiz, timestamp)
timestamp = time.time()
quiz = test_letter_match(section_length)
report("Letter Match", quiz, timestamp)
