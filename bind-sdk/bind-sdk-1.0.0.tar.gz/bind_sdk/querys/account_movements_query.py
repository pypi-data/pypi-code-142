class AccountMovementsQuery:
    def __init__(
        self,
        obp_sort_direction=None,
        obp_limit=None,
        obp_offset=None,
        obp_from_date=None,
        obp_to_date=None,
        obp_categories=None,
    ):
        self.obp_sort_direction = obp_sort_direction
        self.obp_limit = obp_limit
        self.obp_offse = obp_offset
        self.obp_from_date = obp_from_date
        self.obp_to_date = obp_to_date
        self.obp_categories = obp_categories

    def get_query(self) -> dict:
        query = {}
        if self.obp_sort_direction:
            query["obp_sort_direction"] = self.obp_sort_direction
        if self.obp_limit:
            query["obp_limit"] = self.obp_limit
        if self.obp_offse:
            query["obp_offse"] = self.obp_offse
        if self.obp_from_date:
            query["obp_from_date"] = self.obp_from_date
        if self.obp_to_date:
            query["obp_to_date"] = self.obp_to_date
        if self.obp_categories:
            query["obp_categories"] = self.obp_categories
        return None if query == {} else query
