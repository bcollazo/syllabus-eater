import os
import sys
import zipfile, re
from bs4 import BeautifulSoup
import pdfextract

def main(argv):
    ipdir = argv[0]
    addr = "../../public/uploads/" + ipdir
    os.chdir(addr)
    for files in os.listdir("."):
        if inputfile.endswith('.pdf'):
            outfile = inputfile[:-3]+'txt'
            pdfextract.pdf2text(inputfile,outfile)
        elif inputfile.endswith('.docx'):
            outfile = inputfile[:-5]+'.txt'
            document = zipfile.ZipFile(inputfile)
            content = document.read('word/document.xml')
            soup = BeautifulSoup(content, 'xml')
            #cleaned = re.sub('<(.|\n)*?>','',content)
            outfp = file(outfile, 'w')
            outfp.write(cleaned)
            outfp.close()
        else:
            print "Error: File not supported"
        return

if __name__ == '__main__': sys.exit(main(sys.argv))
