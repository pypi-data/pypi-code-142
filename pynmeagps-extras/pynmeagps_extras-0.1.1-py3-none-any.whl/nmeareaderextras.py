from pynmeagps_extras.messages.bestposmessage import BESTPOSMessage
from pynmeagps_extras.messages.headingmessage import HEADINGMessage


class NMEAReaderExtras:
    @staticmethod
    def parse(data: str) -> BESTPOSMessage or HEADINGMessage:
        """Summary: Parse a string of NMEA data and return an object of the appropriate type.

        Args:
            data (str): A string of NMEA data.

        Raises:
            ValueError: If the data is not valid NMEA data.

        Returns:
            BESTPOSAMessage or HEADINGAMessage: An object of the appropriate type.
        """

        if data.startswith("#BESTPOSA"):
            return BESTPOSMessage(data)
        elif data.startswith("#HEADINGA"):
            return HEADINGMessage(data)
        else:
            raise ValueError("Invalid data type")
