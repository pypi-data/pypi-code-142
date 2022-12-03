# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import base64
import calendar
import codecs
import collections
import datetime
import json
import locale
import math
import pickle as pickle
import re
import time
import uuid
import zlib
from datetime import tzinfo, timedelta

import pytz
import tzlocal
import yaml
from sqlalchemy.engine.row import RowProxy

"""
    builtin-types utility.
"""

RE_FLAG_UNICODE = re.RegexFlag.UNICODE
RE_FLAG_IGNORECASE = re.RegexFlag.IGNORECASE
RE_FLAG_DOTALL = re.RegexFlag.DOTALL
RE_FLAG_DOTALL = re.RegexFlag.UNICODE


def is_none(value):
    """
    Check if value is None
    :param value:
    :return:
    """
    return value is None


def is_str(value):
    """
        Check if value is string type or not
    """
    if isinstance(value, str):
        return True
    return False


def _str_strips(direction, text, remove):
    if isinstance(remove, (list, tuple)):
        for subr in remove:
            text = _str_strips(direction, text, subr)
        return text

    if direction == 'l':
        if text.startswith(remove):
            return text[len(remove):]
    elif direction == 'r':
        if text.endswith(remove):
            return text[:-len(remove)]
    else:
        raise ValueError("Direction needs to be r or l.")
    return text


def str_rstrips(text, remove):
    """
    removes the string `remove` from the right of `text`
        >>> rstrips("foobar", "bar")
        'foo'
    """
    return _str_strips('r', text, remove)


def str_lstrips(text, remove):
    """
    removes the string `remove` from the left of `text`
        >>> lstrips("foobar", "foo")
        'bar'
        >>> lstrips('http://foo.org/', ['http://', 'https://'])
        'foo.org/'
        >>> lstrips('FOOBARBAZ', ['FOO', 'BAR'])
        'BAZ'
        >>> lstrips('FOOBARBAZ', ['BAR', 'FOO'])
        'BARBAZ'
    """
    return _str_strips('l', text, remove)


def str_strips(text, remove):
    """
    removes the string `remove` from the both sides of `text`
        >>> str_strips("foobarfoo", "foo")
        'bar'
    """
    return str_rstrips(str_lstrips(text, remove), remove)


def str_numify(string):
    """
    Removes all non-digit characters from `string`.
    
        >>> numify('800-555-1212')
        '8005551212'
        >>> numify('800.555.1212')
        '8005551212'
    
    """
    return ''.join([c for c in str(string) if c.isdigit()])


def str_denumify(string, pattern):
    """
    Formats `string` according to `pattern`, where the letter X gets replaced
    by characters from `string`.
    
        >>> str_denumify("8005551212", "(XXX) XXX-XXXX")
        '(800) 555-1212'
    
    """
    out = []
    for c in pattern:
        if c == "X":
            out.append(string[0])
            string = string[1:]
        else:
            out.append(c)
    return ''.join(out)


def str_commify(n):
    """
    Add commas to an integer `n`.

        >>> commify(1)
        '1'
        >>> commify(123)
        '123'
        >>> commify(1234)
        '1,234'
        >>> commify(1234567890)
        '1,234,567,890'
        >>> commify(123.0)
        '123.0'
        >>> commify(1234.5)
        '1,234.5'
        >>> commify(1234.56789)
        '1,234.56789'
        >>> commify('%.2f' % 1234.5)
        '1,234.50'
        >>> commify(None)
        >>>

    """
    if n is None: return None
    n = str(n)
    if '.' in n:
        dollars, cents = n.split('.')
    else:
        dollars, cents = n, None

    r = []
    for i, c in enumerate(str(dollars)[::-1]):
        if i and (not (i % 3)):
            r.insert(0, ',')
        r.insert(0, c)
    out = ''.join(r)
    if cents:
        out += '.' + cents
    return out


def str_dateify(datestring):
    """
    Formats a numified `datestring` properly.
    """
    return str_denumify(datestring, "XXXX-XX-XX XX:XX:XX")


def str_lower_first(value):
    """
        Convert the first alphabit to lowcase and keep the others unchange.
    """
    return value[0:1].lower() + value[1:]


def str_upper_first(value):
    """
    Convert the first alphabit to uppercase and keep the others unchange.
    """
    return value[0:1].upper() + value[1:]


