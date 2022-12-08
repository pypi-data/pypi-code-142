import time

def is_valid_decimal(s):
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True 

def decimal_to_time(value):
        if (str(value).isnumeric() or is_valid_decimal(value)):
            milisecs = str(round(float(value) % 1,3)).ljust(5,'0').replace('0.','')
            new_value = time.strftime('%H:%M:%S.' + str(milisecs), time.gmtime(value))
            return new_value
        else:
            return 0 