from kingGenerator.variables import print_error_application, print_error_connection, print_time_load

from fordev import generators


def generator_name(quant_names):
    print_time_load('NAMEs')
    confirm_int = int(quant_names)
    count_how_loops = 0
    list_names = []
    while count_how_loops < confirm_int:
        count_how_loops += 1
        
        try:
             peoples = generators.people()
        except ConnectionError as error:
            print_error_connection(error)
        except Exception as error:
            print_error_application(error)
        
        for people in peoples:
            only_name = people['nome']
            list_names.append(only_name)
            
    return list_names