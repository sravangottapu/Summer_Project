from  tkinter import *
from tkinter import filedialog
from functools import partial
import sys
sys.path.insert(0, '/home/rahulranjan/TextMiner/Processor')
import ne

def process(myText,root):
 	myTextWidget=Text(root)
 	ne_array=ne.extract_entities(myText)
 	for i in ne_array:
 		myTextWidget.insert(0.0,i+"\n")		
 	myTextWidget.pack(fill=BOTH)
 
def readfile(root):
 	root1 = Tk() 
 	filename = filedialog.askopenfilename(initialdir = "/home/rahulranjan/TextMiner/Data",title = "Choose your file",filetypes = (("Text files","*.txt"),))
 	myFile=open(filename,"r")
 	myText=myFile.read()
 	myTextWidget=Text(root)
 	myTextWidget.insert(0.0,myText)
 	myTextWidget.pack(fill=BOTH)
 	process_but = Button(root,text="Process",fg="red",command=partial(process,myText,root))
 	process_but.pack()
 	root1.withdraw()



root = Tk()
readfiles = partial(readfile,root)
browse = Button(root,text="Browse",fg="red",command=readfiles)
browse.pack()
root.mainloop()
-------------------
docview.title("Document: "+self.name)
  f=open(self.filename,"r+")
  data = f.read()
  S = Scrollbar(docview)
  T = Text(docview,height=20)
  S.pack(side=RIGHT,fill=Y)
  T.pack(fill=Y)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  T.insert(END,data)
  T.config(state=DISABLED)
  docview.mainloop()
