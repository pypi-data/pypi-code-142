import re

def format_phone(phone_number:str, format:str='tuple', custom_format:str=None):
    '''
    params:
    phone_number: must be >= 10 digits long.
    format: must be a string matching a format in the formats tuple below the docstring.
    custom_format: string that is example of how you want the output to be. 
    '''
    formats = ('tuple', 'dict', 'E.164')

    # Input verification
    try:
        if len(phone_number) < 10:
            print("Input to format_phone too short to be a phone number, must be at least 10 digits.")
            return phone_number
        if format not in formats:
            print(f"Param format not in {formats}")
            return phone_number
    except TypeError:
        print("Input to format_phone must be str.")
        return phone_number

    try:
        groups = list(re.findall(r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})[-.\s]*$", phone_number)[0])
    except IndexError as err:
        print(f"Error calling format_phone on: {phone_number}. Input phone number probably had too many digits.")
        return phone_number

    if not groups:
        print(f"Invalid phone number input to format_phone: {phone_number}.")
        return phone_number

    # If no country code is given, assume it is American.
    if not groups[0]:
        country_code = "1"
    else:
        country_code = groups[0]

    # Break down the input into groups for easy formatting.
    area_code = groups[1]
    exchange = groups[2]
    sub_num = groups[3]

    if not custom_format:
        if format == 'tuple':
            return (country_code, area_code, exchange, sub_num)
        elif format == 'dict':
            return {
                'country_code':country_code,
                'area_code':area_code,
                'exchange':exchange,
                'subscriber_numbers':sub_num,
            }
        elif format == 'E.164':
            return "+" + country_code + area_code + exchange + sub_num
    else:
        try:
            if len(custom_format) < 10:
                raise ValueError("Param custom_format must be at least 10 digits long.")
        except TypeError:
            print("Invalid custom_format")

        values = [country_code, area_code, exchange, sub_num]
        match = re.match(r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})[-.\s]*$", custom_format)
        # If no country code is given, assume it is American.
        result = ''
        last_match = 0
        i = 0
        for group in match.groups():
            if not group:
                i+=1
                continue
            result += custom_format[last_match:match.start(i+1)]
            result += values[i]
            last_match = match.end(i+1)
            i+= 1
        return result
