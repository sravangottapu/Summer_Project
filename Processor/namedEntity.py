import nltk

def namedEntity(text):
 ne_array=set()
 for sent in nltk.sent_tokenize(text):
  for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
   if hasattr(chunk, 'label'):
    string=""
    for c in chunk.leaves():
     string+=" " + c[0]
    string+=" : " + chunk.label()
    ne_array.add(string)
 return ne_array 
                


