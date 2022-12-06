from  dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI

from o import FormatEnum,set_global_domain,start_scrapper
c_s_v=FormatEnum.csv
ex_ce_l=FormatEnum.xlsx
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
# k=input("enter the  url name")
# output=None

# start_scrapper(k,r"C:\Users\Rohit-VM\Desktop\my_folder",c_s_v)


def single_webiste(k,file_path):
    set_global_domain(k)
 
  
    start_scrapper(k,file_path,c_s_v)
    print("excel file is saved at provided loation")
    
    

    




