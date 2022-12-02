


from typing import Literal, get_args




mainentance_mode:bool=False
'''If True, all requests are denied unless the requestor has a bypass header or cookie'''

coming_soon_mode:bool=False
'''If True, all requests are denied unless the requestor has a bypass header or cookie'''



log_to_console:bool=True
'''If True, all messages sent through the Log module are printed to the console'''


literal_valid_request_methods=Literal["GET","POST","PATCH","PUT","DELETE","OPTIONS","HEAD"]
valid_request_methods:list = ["GET","POST","PATCH","PUT","DELETE","OPTIONS","HEAD"]
'''A list of valid request method names'''



