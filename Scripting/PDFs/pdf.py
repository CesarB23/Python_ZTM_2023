import PyPDF2

with open("dummy.pdf","rb") as pdf:
    reader = PyPDF2.PdfReader(pdf)
    page = reader.pages[0]
    page.rotate(-90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("dummy_rotated.pdf","wb") as new_file:
        writer.write(new_file)