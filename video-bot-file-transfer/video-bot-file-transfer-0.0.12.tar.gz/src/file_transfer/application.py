from dotenv import load_dotenv

from file_transfer.handler import handler
from file_transfer.utils.lambda_helpers import get_json
from file_transfer.get_event import get_event



class Application:
   
    def run(self):
        load_dotenv()
        event = get_event()
        result = handler(event, None)
        json_str = get_json(result)
        return json_str
           


    

  








    

    
    
