import PyPDF2

# rb = read binary
# Converts file to binary mode; otherwise, PDfFileReader cannot read it.
with open("dummy.pdf", 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)