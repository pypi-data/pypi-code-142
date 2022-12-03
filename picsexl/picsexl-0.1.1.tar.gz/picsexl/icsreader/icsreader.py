import typing
from datetime import date, datetime, timezone

import pytz
from dateutil.rrule import rruleset, rrulestr
from icalendar import Calendar

from picsexl.icsreader.exceptions import ICSReaderException

TZ_EUROPE_MOSCOW = "Europe/Moscow"


class ICSReader:
    def __init__(
        self, ics_string: str, mail_to: str, start_date: datetime, end_date: datetime
    ):
        self.__ics_string: str = ics_string
        self.__mail_to: str = mail_to
        self.__start_date: datetime = start_date
        self.__end_date: datetime = end_date
        self.__events: typing.List = []
        self.__cal = filter(
            lambda c: c.name == "VEVENT", Calendar.from_ical(self.__ics_string).walk()
        )

    def get_events_from_ics(self):
        try:
            return self.__get_events_from_ics()
        except Exception as exc:
            raise ICSReaderException(exc=exc)

    def __get_events_from_ics(self):
        for vevent in self.__cal:
            summary = str(vevent.get("summary"))
            raw_star_dt = vevent.get("dtstart")
            raw_end_dt = vevent.get("dtend")
            if raw_star_dt:
                raw_star_dt = raw_star_dt.dt
            if raw_end_dt:
                raw_end_dt = raw_end_dt.dt
            organizer = vevent.get("organizer")
            has_organizer = organizer and not isinstance(organizer, str)

            attendee = vevent.get("attendee")
            has_attendee = attendee and not isinstance(attendee, str)

            your_status = ""
            declined_by_organizer = False

            if has_attendee:
                for a in attendee:
                    if (
                        has_organizer
                        and a.params.get("cn") == organizer.params.get("cn")
                        and a.params.get("partstat") == "DECLINED"
                    ):
                        declined_by_organizer = True
                    if a.params.get("cn") == self.__mail_to:
                        your_status = a.params.get("partstat")

            end_dt = self.__end_date
            all_day = False
            if not isinstance(raw_star_dt, datetime):
                all_day = True
                start_dt = self.__date_to_datetime(raw_star_dt)
                if raw_end_dt:
                    end_dt = self.__date_to_datetime(raw_end_dt)
            else:
                start_dt = raw_star_dt
                end_dt = raw_end_dt or end_dt

            rrule = vevent.get("rrule")
            ex_date = vevent.get("exdate")
            if rrule:
                until = rrule.get("until")
                if until and self.__exclude_by_rrule_until(until[0], self.__start_date):
                    continue
                if until:
                    rrule.get("until")[0] = self.__tz_x(until[0])
                reoccur = rrule.to_ical().decode("utf-8")
                for rd in self.__get_recurrent_datetimes(
                    reoccur,
                    self.__tz_x(start_dt),
                    self.__tz_x(self.__end_date),
                    ex_date,
                ):
                    end_dt_ = rd + (end_dt - start_dt) if end_dt else None
                    new_e = {
                        "start_date": rd.date(),
                        "summary": summary,
                        "start_time": rd.time(),
                        "end_time": end_dt_.time() if end_dt_ else None,
                        "your_status": your_status,
                        "all_day": all_day,
                        "end_date": end_dt_.date() if end_dt_ else None,
                        "declined_by_organizer": declined_by_organizer,
                        "startdt": rd,
                        "enddt": end_dt_,
                    }
                    self.__append_event(
                        ne=new_e, start=self.__start_date, end=self.__end_date
                    )
            else:
                start_dt_ = (
                    start_dt
                    if all_day
                    else start_dt.astimezone(pytz.timezone(TZ_EUROPE_MOSCOW))
                )
                end_dt_ = (
                    end_dt
                    if all_day
                    else end_dt.astimezone(pytz.timezone(TZ_EUROPE_MOSCOW))
                )
                self.__append_event(
                    {
                        "start_date": start_dt_.date(),
                        "summary": summary,
                        "start_time": start_dt_.time(),
                        "end_time": end_dt_.time(),
                        "your_status": your_status,
                        "all_day": all_day,
                        "end_date": end_dt_.date(),
                        "declined_by_organizer": declined_by_organizer,
                        "startdt": start_dt_,
                        "enddt": end_dt_,
                    },
                    start=self.__start_date,
                    end=self.__end_date,
                )
        self.__events.sort(key=lambda event: event["startdt"])
        self.__setup_none_tzinfo()
        return self.__events

    def __append_event(self, ne, start, end) -> None:
        if ne["startdt"] > end:
            return
        if ne["enddt"]:
            if ne["enddt"] < start:
                return

        self.__events.append(ne)

    def __exclude_by_rrule_until(self, until, start) -> bool:
        if isinstance(until, date):
            until = datetime(
                until.year, until.month, until.day, 23, 59, 59, tzinfo=timezone.utc
            )
        if isinstance(until, datetime):
            if start > until:
                return True
        return False

    def __setup_none_tzinfo(self):
        for event in self.__events:
            for ek, ev in event.items():
                if isinstance(ev, datetime):
                    event[ek] = self.__tz_x(ev)

    def __tz_x(self, dt, tzx=None) -> datetime:
        if isinstance(dt, datetime):
            return datetime(
                dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, tzinfo=tzx
            )
        elif isinstance(dt, date):
            return datetime(dt.year, dt.month, dt.day, 0, 0, 0, tzinfo=tzx)

    def __get_recurrent_datetimes(
        self, recur_rule, start: datetime, end: datetime, exclusions
    ) -> typing.List[datetime]:
        rules = rruleset()
        first_rule = rrulestr(recur_rule, dtstart=start)
        rules.rrule(first_rule)
        if not isinstance(exclusions, list):
            exclusions = [exclusions]

        for xdt in exclusions:
            try:
                rules.exdate(xdt.dt)
            except AttributeError:
                pass

        dates = []

        for dl in rules.between(start, end):
            dates.append(self.__tz_x(dl, tzx=timezone.utc))
        return dates

    @staticmethod
    def __date_to_datetime(dt):
        return datetime(dt.year, dt.month, dt.day, tzinfo=timezone.utc)
