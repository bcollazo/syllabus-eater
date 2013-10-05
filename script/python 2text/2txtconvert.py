import zipfile, re
import pdfextract

def main(inputfile):
    if inputfile.endswith('.pdf'):
        outfile = inputfile[:-3]+'txt'
        pdfextract.pdf2text(inputfile,outfile)
    elif inputfile.endswith('.docx'):
        outfile = inputfile[:-5]+'.txt'
        document = zipfile.ZipFile(inputfile)
        content = document.read('word/document.xml')
        cleaned = re.sub('<(.|\n)*?>','',content)
        outfp = file(outfile, 'w')
        outfp.write(cleaned)
        outfp.close()
    else:
        print "Error: File not supported"
    return
