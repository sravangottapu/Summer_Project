import sys
import os.path	
import getpass
sys.path.insert(0,'/home/'+getpass.getuser()+'/TextMiner/Processor')
import polyglotName
text = "sachin is a great cricket player"
sent_array = ""
name_array = polyglotName.polyNameTokenize(text)
var = 1
for i in name_array:
	if(i=="000000"):
		var = 1
	elif(var==1):
		i = i.split('-')
		print(i[1])
		var = 0
	else:
		print(i)