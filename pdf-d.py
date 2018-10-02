# Author: Johnjimy Som
# Date: September 27, 2018
# Description: decrypter for PDFs, it will output a another file that can be readable without pw.

import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted

pdfReader.getPage(0)
pdfReader.decrypt('rosebud')#not the right password but to test


pageObj = pdfReader.getPage(0)