import tkinter
from  tkinter import *
from tkinter import filedialog
import os.path
import getpass
from tkinter import messagebox
sys.path.insert(0,'/home/'+getpass.getuser()+'/TextMiner/Processor')
import namedEntity
import polyglotSent
import partofSpeech
import sentTokenize
import wordTokenize
import MySQLdb
from functools import partial

class gui:
 

 def __init__(self):
  self.maindisplay()
  

 def maindisplay(self):
  root = Tk()
  root.minsize(250, 250)
  var  = StringVar(root)
  self.er = var
  var.set("nltk")
  root.title("TextMiner")
  icon = tkinter.Image("photo", file="/home/"+getpass.getuser()+"/TextMiner/Data/icon.png")
  root.tk.call('wm','iconphoto',root._w,icon)
  self.browseButton(root)
  self.neButton(root)
  self.posButton(root)
  self.stButton(root)
  self.wtButton(root)
  self.manualButton(root)
  self.getManualButton(root)
  self.dictionaryButton(root)
  option = OptionMenu(root, var, "nltk","polyglot")
  option.pack()
  self.getLibraryButton(root)
  root.mainloop()


 def getLibraryButton(self,root):
  okbutton = Button(root,text="ok",bg="yellow",command=self.ok)
  okbutton.pack()
 

 def browseButton(self,root):
  browseButton = Button(root,text="Browse",bg="red",command=partial(self.browse,root))
  browseButton.pack()
 

 def neButton(self,root):
  neButton=Button(root,text="NE Miner",bg="red",command=self.namedEntity)
  neButton.pack()
 

 def posButton(self,root):
  posButton=Button(root,text="POS Tagger",bg="red",command=self.partofSpeech)
  posButton.pack()
 

 def stButton(self,root):
  stButton=Button(root,text="Sent. Tokenize",bg="red",command=self.sentTokenizechecker)
  stButton.pack()
 

 def wtButton(self,root):
  wtButton=Button(root,text="Word Tokenize",bg="red",command=self.wordTokenize)
  wtButton.pack()

 def manualButton(self,root):
  manualButton=Button(root,text="Manual Annotate",bg="red",command=self.manual)
  manualButton.pack()

 def getManualButton(self,root):
  getManualButton=Button(root,text="Get Manual Annotations",bg="red",command=self.getManual)
  getManualButton.pack()


 def dictionaryButton(self,root):
  dictionaryButton = Button(root,text="Give Dictionary",bg="red",command=self.dictionary)
  dictionaryButton.pack()
 def sentTokenizechecker(self):
  if hasattr(self, "name"):
    if hasattr(self, "value"):
      if(self.value==0):
       self.sentTokenize()
       print("nltk")
      else:
        print("POlyglot")
        self.sentTokenizePolyglot()
    else:
     self.sentTokenize()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)

 def sentTokenizePolyglot(self):
  polyglotsent = Tk()
  polyglotsent.title("Tokenized Sentences List with PolyGlot: "+self.name)
  data = self.myText
  sent_array = polyglotSent.polySentTokenize(data)
  string=""
  for i in sent_array:
    string = string + str(i) + "\n"
  data = string
  S = Scrollbar(polyglotsent)
  T = Text(polyglotsent,height=20)
  S.pack(side=RIGHT,fill=Y)
  T.pack(expand = 1, fill= BOTH)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  T.insert(END,data)
  T.config(state=DISABLED)
  polyglotsent.mainloop()


 def browse(self,root):

  filename = filedialog.askopenfilename(initialdir = "/home/"+getpass.getuser()+"/TextMiner/Data",title = "Choose your file",filetypes = (("Text files","*.txt"),))
  self.name=(filename.split('/')[-1]).split('.')[0]
  self.docview(filename,root)
 def ok(self):
  vare = self.er
  a = vare.get()
  if(a=="nltk"):
    print(a)
    self.value=0
  elif(a=="polyglot"):
    print(a)
    self.value=1
  else:
    print("sravn")
  print(self.value)


 def docview(self,filename,root):
  docview = Tk()
  docview.title("Document: "+self.name)
  f=open(filename,"r+")
  data = f.read()
  self.myText=data
  S = Scrollbar(docview)
  docWidget = Text(docview,height=20)
  S.pack(side=RIGHT,fill=Y)
  docWidget.pack(expand = 1, fill= BOTH)
  S.config(command=docWidget.yview)
  docWidget.config(yscrollcommand=S.set)
  docWidget.insert(END,data)
  docWidget.config(state=DISABLED)
  getPersonButton=Button(docview,text="Get Person Annotated",bg="red",command=partial(self.getPerson,docWidget))
  getPersonButton.pack(side=LEFT)
  highlighDictionaryButton =Button(docview,text="Highlight Dictionary",bg="red",command=partial(self.highlightDictionary,docWidget))
  highlighDictionaryButton.pack(side=RIGHT)
  docview.mainloop()


 def getPerson(self,widget):
  db = MySQLdb.connect("localhost","root","","manual_annotations")
  cursor = db.cursor()
  sql = """SELECT name FROM annotations WHERE category = 'Person' """ 
  cursor.execute(sql)
  results = cursor.fetchall()
  for row in results:
    name = row[0]
    self.highlight(name,widget,"yellow",1)
  db.commit()

 
 def dictionary(self):
  self.dicfileName = filedialog.askopenfilename(initialdir = "/home/"+getpass.getuser()+"/TextMiner/Data",title = "Choose your file",filetypes = (("Text files","*.txt"),))
  self.dicName=(self.dicfileName.split('/')[-1]).split('.')[0]
  with open(self.dicfileName) as fp:
    for line in fp:
      line = line.strip('\n')
      print(line)


 def highlightDictionary(self,widget):
  if hasattr(self, "dicfileName"):
    with open(self.dicfileName) as fp:
      for line in fp:
        line = line.strip('\n')
        self.highlight(line,widget,"green",1)
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)



 def namedEntity(self):  
  if hasattr(self, 'name'):
    ne=Tk()
    ne.title("Named-Entity List: "+self.name)
    neWidget=Text(ne)
    ne_array=namedEntity.namedEntity(self.myText)
    string=""
    for i in ne_array:
     string = string + i + "\n"
    data = string
    S = Scrollbar(ne)
    T = Text(ne,height=20)
    S.pack(side=RIGHT,fill=Y)
    T.pack(expand = 1, fill= BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END,data)
    T.config(state=DISABLED)
    ne.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)

 
 def partofSpeech(self):
  if hasattr(self,'name'):
    pos=Tk()
    pos.title("POS Tagged List: "+self.name)
    posWidget=Text(pos)
    pos_array=partofSpeech.partofSpeech(self.myText)
    string = ""
    for i in pos_array:
      string = string + i + "\n"
    data = string  
    S = Scrollbar(pos)
    T = Text(pos,height=20)
    S.pack(side=RIGHT,fill=Y)
    T.pack(expand = 1, fill= BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END,data)
    T.config(state=DISABLED)
    pos.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)

 

 def sentTokenize(self):
  if hasattr(self,'name'):
    st=Tk()
    st.title("Tokenized Sentences List: "+self.name)
    stWidget=Text(st)
    st_array=sentTokenize.sentTokenize(self.myText)
    string = ""
    for i in st_array:
      string = string + i + "\n"
    data = string  
    S = Scrollbar(st)
    T = Text(st,height=20)
    S.pack(side=RIGHT,fill=Y)
    T.pack(expand = 1, fill= BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END,data)
    T.config(state=DISABLED)
    st.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def wordTokenize(self):
  if hasattr(self,'name'):
    wt=Tk()
    wt.title("Tokenized Words List: "+self.name)
    wtWidget=Text(wt)
    wt_array=wordTokenize.wordTokenize(self.myText)
    string = ""
    for i in wt_array:
      string = string + i + "\n"
    data = string  
    S = Scrollbar(wt)
    T = Text(wt,height=20)
    S.pack(side=RIGHT,fill=Y)
    T.pack(expand = 1, fill= BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END,data)
    T.config(state=DISABLED)      
    wt.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def manual(self):
  if hasattr(self,'name'):
    manual=Tk()
    manual.title("Manually Annotate: "+self.name)
    manualWidget=Text(manual)
    manualWidget.insert(0.0,self.myText)
    manualWidget.pack(expand = 1, fill= BOTH)
    label_1=Label(manual,text="Word")
    label_2=Label(manual,text="Category")
    self.entry_1=Entry(manual)
    self.entry_2=Entry(manual)
    label_1.pack()
    label_2.pack()
    self.entry_1.pack()
    self.entry_2.pack()
    self.manual_array=set()
    self.entry_3=Entry(manual)
    self.entry_3.pack()
    submit=Button(manual,text="Submit",bg="red",command=self.submit)
    submit.pack()
    done=Button(manual,text="Done",bg="red",command=self.done)
    done.pack()
    highlight=Button(manual,text="HIGHLIGHT",bg="red",command=partial(self.getText,manualWidget))
    highlight.pack()
    manual.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def getText(self,manualWidget):
  text=self.entry_3.get()
  self.highlight(text,manualWidget,"yellow",0)


 def highlight(self,text,widget,color,cond): #pass cond=1 if you want to recursively highlight a set of words from the text,else pass cond=0

  try:
    search = " " + text + " "
    start=1.0
    first=widget.search(search,1.0,stopindex=END)
    widget.tag_configure("COLOR", background=color)
    if(cond==0):
     widget.tag_remove("COLOR", 1.0, "end")
    while first:
     row,col=first.split('.')
     col = int(col) + 1
     first = row+'.'+str(col)
     last=int(col)+len(search) - 2
     last=row+'.'+str(last)
     row,col=last.split('.') 
     print(first)
     print(last)
     widget.tag_add("COLOR", first,last)
     start=last
     first=widget.search(search,start,stopindex=END)
  except:
    content = "Please Enter a text in highlight box"
    messagebox.showinfo("Error! Oops",content)



 def submit(self):
  db = MySQLdb.connect("localhost","root","","manual_annotations")
  cursor = db.cursor()
  var1 = self.entry_1.get()
  print(var1)
  var2 = self.entry_2.get()
  sql = "INSERT INTO annotations(name, \
         category) \
         VALUES ('%s','%s')" % \
         (var1,var2)
  cursor.execute(sql)
  db.commit()
  self.manual_array.add(self.entry_1.get()+"~"+self.entry_2.get())
 
 def done(self):
  f = open(self.name + "_manualAnnot.txt","w")
  for i in self.manual_array:
   f.write(i)
   f.write("\n")
  self.manual.destroy()
    
 def getManual(self):
  if hasattr(self,'name'):
    manualAnnot=Tk()
    manualAnnot.title("Manual Annotate: "+self.name)
    manualFile=open(self.name + "_manualAnnot.txt","r+")
    manualText=manualFile.read()
    manualAnnotWidget=Text(manualAnnot)
    manualAnnotWidget.insert(0.0,manualText)
    manualAnnotWidget.pack(expand = 1, fill= BOTH)
    manualAnnot.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)



mainWindow=gui()


