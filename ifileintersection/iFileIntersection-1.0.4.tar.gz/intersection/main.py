import logging
import tempfile

from intersection.args import process_command_line_args
from intersection.file.base import FileWrapper
from intersection.file.large_file_processor import LargeFileProcessor
from intersection.handler.file_intersection_handler import FileIntersectionHandler
from intersection.validation import validate_mandatory_args


def setup_for_cleanup(method):
    """
    Decorator to cleanup all intermediate files used during the processing
    :param method: the method invoked for finding the intersection
    :return: returned value from underlying method invocation
    """

    def process(*args, working_directory=None, **kwargs):
        if working_directory:
            return method(*args, working_dir=working_directory, **kwargs)
        else:
            with tempfile.TemporaryDirectory() as working_directory:
                return method(*args, working_dir=working_directory, **kwargs)

    return process


@setup_for_cleanup
def find_intersection(left_file_path, right_file_path, output_file_path, chunk_size=None, working_dir=None):
    """
    Finds the common integers given two file paths.

    NOTE:
    - Assumption here is that the files provided are too huge.
    - Hence can't be kept in memory and processed to find the common integers

    :param left_file_path: fully qualified path to the first file (a.k.a left file) containing integers
    :param right_file_path: fully qualified path to the second file (a.k.a right file) containing integers
    :param output_file_path: fully qualified path to the output file where the results will be stored
    :param chunk_size: the size in MB to split the files into chunks. Chunks would be approx the size provided
    :param working_dir: the directory to  place intermediate files. If none specified a dir in temp is used
    :return: fully qualified path to the output file
    """
    # Validate output file path
    validate_mandatory_args([output_file_path])
    # Initialize processors
    # We can inject a child class of FileProcessor here. For now sticking to the scope of large files.
    # It could be extended to support small files based on the size, etc.
    left, right = LargeFileProcessor(left_file_path, working_dir), LargeFileProcessor(right_file_path, working_dir)
    if left.file.size > right.file.size:
        # This ensures we have a smaller file to lookup when finding common integers
        left, right = right, left
    # Generate a sorted file
    left_sorted_file = left.process(chunk_size)
    right_sorted_file = right.process(chunk_size)
    # Find common integers
    intersection_handler = FileIntersectionHandler(FileWrapper(left_sorted_file), working_dir)
    intersection_handler.handle(FileWrapper(right_sorted_file), output_file_path)


def main():
    if __name__ == '__main__':
        logging.basicConfig(level=logging.DEBUG)
        cmd_args = process_command_line_args()
        find_intersection(cmd_args.left, cmd_args.right, cmd_args.out_file_path, chunk_size=cmd_args.file_chunk_size)


main()
