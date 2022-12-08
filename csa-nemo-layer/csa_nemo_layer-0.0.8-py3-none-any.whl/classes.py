class Finding:
    def __init__(self, **kwargs) -> None:
        """
        Class for CSA Nemo project's findings
        :params:
        id: string
        target: string
        controlId: string
        Reason: list of strings
        Identifier: string
        IdentifierType: string
        Region: (Optional) string
        """
        self.id = kwargs.get('id')
        self.target = kwargs.get('target', '')
        self.controlId = kwargs.get('controlId', '')
        reason = kwargs.get('reason')
        self.Reason = []
        if reason:
            self.Reason.append(str(reason))
        self.Identifier = kwargs.get('identifier', '')
        self.IdentifierType = kwargs.get('identifier_type', '')
        if kwargs.get('region'):
            self.Region = kwargs['region']

    def json(self) -> dict:
        json_obj = self.__dict__
        json_obj['Reason'] = '\n'.join(self.Reason)
        return json_obj

# TO-DO: Add classes for targets