def str_to_bool(value, default=False):
    if str_is_blank(value) or not str_is_bool(value):
        return default
    value = str(value)
    if value.lower() in ('true', 'yes', '1', 'y'):
        return True
    else:
        return False


def str_to_datetime(value, fmt=None, default=None):
    fmt = tz_datetime_format() if fmt is None else fmt
    if str_is_blank(value) or not str_is_datetime(value, fmt=fmt):
        return default
    else:
        value = str(value)
        dt = datetime.datetime.strptime(value, fmt)
        dt = dt.replace(tzinfo=tz_utc())
        return dt


def str_to_int(value, default=None):
    if str_is_blank(value) or not str_is_int(value):
        return default
    else:
        value = str(value)
        return int(value)


def str_to_float(value, default=None):
    if str_is_blank(value) or (not str_is_int(value) and not str_is_float(value)):
        return default
    else:
        value = str(value)
        return float(value)


def str_to_dict(value, default=None):
    """
    Convert key value string to dict
    :param str value:  key value string, such as  a:b,c:d,e:f
    :param dict default:
    :return dict: such as {'a': 'b', 'c': 1}
    """
    if str_is_blank(value):
        return default
    d = {}
    values = value.split(',')
    for val in values:
        key, v = val.split(":")
        d[key] = v
    return d


def yaml_to_object(yaml_str, clazz=None, loaded_keys=None):
    """load yaml string to object of clazz."""
    obj = ValueObj() if clazz is None else clazz
    items = yaml.safe_load(yaml_str)
    for key, value in items.items():
        if loaded_keys is None or key in loaded_keys:
            setattr(obj, key, value)
    return obj


def obj_to_yaml(obj):
    """Dump obj to yaml."""
    if isinstance(obj, ValueObj):
        obj = obj.to_dict()
    return yaml.safe_dump(obj)


def kilostr_to_int(text, times=1):
    """
        Return the int value of the kilo float string.
        @param str text: the string to be converted
        @param int times: how many times to be multiplied by
    """
    locale.setlocale(locale.LC_NUMERIC, 'English_US')
    to = locale.atof(text)
    return int(to * times)


def kilostr_to_float(text, times=1):
    """
        Return the float value of the kilo float string.
        @param str text: the string to be converted
        @param int times: how many times to be multiplied by
    """
    locale.setlocale(locale.LC_NUMERIC, 'English_US')
    to = locale.atof(text)
    return float(to * times)


def obj_to_str(value, default=None, fmt=None):
    if value is None:
        return default
    if type(value) == list or type(value) == tuple:
        value = obj_to_json(value)
    elif type(value) == dict:
        value = obj_to_json(value)
    elif type(value) == datetime.datetime or type(value) == datetime.date:
        value = tz_datetime_to_str(value, fmt)
    else:
        value = str(value)
    return value


def obj_to_pickle(value):
    pickled = codecs.encode(pickle.dumps(value), "base64").decode()
    return pickled


def pickle_to_obj(value):
    unpickled = pickle.loads(codecs.decode(value.encode(), "base64"))
    return unpickled


def str_replce_html_entities(value):
    if str_is_blank(value):
        return value
    value = str(value)
    value = value.replace("<", "&lt;")
    value = value.replace(">", "&gt;")
    return value


def str_is_int(value):
    reg = re.compile(r"^[-]?\d+?$")
    if str_is_blank(value):
        return False
    else:
        try:
            value = str(value)
            result = reg.match(value)
            if result is not None:
                return True
            else:
                return False
        except:
            return False


def str_is_float(value):
    reg = re.compile("^[-]?\d+?\.\d+?$")
    if str_is_blank(value):
        return False
    else:
        try:
            value = str(value)
            result = reg.match(value)
            if result is not None:
                return True
            else:
                return False
        except:
            return False


def str_is_date(value, fmt=None):
    fmt = tz_date_format() if fmt is None else fmt
    try:
        time.strptime(value, fmt)
        return True
    except BaseException:
        return False


def str_is_datetime(value, fmt=None):
    fmt = tz_datetime_format() if fmt is None else fmt
    try:
        time.strptime(value, fmt)
        return True
    except:
        return False


