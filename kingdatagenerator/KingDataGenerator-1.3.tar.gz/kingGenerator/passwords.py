from kingGenerator.variables import print_error_application, print_error_connection, print_time_load

from fordev import generators

def generator_password(quant_passwords):
    print_time_load('PASSWORDs')
    confirm_int = int(quant_passwords)
    count_how_loops = 0
    list_passwords = []
    while count_how_loops < confirm_int:
        count_how_loops += 1
        
        try:
            peoples = generators.people()
        except ConnectionError as error:
            print_error_connection(error)
        except Exception as error:
            print_error_application(error)
        
        for people in peoples:
            only_password = people['senha']
            list_passwords.append(only_password)
    
    return list_passwords