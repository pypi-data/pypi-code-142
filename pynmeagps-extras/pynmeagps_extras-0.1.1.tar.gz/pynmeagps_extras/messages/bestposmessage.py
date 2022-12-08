class BESTPOSMessage:
    """Best position message."""

    def __init__(self, data: str):
        self.fields = data.replace(";", ",").split(",")
        if self.fields[0] != "#BESTPOSA":
            raise ValueError("Invalid data type")
        if len(self.fields) != 31:
            raise ValueError("Invalid data length")

    @property
    def log_header(self) -> str:
        return self.fields[0]

    @property
    def serial_port(self) -> str:
        return self.fields[1]

    @property
    def message_number(self) -> str:
        return self.fields[2]

    @property
    def idle_time(self) -> str:
        return self.fields[3]

    @property
    def time_status(self) -> str:
        return self.fields[4]

    @property
    def number_of_gps_weeks(self) -> str:
        return self.fields[5]

    @property
    def number_of_seconds(self) -> str:
        return self.fields[6]

    @property
    def receiver_status(self) -> str:
        return self.fields[7]

    @property
    def reserved_log_header(self) -> str:
        return self.fields[8]

    @property
    def receiver_software_version(self) -> str:
        return self.fields[9]

    @property
    def solution_status(self) -> str:
        return self.fields[10]

    @property
    def position_type(self) -> str:
        return self.fields[11]

    @property
    def latitude(self) -> str:
        return self.fields[12]

    @property
    def longitude(self) -> str:
        return self.fields[13]

    @property
    def height(self) -> str:
        return self.fields[14]

    @property
    def undulation(self) -> str:
        return self.fields[15]

    @property
    def datum(self) -> str:
        return self.fields[16]

    @property
    def latitude_standard_deviation(self) -> str:
        return self.fields[17]

    @property
    def longitude_standard_deviation(self) -> str:
        return self.fields[18]

    @property
    def height_standard_deviation(self) -> str:
        return self.fields[19]

    @property
    def base_station_id(self) -> str:
        return self.fields[20]

    @property
    def differential_age(self) -> str:
        return self.fields[21]

    @property
    def solution_age(self) -> str:
        return self.fields[22]

    @property
    def satellites_tracked(self) -> str:
        return self.fields[23]

    @property
    def satellites_used_in_solution(self) -> str:
        return self.fields[24]

    @property
    def satellites_with_LEB_signals_used_in_solution(self) -> str:
        return self.fields[25]

    @property
    def satellites_with_multifrequency_signals_used_in_solution(self) -> str:
        return self.fields[26]

    @property
    def reserved(self) -> str:
        return self.fields[27]

    @property
    def extension_solution_status(self) -> str:
        return self.fields[28]

    @property
    def galileo_and_beidou_signals_used_mask(self) -> str:
        return self.fields[29]

    @property
    def gps_and_glonass_signals_used_mask(self) -> str:
        return self.fields[30][:2]

    @property
    def checksum(self) -> str:
        return self.fields[30][3:]

    @log_header.setter
    def log_header(self, value: str):
        self.fields[0] = value

    @serial_port.setter
    def serial_port(self, value: str):
        self.fields[1] = value

    @message_number.setter
    def message_number(self, value: str):
        self.fields[2] = value

    @idle_time.setter
    def idle_time(self, value: str):
        self.fields[3] = value

    @time_status.setter
    def time_status(self, value: str):
        self.fields[4] = value

    @number_of_gps_weeks.setter
    def number_of_gps_weeks(self, value: str):
        self.fields[5] = value

    @number_of_seconds.setter
    def number_of_seconds(self, value: str):
        self.fields[6] = value

    @receiver_status.setter
    def receiver_status(self, value: str):
        self.fields[7] = value

    @reserved_log_header.setter
    def reserved_log_header(self, value: str):
        self.fields[8] = value

    @receiver_software_version.setter
    def receiver_software_version(self, value: str):
        self.fields[9] = value

    @solution_status.setter
    def solution_status(self, value: str):
        self.fields[10] = value

    @position_type.setter
    def position_type(self, value: str):
        self.fields[11] = value

    @latitude.setter
    def latitude(self, value: str):
        self.fields[12] = value

    @longitude.setter
    def longitude(self, value: str):
        self.fields[13] = value

    @height.setter
    def height(self, value: str):
        self.fields[14] = value

    @undulation.setter
    def undulation(self, value: str):
        self.fields[15] = value

    @datum.setter
    def datum(self, value: str):
        self.fields[16] = value

    @latitude_standard_deviation.setter
    def latitude_standard_deviation(self, value: str):
        self.fields[17] = value

    @longitude_standard_deviation.setter
    def longitude_standard_deviation(self, value: str):
        self.fields[18] = value

    @height_standard_deviation.setter
    def height_standard_deviation(self, value: str):
        self.fields[19] = value

    @base_station_id.setter
    def base_station_id(self, value: str):
        self.fields[20] = value

    @differential_age.setter
    def differential_age(self, value: str):
        self.fields[21] = value

    @solution_age.setter
    def solution_age(self, value: str):
        self.fields[22] = value

    @satellites_tracked.setter
    def satellites_tracked(self, value: str):
        self.fields[23] = value

    @satellites_used_in_solution.setter
    def satellites_used_in_solution(self, value: str):
        self.fields[24] = value

    @satellites_with_LEB_signals_used_in_solution.setter
    def satellites_with_LEB_signals_used_in_solution(self, value: str):
        self.fields[25] = value

    @satellites_with_multifrequency_signals_used_in_solution.setter
    def satellites_with_multifrequency_signals_used_in_solution(self, value: str):
        self.fields[26] = value

    @reserved.setter
    def reserved(self, value: str):
        self.fields[27] = value

    @extension_solution_status.setter
    def extension_solution_status(self, value: str):
        self.fields[28] = value

    @galileo_and_beidou_signals_used_mask.setter
    def galileo_and_beidou_signals_used_mask(self, value: str):
        self.fields[29] = value

    @gps_and_glonass_signals_used_mask.setter
    def gps_and_glonass_signals_used_mask(self, value: str):
        self.fields[30][:2] = value

    @checksum.setter
    def checksum(self, value: str):
        self.fields[30][3:] = value

    def serialize(self) -> bytes:
        """Serialize the object into a byte string."""

        field_counter = 1
        data = ""
        for field in self.fields:
            if field_counter == 10:
                data += field + ";"
            else:
                data += field + ","
            field_counter += 1
        data = data[:-1] + "\r\n"
        return data.encode("utf-8")
