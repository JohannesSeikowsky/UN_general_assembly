# converting the downloaded pdfs to txt files
import os, subprocess

files = os.listdir("pdfs/")

for pdf in files:
	txt = pdf.replace("pdf", "txt")	
	call_string = 'pdftotext pdfs/' + pdf + ' txts/' + txt
	subprocess.call([call_string], shell=True)
	print("1 file converted.")
