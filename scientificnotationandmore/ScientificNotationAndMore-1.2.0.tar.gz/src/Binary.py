def Binary(into, output_file):
    """Outputs the number in binary to the file"""
    b = bin(into)
    b = str(b)
    b = list(b)
    del b[0]
    del b[1]
    b = str(b)
    b_file = open(output_file, "w")
    b_file.write(b)
    b_file.close()


# Update 1.0.1
def get_binary(number):
    b = bin(number)
    unneeded, binary = b.split("b")
    return binary
