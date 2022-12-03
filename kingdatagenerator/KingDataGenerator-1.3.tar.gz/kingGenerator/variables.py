error_connection_print = "\n[/] Connection with Frida Lib broke failed >:( | Try AGAIN\n[/]ERROR - "
error_application = "\n[/]Some error is preventing the code run | Try AGAIN\n[/]ERROR - "

def print_error_application(error):
    print(f'{error_application}{error}')

def print_error_connection(error):
    print(f'{error_connection_print}{error}')

def print_time_load(item):
    time_to_load = f"\n[*] Please wait...{item} are being generated\n"
    print(time_to_load)