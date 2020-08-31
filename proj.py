import PyPDF2
#Replace this path with your file's path
myFile=open(r"C:\Users\Abhishek\Documents\Sample.pdf","rb")
read_obj=PyPDF2.PdfFileReader(myFile)
num_pages=read_obj.numPages
s=""
for i in range(0,num_pages):
    pageNo_I=read_obj.getPage(i)
    s=s+pageNo_I.extractText()
myFile.close()

from gtts import gTTS
import os
language='en'
myobj=gTTS(text=s,lang=language,slow=False)
myobj.save("Converted_Audio_File.mp3")
os.system("mpg321 Converted_Audio_File.mp3")
