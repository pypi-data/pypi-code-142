import requests


class Exotel:
    """Class For Creating An Exotel Call Instance

    Attributes:
    sid: str
        Your Exotel SID
    api: str
        Your Exotel API Key
    domain: str
        Your Exotel Domain

    Typical usage example:
        call_instance = Exotel(sid="exotel_sid", api="exotel_api_key", domain="exotel_domain")
        call_instance.call()

    Methods:
    call(agent_number, customer_number,called_id)
        Creates Post Request For Call. Returns JSON response from exotel server
    """

    def __init__(self, sid: str, api: str, secret: str, domain: str):
        """
        Parameters:
        sid: str
            Your Exotel SID
        api: str
            Your Exotel API Key
        domain: str
            Your Exotel Domain
        """

        self.sid = sid
        self.api = api
        self.secret = secret
        self.domain = domain
        self.call_url = f"https://{self.api}:{self.secret}{self.domain}/v1/Accounts/{self.sid}/Calls/connect.json"

    def call(self, agent_number, customer_number, called_id):
        """
        Place Call From Agent Number To Customer Number By Using Exotel Caller ID

        Parameters:
        agent_number: str
            Your Exotel Agent Number param agent_number:
        customer_number: str
            Customer Number/ To Number
        called_id: str
            Your Exotel Account Caller ID

        Returns:JSON Object
            JSON Response From Exotel Server
        """

        params = {
            'From': str(agent_number),
            'To': str(customer_number),
            'CallerId': str(called_id),
        }

        return requests.post(self.call_url, params).json()

    def connect_flow(self, customer_number, called_id, flow_id):
        """
        Place Call From Customer Number To Agent Number By Using Exotel Flow ID

        Parameters:
        customer_number: str
            Customer Number/ To Number Preferably in E.164 format
        called_id: str
            Your Exotel Account Caller ID
        flow_id: str
            Your Exotel Flow ID
        """
        params = {
            'From': str(customer_number),
            'Url': f"http://my.exotel.com/{self.sid}/exoml/start_voice/{flow_id}",
            'CallerId': str(called_id),
        }
        return requests.post(self.call_url, params).json()

    def get_call_info(self, call_sid):
        """
        Get Call Info By Call Sid

        Parameters:
        call_sid: str
            Exotel Call Sid
        """
        url = f"https://{self.api}:{self.secret}{self.domain}/v1/Accounts/{self.sid}/Calls/{call_sid}.json"
        return requests.get(url).json()

    def get_phone_info(self, phone_number):
        """
        Get Phone Info  Such As Telecom Circle, Name, Number Type, DND/Non-DND Status By Phone Number

        Parameters:
        phone_number: str
            Pass A Phone Number
        """

        url = f"https://{self.api}:{self.secret}{self.domain}/v1/Accounts/{self.sid}/Numbers/{phone_number}.json"
        return requests.get(url).json()
