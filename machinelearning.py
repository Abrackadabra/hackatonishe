import re
import pymorphy2; 
morph = pymorphy2.MorphAnalyzer()

def is_good(userdict, string):
	string = string.lower()
	string = re.sub('[^a-zа-я ]', '', string)
	words = []
	for w in string.split():
		if len(w) > 3:
			try:
				words.append(morph.parse(w)[0].normal_form)
			except:
				pass
	print(words)
	score = 0
	for word in words:
		try:
			score += userdict[word]
		except:
			pass

	print(score)
	edge = -2
	return score > edge

if __name__ == '__main__':
	userdict = {'бабушка': 5, 'дедушка': 3, 'porn': -5, 'pony': 10}
	string = 'My Little Pony porn с бабушками s03p12'
	test(userdict, string)