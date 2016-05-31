import tkinter
import nltk
from nltk.tokenize import *
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from functools import partial
from tkinter.filedialog import askopenfilename
root = Tk()
img = PhotoImage(file='imag.png')
root.tk.call('wm','iconphoto',root._w,img)
#root.iconbitmap(r'/home/sravan/Desktop/imag.png')
root.wm_title("Text Miner")
count = 0
cat = 0
content = " "
data = " "
new = Text(root)
T = Text(root)
def extract_entities(text):
    ne_array=set()
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
               string="\t\t\t" + str(chunk.leaves()[0][0]) + "\t\t\t"+chunk.label()
               ne_array.add(string)
    return ne_array 
def process():
	global S,new
	global data
	global cat
	try:
		content = T.selection_get()
		random = content
		content = nltk.word_tokenize(content)
		content = nltk.pos_tag(content)
		messagebox.showinfo("Annotated Text",content)
		print(content)
	except:
		a = "random"
	#T.pack_forget()
	new.pack_forget()
	S.pack_forget()
	sentences = nltk.sent_tokenize(data)
	ne_array=extract_entities(data)
	print(ne_array)	
	label_1 = Label(root,text="Word\t\tCategory")
	label_1.pack()
	for laer in ne_array:
		new.insert(0.0,laer+"\n")
	#new.insert(0.0,"Sravan")
	#new.insert(0.0,"Word\t\tCategory\n",font="Verdana 24")
	new.tag_config("Word",background="yellow", foreground="blue")
	if(cat==0):
		new.pack(fill=BOTH)
	cat=1
	#new.tag_config(random,background="blue")
def BrowseTextFiles():
	global count
	global T,S,data
	global content
	count = 1
	if(count==1):
		button_1.pack_forget()
	name = askopenfilename(filetypes=(("Text File","*.txt"),("All Files","*.*")),title="Choose a File",initialdir="/home/sravan/TextMiner/Data")
	f = open(name,'r')
	data = f.read()
	S = Scrollbar(root)
	T = Text(root,height=20)
	S.pack(side=RIGHT,fill=Y)
	T.pack(fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	T.insert(END,data)
	T.config(state=DISABLED)
	button_2 = Button(root,text="Process",command=process)
	button_2.pack(side=BOTTOM)
button_1 =Button(root, text = "Browse", command=BrowseTextFiles)
button_1.pack()

root.mainloop()
