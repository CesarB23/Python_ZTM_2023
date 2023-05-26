import sys, PyPDF2

inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("Merged PDF.pdf")

pdf_merger(inputs)