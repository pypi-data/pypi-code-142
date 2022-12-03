import os
import re

class RegexPatterns:
    int = '\d+'
    optional_int = '\d*'
    float = f'{int}\.?\d*'
    optional_float = f'{optional_int}\.?\d*'

def getFileNamesFromRegex(regex="*", dir=""):
        pattern = re.compile(regex)
        files = os.listdir(dir)
        return [f'{file}' for file in files if pattern.match(file)]

def formatted_string2dict(s, format):
    """
    Converts a string of parameters into a dictionary.
    example:
        - if s = "T=10K-I=1.5A.csv" and format = "T=<temp>K-I=<current>A.csv", the function returns {"temp": "10", "current": "1.5"}
    """
    # get the names of the parameters
    names = re.findall("<.*?>", format) # ["<temp>", "<current>"]
    # remove the "<" and ">" characters
    names = [name[1:-1] for name in names] # ["temp", "current"]
    # remove the parameters from the format
    format = re.sub("<.*?>", "(.*?)", format) # "T=(.*?)K-I=(.*?)A.csv"
    # compile the format
    pattern = re.compile(format) 
    # match the string with the format
    match = pattern.match(s)
    # get the values of the parameters
    values = match.groups() # ("10", "1.5")
    # create the dictionary
    d = {}
    for name, value in zip(names, values):
        d[name] = value
    return d

def dict2formatted_string(dict, format):
    """
    Converts a dictionary of parameters into a string.
    example:
        - if dict = {"temp": "10", "current": "1.5"} and format = "T=<temp>K-I=<current>A.csv", the function returns "T=10K-I=1.5A.csv"
    """
    # get the names of the parameters
    names = re.findall("<.*?>", format) # ["<temp>", "<current>"]
    # remove the "<" and ">" characters
    names = [name[1:-1] for name in names] # ["temp", "current"]
    # replace the parameters in the format
    for name in names:
        format = format.replace(f"<{name}>", dict[name])
    return format