import argparse
from src.taskAutom import taskAutom

if __name__ == '__main__':

    command_parser = argparse.ArgumentParser(prog='logToTopo')

    subparsers   = command_parser.add_subparsers(help='Choose a command', dest='command', title='commands')

    taParser     = subparsers.add_parser('taskAutom', help='use taskAutom to collect the data')
    manualParser = subparsers.add_parser('manual',    help='use local file to process the data')
    manualParser.add_argument('-xf'  ,'--xlsFile',      required=True, type=str, help='Name of Excel file where information about interfaces and subnets, reside.')
    manualParser.add_argument('-xs'  ,'--xlsSheetName', required=True, type=str, default='sh_rtr_iface', help='Name of excel sheet, where data resides.')

    command = vars(command_parser.parse_args())['command']

    command_parser.parse_args()

    print(command_parser.parse_args())