def str_is_bool(value):
    if str_is_blank(value):
        return False
    value = str(value)
    if value.lower() in ('true', 'yes', '1'):
        return True
    elif value.lower() in ('false', 'no', '0'):
        return True
    else:
        return False


def str_is_blank(value):
    if value is None:
        return True
    else:
        if isinstance(value, str):
            value = str(value).strip()
            return len(value) == 0
        else:
            return False


def str_compress(value):
    """Compress string."""
    if str_is_blank(value):
        return value
    value = unicode_bytes(value)
    value = zlib.compress(value, zlib.Z_BEST_COMPRESSION)
    value = base64.urlsafe_b64encode(value)
    value = unicode_str(value)
    return value


def str_decompress(value):
    """Decompress string."""
    if str_is_blank(value):
        return value
    value = unicode_str(value)
    value = unicode_bytes(value)
    value = base64.urlsafe_b64decode(value)
    value = zlib.decompress(value)
    return unicode_str(value)


def str_camel_to_snake_case(value):
    """convert camel case string to snake case"""
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in value]).lstrip('_')


def str_snake_case_to_camel(value, capital=False):
    """convert snake case to camel case string"""
    temp = value.split('_')
    first = temp[0].capitalize() if capital else temp[0].lower()
    res = first + ''.join(x.title() for x in temp[1:])
    return str(res)


def int_nthstr(n):
    """
    Formats an ordinal.
    Doesn't handle negative numbers.

        >>> nthstr(1)
        '1st'
        >>> nthstr(0)
        '0th'
        >>> [nthstr(x) for x in [2, 3, 4, 5, 10, 11, 12, 13, 14, 15]]
        ['2nd', '3rd', '4th', '5th', '10th', '11th', '12th', '13th', '14th', '15th']
        >>> [nthstr(x) for x in [91, 92, 93, 94, 99, 100, 101, 102]]
        ['91st', '92nd', '93rd', '94th', '99th', '100th', '101st', '102nd']
        >>> [nthstr(x) for x in [111, 112, 113, 114, 115]]
        ['111th', '112th', '113th', '114th', '115th']

    """

    assert n >= 0
    if n % 100 in [11, 12, 13]: return '%sth' % n
    return {1: '%sst', 2: '%snd', 3: '%srd'}.get(n % 10, '%sth') % n


def tz_daysofmonth(year, month):
    return calendar.monthrange(year, month)[1]


def tz_timezone(tz=None):
    """
    Interprets an object as a timezone.
    :param tz str|tzinfo
    :rtype: tzinfo  return localzone if tzinfo is None
    """
    if tz is None:
        return tzlocal.get_localzone()
    elif isinstance(tz, str):
        return pytz.timezone(tz)
    if isinstance(tz, tzinfo):
        if not hasattr(tz, 'localize') or not hasattr(tz, 'normalize'):
            raise TypeError('Only timezones from the pytz library are supported')
        if tz.zone == 'local':
            raise ValueError(
                'Unable to determine the name of the local timezone -- you must explicitly '
                'specify the name of the local timezone. Please refrain from using timezones like '
                'EST to prevent problems with daylight saving time. Instead, use a locale based '
                'timezone name (such as Europe/Helsinki).')
        return tz
    if tz is not None:
        raise TypeError('Expected tzinfo, got %s instead' % tz.__class__.__name__)


def tz_localzone():
    return tz_timezone(tz=None)


def tz_utc():
    return pytz.utc


def tz_china():
    """
    :rtype tzinfo
    """
    return tz_timezone("Asia/Shanghai")


def tz_localnow(tz=None):
    tz = tz_timezone(tz)
    now = tz_utcnow()
    local = tz_utc_to_local(now, tz)
    return local


def tz_localtoday(tz=None):
    local = tz_localnow(tz=tz)
    return tz_datetime_to_date(local)


def tz_utcnow():
    utcnow = datetime.datetime.utcnow()
    utcnow = utcnow.replace(tzinfo=tz_utc())
    return utcnow


def tz_utctoday():
    now = tz_utcnow()
    return datetime.date(now.year, now.month, now.day)


