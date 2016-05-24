from re import sub, match

def parse(sentence, sender):
	sentence = sentence.lower().split(" ")
	print sentence
	if sentence[0] == 'send' or sentence[0] == 'pay' or sentence[0] == 'show':
		if sentence[0] == "show":
			return (sender, sender, 0.0)
		else:
			for word in sentence[1:]:
				if match(r'[$][0-9]+[.]*[0-9]*', word):
					temp = ''.join(word.split('$')[-1])
					amount = round(float(temp), 2)
				elif word == 'to':
					pass
				else:
					receiver = word
		return (sender, receiver, amount)
	else:
		return ("", "", 0.0)