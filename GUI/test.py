import sys
import os.path	
import getpass
sys.path.insert(0,'/home/'+getpass.getuser()+'/TextMiner/Processor')
import polyglotSent
text = "Sachin is a good boy"
sent_array = polyglotSent.polySentTokenize(text)
for i in sent_array:
	print(i)