def tz_local_to_utc(localdt):
    """
        if tzinfo is None of localdt, localzone is used for the conversion.
    """
    if localdt is None:
        return localdt
    localtz = localdt.tzinfo
    if localtz is None:
        localtz = tz_utc()
        localdt = localdt.replace(tzinfo=localtz)
    if localtz == tz_utc():
        return localdt
    time_struct = time.mktime(localdt.timetuple())
    utcdt = datetime.datetime.utcfromtimestamp(time_struct)
    utcdt = utcdt.replace(tzinfo=tz_utc())
    return utcdt


def tz_utc_to_local(utcdt, tz=None):
    """
        if tz is None, it is returned specified datetime with localzone.
    """
    if utcdt is None:
        return utcdt
    tz = tz_timezone(tz)
    if utcdt.tzinfo is None:
        utcdt = utcdt.replace(tzinfo=tz_utc())
    elif utcdt.tzinfo != tz_utc():
        raise ValueError("datetime is not in UTC timezone. - %s" % utcdt.tzinfo)
    utcdt = utcdt.replace(tzinfo=tz_utc())
    localdt = utcdt.astimezone(tz)
    localdt = localdt.replace(tzinfo=None)
    return tz.localize(localdt)


def tz_datetime_to_date(value):
    return datetime.date(value.year, value.month, value.day)


def tz_date_to_datetime(value):
    return datetime.datetime(value.year, value.month, value.day, 0, 0, 0)


def tz_datetime_to_timestamp(dt, tz=None):
    """
    :param datetime dt:
    :param timezone tz:
    """
    tz = tz_utc() if tz is None else tz
    dt.replace(tzinfo=tz)
    return dt.timestamp()


def tz_datetime_to_str(value, fmt=None):
    if fmt is None:
        fmt = tz_datetime_format()
    return value.strftime(fmt)


def tz_datetime_to_utc_timestamp(dt: datetime.datetime):
    """
    Converts a datetime instance to a timestamp.
    :type dt: datetime
    :rtype: float
    """
    return int(dt.timestamp() * 1000)


def tz_utc_timestamp_to_datetime(timestamp: int):
    """
    Converts the given ms timestamp (length=13) to a datetime instance.
    :type timestamp: float
    :rtype: datetime
    """
    return datetime.datetime.fromtimestamp(timestamp / 1000, tz_utc())


def tz_timedelta_seconds(delta: datetime.timedelta):
    """
    Converts the given timedelta to seconds.

    :type delta: timedelta
    :rtype: float
    """
    return delta.days * 24 * 60 * 60 + delta.seconds + delta.microseconds / 1000000.0


def tz_datetime_ceil(dt: datetime.datetime):
    """
    Rounds the given datetime object upwards.

    :type dt: datetime
    """
    if dt.microsecond > 0:
        return dt + timedelta(seconds=1, microseconds=-dt.microsecond)
    return dt


def tz_datetime_floor(dt: datetime.datetime):
    """
    Rounds the given datetime object downwards.

    :type dt: datetime
    """
    if dt.microsecond > 0:
        return dt + timedelta(seconds=0, microseconds=-dt.microsecond)
    else:
        return dt.isoformat()


def tz_datetime_format():
    """The datetime format with time zone."""
    return "%Y-%m-%dT%H:%M:%S%z"


def tz_date_format():
    """The date format with time zone."""
    return "%Y-%m-%d%z"


def obj_to_json(obj):
    return json.dumps(obj, ensure_ascii=False, cls=ExtJsonEncoder)


def json_to_object(jsonstr):
    if jsonstr is not None and jsonstr.strip() != '':
        return json.loads(jsonstr)
    else:
        return None


def list_group(seq, size):
    """
    Returns an iterator over a series of lists of length size from iterable.

        >>> list(group([1,2,3,4], 2))
        [[1, 2], [3, 4]]
        >>> list(group([1,2,3,4,5], 2))
        [[1, 2], [3, 4], [5]]
    """

    def take(seq, n):
        for i in range(n):
            yield seq.next()

    if not hasattr(seq, 'next'):
        seq = iter(seq)
    while True:
        x = list(take(seq, size))
        if x:
            yield x
        else:
            break


