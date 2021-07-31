from pdf2image import convert_from_path
images = convert_from_path('/pdf2jpg/SE_practical-8.pdf')

i=0
for page in images:
    page.save('out'+str(i)+'.jpg','JPEG')
    i=i+1
