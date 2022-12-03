from KingDataGenerators.variables import print_error_application, print_error_connection, print_time_load

from fordev import generators

def generator_email(quant_emails):
    print_time_load('EMAILs')
    confirm_int = int(quant_emails)
    count_how_loops = 0
    list_emails = []
    while count_how_loops < confirm_int:
        count_how_loops += 1
        
        try:
            peoples = generators.people()
        except ConnectionError as error:
            print_error_connection(error)
        except Exception as error:
            print_error_application(error)
        
        for people in peoples:
            only_email = people['email']
            list_emails.append(only_email)
    
    return list_emails