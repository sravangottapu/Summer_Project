import polyglot
from polyglot.text import Text, Word
def polySentTokenize(text):
	sent_array=set()
	text = Text(text)
	for sent in text.sentences:
		sent_array.add(sent)
	return sent_array