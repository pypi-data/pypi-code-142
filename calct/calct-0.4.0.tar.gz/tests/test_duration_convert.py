#   calct: Easily do calculations on hours and minutes using the command line
#   Copyright (C) 2022  Philippe Warren
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

from calct.duration import Duration, timedelta


def test_duration_to_timedelta():
    duration = Duration(minutes=2)
    time_delta = duration.as_timedelta
    assert time_delta == timedelta(minutes=2)
    assert isinstance(time_delta, timedelta)


def test_duration_from_timedelta():
    time_delta = timedelta(hours=3, minutes=32)
    duration = Duration.from_timedelta(time_delta)
    assert duration == Duration(hours=3, minutes=32)
    assert isinstance(duration, Duration)


def test_duration_get_hours():
    assert Duration(hours=2, minutes=60).hours == 3


def test_duration_get_hours_negative():
    assert Duration(hours=-1, minutes=-30).hours == -1


def test_duration_set_hours():
    duration = Duration()
    assert duration.hours == 0
    duration.hours = 4
    assert duration == Duration(hours=4)


def test_duration_set_hours_negative():
    duration = Duration()
    assert duration.hours == 0
    duration.hours = -4
    assert duration == Duration(hours=-4)


def test_duration_get_minutes():
    assert Duration(hours=1, minutes=30).minutes == 30


def test_duration_get_minutes_negative():
    assert Duration(hours=-1, minutes=-30).minutes == -30


def test_duration_set_minutes():
    duration = Duration()
    assert duration.minutes == 0
    duration.minutes = 4
    assert duration == Duration(minutes=4)


def test_duration_set_minutes_negative():
    duration = Duration()
    assert duration.minutes == 0
    duration.minutes = -4
    assert duration == Duration(minutes=-4)


def test_duration_set_minutes_conserve_hours():
    duration = Duration(hours=3)
    assert duration.minutes == 0
    assert duration.hours == 3
    duration.minutes = 4
    assert duration == Duration(hours=3, minutes=4)


def test_duration_set_minutes_negative_conserve_hours():
    duration = Duration(hours=3)
    assert duration.minutes == 0
    assert duration.hours == 3
    duration.minutes = -4
    assert duration == Duration(hours=3, minutes=-4)


def test_duration_set_minutes_conserve_hours_negative():
    duration = Duration(hours=-3)
    assert duration.minutes == 0
    assert duration.hours == -3
    duration.minutes = 4
    assert duration == Duration(hours=-3, minutes=4)


def test_duration_set_minutes_negative_conserve_hours_negative():
    duration = Duration(hours=-3)
    assert duration.minutes == 0
    assert duration.hours == -3
    duration.minutes = -4
    assert duration == Duration(hours=-3, minutes=-4)


def test_duration_get_total_minutes():
    assert Duration(hours=1, minutes=30).total_minutes == 90


def test_duration_get_total_minutes_negative():
    assert Duration(hours=-1, minutes=-30).total_minutes == -90
