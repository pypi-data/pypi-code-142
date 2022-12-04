import logging
import random


def generate_input_file(file_name, start=-500, end=500, num_of_elements=1000):
    """
    Generates a file which is huge enough to test the logic out
    :param file_name: the name of the generated file
    :param start: the start range for the integer values to be placed in output file
    :param end: the end range for the integer values to be placed in output file
    :param num_of_elements: number of elements to be generated
    :return: the input file path
    """
    logging.info(f"Generating input file: {file_name}")
    with open(file_name, 'w') as temp_f:
        for _ in range(num_of_elements):
            temp_f.write(f"{random.randint(start, end)}\n")
    return file_name


def find_intersection_in_memory(file1, file2, output_file):
    file1_contents = set(open(file1, 'r'))
    file2_contents = set(open(file2, 'r'))
    out_contents = set(open(output_file, 'r'))
    print(len(file1_contents & file2_contents))
    print(len(out_contents))
