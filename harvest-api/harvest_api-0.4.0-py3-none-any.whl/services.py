import calendar
from datetime import date
from datetime import datetime
from datetime import timedelta
from harvest.endpoints import (
    TimeEntryEndpoint,
    ProjectsEndpoint,
    TasksEndpoint,
    UsersMeEndpoint,
    UsersProjectAssignmentsEndpoint,
    UsersMeProjectAssignmentsEndpoint,
    )


class BaseService(object):
    def __init__(self, credential):
        self.credential = credential


class PaginatedService(BaseService):

    def get_endpoint(self):
        return self.endpoint_class(credential=self.credential)

    def get_entries(self):
        endpoint = self.get_endpoint()
        resp = endpoint.get()
        if resp.status_code != 200:
            resp.raise_for_status()
        total_pages = resp.json()["total_pages"]
        for i in range(1, total_pages + 1):
            resp = endpoint.get(page=i)
            if resp. status_code != 200:
                resp.raise_for_status()
            for entry in resp.json()[self.endpoint_data_key]:
                yield entry


class TimeRangeBaseService(BaseService):
    def __init__(self, credential):
        self.today = datetime.now()
        super(TimeRangeBaseService, self).__init__(credential)

    def get_date_range(self):
        raise NotImplementedError

    def all(self, page=1):
        date_range = self.get_date_range()
        api = TimeEntryEndpoint(credential=self.credential)
        resp = api.get(params={"from": date_range[0], "to": date_range[1]})
        return resp.json()

    def blanks(self):
        resp = self.all()
        empty_time_entries = []
        for entry in resp["time_entries"]:
            if not entry["notes"]:
                empty_time_entries.append(entry)
        resp["time_entries"] = empty_time_entries
        return resp


class SingleDayTimeEntries(TimeRangeBaseService):
    def __init__(self, credential, date):
        self.date = date
        super(SingleDayTimeEntries, self).__init__(credential)

    def get_date_range(self):
        return (self.date, self.date)


class TodayTimeEntries(TimeRangeBaseService):
    def get_date_range(self):
        self.date_from = self.today.strftime("%Y-%m-%d")
        self.date_to = self.today.strftime("%Y-%m-%d")
        return (self.date_from, self.date_to)


class MonthTimeEntries(TimeRangeBaseService):
    def set_month(self, year, month):
        self.year = year
        self.month = month
        self.last_day = calendar.monthrange(year, month)[1]

    def get_date_range(self):
        self.date_from = date(self.year, self.month, 1)
        self.date_to = date(self.year, self.month, self.last_day)
        return (
            self.date_from.strftime("%Y-%m-%d"),
            self.date_to.strftime("%Y-%m-%d"),
            )


class CurrentWeekTimeEntries(TimeRangeBaseService):
    def get_date_range(self):
        self.date_from = self.today - timedelta(days=self.today.weekday())
        self.date_to = self.date_from + timedelta(days=6)
        self.date_from = self.date_from.strftime("%Y-%m-%d")
        self.date_to = self.date_to.strftime("%Y-%m-%d")
        return (self.date_from, self.date_to)


class PreviousWeekTimeEntries(TimeRangeBaseService):
    def get_date_range(self):
        self.today = self.today - timedelta(days=(6 - self.today.weekday()))
        self.date_from = self.today - timedelta(days=self.today.weekday())
        self.date_to = self.date_from + timedelta(days=6)
        return (
            self.date_from.strftime("%Y-%m-%d"),
            self.date_to.strftime("%Y-%m-%d"),
            )


class WeekTimeEntriesService(TimeRangeBaseService):

    def __init__(self, credential, date):
        """
        Params:
            credential (harvest.credentials.OAuth2Credential):
            date (datetime.datetime):
        """
        super(WeekTimeEntriesService, self).__init__(credential)
        self.date = date

    def get_date_range(self):
        start = self.date + timedelta(0 - self.date.weekday())
        end = self.date + timedelta(6 - self.date.weekday())
        ret = (
            start.date(),
            end.date(),
        )
        return ret


class AllProjects(BaseService):
    endpoint_class = ProjectsEndpoint
    endpoint_data_key = "projects"


class AllTasks(BaseService):
    endpoint_class = TasksEndpoint
    endpoint_data_key = "tasks"


class CurrentUser(BaseService):
    def get(self):
        resp = UsersMeEndpoint(credential=self.credential).get()
        return resp.json()


class UsersProjectAssignmentsService(BaseService):
    endpoint_class = UsersProjectAssignmentsEndpoint
    endpoint_data_key = "project_assignments"


class MyProjectAssignmentsService(PaginatedService):
    endpoint_class = UsersMeProjectAssignmentsEndpoint
    endpoint_data_key = "project_assignments"

