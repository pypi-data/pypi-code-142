from datetime import timedelta


class ForUser:
    model = "user"


class ForIp:
    model = "ip"


class Time:
    def __init__(self, day: int = None, hour: int = None, minute: int = None, second: int = None):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def time(self):
        time = timedelta()
        if self.day:
            time += timedelta(days=self.day)
        if self.hour:
            time += timedelta(hours=self.hour)
        if self.minute:
            time += timedelta(minutes=self.minute)
        if self.second:
            time += timedelta(seconds=self.second)
        return time

    def check(self):
        if not self.day and not self.hour and not self.minute and not self.second:
            raise ValueError(
                "at least one of day, hour, minute, second must be greater than 0")
        if self.day and self.day <= 0:
            raise ValueError("day must be greater than 0")
        if self.hour and self.hour <= 0:
            raise ValueError("hour must be greater than 0")
        if self.minute and self.minute <= 0:
            raise ValueError("minute must be greater than 0")
        if self.second and self.second <= 0:
            raise ValueError("second must be greater than 0")


class RateTime(Time):

    def __init__(self, count: int, day: int = None, hour: int = None, minute: int = None, second: int = None):
        self.count = count
        super().__init__(day, hour, minute, second)

    def time(self):
        print(super().time())
        return super().time()

    def check(self):
        if self.count <= 0:
            raise ValueError("count must be greater than 0")
        super().check()


class Block(Time):

    def __init__(self, active: bool = None, day: int = None, hour: int = None, minute: int = None, second: int = None):
        self.active = active
        super().__init__(day, hour, minute, second)

    def time(self):
        print("asd", super().time())
        return super().time()

    def check(self):
        if self.active:
            super().check()

