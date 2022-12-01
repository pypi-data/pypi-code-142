from pyadvdocx import text as pyadvdocx_text
from docx import Document
import os
__data_replace={
    "${Title}": "PyAdvDocx",
    "${para1}": "PyAdvDocx is awesome!",
    "${para2}": "You are awesome!",
    "${header1}": "Mega table",
    "${header2}": "Omega Mega table",
    "${text}": "Value of the project",
    "${chart_title}": "Something new",
}


def main():
    docx_path=os.path.join(os.path.curdir,"test","data","Text_Replace.docx")
    docx_path_done=os.path.join(os.path.curdir,"test","data","Text_Replace_done.docx")
    __doc_obj=Document(docx_path)
    print(pyadvdocx_text.replace(docx=__doc_obj,**__data_replace))


    __doc_obj.save(docx_path_done)




if __name__=='__main__':
    main()