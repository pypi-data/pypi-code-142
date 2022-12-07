
import os
import pandas
import numpy as np
from pathlib import Path
from domainfinderbyrohit.dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
from urllib.parse import *
import requests
from enum import Enum
global data_frame
data_frame = None




def set_global_domain(inp):
    global input_domain
    input_domain=inp
    

    
class FormatEnum(Enum):
    csv = 'csv'
    xlsx = 'xlsx'

    def __str__(self):
        return self.value


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        df = pandas.read_csv(arg)
        list_domains = df['domains'].tolist()
        print(
            f"found {len(list_domains)} domains in the csv and starting Script")
        return list_domains


def save_dataframe_to_file(dataframe, output_dir, format=FormatEnum.csv):
    

    file_path = os.path.join(output_dir, f'{input_domain}.{format}')
    print(file_path)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    if not os.path.exists(output_dir):
        print(f"Error saving to :{output_dir}")
        file_path = f'{input_domain}.{format}'
    print(f'Attempting to save to {file_path}')
    

    if format == FormatEnum.csv:
        
        dataframe.to_csv(file_path)
    elif format == FormatEnum.xlsx:
        dataframe.to_excel(file_path, sheet_name=input_domain)

    print(f"File Saved to: {file_path}")


def run_scrapper(input_domain) -> pandas.DataFrame():
   
    print(f"Running Scrapper for {input_domain}")
    records = DNSDumpsterAPI({'verbose':True}).search(
            input_domain).get('dns_records')
    print("o",records)
    
    try:
        print(input_domain," o")
       
        records = DNSDumpsterAPI({'verbose':True}).search(
            input_domain).get('dns_records')
        
     
    except Exception as e:
        records = {}
        print(e)
        return None

    list_of_resultant_records = []
    if isinstance(records, dict):
        for record_type, list_of_record in records.items():
            for record in list_of_record:
                if not isinstance(record, dict):
                    pass
                else:
                    record["type"] = record_type
                    response = requests.get(
                        f'https://internetdb.shodan.io/{record.get("ip")}')
                    if response.status_code == 200:
                        json_res = response.json()
                        record = {
                            **record,
                            **json_res
                        }
                    list_of_resultant_records.append(record)

    result_df = pandas.DataFrame(list_of_resultant_records)
    result_df.index = np.arange(1, len(result_df) + 1)

    return result_df


def start_scrapper(input_domain, output_dir, format, multiple=False, *args, **kwargs):
    if not output_dir:
        output_dir = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'output')

    print(
        f'Hold your horses, Starting Script for {input_domain} and lookout for files in {output_dir}')
    global data_frame
    if multiple:
        if data_frame is None:
            print("a")
            data_frame = run_scrapper(input_domain)
        else:
            print("b")
            data_frame = pandas.concat(
                [data_frame, run_scrapper(input_domain)])
            data_frame.index = np.arange(1, len(data_frame) + 1)
            print(f"\n\n\n {len(data_frame)}")
    else:
        print("c")
        print(input_domain)
        data_frame = run_scrapper(input_domain)
        print(data_frame)

    save_dataframe_to_file(data_frame, output_dir, format)


def main():
    pass


# if __name__ == '__main__':

#     parser = argparse.ArgumentParser(description="""    
#                                      Extract various dns records from the domains 
#                                      and extract ip-address,hostnames and scan for 
#                                      openports and Vunrabilities""",
#                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#     parser.add_argument(
#         "input_domain", help="input domain or file name in input csv is provided", default=None)
#     parser.add_argument("-o", "--output-dir",
#                         help="path to output directory")
#     parser.add_argument("-f", "--format", help="format of saving file ",
#                         type=FormatEnum, choices=list(FormatEnum), default=FormatEnum.csv)
#     parser.add_argument("-i", "--input-list", help="input file",
#                         metavar="FILE", type=lambda x: is_valid_file(parser, x))

#     args = parser.parse_args()
    
#     config = vars(args)

#     global input_domain
#     input_domain = config.get("input_domain")
#     list_of_domains = config.pop("input_list", [])
#     if not list_of_domains is None and len(list_of_domains) > 0:
#         for domain in list_of_domains:
#             start_scrapper(domain, None, config.get('format'), multiple=True)
#     else:
#         start_scrapper(**config)
