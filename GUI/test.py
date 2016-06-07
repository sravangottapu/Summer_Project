import sys
import os.path	
import getpass
sys.path.insert(0,'/home/'+getpass.getuser()+'/TextMiner/Processor')
import polyglotWord
text = "sachin is a great cricket player"
sent_array = ""
word_array = polyglotWord.polyWordTokenize(text)
for i in word_array:
	print(i)