def list_uniq(seq, key=None):
    """
    Removes duplicate elements from a list while preserving the order of the rest.

        >>> uniq([9,0,2,1,0])
        [9, 0, 2, 1]

    The value of the optional `key` parameter should be a function that
    takes a single argument and returns a key to test the uniqueness.

        >>> uniq(["Foo", "foo", "bar"], key=lambda s: s.lower())
        ['Foo', 'bar']
    """
    key = key or (lambda x: x)
    seen = set()
    result = []
    for v in seq:
        k = key(v)
        if k in seen:
            continue
        seen.add(k)
        result.append(v)
    return result


def list_restack(stack, index=0):
    """Returns the element at index after moving it to the top of stack.

           >>> x = [1, 2, 3, 4]
           >>> list_restack(x)
           1
           >>> x
           [2, 3, 4, 1]
    """
    x = stack.pop(index)
    stack.append(x)
    return x


def list_get(lst, ind, default=None):
    """
    Returns `lst[ind]` if it exists, `default` otherwise.
    
        >>> listget(['a'], 0)
        'a'
        >>> listget(['a'], 1)
        >>> listget(['a'], 1, 'b')
        'b'
    """
    if len(lst) - 1 < ind:
        return default
    return lst[ind]


def list_len(lst):
    """Return length of list. Return 0 if lst is None."""
    return 0 if lst is None else len(lst)


def generator_next(g):
    """
        Return next elements in generator.
        :param g|generator:
        :rtype generator: return None if stopping iteration.
    """
    try:
        e = g.__next__()
        return e
    except StopIteration:
        return None


def generator_concat(generators):
    """
        Concat multiple generators to one generator
    """
    for g in generators:
        for r in g:
            yield r


def generator_to_list(generator, max_count=None):
    """
        Convert generator to list
        :param max_count|int: the maximum element count to be joined.
    """
    datas = []
    count = 0
    for r in generator:
        count += 1
        datas.append(r)
        if max_count is not None and count >= max_count:
            break
    return datas


def generator_append(a, b):
    """
        Append b generator to a.
    """
    for r in a:
        yield r
    for r in b:
        yield r


def generator_merge(g1, g2):
    """
        Merge two generators.
        :param g1,g2|generator: the elements in generator must be the dict  
    """
    while True:
        d1 = generator_next(g1)
        if d1 is None:
            return
        d2 = generator_next(g2)
        if d2 is not None:
            for k in d2:
                d1[k] = d2[k]
        yield d1


def generator_cross(g1, g2):
    """
        Multiple all elements in generator g1 and all the elements in generator g2 .eg.
        g1 = [{'a':1,'b':2}, {'a':3,'b':4}],g2 = [{'c':1,'d':2}, {'c':3,'d':4}],return 
        [{'a':1,'b':2,'c':1,'d':2},{'a':1,'b':2,'c':3,'d':4},{'a':3,'b':4,'c':1,'d':2},{'a':3,'b':4,'c':3,'d':4}]
        :param g1,g2|generator: the elements in generator must be the dict.        
    """
    l = list(g2)
    for r1 in g1:
        r1 = dict.copy(r1)
        for r2 in l:
            for key in r2:
                r1[key] = r2[key]
            yield dict.copy(r1)


def generator_mix(g1, g2):
    """
        Mix the elements in generator g1,g2. Pick one from g1 then pick the other from g2.  
        :param g1:generator:
        :param g2:generator:
    """
    while True:
        r1 = generator_next(g1)
        if r1 is not None:
            yield r1
        r2 = generator_next(g2)
        if r2 is not None:
            yield r2
        if r1 is None and r2 is None:
            return


def dict_merge(d1, d2, keys=None):
    """
        Merge items of d2 to d1. if keys is None, merge all keys in d2.
        :param d1:dict: the dict to be merged to.
        :param d2:dict: the dict to be merged from.
        :param keys:str,list: the keys to be merged.
    """
    if d2 is None:
        return d1
    if keys is None:
        for r in d2:
            d1[r] = d2[r]
    else:
        if type(keys) == str:
            keys = [keys]
        for r in keys:
            d1[r] = d2[r]
    return d1


def dict_reverse(mapping):
    """
    Returns a new dictionary with keys and values swapped.
    
        >>> dictreverse({1: 2, 3: 4})
        {2: 1, 4: 3}
    """
    return dict([(value, key) for (key, value) in mapping.iteritems()])


