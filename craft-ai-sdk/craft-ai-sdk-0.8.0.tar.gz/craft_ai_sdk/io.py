class Input:
    def __init__(
        self, name, data_type, description=None, is_required=None, default_value=None
    ):
        self.name = name
        self.data_type = data_type
        self.description = description
        self.is_required = is_required
        self.default_value = default_value

    def to_dict(self):
        dict = {
            "name": self.name,
            "data_type": self.data_type,
        }
        if self.description is not None:
            dict["description"] = self.description
        if self.is_required is not None:
            dict["is_required"] = self.is_required
        if self.default_value is not None:
            dict["default_value"] = self.default_value
        return dict


class Output:
    def __init__(self, name, data_type, description):
        self.name = name
        self.data_type = data_type
        self.description = description

    def to_dict(self):
        dict = {
            "name": self.name,
            "data_type": self.data_type,
        }
        if self.description is not None:
            dict["description"] = self.description
        return dict
