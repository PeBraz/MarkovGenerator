#!/usr/bin/python
import sys
import random


def create_markov(words):
	markov_struct = dict()
	for i in xrange(2,len(words)):	
		markov_struct.setdefault((words[i-2], words[i-1]), [])\
					 .append(words[i])
	return markov_struct
	
def get_markov(markov_struct, phrases=1):
	starters = filter(lambda word: word[0].strip().istitle(), markov_struct.keys())
	present = random.choice(starters)
	text = [present[0], present[1]]
	
	while phrases > 0:
		text.append(random.choice(markov_struct[present]))
		present = (present[1],text[-1])
		if present not in markov_struct:
			break
		if '.' in text[-1]: phrases -=1 

	print ' '.join(text)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Usage: python Markov.py <filename>; exiting now."
		sys.exit(1)

	with open(sys.argv[1]) as f:
		get_markov(create_markov(f.read().split()))