def dict_find(dictionary, element):
    """
    Returns a key whose value in `dictionary` is `element` 
    or, if none exists, None.
    
        >>> d = {1:2, 3:4}
        >>> dictfind(d, 4)
        3
        >>> dictfind(d, 5)
    """
    for (key, value) in dictionary.iteritems():
        if element is value:
            return key


def dict_findall(dictionary, element):
    """
    Returns the keys whose values in `dictionary` are `element`
    or, if none exists, [].
    
        >>> d = {1:4, 3:4}
        >>> dictfindall(d, 4)
        [1, 3]
        >>> dictfindall(d, 5)
        []
    """
    res = []
    for (key, value) in dictionary.iteritems():
        if element is value:
            res.append(key)
    return res


def dict_incr(dictionary, element):
    """
    Increments `element` in `dictionary`, 
    setting it to one if it doesn't exist.
    
        >>> d = {1:2, 3:4}
        >>> dictincr(d, 1)
        3
        >>> d[1]
        3
        >>> dictincr(d, 5)
        1
        >>> d[5]
        1
    """
    dictionary.setdefault(element, 0)
    dictionary[element] += 1
    return dictionary[element]


def dict_add(*dicts):
    """
    Returns a dictionary consisting of the keys in the argument dictionaries.
    If they share a key, the value from the last argument is used.
    
        >>> dictadd({1: 0, 2: 0}, {2: 1, 3: 1})
        {1: 0, 2: 1, 3: 1}
    """
    result = {}
    for dct in dicts:
        result.update(dct)
    return result


def dict_len(dicts):
    """Return length of dict. Return 0 if dicts is None."""
    return 0 if dicts is None else len(dicts)


def dict_to_hash(dictionary):
    """
    http://stackoverflow.com/questions/5884066/hashing-a-python-dictionary
    works only for hashable items in dict
    """
    return hash(frozenset(dictionary.items()))


def uuid_long(k=4):
    """
    Get uuid string without char '-'
    :param k: 1:uuid1, 3:uuid3, 4:uuid4, 5: uuid5
    :return str: eg: b64fcfd76fcb4060be51132f882914b1
    """
    if k == 1:
        uid = uuid.uuid1()
    elif k == 3:
        uid = uuid.uuid3()
    elif k == 4:
        uid = uuid.uuid4()
    elif k == 5:
        uid = uuid.uuid5()
    else:
        uid = uuid.uuid4()
    uid = str(uid).replace('-', '')
    return uid


def uuid_short(k=4, alpha=True):
    """
    Get short 8-16 bit uuid
    :param k:int: 1:uuid1, 3:uuid3, 4:uuid4, 5: uuid5
    :param alpha:bool: the short uuid includes alpha or not.
    :return: fd76fcbA or 4492202220231722
    """
    uid = uuid_long(k)
    if alpha:
        uuid_chars = ("a", "b", "c", "d", "e", "f",
                      "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
                      "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
                      "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                      "W", "X", "Y", "Z")
    else:
        uuid_chars = ("10", "11", "12", "13", "14", "15",
                      "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28",
                      "29", "30", "31", "32", "33", "34", "35", "0", "1", "2", "3", "4", "5",
                      "6", "7", "8", "9", "36", "37", "38", "39", "40", "41", "42", "43", "44",
                      "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57",
                      "58", "59", "60", "61")
    result = ''
    for i in range(0, 8):
        sub = uid[i * 4: i * 4 + 4]
        x = int(sub, 16)
        result += uuid_chars[x % 0x3E]
    return result


def unicode_str(obj, encoding='utf8'):
    """
    Make sure string is unicode type, decode with given encoding if it's not.

    If parameter is a object, object.__str__ will been called
    """
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, bytes):
        return obj.decode(encoding)
    else:
        return str(obj)


def unicode_bytes(string):
    """
    Make sure string is utf8 encoded bytes.

    If parameter is a object, object.__str__ will been called before encode as bytes
    :rtype bytes:
    """
    if isinstance(string, str):
        return string.encode('utf-8')
    elif isinstance(string, bytes):
        return string
    else:
        return str(string).encode('utf-8')


def unicode_dict(dict1):
    """
    Make sure keys and values of dict is unicode.
    """
    r = {}
    for k, v in dict1.items():
        r[str(k)] = unicode_object(v)
    return r


