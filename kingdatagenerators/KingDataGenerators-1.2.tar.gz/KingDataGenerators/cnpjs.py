from KingDataGenerators.variables import print_error_application, print_error_connection, print_time_load

from fordev import generators

def generator_cnpj(quant_cnpjs):
    print_time_load('CNPJs')
    confirm_int = int(quant_cnpjs)
    count_how_loops = 0
    list_cnpjs = []
    while count_how_loops < confirm_int:
        count_how_loops += 1
        
        try:
            cnpjs = generators.cnpj()
        except ConnectionError as error:
            print_error_connection(error)
        except Exception as error:
            print_error_application(error)
            
        list_cnpjs.append(cnpjs)
    
    return list_cnpjs
