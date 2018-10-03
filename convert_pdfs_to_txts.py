# converting the downloaded pdfs to txt files
import os, subprocess

files = os.listdir("pdfs/")

for pdf_name in files:
	txt_name = pdf_name.replace("pdf", "txt")	
	call_string = 'pdftotext pdfs/' + pdf_name + ' txts/' + txt_name
	subprocess.call([call_string], shell=True)
	print("1 file converted.")