def unicode_list(list1):
    """
    Make sure every element in list is unicode. bytes will encode in base64
    """
    return [unicode_object(x) for x in list1]


def unicode_object(obj):
    """
    Make sure keys and values of dict/list/tuple is unicode. bytes will encode in base64.

    Can been decode by `de_unicode_object`
    """
    if obj is None:
        return obj

    if isinstance(obj, dict):
        return unicode_dict(obj)
    elif isinstance(obj, (list, tuple)):
        return unicode_list(obj)
    elif isinstance(obj, str):
        return str(obj)
    elif isinstance(obj, (int, float)):
        return obj
    else:
        try:
            return unicode_str(obj)
        except:
            return unicode_str(repr(obj))


def de_unicode_object(obj):
    """
    Decode unicoded dict/list/tuple encoded by `unicode_obj`
    """
    if isinstance(obj, dict):
        r = {}
        for k, v in obj.items():
            r[str(k)] = de_unicode_object(v)
        return r
    elif isinstance(obj, str):
        return str(obj)
    elif isinstance(obj, (list, tuple)):
        return [de_unicode_object(x) for x in obj]
    else:
        return obj


class Stack(object):

    def __init__(self, array):
        self._array = array

    def push(self, obj):
        self._array.append(obj)

    def peek(self):
        return self._array[len(self._array) - 1]

    def is_empty(self):
        return len(self._array) == 0

    def size(self):
        return len(self._array)

    def pop(self):
        return self._array.pop()


class JsonMixin(object):
    """
        Object that is about to be JSON serialized should extend this object
    """

    def to_dict(self):
        raise NotImplementedError("JsonMixin.to_dict is not implemented.")


class ValueObj(JsonMixin):
    """
        A ValueObj object is like a dictionary except `obj.foo` can be used
        in addition to `obj['foo']`.
    """

    def __init__(self, **kwargs):
        if kwargs is None:
            return
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __hash__(self):
        return id(self)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __contains__(self, key):
        return key in self.__dict__

    has_key = __contains__

    def __getattr__(self, key):
        return self.__dict__[key]

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __delattr__(self, key):
        del self.__dict__[key]

    def clear(self):
        self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def get(self, key, default=None):
        return self.__dict__.get(key, default)

    def items(self):
        return self.__dict__.items()

    def iteritems(self):
        return self.__dict__.iteritems()

    def keys(self):
        return self.__dict__.keys()

    def iterkeys(self):
        return self.__dict__.iterkeys()

    iter = iterkeys

    def values(self):
        return self.__dict__.values()

    def itervalues(self):
        return self.__dict__.itervalues()

    def pop(self, key, *args):
        return self.__dict__.pop(key, *args)

    def popitem(self):
        return self.__dict__.popitem()

    def setdefault(self, key, default=None):
        return self.__dict__.setdefault(key, default)

    def update(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)

    def to_dict(self):
        return self.__dict__

    def __repr__(self):
        return '<ValueObj %r>' % self.__dict__

    __str__ = __repr__

    def __getstate__(self):
        """Return state values to be pickled."""
        return self.__dict__

    def __setstate__(self, state):
        """Restore state from the unpickled state values."""
        dict_merge(self.__dict__, state)

    def __len__(self):
        return len(self.__dict__)


