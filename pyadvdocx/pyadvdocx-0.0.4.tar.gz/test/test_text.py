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
    "${nume_client}":"pyadvdocx"
}


def main():
    docx_path=os.path.join(os.getcwd(),"test","data","venv_s2_input - Copy.docx")
    docx_path_done=os.path.join(os.getcwd(),"test","data","venv_s2_input_done.docx")
    __doc_obj=Document(docx_path)
    __docx_obj=pyadvdocx_text.replace(docx=__doc_obj,**__data_replace)


    __docx_obj.save(docx_path_done)




if __name__=='__main__':
    main()