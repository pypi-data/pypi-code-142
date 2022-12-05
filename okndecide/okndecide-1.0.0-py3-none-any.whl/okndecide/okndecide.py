import sys
import argparse
import json
import csv
import os
import time
import commentjson
from multiprocessing import freeze_support


# This function is to get header position from the given array
def get_index(search_input, array_in):
    idx_found = False
    return_idx = None
    for idx, val in enumerate(array_in):
        if val == search_input:
            idx_found = True
            return_idx = idx
            break

    if not idx_found:
        print(f"{search_input} can not be found!")

    return return_idx


# This function is to get file name from the given directory
def get_file_name(dir_input):
    output_file_name = None
    dir_input = str(dir_input).replace("\\\\", "\\")
    string_array = str(dir_input).split("\\")
    if len(string_array) > 0:
        output_file_name = string_array[-1]

    return output_file_name


def read_signal_csv(input_file_dir1):
    file1 = open(input_file_dir1)
    csv_reader = csv.reader(file1)
    header_array = []
    rows = []
    data_table_dict = {}
    count_one = 0

    for row in csv_reader:
        if count_one <= 0:
            header_array = row
            count_one += 1
        else:
            rows.append(row)

    for header in header_array:
        header_position = get_index(header, header_array)
        value_array = []
        for row in rows:
            value_array.append(row[header_position])
        data_table_dict[header] = value_array

    return data_table_dict


# This function is to read the signal.csv and retrieve max chain length and unchained okn total
def signal_checker(csv_input):
    print(f"Sending the following directory: {csv_input} to signal checker!")
    start_time = time.time()
    # Add signal.csv to directory
    # Comment out in this okndecide but not in oknserver
    # csv_input = csv_input + "\\signal.csv"
    data_table = read_signal_csv(csv_input)
    result_id_array = data_table["result_id"]
    result_chain_id_array = data_table["result_chain_id"]
    signal_data = {}
    result_data = []
    temp_max_chain_length = 0
    temp_unchained_okn_total = 0

    # Looking for result id and result chain id.
    # When they are found, they are added into result data array
    for r_id, r_c_id in zip(result_id_array, result_chain_id_array):
        if int(r_id) != -1 and int(r_c_id) != -1:
            result_data.append((int(r_c_id), int(r_id)))

    # remove duplicate number from result data array
    unique_result_data = list(dict.fromkeys(result_data))
    # print(unique_result_data)

    # taking only result id
    raw_unique_result_id_array = []
    for ri in unique_result_data:
        raw_unique_result_id_array.append(ri[0])

    # remove duplicate result id from raw unique result id array
    unique_result_id_array = list(dict.fromkeys(raw_unique_result_id_array))

    final_data_array = []

    # looping unique result id array to get all result chain id which are
    # related to their individual result id into temp array
    # after that, add result id and its related result chain id into final data array as a tuple
    for rid in unique_result_id_array:
        temp_array = []
        for data in unique_result_data:
            if rid == data[0]:
                temp_array.append(data[1])
        final_data_array.append((rid, temp_array))

    # determine the max chain length and unchained okn total from final data array
    if len(final_data_array) > 0:
        print(f"Raw result: {final_data_array}")
        for tuple_item in final_data_array:
            chain_length = len(tuple_item[1])
            if chain_length > temp_max_chain_length:
                temp_max_chain_length = chain_length
            if chain_length == 1:
                temp_unchained_okn_total += 1
        signal_data["max_chain_length"] = temp_max_chain_length
        signal_data["unchained_okn_total"] = temp_unchained_okn_total
    else:
        print("There is no chain or okn")
        signal_data["max_chain_length"] = 0
        signal_data["unchained_okn_total"] = 0

    print(f"Signal data: {signal_data} is collected and it took {time.time() - start_time} sec.")
    print("--------------------------------------------------------------------------------------")

    return signal_data


