def send_array(array, filename="my_array", mode="w", file_type="txt"):
    """Do not add file extension to filename, file_type can be either 'csv' or 'txt' The mode must be either 'w' for
    writing or 'a' for appending."""
    if file_type == "txt":
        file = open((filename + "." + file_type), mode)
        array_els = []
        for i in array:
            array_els.append(i)
        for i in range(len(array_els)):
            l1 = ""
            for j in range(len(array_els[i])):
                l1 += (" " + str(array_els[i][j]))
            l1 += "\n"
            file.write(l1)
        file.close()
    elif file_type == "csv":
        file = open((filename + "." + file_type), mode)
        array_els = []
        for i in array:
            array_els.append(i)
        for i in range(len(array_els)):
            l1 = ""
            for j in range(len(array_els[i])):
                l1 += ( str(array_els[i][j]) + ",")
            l1 += "\n"
            file.write(l1)
        file.close()
    else:
        raise FileNotFoundError


def grab_section(array, size: tuple, offset: tuple = (0, 0)):
    new = array[offset[0] + 1: size[0] + 1, offset[1] + 1: size[1] + 1]
    return new
