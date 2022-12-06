# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
══════════════════════════════
@Time    : 2022/12/05 14:09:42
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey"s basic method
══════════════════════════════
'''


import os
import time
import random
import pprint
from pandas import DataFrame, Series
from urwid import old_str_util
from varname import nameof


def if_iterable(obj: "object", exclude_type: "list"=[str, bytes]) -> "bool":
    """
    Judge if iterable.
    """

    check_parm(exclude_type, list)

    obj_type = type(obj)
    if obj_type in exclude_type:
        return False
    try:
        obj_dir = obj.__dir__()
    except TypeError:
        return False
    if "__iter__" in obj_dir:
        return True
    else:
        return False

def flatten(data: "object", flattern_data: "list"=[]) -> "dict":
    """
    Flatten data.
    """

    check_parm(flattern_data, list)

    data_type = type(data)
    if data_type == dict:
        for element in data.values():
            _ = flatten(element, flattern_data)
    elif if_iterable(data):
        for element in data:
            _ = flatten(element, flattern_data)
    else:
        flattern_data.append(data)
    return flattern_data

def get_info(data: "object", info: "dict"={"size": 0, "total": 0, "types": {}}, surface: "bool"=True) -> "dict":
    """
    Get data informationTrue.
    """

    check_parm(info, dict)
    check_parm(surface, bool)

    data_type = type(data)
    info["total"] += 1
    info["types"][data_type] = info["types"].get(data_type, 0) + 1
    if data_type == dict:
        for element in data.values():
            get_info(element, info, False)
    elif if_iterable(data):
        for element in data:
            get_info(element, info, False)
    else:
        info["size"] = info["size"] + 1
    if surface:
        sorted_func = lambda key: info["types"][key]
        sorted_key = sorted(info["types"], key=sorted_func, reverse=True)
        info["types"] = {key: info["types"][key] for key in sorted_key}
        return info

def split_text(text: "str", length: "int", by_width: "bool"=False) -> "list":
    """
    Split text by length or not greater than display width.
    """

    check_parm(text, str)
    check_parm(length, int)
    check_parm(by_width, bool)

    texts = []
    if by_width:
        str_group = []
        str_width = 0
        for char in text:
            char_width = get_width(char)
            str_width += char_width
            if str_width > length:
                string = "".join(str_group)
                texts.append(string)
                str_group = [char]
                str_width = char_width
            else:
                str_group.append(char)
        string = "".join(str_group)
        texts.append(string)
    else:
        test_len = len(text)
        split_n = test_len // length
        if test_len % length:
            split_n += 1
        for n in range(split_n):
            start_indxe = length * n
            end_index = length * (n + 1)
            text_group = text[start_indxe:end_index]
            texts.append(text_group)
    return texts

def fill_width(text: "str", char: "str", width: "int", align: "str"="right") -> "str":
    """
    Text fill character by display width.

    Parameters
    ----------
    text : str
        Fill text.
    char : str
        Fill character.
    width : width
        Fill width.
    align : str {'left', 'right', 'center'}
        Align orientation.

        - 'left' : Fill right, align left.
        - 'right' : Fill left, align right.
        - 'center': Fill both sides, align center.
    
    Returns
    -------
    str
        Text after fill.
    """

    check_parm(text, str)
    check_parm(char, str)
    check_parm(width, int)
    check_parm(align, str)

    if get_width(char) != 1:
        raise ValueError("parameter char value error!")
    text_width = get_width(text)
    fill_width = width - text_width
    if fill_width > 0:
        if align == "left":
            new_text = "%s%s" % (char * fill_width, text)
        elif align == "right":
            new_text = "%s%s" % (text, char * fill_width)
        elif align == "center":
            fill_width_left = int(fill_width / 2)
            fill_width_right = fill_width - fill_width_left
            new_text = "%s%s%s" % (char * fill_width_left, text, char * fill_width_right)
        else:
            raise ValueError("parameter align value error!")
    else:
        new_text = text
    return new_text

def format_data(data: "object", indent_char: "str"="    ") -> "str":
    """
    Format data as string.
    """

    check_parm(indent_char, str)

    data_str = str(data).replace(" ", "")
    indent_n = 0
    data = []
    for char_index in range(len(data_str)):
        char = data_str[char_index]
        if char == ",":
            data.append(char)
            data.append("\n" + indent_char * indent_n)
        elif char == ":":
            data.append(char + " ")
        elif char in "[({" and data_str[char_index + 1] not in "])}":
            indent_n += 1
            data.append(char)
            data.append("\n" + indent_char * indent_n)
        elif char in "])}" and data[-1] not in "[({":
            indent_n -= 1
            data.append("\n" + indent_char * indent_n)
            data.append(char)
        else:
            data.append(char)
    data = "".join(data)
    return data

def pformat(content: "object", width: "int"=100) -> "str":
    """
    Based on module pprint.pformat, modify the chinese width judgment.
    """

    def _format(_self, object, stream, indent, allowance, context, level):
        objid = id(object)
        if objid in context:
            stream.write(pprint._recursion(object))
            _self._recursive = True
            _self._readable = False
            return
        rep = _self._repr(object, context, level)
        max_width = _self._width - indent - allowance
        width = get_width(rep)
        if width > max_width:
            p = _self._dispatch.get(type(object).__repr__, None)
            if p is not None:
                context[objid] = 1
                p(_self, object, stream, indent, allowance, context, level + 1)
                del context[objid]
                return
            elif isinstance(object, dict):
                context[objid] = 1
                _self._pprint_dict(object, stream, indent, allowance,
                                context, level + 1)
                del context[objid]
                return
        stream.write(rep)

    pprint.PrettyPrinter._format = _format
    content_str = pprint.pformat(content, width=width, sort_dicts=False)
    return content_str

def print_frame(content: "list", title: "str"=None, width: "int"=100) -> "None":
    """
    Print frame.
    """

    check_parm(content, list)
    check_parm(title, str, None)
    check_parm(width, int)
    
    width -= 2
    has_error = False
    print_blocks = []
    for block in content:
        try:
            if id(block) == id("-"):
                frame_split_line = "╠%s╣" % ("═" * width)
                print_blocks.append(frame_split_line)
            else:
                block_str = str(block)
                rows_str = block_str.split("\n")
                rows_str =[_row_str for row_str in rows_str for _row_str in split_text(row_str, width, True)]
                rows_str = ["║%s║" % fill_width(string, " ", width) for string in rows_str]
                block_str = "\n".join(rows_str)
                print_blocks.append(block_str)
        except Exception as e:
            has_error = True
            print_blocks.append(block)
    if title == None:
        title = ""
    else:
        title = f"╡ {title} ╞"
    if has_error:
        frame_top = "╒%s╕" % title.center(width, "═")
        frame_bottom = "╘%s╛" % ("═" * width)
    else:
        frame_top = "╔%s╗" % title.center(width, "═")
        frame_bottom = "╚%s╝" % ("═" * width)
    print_contents = [
        frame_top,
        *print_blocks,
        frame_bottom
    ]
    for print_content in print_contents:
        print(print_content)

def rprint(
        *args: "object",
        width: "int"=100,
        title: "str"=None,
        print_info: "bool"=False,
        format_module: "str | None"="pprint"
    ) -> "None":
    """
    Print data and data information.

    Parameters
    ----------
    *args : object
        Print contents.
    width : int
        Print frame width.
    title : str
        Print frame title.
    print_info : bool
        Whether print content data information.
    format_module : str {'pprint', 'reytool'} or None
        Content format module.

        - "pprint" : Use function pformat.
        - "reytool" : Use function format_data.
        - None : Not format.
    """

    check_parm(print_info, bool)
    check_parm(width, int)
    check_parm(title, str, None)
    check_parm(format_module, "pprint", "reytool", None)

    datas = []
    for data in args:
        datas.extend(["-", data])
    datas = datas[1:]
    if print_info:
        try:
            info = get_info(args)
        except:
            info = False
        if info:
            if info["types"][tuple] == 1:
                del info["types"][tuple]
            else:
                info["types"][tuple] -= 1
            info["types"] = ["%s: %s" % (key.__name__, val) for key, val in info["types"].items()]
            info["types"] = ", ".join(info["types"])
            datas = [
                f"size: {info['size']}",
                f"total: {info['total'] - 1}",
                info["types"],
                "-",
                *datas
            ]
    if title == None:
        try:
            title = nameof(*args, frame=2)
            if type(title) == tuple:
                title = " │ ".join(title)
        except:
            title = None
    dates_index = range(len(datas))
    if format_module == "pprint":
        _width = width - 2
        for date_index in dates_index:
            try:
                if datas[date_index] != "-":
                    datas[date_index] = pformat(datas[date_index], _width)
            except:
                pass
    elif format_module == "reytool":
        for date_index in dates_index:
            try:
                if datas[date_index] != "-":
                    datas[date_index] = format_data(datas[date_index])
            except:
                pass
    print_frame(datas, title, width)

def get_width(text: "str") -> "int":
    """
    Get text display width.
    """

    check_parm(text, str)
    
    total_width = 0
    for char in text:
        char_unicode = ord(char)
        char_width = old_str_util.get_width(char_unicode)
        total_width += char_width
    return total_width

def get_first_notnull(*args: "object", default: "object"=None, exclude: "list"=[]) -> object:
    """
    Get first notnull element.
    """

    check_parm(exclude, list)
    
    for element in args:
        if element not in [None, *exclude]:
            return element
    return default
    
def check_parm(value: "object", *args: "object | type", print_var_name: "bool"=True) -> "None":
    """
    Check the content or type of the value.
    """

    if type(value) in args:
        return
    args_id = [id(element) for element in args]
    if id(value) in args_id:
        return
    if print_var_name:
        try:
            var_name = nameof(value, frame=2)
            var_name = " '%s'" % var_name
        except:
            var_name = ""
    else:
        var_name = ""
    include_str = ", ".join([repr(element) for element in args])
    error = "parameter%s the value content or type must in [%s], now: %s" % (var_name, include_str, repr(value))
    raise ValueError(error)
    
def check_parm_least_one(*args: "object") -> "None":
    """
    Check that at least one of multiple values is not None.
    """

    for value in args:
        if value != None:
            return
    try:
        vars_name = nameof(*args, frame=2)
    except:
        vars_name = None
    if vars_name:
        vars_name_str = " " + " and ".join(["\"%s\"" % var_name for var_name in vars_name])
    else:
        vars_name_str = ""
    error = "at least one of parameters%s is not None" % vars_name_str
    raise ValueError(error)

def log(records: "list[iter,] | list[dict,] | DataFrame | Series", fields: "iter"=None, path: "str"="log.csv") -> "None":
    """
    Write or create log file.
    """

    from .rtime import now
    
    check_parm(records, list, DataFrame, Series)
    check_parm(path, str)

    if not len(records):
        return
    records_type = type(records)
    exists_bool = os.path.exists(path)
    if not exists_bool:
        start_id = 0
        if fields:
            fields = ["id", "datetime"] + fields
        else:
            fields = ["id", "datetime"]
            if records_type == list:
                element_type = type(records[0])
                if element_type == dict:
                    fields.extend(records[0].keys())
                else:
                    fields.extend([""] * len(records[0]))
            elif records_type == DataFrame:
                fields.extend(records.columns)
            elif records_type == Series:
                name = records.name
                name = str(name) if name else ""
                fields.append(name)
        fields_text = ",".join(fields)
    else:
        with open(path, "r", encoding="utf-8") as f:
            log_texts = f.readlines()
        start_id = int(log_texts[-1].split(",")[0]) + 1
        fields_text = ""
    records_len = len(records)
    records_ids = range(start_id, start_id + records_len)
    datetime_now = now()
    if records_type == list:
        element_type = type(records[0])
        if element_type == dict:
            records = [row.values() for row in records]
        values_texts = [
            ",".join(
                [
                    str(id),
                    datetime_now,
                    *[str(element) for element in row]
                ]
            )
            for id, row in list(zip(records_ids, records))
        ]
        values_text = "\n".join(values_texts)
    elif records_type == DataFrame:
        records = records.fillna("")
        records.insert(0, "id", records_ids, allow_duplicates=True)
        records.insert(1, "datetime", datetime_now, allow_duplicates=True)
        records = records.astype(str)
        func = lambda ser: ser.str.cat(sep=",")
        values_ser = records.apply(func=func, axis=1)
        values_text = values_ser.str.cat(sep="\n")
    elif records_type == Series:
        records = records.fillna("")
        records = DataFrame(records)
        records.insert(0, "id", records_ids, allow_duplicates=True)
        records.insert(1, "datetime", datetime_now, allow_duplicates=True)
        records = records.astype(str)
        func = lambda ser: ser.str.cat(sep=",")
        values_ser = records.apply(func=func, axis=1)
        values_text = values_ser.str.cat(sep="\n")
    records_text = "\n".join([fields_text, values_text])
    with open(path, "a", encoding="utf-8") as f:
        f.write(records_text)

def sleep_random_seconds(*args: "int | float") -> "float":
    """
    Sleep random seconds.
    """
    
    for parm in args:
        check_parm(parm, int, float, print_var_name=False)

    max_second = args[-1]
    if len(args) == 1:
        min_second = 0
    elif len(args) == 2:
        min_second = args[0]
    else:
        error = TypeError("number of parameter *args must is one or two")
        raise error
    max_second_hundred = int(max_second * 100)
    min_second_hundred = int(min_second * 100)
    random_n_hundred = random.randint(min_second_hundred, max_second_hundred)
    random_n = random_n_hundred / 100
    time.sleep(random_n)
    return random_n

def split_array(array: "iter", bin_size: "int"=None, share: "int"=10) -> "list":
    """
    Split array into multiple array.
    """

    check_parm(bin_size, int, None)
    check_parm(share, int, None)
    check_parm_least_one(bin_size, share)

    array = list(array)
    array_len = len(array)
    arrays = []
    arrays_len = 0
    if bin_size == None:
        average = array_len / share
        for n in range(share):
            bin_size = int(average * (n + 1)) - int(average * n)
            _array = array[arrays_len:arrays_len + bin_size]
            arrays.append(_array)
            arrays_len += bin_size
    else:
        while True:
            _array = array[arrays_len:arrays_len + bin_size]
            arrays.append(_array)
            arrays_len += bin_size
            if arrays_len > array_len:
                break
    return arrays

def get_paths(path: "str | None"=None, target: "str"="all", recursion: "bool"=True) -> "list":
    """
    Get the path of files and folders in the path.

    Parameters
    ----------
    path : str or None
        When None, then work path.
    target : str {'all, 'file', 'folder'}
        Target data.

        - "all" : return file and folder path.
        - "file : return file path.
        - "folder" : return folder path.

    recursion : bool
        Is recursion directory.

    Returns
    -------
    list(str,)
        String is path.
    """

    check_parm(path, str, None)
    check_parm(target, "all", "file", "folder")
    check_parm(recursion, bool)

    if path == None:
        path = ""
    path = os.path.abspath(path)
    paths = []
    if recursion:
        obj_walk = os.walk(path)
        if target == "all":
            targets_path = [
                os.path.join(path, file_name)
                for path, folders_name, files_name in obj_walk
                for file_name in files_name + folders_name
            ]
            paths.extend(targets_path)
        elif target == "file":
            targets_path = [
                os.path.join(path, file_name)
                for path, folders_name, files_name in obj_walk
                for file_name in files_name
            ]
            paths.extend(targets_path)
        elif target in ["all", "folder"]:
            targets_path = [
                os.path.join(path, folder_name)
                for path, folders_name, files_name in obj_walk
                for folder_name in folders_name
            ]
            paths.extend(targets_path)
    else:
        names = os.listdir(path)
        if target == "all":
            for name in names:
                target_path = os.path.join(path, name)
                paths.append(target_path)
        elif target == "file":
            for name in names:
                target_path = os.path.join(path, name)
                is_file = os.path.isfile(target_path)
                if is_file:
                    paths.append(target_path)
        elif target == "folder":
            for name in names:
                target_path = os.path.join(path, name)
                is_dir = os.path.isdir(target_path)
                if is_dir:
                    paths.append(target_path)
    return paths