from kingGenerator.variables import print_error_application, print_error_connection, print_time_load

from fordev import generators

def generator_cel(quant_cel, dd='(11)'):
    print_time_load('NUMBERs')
    confirm_int = int(quant_cel)
    count_how_loops = 0
    list_celulares = []
    while count_how_loops < confirm_int:
        count_how_loops += 1
        
        try:
            peoples = generators.people()
        except ConnectionError as error:
            print_error_connection(error)
        except Exception as error:
            print_error_application(error)
        
        for people in peoples:
            only_cel = people['celular'].replace('()', dd).replace(' ', '').replace('-', '').strip()
            list_celulares.append(only_cel.strip())
    
    return list_celulares