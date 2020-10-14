<p><span style="font-family: Arial, Helvetica, sans-serif;">#/usr/bin/env python</span></p>#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
from pdfminer.converter import PDFPageAggregator
import re
 
 
# Open a PDF file.
fp = open('your input pdf file', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
document = PDFDocument(parser)
 
# Process each page contained in the document.
text_content = []
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            text_content.append(lt_obj.get_text())
        else:
            pass
 
 
# text_content 
total_text = ''.join(text_content).replace("\n","")

file = open("the file your want to save","w")
p = re.compile('\[\d+\][^\[\]]*\d\.')
m = p.findall(total_text)
for i in m:
    #print i
    if i.startswith("["):
        file.write(str(i))
        file.write("\n")
file.close()