#decrypter for PDFs

import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted

pdfReader.getPage(0)
pdfReader.decrypt('rosebud')


pageObj = pdfReader.getPage(0)