# This function is to decide whether there is okn or not by the given rules
def apply_okn_detection_rule(data, min_chain_length_input, min_unchained_okn_input):
    print(f"Start applying the okn detection rule.")
    print(f"Minimum chain length must be greater than equal {min_chain_length_input}.")
    print(f"Minimum unchained okn must be greater than equal {min_unchained_okn_input}.")
    start_time = time.time()
    # Rule 1
    is_chained = (data["max_chain_length"] >= min_chain_length_input)

    # Rule 2
    is_unchained = (data["unchained_okn_total"] >= min_unchained_okn_input)
    i = is_chained | is_unchained
    print(f"Data:{data} has been measured by okn detection rules!")
    if i:
        print("There is an okn!")
    else:
        print("There is no okn!")
    print(f"The process took {time.time() - start_time} sec.")
    print("--------------------------------------------------------------------------------------")

    return i


def main():
    parser = argparse.ArgumentParser(prog='okndecide',
                                     description='OKN config file modifier program.')
    parser.add_argument('--version', action='version', version='1.0.0'),
    parser.add_argument("-i", dest="input_file", required=True, default=sys.stdin,
                        help="input file", metavar="input file")
    parser.add_argument("-c", dest="config_file", required=True, default=sys.stdin,
                        help="config file", metavar="config file")
    parser.add_argument("-o", dest="output_file", required=False, default=sys.stdin,
                        help="output file", metavar="output file")

    args = parser.parse_args()
    input_file = str(args.input_file)
    config_file = str(args.config_file)
    output_file = str(args.output_file)

    if "_io.TextIOWrapper" in output_file:
        signal_file_name = get_file_name(input_file)
        output_file = str(input_file).replace(signal_file_name, "output.json")
        print("Output file is not given.")
        print(f"Therefore output file will be {output_file}.")

    # Opening oknserver config
    with open(config_file) as f:
        config_info = commentjson.load(f)
        if config_info is not None:
            print("oknserver_config.json is found.")
        else:
            print("Essential config file oknserver_config.json is missing.")
    rule_set = config_info["rule_set"]
    # rule_set = [
    #     {"name": "main1", "min_chain_length": 2, "min_unchained_okn": 3},
    #     {"name": "main2", "min_chain_length": 2, "min_unchained_okn": 4},
    #     {"name": "main3", "min_chain_length": 3, "min_unchained_okn": 3},
    #     {"name": "main4", "min_chain_length": 2, "min_unchained_okn": 2}
    # ]
    default_rule_set_name = config_info["default_rule_set"]
    # default_rule_set_name = "main1"
    default_rule_set_info = None
    for rs in rule_set:
        if rs["name"] == default_rule_set_name:
            default_rule_set_info = rs
            break
    if default_rule_set_info is not None:
        min_chain_length = default_rule_set_info["min_chain_length"]
        min_unchained_okn = default_rule_set_info["min_unchained_okn"]

        print(f"default_rule_set: {default_rule_set_name}")
        print(f"min_chain_length: {min_chain_length}")
        print(f"min_unchained_okn: {min_unchained_okn}")

        signal_data = signal_checker(input_file)
        is_there_okn = apply_okn_detection_rule(signal_data, min_chain_length, min_unchained_okn)
        signal_data_max_chain_length = signal_data["max_chain_length"]
        signal_data_unchained_okn_total = signal_data["unchained_okn_total"]
        # print(signal_data)
        # print(is_there_okn)
        config_info["max_chain_length"] = signal_data_max_chain_length
        config_info["unchained_okn_total"] = signal_data_unchained_okn_total
        config_info["okn_present"] = is_there_okn
        # print(config_info)

        # Writing to decide.info.json
        with open(output_file, "w") as outfile:
            outfile.write(json.dumps(config_info))
            print(f"Output file is written in the {output_file}")

    else:
        print("Default rule set is not found!")
        print("Please check spelling of \"default_rule_set\" in the given config.")
