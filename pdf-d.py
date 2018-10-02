# Author: Johnjimy Som
# Date: September 27, 2018
# Description: decrypter for PDFs, it will output a another file that can be readable without pw.

import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted #check a pdf file that is encrypted, output would be true or false (boolean)


pdfReader.getPage(0)
pdfReader.decrypt('bowsettelmao123')#not the right password but to test
pdfReader.getPage(0)

pageObj = pdfReader.getPage(0)