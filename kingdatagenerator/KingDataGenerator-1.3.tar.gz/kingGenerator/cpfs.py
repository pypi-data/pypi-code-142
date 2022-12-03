from kingGenerator.variables import print_error_application, print_error_connection, print_time_load

from fordev import generators

def generator_cpf(quant_cpfs):
    print_time_load('CPFs')
    confirm_int = int(quant_cpfs)
    count_how_loops = 0
    list_cpfs = []
    while count_how_loops < confirm_int:
        count_how_loops += 1 
        
        try:
            cpf = generators.cpf()
        except ConnectionError as error:
            print_error_connection(error)
        except Exception as error:
            print_error_application(error)
            
        list_cpfs.append(cpf)
    
    return list_cpfs