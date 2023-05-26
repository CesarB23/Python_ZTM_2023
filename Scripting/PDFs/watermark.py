


# def watermark(
#     content_pdf,
#     stamp_pdf,
#     pdf_result
# ):
#     reader = PdfReader(content_pdf)
#     reader_stamp = PdfReader(stamp_pdf)
#     writer = PdfWriter()

#     for index in range(len(reader.pages)):
#         content_page = reader.pages[index]
#         image_page = reader_stamp.pages[0]
#         image_page.merge_page(content_page)
#         writer.add_page(image_page)

#     with open(pdf_result, "wb") as fp:
#         writer.write(fp)

from PyPDF2 import PdfWriter, PdfReader

template = PdfReader('Merged PDF.pdf', 'rb')
watermark = PdfReader('wtr.pdf', 'rb')
output = PdfWriter()

for i in range(len(template.pages)):
  page = template.pages[i]
  page.merge_page(watermark.pages[0])
  output.add_page(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
  