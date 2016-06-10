import polyglot
from polyglot.text import Text, Word
def polySpeechTokenize(text):
	text = Text(text)
	speech_array = []
	for word, tag in text.pos_tags:
		speech_array.append(word)
		speech_array.append(tag)
	return speech_array