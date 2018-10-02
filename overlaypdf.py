# Author: Johnjimy Som
# Date: October 2, 2018
# Description: This python script allows to have 2 pdfs to be merged and into a new file. Still keep the old pdf files.


import PyPDF2
minutesFile = open('test.pdf', 'rb') #meetingminutes.pdf
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('wk1.pdf', 'rb')) #watermark.pdf
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
           pageObj = pdfReader.getPage(pageNum)
           pdfWriter.addPage(pageObj)
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()