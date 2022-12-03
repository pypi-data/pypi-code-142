"""
  ____              _______ _   ______ _       ___ __    __
 |  _ \            /__   __(_)/__   __(_) _ __|_| |\ \\  / /
 | |_) |_   _         | |   _    | |   _ | '__| | | \ \\/ /
 |  _ <| | | |        | |  | |   | |  | || |    | |  \  \\
 | |_) | |_| |        | |  | |   | |  | || |    | | / /\ \\
 |____/ \__, |        |_|  |_|   |_|  |_||_|    |_|/_/  \_\\
         __/ |                                               
        |___/
"""

import os, re
import logging

logging.basicConfig(level=logging.INFO)

def os_commands_regex(os_command:str, regex_function:str, regex_parameters:str, show_log=False):
    """Designed to create variables with results that you can obtain by filtering the log that your terminal gives you by os commands :D

    Args:
        os_command (str): OS command to execute
        regex_function (str): 'findall', 'search', 'split', 'sub'
        regex_parameters (str): parameters to execute. Example:
        >>> ip_adress = os_commands_regex(os_command='ipconfig', regex_function='search', regex_parameters='IP Address.+: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
        >>> print(ip_adress)
        ['192.168.0.101']

        # convert list to string:
        >>> ip =''.join(ip_adress)
        >>> print(ip)
        192.168.0.101

    Returns:
        list: Returns the output of regex.
    """

    os.system(f'{os_command} > ./last_log.txt')

    if regex_function == 'findall':
        temp_log = open('./last_log.txt', 'r')
        regex_output = re.findall(regex_parameters, temp_log.read())
        return regex_output
        

    elif regex_function == 'search':
        temp_log = open('./last_log.txt', 'r')
        regex_output = re.findall(regex_parameters, temp_log.read())
        return regex_output

    elif regex_function == 'split':
        temp_log = open('./last_log.txt', 'r')
        regex_output = re.findall(regex_parameters, temp_log.read())
        return regex_output

    elif regex_function == 'sub':
        temp_log = open('./last_log.txt', 'r')
        regex_output = re.findall(regex_parameters, temp_log.read())
        return regex_output

def show_last_log():
    """_summary_
    It is useful for copying special characters (which do not load in your text editor) and using them in regex parameters.
    """
    temp_log = open('./last_log.txt', 'r')
    logging.info(temp_log.read())
    temp_log.close()
    
