#decrypter for PDFs

import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted

pdfReader.getPage(0)
pdfReader.decrypt('rosebud')#not the right password but to test


pageObj = pdfReader.getPage(0)