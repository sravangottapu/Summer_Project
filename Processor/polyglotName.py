import polyglot
from polyglot.text import Text, Word

def polyNameTokenize(text):
	name_array=[]
	text = Text(text)
	for te in text.entities:
		name_array.append("000000")
		name_array.append(te.tag)
		for i in te:
			name_array.append(i)
	#print(text.entities)
	return name_array