import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfReader = PyPDF2.PdfReader(book)  

pages = len(pdfReader.pages)

for num in range(pages): 
    page = pdfReader.pages[num]  #fileREader
    text = page.extract_text() 
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()