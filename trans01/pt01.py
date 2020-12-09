import PyPDF2
pdffileobj=open('08692946.pdf', 'rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()

file1=open(r"C:\002\08692946.txt", "a")
file1.writelines(text)
file1.close()