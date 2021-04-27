# coding:utf-8
import  PyPDF2
from PyPDF2 import PdfFileReader

def Evidence(path):
    #读取并打印PDF的元信息
    #   请在此添加实现代码   #
    # ********** Begin *********#
    pdf = PdfFileReader(open(path,"rb"))
    docinfo = pdf.getDocumentInfo()
    for key in docinfo:
        print(key[1:], ":" , docinfo[key])
    # content =""
    # for i in range(0,pdf.getNumPages()):
    #     pageObj = pdf.getPage(i)
    #     extractedText = pageObj.extractText()
    #     content+=extractedText+"\n"
    # content.encode("ascii", "ignore")
    # print( content)

    # ********** End **********#