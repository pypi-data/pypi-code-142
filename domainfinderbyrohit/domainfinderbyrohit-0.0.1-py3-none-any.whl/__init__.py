


from   domainfinderbyrohit.demo import FormatEnum,set_global_domain,start_scrapper
c_s_v=FormatEnum.csv
ex_ce_l=FormatEnum.xlsx




def single_webiste(k,file_path):
    print(file_path,"lhukgjy")
    set_global_domain(k)
 
  
    start_scrapper(k,file_path,c_s_v)
    print("excel file is saved at provided loation")
    

    