class Counter(ValueObj):
    """
    Keeps count of how many times something is added.
        >>> c = counter()
        >>> c.add('x')
        >>> c.add('x')
        >>> c.add('x')
        >>> c.add('x')
        >>> c.add('x')
        >>> c.add('y')
        >>> c
        <Counter {'y': 1, 'x': 5}>
        >>> c.most()
        ['x']
    """

    def add(self, n):
        self.setdefault(n, 0)
        self[n] += 1

    def most(self):
        """
        Returns the keys with maximum count.
        """
        m = max(self.itervalues())
        return [k for k, v in self.iteritems() if v == m]

    def least(self):
        """
        Returns the keys with mininum count.
        """
        m = min(self.itervalues())
        return [k for k, v in self.iteritems() if v == m]

    def percent(self, key):
        """
        Returns what percentage a certain key is of all entries.
           >>> c = counter()
           >>> c.add('x')
           >>> c.add('x')
           >>> c.add('x')
           >>> c.add('y')
           >>> c.percent('x')
           0.75
           >>> c.percent('y')
           0.25
        """
        return float(self[key]) / sum(self.values())

    def sorted_keys(self):
        """
        Returns keys sorted by value.
             >>> c = counter()
             >>> c.add('x')
             >>> c.add('x')
             >>> c.add('y')
             >>> c.sorted_keys()
             ['x', 'y']
        """
        return sorted(self.keys(), key=lambda k: self[k], reverse=True)

    def sorted_values(self):
        """Returns values sorted by value.
            >>> c = counter()
            >>> c.add('x')
            >>> c.add('x')
            >>> c.add('y')
            >>> c.sorted_values()
            [2, 1]
        """
        return [self[k] for k in self.sorted_keys()]

    def sorted_items(self):
        """Returns items sorted by value.
            >>> c = counter()
            >>> c.add('x')
            >>> c.add('x')
            >>> c.add('y')
            >>> c.sorted_items()
            [('x', 2), ('y', 1)]
        """
        return [(k, self[k]) for k in self.sorted_keys()]

    def __repr__(self):
        return '<Counter ' + dict.__repr__(self) + '>'


class ExtJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = obj.isoformat()
        elif isinstance(obj, datetime.date):
            encoded_object = obj.isoformat()
        elif isinstance(obj, JsonMixin):
            encoded_object = obj.to_dict()
        elif isinstance(obj, RowProxy):
            encoded_object = dict(obj)
        else:
            encoded_object = json.JSONEncoder.default(self, obj)
        return encoded_object


class Pagination(JsonMixin):
    """Pagination object."""

    def __init__(self, page, per_page, count, rows):
        #: the current page number (1 indexed)
        self._page = page
        #: the number of items to be displayed on a page.
        self._per_page = per_page
        #: the total number of items
        self._count = count
        #: the items for the current page
        self._rows = rows

    @staticmethod
    def cal_offset(page, per_page):
        page = int(page)
        per_page = int(per_page)
        return (page - 1) * per_page

    @staticmethod
    def cal_page(offset, limit):
        offset = int(offset)
        limit = int(limit)
        return offset * limit + 1

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page):
        self._page = page

    @property
    def per_page(self):
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        self._per_page = per_page

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, rows):
        self._rows = rows

    @property
    def pages(self):
        """The total number of pages"""
        if self.per_page == 0:
            pages = 0
        else:
            pages = int(math.ceil(self.total / float(self.per_page)))
        return pages

    @property
    def prev_num(self):
        """Number of the previous page."""
        if not self.has_prev:
            return None
        return self.page - 1

    @property
    def has_prev(self):
        """True if a previous page exists"""
        return self.page > 1

    @property
    def has_next(self):
        """True if a next page exists."""
        return self.page < self.pages

    @property
    def next_num(self):
        """Number of the next page"""
        if not self.has_next:
            return None
        return self.page + 1

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        """Iterates over the page numbers in the pagination.  The four
        parameters control the thresholds how many numbers should be produced
        from the sides.  Skipped page numbers are represented as `None`.
        This is how you could render such a pagination in the templates:

        .. sourcecode:: html+jinja

            {% macro render_pagination(pagination, endpoint) %}
              <div class=pagination>
              {%- for page in pagination.iter_pages() %}
                {% if page %}
                  {% if page != pagination.page %}
                    <a href="{{ url_for(endpoint, page=page) }}">{{ page }}</a>
                  {% else %}
                    <strong>{{ page }}</strong>
                  {% endif %}
                {% else %}
                  <span class=ellipsis>…</span>
                {% endif %}
              {%- endfor %}
              </div>
            {% endmacro %}
        """
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
                    (num > self.page - left_current - 1 and
                     num < self.page + right_current) or \
                    num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

    def to_dict(self):
        return {
            'page': self._page,
            'per_page': self._per_page,
            'count': self._count,
            'rows': self._rows,
        }


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
            Singleton metaclass.
            Usage for example:
            class Cls(metaclass=Singleton):
                pass
        """
        key = cls.__name__
        if key not in cls._instances:
            cls._instances[key] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[key]


class ReadOnlyDict(collections.Mapping):

    def __init__(self, data):
        self._data = data

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)