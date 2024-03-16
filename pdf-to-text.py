
file="test-doc.pdf.pdf"

#//https://www.pdf2go.com/pdf-to-text
# https://www.pdf2go.com/pdf-to-text
# importing required modules 
from pypdf import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader(file) 
  
# printing number of pages in pdf file 
print(len(reader.pages)) 
  
# getting a specific page from the pdf file 
page = reader.pages[0] 
  
# extracting text from page 
text = page.extract_text() 
print(text) 