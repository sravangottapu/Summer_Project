import polyglot
from polyglot.text import Text,Word
def polyWordTokenize(text):
	text = Text(text)
	word_array = []
	for i in text.words:
		word_array.append(i)
	return word_array