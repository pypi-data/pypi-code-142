class HEADINGMessage:
    """Heading message."""

    def __init__(self, data: str):
        self.fields = data.replace(";", ",").split(",")
        if self.fields[0] != "#HEADINGA":
            raise ValueError("Invalid data type")
        if len(self.fields) != 27:
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
    def heading_status(self) -> str:
        return self.fields[11]

    @property
    def heading_baseline_length(self) -> str:
        return self.fields[12]

    @property
    def heading_in_degrees(self) -> str:
        return self.fields[13]

    @property
    def pitch(self) -> str:
        return self.fields[14]

    @property
    def reserved_first(self) -> str:
        return self.fields[15]

    @property
    def heading_standard_deviation(self) -> str:
        return self.fields[16]

    @property
    def pitch_standard_deviation(self) -> str:
        return self.fields[17]

    @property
    def station_id(self) -> str:
        return self.fields[18]

    @property
    def number_of_satellites_tracked(self) -> str:
        return self.fields[19]

    @property
    def number_of_sattelites_used_in_heading_solution(self) -> str:
        return self.fields[20]

    @property
    def number_of_satellites_above_the_elevation_mask_angle(self) -> str:
        return self.fields[21]

    @property
    def number_of_satellites_above_the_mask_angle_with_l2(self) -> str:
        return self.fields[22]

    @property
    def reserved_second(self) -> str:
        return self.fields[23]

    @property
    def extended_solution_status(self) -> str:
        return self.fields[24]

    @property
    def reserved_third(self) -> str:
        return self.fields[25]

    @property
    def signals_used_in_the_solution(self) -> str:
        return self.fields[26][:2]

    @property
    def checksum(self) -> str:
        return self.fields[26][3:]

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

    @heading_status.setter
    def heading_status(self, value: str):
        self.fields[11] = value

    @heading_baseline_length.setter
    def heading_baseline_length(self, value: str):
        self.fields[12] = value

    @heading_in_degrees.setter
    def heading_in_degrees(self, value: str):
        self.fields[13] = value

    @pitch.setter
    def pitch(self, value: str):
        self.fields[14] = value

    @reserved_first.setter
    def reserved_first(self, value: str):
        self.fields[15] = value

    @heading_standard_deviation.setter
    def heading_standard_deviation(self, value: str):
        self.fields[16] = value

    @pitch_standard_deviation.setter
    def pitch_standard_deviation(self, value: str):
        self.fields[17] = value

    @station_id.setter
    def station_id(self, value: str):
        self.fields[18] = value

    @number_of_satellites_tracked.setter
    def number_of_satellites_tracked(self, value: str):
        self.fields[19] = value

    @number_of_sattelites_used_in_heading_solution.setter
    def number_of_sattelites_used_in_heading_solution(self, value: str):
        self.fields[20] = value

    @number_of_satellites_above_the_elevation_mask_angle.setter
    def number_of_satellites_above_the_elevation_mask_angle(self, value: str):
        self.fields[21] = value

    @number_of_satellites_above_the_mask_angle_with_l2.setter
    def number_of_satellites_above_the_mask_angle_with_l2(self, value: str):
        self.fields[22] = value

    @reserved_second.setter
    def reserved_second(self, value: str):
        self.fields[23] = value

    @extended_solution_status.setter
    def extended_solution_status(self, value: str):
        self.fields[24] = value

    @reserved_third.setter
    def reserved_third(self, value: str):
        self.fields[25] = value

    @signals_used_in_the_solution.setter
    def signals_used_in_the_solution(self, value: str):
        self.fields[26][:2] = value

    @checksum.setter
    def checksum(self, value: str):
        self.fields[26][3:] = value

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
