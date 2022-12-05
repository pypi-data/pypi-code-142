import numpy as np
import re

def retrieve_postcode(item:str):
    """ This function retrieves the postal code of a string by searching specifc regex in line with Dutch postal codes.
        Regex source: https://forum.mendix.com/link/questions/88423
    """
    try:
        # find position of 4 digits
        output = re.findall(r"^[1-9][0-9]{3}\s?[a-zA-Z]{2}$", item)[-1]
        output = ''.join(output.upper().split())
        return output
    except:
        return np.nan


def retrieve_housenumber(item:str):
    """ This function retrieves the housenumber of an address (string).
        It assumes that the last number in the string is housenumber.
    """
    if item in [np.nan]:
        return np.nan
    else:
        try:
            return re.findall("\d+", item)[-1]
        except:
            return np.nan