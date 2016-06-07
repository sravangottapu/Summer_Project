import nltk

def partofSpeech(text):
 pos_array=set()
 for sent in nltk.sent_tokenize(text):
  for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
   if hasattr(chunk, 'label'):
    pos_array.add(str(chunk.leaves()))
 return pos_array 
   