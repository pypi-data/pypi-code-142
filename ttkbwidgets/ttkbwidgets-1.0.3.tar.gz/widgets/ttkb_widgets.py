from abc import abstractmethod
from datetime import datetime, date, time
from decimal import Decimal
import re
import tkinter as tk
import ttkbootstrap as ttkb
import ttkbootstrap.dialogs.dialogs as dialogs
from ttkbootstrap.validation import add_validation
from ttkbootstrap.constants import *

from typing import Any, Callable, Literal, Optional, Union

from widgets.ttkb_validators import month_validator, day_validator, year_validator, hour_validator, \
    minute_validator


class Radiobutton(ttkb.Radiobutton):
    """
    Subclass of ttkbootstrap.Radiobutton that changes it appears when it is in focus, so that the user
    can tell when that can use the space bar to select or unselect a button

    """

    def __init__(self, parent, text: str, value: str, variable: ttkb.StringVar, command=None,
                 width=None):
        ttkb.Radiobutton.__init__(self, parent, text=text, value=value, variable=variable,
                                  command=command, width=width, bootstyle='primary')
        self.bind('<FocusIn>', self.focus_in)
        self.bind('<FocusOut>', self.focus_out)

    def focus_in(self, event) -> None:
        """
        Handler for the <FocusIn> event. Changes config parm bootstyle to 'toolbutton'
        :param event:
        :return: None
        """
        self.configure(bootstyle='toolbutton')

    def focus_out(self, event):
        """
        Handler for the <FocusOut> event.  Changes config parm bootstyle to 'primary'
        :param event:
        :return:
        """
        self.configure(bootstyle='primary')


class Checkbutton(ttkb.Checkbutton):
    """
    Subclass of ttkbootstrap.Checkbutton that changes it appears when it is in focus, so that the user
    can tell when that can use the space bar to select or unselect a checkbox
    """

    def __init__(self, parent, text, variable, command=None, padding=None, width=None):
        ttkb.Checkbutton.__init__(self, parent, text=text, variable=variable, command=command, padding=padding,
                                  width=width, bootstyle='primary')
        self.bind('<FocusIn>', self.focus_in)
        self.bind('<FocusOut>', self.focus_out)
        self.row: int = -1
        self.column: int = -1

    def focus_in(self, event):
        """
        Handler for the <FocusIn> event. Changes config parm bootstyle to 'toolbutton'
        :param event:
        :return: None
        """
        self.configure(bootstyle='toolbutton')

    def focus_out(self, event):
        """
        Handler for the <FocusOut> event.  Changes config parm bootstyle to 'primary'
        :param event:
        :return:
        """
        self.configure(bootstyle='primary')


class EntryWidget:
    """
    An abstract base class for entry label/widget pairs
    """

    def __init__(self, parent, label_text: Optional[str], entry_width: int, regex_str: Optional[str] = None):
        """
        Create an instance of EntryWidget

        :param parent: the GUI parent of this class
        :param label_text: the text to be used in creating the label
        :type label_text: str`
        :param regex_str:
        """
        self.parent = parent
        self.label_text = label_text
        if regex_str is not None:
            self.regex_pattern: Optional[re.Pattern] = re.compile(regex_str)
        else:
            self.regex_pattern = None
        self.strvar = ttkb.StringVar()
        self.entry = ttkb.Entry(master=parent, textvariable=self.strvar, validate='focusout', width=entry_width,
                                validatecommand=self.validate, invalidcommand=self.invalid)

    def invalid(self):
        """
        This method is used as an 'invalidcommand' callback.  It is invoked when validation fails.  It sets the widget
        background color to red, which gives it a red border, then calls focus_set on the widget

        :return: None

        """
        self.entry.config(background='red')
        self.focus_set()

    def focus_set(self):
        """
        Delegates focus_set calls to the entry widget

        :return: None

        """
        self.entry.focus_set()
        self.entry.selection_range('0', tk.END)

    def bind(self, sequence: str | None = ...,
             func: Callable[[tk.Event], Any] | None = ...,
             add: Literal["", "+"] | bool | None = ..., ) -> str:
        """
        Delegate bind calls to the entry widget

        :param sequence: the name of the event to be bound
        :type sequence: str | None
        :param func: the callback to be invoked when the event is captured
        :type func: Callable[[tk.Event], Any]
        :param add: allows multiple bindings for single event
        :type add: Literal["", "+"] | bool | None
        :return: None

        """
        return self.entry.bind(sequence, func, add)

    def grid(self, **kwargs):
        """
        Delegate grid calls to the entry widget

        :param kwargs: key word args
        :type kwargs: dict[str,Any]
        :return: None

        """
        self.entry.grid(kwargs)

    def set_regex(self, regex_str: str) -> None:
        """
        Set the regular expression used to validate user input

        :param regex_str: a regular expression
        :type regex_str: str
        :return: None

        """
        self.regex_pattern = re.compile(regex_str)

    def apply_regex(self, value=None) -> Optional[tuple[Any, ...]]:
        """
        Apply the widget's regex either to the proved string or to the value entered to the widget prompt

        :param value: if not None, the regex will be applied to this value
        :type value: str
        :return: returns the groups collected by the regex
        :rtype: Optional[tuple[Any, ...]]

        """
        if value is None:
            match = self.regex_pattern.match(self.strvar.get())
        else:
            match = self.regex_pattern.match(value)

        if match is None:
            return None
        else:
            return match.groups()

    def get_var(self) -> ttkb.StringVar:
        """
        Returns the StringVar associated with the entry widget

        :return: the StringVar associated with the entry widget
        :rtype: ttkb.StringVar

        """
        return self.strvar

    @abstractmethod
    def get_value(self) -> str:
        """
        An abstract method to be implemented by subclasses to return the entry widget value

        :return: the entry widget value
        :rtype: implementation dependant

        """
        return self.strvar.get()

    @abstractmethod
    def set_value(self, value: Union[int, Decimal, str]) -> None:
        """
        An abstract method implemented by subclasses to set the entry widget value

        :param value:  value to be set
        :type value: Union[int, Decimal, str]
        :return: None

        """
        if isinstance(value, str):
            self.strvar.set(value)
        elif isinstance(value, int):
            self.strvar.set(f'{value:d}')
        else:
            self.strvar.set(f'{value:.2f}')

    @abstractmethod
    def validate(self) -> int:
        """
        An abstract method implemented by subclasses to set the entry widget value

        :return: 1 if valid, 0 if not

        """
        ...


class TextWidget(EntryWidget):
    """
    A regex validated text entry widget

    """

    def __init__(self, parent, label_text: str, entry_width: int, regex_str: Optional[str] = None):
        """
        Creates and instance of TextWidget

        :param parent: the GUI parent of this widget
        :param label_text: the text for the label that will be associated with the widget.  The label is not
            created with the entry widget, but the label text is used to create ValueError exception messages
        :type label_text: str
        :param regex_str: The regular expression that will be used to validate data entered to the widget
        :type regex_str: str

        """
        EntryWidget.__init__(self, parent=parent, label_text=label_text, entry_width=entry_width, regex_str=regex_str)

    def validate(self) -> int:
        """
        A validation callback for the validationcommand parameter of the tkinter Entry widget

        :return: 1 if validate, otherwise 0
        :rtype: int

        """
        if self.regex_pattern is not None:
            str_value = self.strvar.get().strip()
            if len(str_value) > 0:
                groups = self.apply_regex()
                if groups is not None and len(groups) == 1:
                    return 1
                else:
                    return 0
            else:
                return 1
        else:
            return 1

    def get_value(self):
        """
        Return the widget's entry value

        :return: the widget's entry value
        :rtype: str

        """
        return self.strvar.get()

    def set_value(self, value: str):
        """
        The argument value is filtered through the validation regex and the resulting regex group is used to set the
        widget's entry value

        :param value: the value to be used to set the entry value
        :type value: str
        :return: None

        """
        if self.regex_pattern is not None:
            groups = self.apply_regex(value)
            if groups is None:
                raise ValueError(f'{value} is not a valid {self.label_text}')
            else:
                self.strvar.set(groups[0])
        else:
            self.strvar.set(value)


class LabeledTextWidget:
    """
    A Frame containing a Label and a TextWidget

    """

    def __init__(self, parent, label_text: str, label_width: int, label_grid_args: dict[str, Any],
                 entry_width: int, entry_grid_args: dict[str, Any], regex_str: Optional[str] = None):
        """
        Creates and instance of LabeledTextWidget

        :param parent: The GUI parent for this Frame
        :param label_text: the text to be used in creating the label
        :type label_text: str
        :param label_width: the width to be used in creating the label
        :type label_width: int
        :param label_grid_args: the arguments to be used in gridding the label
        :type label_grid_args: dict[str, Any]
        :param entry_width: the width to be used in creating the entry widget
        :type entry_width: int
        :param entry_grid_args: the arguments to be used in gridding the entry widet
        :type entry_grid_args: dict[str, Any]
        :param regex_str: the regular expression to be used for validation of input: default '\\s*(\\w*)\\s*'
        :type regex_str: str

        """
        # ttkb.Frame.__init__(self, master=parent)
        anchor = tk.W
        if 'row' in label_grid_args and 'row' in entry_grid_args and 'sticky' not in entry_grid_args:
            if label_grid_args['row'] == entry_grid_args['row']:
                entry_grid_args['sticky'] = tk.W
                anchor = tk.E
        self.label = ttkb.Label(master=parent, text=label_text, width=label_width, anchor=anchor)
        self.label.grid(**label_grid_args)
        self.entry = TextWidget(parent=parent, label_text=label_text, entry_width=entry_width, regex_str=regex_str)
        self.entry.grid(**entry_grid_args)

    def focus_set(self):
        """
        Delegates calls to focus_set to the entry widget

        :return: None

        """
        self.entry.focus_set()

    def bind(self, sequence: str | None = ...,
             func: Callable[[tk.Event], Any] | None = ...,
             add: Literal["", "+"] | bool | None = ..., ) -> str:
        """
        Delegate bind calls to the entry widget

        :param sequence: the name of the event to be bound
        :type sequence: str | None
        :param func: the callback to be invoked when the event is captured
        :type func: Callable[[tk.Event], Any]
        :param add: allows multiple bindings for single event
        :type add: Literal["", "+"] | bool | None
        :return: None

        """
        return self.entry.bind(sequence, func, add)

    def get_value(self) -> str:
        """
        Return the widget's entry value

        :return: the widget's entry value
        :rtype: str

        """
        return self.entry.get_value()

    def set_value(self, value: str) -> None:
        """
        The argument value is filtered through the validation regex and the resulting regex group is used to set the
        widget's entry value

        :param value: the value to be used to set the entry value
        :type value: str
        :return: None

        """
        self.entry.set_value(value)

    @staticmethod
    def label_width(text: str, min_width: int) -> int:
        """
        Calculates a width for the label based on the label text and a minumum width

        :param text: the label test
        :type text: str
        :param min_width: the minimum label width
        :type min_width: int
        :return: the calculated label width
        :rtype: int

        """
        text_width = len(text) + 2
        if text_width < min_width:
            return min_width
        else:
            return text_width


class IntegerWidget(EntryWidget):
    def __init__(self, parent, label_text: str, regex_str: Optional[str] = '\\s*(\\d*)\\s*'):
        """
        Creates and instance of IntegerWidget

        :param parent: the GUI parent of this widget
        :param label_text: the text for the label that will be associated with the widget.  The label is not
            created with the entry widget, but the label text is used to create ValueError exception messages
        :type label_text: str
        :param regex_str: The regular expression used to validate data entered: default '\\s*(\\d*)\\s*'
        :type regex_str: str

        """
        EntryWidget.__init__(self, parent=parent, label_text=label_text, entry_width=10, regex_str=regex_str)

    def validate(self):
        """
        A validation callback for the validationcommand parameter of the tkinter Entry widget

        :return: 1 if validate, otherwise 0
        :rtype: int

        """
        str_value = self.strvar.get().strip()
        if len(str_value) > 0:
            groups = self.apply_regex()
            if groups is not None and len(groups) == 1:
                if groups[0].isnumeric():
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 1

    def get_value(self):
        """
        Return the widget's entry value

        :return: the widget's entry value as an integer
        :rtype: int

        """
        value = self.strvar.get().strip()
        if len(value) == 0:
            return 0
        else:
            return int(self.strvar.get().strip())

    def set_value(self, value: Union[int, str]):
        """
        The argument value is filtered through the validation regex and the resulting regex group is used to set the
        widget's entry value

        :param value: the value to be used to set the entry value
        :type value: Union[int, str]
        :return: None

        """
        if isinstance(value, int):
            self.strvar.set(f'{value:d}')
        elif isinstance(value, str) and value.isnumeric():
            if len(value.strip()) > 0:
                re_groups = self.apply_regex(value)
                int_value: int = int(re_groups[0])
                self.strvar.set(f'{int_value:d}')
            else:
                self.strvar.set('0')
        else:
            raise ValueError(f'{value} is not a valid {self.label_text}')


class LabeledIntegerWidget:
    def __init__(self, parent, label_text: str, label_width: int, label_grid_args: dict[str, Any],
                 entry_width: int, entry_grid_args: dict[str, Any], regex_str: Optional[str] = '\\s*(\\d*)\\s*'):
        """
        Creates and instance of LabeledIntegerWidget

        :param parent: The GUI parent for this Frame
        :param label_text: the text to be used in creating the label
        :type label_text: str
        :param label_width: the width to be used in creating the label
        :type label_width: int
        :param label_grid_args: the arguments to be used in gridding the label
        :type label_grid_args: dict[str, Any]
        :param entry_width: the width to be used in creating the entry widget
        :type entry_width: int
        :param entry_grid_args: the arguments to be used in gridding the entry widet
        :type entry_grid_args: dict[str, Any]
        :param regex_str: the regular expression to be used for validation of input: default value '\\s*(\\d*)\\s*'
        :type regex_str: str

        """
        # ttkb.Frame.__init__(self, master=parent)
        row_str: str = 'row'
        sticky_str: str = 'sticky'
        anchor = tk.W
        if row_str in label_grid_args and row_str in entry_grid_args and sticky_str not in entry_grid_args:
            if label_grid_args[row_str] == entry_grid_args[row_str]:
                anchor = tk.E
                entry_grid_args[sticky_str] = tk.W
        self.label = ttkb.Label(master=parent, text=label_text, width=label_width, anchor=anchor)
        self.label.grid(**label_grid_args)
        self.entry = IntegerWidget(parent=parent, label_text=label_text, regex_str=regex_str)
        self.entry.grid(**entry_grid_args)

    def focus_set(self):
        """
        Delegates calls to focus_set to the entry widget

        :return: None

        """
        self.entry.focus_set()

    def bind(self, sequence: str | None = ...,
             func: Callable[[tk.Event], Any] | None = ...,
             add: Literal["", "+"] | bool | None = ..., ) -> str:
        """
        Delegate bind calls to the entry widget

        :param sequence: the name of the event to be bound
        :type sequence: str | None
        :param func: the callback to be invoked when the event is captured
        :type func: Callable[[tk.Event], Any]
        :param add: allows multiple bindings for single event
        :type add: Literal["", "+"] | bool | None
        :return: None

        """
        return self.entry.bind(sequence, func, add)

    def get_value(self) -> int:
        """
        Return the widget's entry value

        :return: the widget's entry value as an integer
        :rtype: int

        """
        return self.entry.get_value()

    def set_value(self, value: Union[int, str]) -> None:
        """
        The argument value is filtered through the validation regex and the resulting regex group is used to set the
        widget's entry value

        :param value: the value to be used to set the entry value
        :type value: Union[int, str]
        :return: None

        """
        self.entry.set_value(value)

    @staticmethod
    def label_width(text: str, min_width: int) -> int:
        """
        Calculates a width for the label based on the label text and a minumum width

        :param text: the label test
        :type text: str
        :param min_width: the minimum label width
        :type min_width: int
        :return: the calculated label width
        :rtype: int

        """
        text_width = len(text) + 2
        if text_width < min_width:
            return min_width
        else:
            return text_width


class DecimalWidget(EntryWidget):
    def __init__(self, parent, label_text: str, regex_str: Optional[str] = '\\s*(\\d+[.]*\\d*)\\s*'):
        """
        Creates and instance of DecimalWidget

        :param parent: the GUI parent of this widget
        :param label_text: the text for the label that will be associated with the widget.  The label is not
            created with the entry widget, but the label text is used to create ValueError exception messages
        :type label_text: str
        :param regex_str: The regular expression used to validate data entered: default '\\s*(\\d+[.]*\\d*)\\s*'
        :type regex_str: str

        """
        EntryWidget.__init__(self, parent=parent, label_text=label_text, entry_width=10, regex_str=regex_str)

    def validate(self):
        """
        A validation callback for the validationcommand parameter of the tkinter Entry widget

        :return: 1 if validate, otherwise 0
        :rtype: int

        """
        str_value = self.strvar.get().strip()
        if len(str_value) > 0:
            groups = self.apply_regex()
            if groups is not None and len(groups) == 1:
                return 1
            else:
                return 0
        else:
            return 1

    def get_value(self) -> Decimal:
        """
        Return the widget's entry value

        :return: the widget's entry value as a Decimal
        :rtype: decimal.Decimal

        """
        if self.validate() == 1:
            str_value = self.strvar.get().strip()
            if len(str_value) == 0:
                return Decimal(0)
            else:
                return Decimal(str_value)
        else:
            raise ValueError(f'{self.strvar.get()} is not a valid {self.label_text}')

    def set_value(self, value: Union[Decimal, str]):
        """
        The argument value is filtered through the validation regex and the resulting regex group is used to set the
        widget's entry value

        :param value: the value to be used to set the entry value
        :type value: Union[decimal.Decimal, str]
        :return: None

        """
        if isinstance(value, Decimal):
            self.strvar.set(f'{value:.1f}')
        elif isinstance(value, str) and value.isnumeric():
            if len(value.strip()) > 0:
                re_groups = self.apply_regex()
                if re_groups is not None:
                    dec_value: Decimal = Decimal(re_groups[0])
                    self.strvar.set(f'{dec_value:.1f}')
                raise ValueError(f'{self.strvar.get()} is not a valid {self.label_text}')
            else:
                self.strvar.set('0.0')
        else:
            raise ValueError(f'{self.strvar.get()} is not a valid {self.label_text}')


class LabeledDecimalWidget:
    def __init__(self, parent, label_text: str, label_width: int, label_grid_args: dict[str, Any],
                 entry_width: int, entry_grid_args: dict[str, Any],
                 regex_str: Optional[str] = '\\s*(\\d+[.]*\\d*)\\s*'):
        """
        Creates and instance of LabeledDecimalWidget

        :param parent: The GUI parent for this Frame
        :param label_text: the text to be used in creating the label
        :type label_text: str
        :param label_width: the width to be used in creating the label
        :type label_width: int
        :param label_grid_args: the arguments to be used in gridding the label
        :type label_grid_args: dict[str, Any]
        :param entry_width: the width to be used in creating the entry widget
        :type entry_width: int
        :param entry_grid_args: the arguments to be used in gridding the entry widet
        :type entry_grid_args: dict[str, Any]
        :param regex_str: the regular expression to be used for validation of input: default value '\\s*(\\d+[.]*\\d*)\\s*'
        :type regex_str: str

        """
        # ttkb.Frame.__init__(self, master=parent)
        row_str: str = 'row'
        sticky_str: str = 'sticky'
        anchor = tk.W
        if row_str in label_grid_args and row_str in entry_grid_args and sticky_str not in entry_grid_args:
            if label_grid_args[row_str] == entry_grid_args[row_str]:
                anchor = tk.E
                entry_grid_args[sticky_str] = tk.W
        self.label = ttkb.Label(parent, text=label_text, width=label_width, anchor=anchor)
        self.label.grid(**label_grid_args)
        self.entry = DecimalWidget(parent=parent, label_text=label_text, regex_str=regex_str)
        self.entry.grid(**entry_grid_args)

    def focus_set(self):
        """
        Delegates calls to focus_set to the entry widget

        :return: None

        """
        self.entry.focus_set()

    def bind(self, sequence: str | None = ...,
             func: Callable[[tk.Event], Any] | None = ...,
             add: Literal["", "+"] | bool | None = ..., ) -> str:
        """
        Delegate bind calls to the entry widget

        :param sequence: the name of the event to be bound
        :type sequence: str | None
        :param func: the callback to be invoked when the event is captured
        :type func: Callable[[tk.Event], Any]
        :param add: allows multiple bindings for single event
        :type add: Literal["", "+"] | bool | None
        :return: None

        """
        return self.entry.bind(sequence, func, add)

    def get_value(self) -> Decimal:
        """
        Return the widget's entry value

        :return: the widget's entry value as a Decimal
        :rtype: decimal.Decimal

        """
        return self.entry.get_value()

    def set_value(self, value: Union[Decimal, str]) -> None:
        """
        The argument value is filtered through the validation regex and the resulting regex group is used to set the
        widget's entry value

        :param value: the value to be used to set the entry value
        :type value: Union[decimal.Decimal, str]
        :return: None

        """
        self.entry.set_value(value)

    @staticmethod
    def label_width(text: str, min_width: int) -> int:
        """
        Calculates a width for the label based on the label text and a minumum width

        :param text: the label test
        :type text: str
        :param min_width: the minimum label width
        :type min_width: int
        :return: the calculated label width
        :rtype: int

        """
        text_width = len(text) + 2
        if text_width < min_width:
            return min_width
        else:
            return text_width

class DateWidget(ttkb.Frame):
    """
    A general purpose date entry widget
    """
    def __init__(self, parent, default_value: datetime.date = None):
        """
        Creates widgets.DateWidget instance
        :param parent: the GUI element that will contain the created widget
        :param default_value: a datetime.date value to be used as an initial value for the month, day and year
        entry fields.
        """
        ttkb.Frame.__init__(self, parent)
        self.month_var = ttkb.StringVar()
        self.day_var = ttkb.StringVar()
        self.year_var = ttkb.StringVar()
        self.prev_entry = None
        self.next_entry = None
        if default_value:
            self.month_var.set(default_value.month)
            self.day_var.set(default_value.day)
            self.year_var.set(default_value.year)
        self.month_entry = ttkb.Entry(self, textvariable=self.month_var, width=3)
        self.month_entry.grid(column=0, row=0, sticky=tk.NW, ipadx=0, padx=0)
        ttkb.Label(self, text="/", width=1, font=('courier', 20, 'bold')).grid(column=1, row=0, sticky=tk.NW, padx=0,
                                                                               pady=5)
        self.month_entry.bind('<KeyPress>', self.month_keypress)
        self.month_entry.bind('<FocusIn>', self.clear_key_count)
        add_validation(self.month_entry, month_validator)
        self.day_entry = ttkb.Entry(self, textvariable=self.day_var, width=3)
        self.day_entry.grid(column=2, row=0, sticky=tk.NW)
        self.day_entry.bind('<KeyPress>', self.day_keypress)
        self.day_entry.bind('<FocusIn>', self.clear_key_count)
        add_validation(self.day_entry, day_validator)
        ttkb.Label(self, text="/", width=1, font=('courier', 20, 'bold')).grid(column=3, row=0, sticky=tk.NW, padx=0,
                                                                               pady=5)
        self.year_entry = ttkb.Entry(self, textvariable=self.year_var, width=6)
        self.year_entry.grid(column=4, row=0, stick=tk.NW)
        self.year_entry.bind('<KeyPress>', self.year_keypress)
        self.year_entry.bind('<FocusIn>', self.clear_key_count)
        self.year_entry.bind('<FocusOut>', self.validate_date)
        add_validation(self.year_entry, year_validator)
        self.grid()
        self.key_count = 0
        self.max_dom: dict[int, int] = {
            1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        self.prev_key_press = None
        self.error: bool = False

    def set_prev_entry(self, entry) -> None:
        """
        Establishes the widget to focus on when the Back Tab key is pressed in the Month field

        :param entry:
        :return: None

        """
        self.prev_entry = entry

    def set_next_entry(self, entry) -> None:
        """
        Establishes the widget to focus on when the Tab key is pressed in the Year field

        :param entry:
        :return: None

        """
        self.next_entry = entry

    def focus_set(self) -> None:
        """
        Delegates focus_set to the month entry

        :return: None

        """
        self.month_entry.focus_set()
        self.key_count = 0
        self.prev_key_press = None

    def disable(self) -> None:
        """
        Disables the month, day and year fields

        :return: None

        """
        self.month_entry.configure(state=DISABLED)
        self.day_entry.configure(state=DISABLED)
        self.year_entry.configure(state=DISABLED)

    def enable(self) -> None:
        """
        Enables the month, day and year fields

        :return: None

        """
        self.month_entry.configure(state=NORMAL)
        self.day_entry.configure(state=NORMAL)
        self.year_entry.configure(state=NORMAL)

    def select_range(self, start, end):
        """
        Delegates select range functionality to the month entry field
        :param start:
        :param end:
        :return:
        """
        self.month_entry.select_range(start, end)

    def clear_key_count(self, event):
        """
        Sets the keystroke counter to 0.  This method is bound to the <FocusIn> event for the month, day and year
        fields
        :param event:
        :return: None
        """
        self.key_count = 0

    def month_keypress(self, event):
        """
        Tracks the keystrokes entered to the month field, puts the day entry field in focus after two keystrokes.
        This method is bound to the <KeyPress> event of the month field.
        :param event:
        :return: None
        """
        if event.char.isnumeric():
            self.key_count += 1
            if self.key_count == 2:
                self.key_count = 0
                self.day_entry.select_range(0, END)
                self.day_entry.focus_set()
            self.prev_key_press = None
        else:
            match event.keysym:
                case 'Tab':
                    self.key_count = 0
                case 'ISO_Left_Tab':
                    self.key_count = 0
                    if self.prev_entry is not None:
                        self.prev_entry.focus_set()
                case 'BackSpace':
                    if self.key_count > 0:
                        self.key_count -= 1
                case 'Up':
                    m = int(self.month_var.get())
                    if m < 12:
                        self.month_var.set(str(m + 1))
                    else:
                        self.month_var.set('01')
                    self.month_entry.update()
                case 'KP_Up':
                    m = int(self.month_var.get())
                    if m < 12:
                        self.month_var.set(str(m + 1))
                    else:
                        self.month_var.set('01')
                    self.month_entry.update()
                case 'Down':
                    m = int(self.month_var.get())
                    if m > 1:
                        self.month_var.set(str(m - 1))
                    else:
                        self.month_var.set('12')
                    self.month_entry.update()
                case 'KP_Down':
                    m = int(self.month_var.get())
                    if m > 1:
                        self.month_var.set(str(m - 1))
                    else:
                        self.month_var.set('12')
                    self.month_entry.update()

            self.prev_key_press = event.keysym

    def day_keypress(self, event):
        """
        Tracks the keystrokes entered to the day field, puts the year entry field in focus after two keystrokes.
        This method is bound to the <KeyPress> event of the day entry field.
        :param event:
        :return: None
        """
        if event.char.isnumeric():
            self.key_count += 1
            if self.key_count == 2:
                self.key_count = 0
                self.year_entry.select_range(0, END)
                self.year_entry.focus_set()
            self.prev_key_press = None
        else:
            match event.keysym:
                case 'Tab':
                    self.key_count = 0
                case 'ISO_Left_Tab':
                    self.key_count = 0
                case 'BackSpace':
                    if self.key_count > 0:
                        self.key_count -= 1
                case 'Up':
                    m = int(self.day_var.get())
                    if m < self.max_dom[int(self.month_var.get())]:
                        self.day_var.set(str(m + 1))
                    else:
                        self.day_var.set('01')
                    self.day_entry.update()
                case 'KP_Up':
                    m = int(self.day_var.get())
                    if m < self.max_dom[int(self.month_var.get())]:
                        self.day_var.set(str(m + 1))
                    else:
                        self.day_var.set('01')
                    self.day_entry.update()
                case 'Down':
                    m = int(self.day_var.get())
                    if m > 1:
                        self.day_var.set(str(m - 1))
                    else:
                        self.day_var.set(str(self.max_dom[int(self.month_var.get())]))
                    self.day_entry.update()
                case 'KP_Down':
                    m = int(self.day_var.get())
                    if m > 1:
                        self.day_var.set(str(m - 1))
                    else:
                        self.day_var.set(str(self.max_dom[int(self.month_var.get())]))
                    self.day_entry.update()

            self.prev_key_press = event.keysym

    def year_keypress(self, event):
        """
        Tracks the keystrokes entered to the year field, puts the next entry field on the GUI in focus after two
        keystrokes. This method is bound to the <KeyPress> event of the year entry field.
        :param event:
        :return: None
        """
        if event.char.isnumeric():
            self.key_count += 1
            if self.key_count == 4:
                self.key_count = 0
                self.next_entry.focus_set()
            self.prev_key_press = None
        else:
            match event.keysym:
                case 'Tab':
                    self.key_count = 0
                    self.next_entry.focus_set()
                case 'ISO_Left_Tab':
                    self.key_count = 0
                case 'BackSpace':
                    if self.key_count > 0:
                        self.key_count -= 1
                case 'Up':
                    m = int(self.year_var.get())
                    self.year_var.set(str(m + 1))
                    self.year_entry.update()
                case 'KP_Up':
                    m = int(self.year_var.get())
                    self.year_var.set(str(m + 1))
                    self.year_entry.update()
                case 'Down':
                    m = int(self.year_var.get())
                    if m > 0:
                        self.year_var.set(str(m - 1))
                        self.year_entry.update()
                case 'KP_Down':
                    m = int(self.year_var.get())
                    if m > 1:
                        self.year_var.set(str(m - 1))
                        self.year_entry.update()

            self.prev_key_press = event.keysym

    def validate_date(self, event):
        """
        Validates the month, day and year elements of the date and presents a Messagebox if any is invalid
        This method is bound to the Focus Out event of the year entry field.
        :param event:
        :return: None
        """
        if self.prev_key_press != 'ISO_Left_Tab':
            valid = True
            if self.month_var.get().isnumeric():
                month: int = int(self.month_var.get())
                if not 1 <= month <= 12:
                    self.month_var.set('')
                    self.month_entry.update()
                    self.month_entry.focus_set()
                    valid = False
                if valid:
                    if self.day_var.get().isnumeric():
                        try:
                            day: int = int(self.day_var.get())
                            if not 1 <= day <= self.max_dom[month]:
                                self.day_var.set('')
                                self.day_entry.update()
                                self.day_entry.focus_set()
                                valid = False
                        except KeyError:
                            # This should never happen, as the month has already been validated
                            pass
                        if valid and not self.year_var.get().isnumeric():
                            self.year_var.set('')
                            self.year_entry.update()
                            self.year_entry.focus_set()
                            valid = False
                    else:
                        # If the day is not numeric
                        self.day_var.set('')
                        self.day_entry.update()
                        self.day_entry.focus_set()
                        valid = False
            else:
                # If the month is not numeric
                self.month_var.set('')
                self.month_entry.update()
                self.month_entry.focus_set()
                valid = False
            if valid and int(self.year_var.get()) < 100:
                year = 2000 + int(self.year_var.get())
                self.year_var.set(f'{year:4d}')
                self.year_entry.update()
            if valid:
                self.next_entry.focus_set()
                self.error = False
            else:
                if not self.error:
                    self.error = True
                    dialogs.Messagebox.ok("Date entered is not valid.", "Date Entry Error")

    def get_date(self) -> date:
        """
        Build a date value from the values entered to the month, day and year entry fields.

        :return: datetime.date instance

        """
        month: int = int(self.month_var.get())
        day: int = int(self.day_var.get())
        year: int = int(self.year_var.get())
        return date(year=year, month=month, day=day)

    def set_date(self, date_value: date):
        """
        Set the month, day and year field from the provided date

        :param date_value: the new value for the date widget
        :type date_value: date
        :return: None

        """
        self.month_var.set(str(date_value.month))
        self.day_var.set(str(date_value.day))
        self.year_var.set(str(date_value.year))


class TimeWidget(ttkb.Frame):
    """
    A general purpose date entry widget
    """
    def __init__(self, parent, default_value: time = None):
        """
        Creates widgets.TimeWidget instance
        :param parent: the GUI element that will contain the created widget
        :param default_value: a datetime.time value to be used as an initial value for the hour and minute
        entry fields.
        """
        ttkb.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=2)
        self.hour_var = ttkb.StringVar()
        self.minute_var = ttkb.StringVar()
        self.ampm_var = ttkb.StringVar()
        self.prev_entry = None
        self.next_entry = None
        if default_value is not None:
            fmt_time = default_value.strftime('%I:%M %p')
            self.hour_var.set(fmt_time[0:2])
            self.minute_var.set(fmt_time[3:5])
            self.ampm_var.set(fmt_time[6:8])
        self.hour_entry = ttkb.Entry(self, textvariable=self.hour_var, width=3)
        self.hour_entry.grid(column=0, row=0, sticky=tk.W, ipadx=0, padx=0, pady=5)
        ttkb.Label(self, text=":", width=1, font=('courier', 20, 'bold')).grid(column=1, row=0, sticky=tk.NW, padx=0,
                                                                               pady=5)
        self.hour_entry.bind('<KeyPress>', self.hour_keypress)
        self.hour_entry.bind('<FocusIn>', self.clear_key_count)
        add_validation(self.hour_entry, hour_validator)
        self.minute_entry = ttkb.Entry(self, textvariable=self.minute_var, width=3)
        self.minute_entry.grid(column=2, row=0, sticky=tk.W, ipadx=0, padx=0, pady=5)
        self.minute_entry.bind('<KeyPress>', self.minute_keypress)
        self.minute_entry.bind('<FocusIn>', self.clear_key_count)
        add_validation(self.minute_entry, minute_validator)
        self.am_button = Radiobutton(self, text='AM', value='AM', variable=self.ampm_var, command=self.validate_time)
        self.am_button.grid(column=3, row=0, stick=tk.W, padx=5, pady=5)
        self.pm_button = Radiobutton(self, text='PM', value='PM', variable=self.ampm_var, command=self.validate_time)
        self.pm_button.bind('<FocusOut>', self.validate_time, '+')
        self.pm_button.grid(column=4, row=0, sticky=tk.W, padx=5, pady=5)
        if self.ampm_var.get() not in ['AM', 'PM']:
            self.ampm_var.set('AM')
        self.grid()
        self.key_count = 0
        self.prev_key_press = None
        self.error: bool = False

    def disable(self) -> None:
        """
        Disables the hour and minute fields and the ap/pm radio buttons.

        :return: None

        """
        self.hour_entry.configure(state=DISABLED)
        self.minute_entry.configure(state=DISABLED)
        self.am_button.configure(state=DISABLED)
        self.pm_button.configure(state=DISABLED)

    def enable(self) -> None:
        """
        Enables the hour and minute fields and the am/pm radio buttons.

        :return: None

        """
        self.hour_entry.configure(state=NORMAL)
        self.minute_entry.configure(state=NORMAL)
        self.am_button.configure(state=NORMAL)
        self.pm_button.configure(state=NORMAL)

    def set_prev_entry(self, entry) -> None:
        """
        Establishes the widget that will receive focus when the Back Tab key is pressed in the hour field.

        :param entry:
        :return: None

        """
        self.prev_entry = entry

    def set_next_entry(self, entry):
        """
        Establishes the widget that will receive focus after the am/pm radio buttons

        :param entry:
        :return: None

        """
        self.next_entry = entry

    def focus_set(self) -> None:
        """
        Delegates set focus functionality to the hour field

        :return: None
        """
        self.hour_entry.focus_set()
        self.key_count = 0
        self.prev_key_press = None

    def select_range(self, start, end) -> None:
        """
        Delegates select range to the hour field

        :param start: start position for selection
        :param end: end position for selection
        :return: None

        """
        self.hour_entry.select_range(start, end)

    def clear_key_count(self, event):
        """
        Sets the keystroke counter to 0.  This method is bound to the <FocusIn> event for the hour and minute entry
        fields
        :param event:
        :return: None
        """
        self.key_count = 0

    def hour_keypress(self, event):
        """
        Tracks the keystrokes entered to the hour field, puts the minute entry field on the GUI in focus after two
        keystrokes. This method is bound to the <KeyPress> event of the hour entry field.
        :param event:
        :return: None
        """
        if event.char.isnumeric():
            self.key_count += 1
            if self.key_count == 2:
                self.key_count = 0
                self.minute_entry.select_range(0, END)
                self.minute_entry.focus_set()
            self.prev_key_press = None
        else:
            match event.keysym:
                case 'Tab':
                    self.key_count = 0
                case 'ISO_Left_Tab':
                    self.key_count = 0
                    if self.prev_entry is not None:
                        self.prev_entry.select_range(0, END)
                        self.prev_entry.focus_set()
                case 'BackSpace':
                    if self.key_count > 0:
                        self.key_count -= 1
                case 'Up':
                    h = int(self.hour_var.get())
                    if h < 12:
                        self.hour_var.set(str(h + 1))
                    else:
                        self.hour_var.set('01')
                    self.hour_entry.update()
                case 'KP_Up':
                    h = int(self.hour_var.get())
                    if h < 12:
                        self.hour_var.set(str(h + 1))
                    else:
                        self.hour_var.set('01')
                    self.hour_entry.update()
                case 'Down':
                    h = int(self.hour_var.get())
                    if h > 1:
                        self.hour_var.set(str(h - 1))
                    else:
                        self.hour_var.set('12')
                    self.hour_entry.update()
                case 'KP_Down':
                    h = int(self.hour_var.get())
                    if h > 1:
                        self.hour_var.set(str(h - 1))
                    else:
                        self.hour_var.set('12')
                    self.hour_entry.update()

            self.prev_key_press = event.keysym

    def minute_keypress(self, event):
        """
        Tracks the keystrokes entered to the minute field, puts the next entry field on the GUI  on the GUI in focus
        after two keystrokes. This method is bound to the <KeyPress> event of the hour entry field.
        :param event:
        :return: None
        """
        if event.char.isnumeric():
            self.key_count += 1
            if self.key_count == 2:
                self.key_count = 0
                self.am_button.focus_set()
            self.prev_key_press = None
        else:
            match event.keysym:
                case 'Tab':
                    self.key_count = 0
                case 'ISO_Left_Tab':
                    self.key_count = 0
                case 'BackSpace':
                    if self.key_count > 0:
                        self.key_count -= 1
                case 'Up':
                    m = int(self.minute_var.get())
                    if m < 59:
                        self.minute_var.set(str(m + 1))
                        self.minute_entry.update()
                    else:
                        self.minute_var.set('00')
                case 'KP_Up':
                    m = int(self.minute_var.get())
                    if m < 59:
                        self.minute_var.set(str(m + 1))
                    else:
                        self.minute_var.set('00')
                    self.minute_entry.update()
                case 'Down':
                    m = int(self.minute_var.get())
                    if m > 1:
                        self.minute_var.set(str(m - 1))
                    else:
                        self.minute_var.set('59')
                    self.minute_entry.update()
                case 'KP_Down':
                    m = int(self.minute_var.get())
                    if m > 1:
                        self.minute_var.set(str(m - 1))
                    else:
                        self.minute_var.set('59')
                    self.minute_entry.update()


            self.prev_key_press = event.keysym

    def am_keypress(self, event):
        """
        If the Tab key is pressed when the AM radio button is in focus, skip over the PM button and set the
        focus on the next_entry field if any has been specified
        :param event:
        :return: None
        """
        if event.keysym == 'Tab' and self.next_entry is not None:
            self.next_entry.focus_set()

    def validate_time(self, event=None):
        """
        Validate the hour and minute values, display a MessageBox if either is invalid. This method is bound
        to the Button-1 events on the AM and PM radio buttons
        :param event:
        :return: None
        """
        if self.prev_key_press != 'ISO_Left_Tab':
            valid = True
            if self.hour_entry.get().isnumeric():
                hour = int(self.hour_var.get())
                if not 1 <= hour <= 12:
                    self.hour_var.set('')
                    self.hour_entry.select_range(0, END)
                    self.hour_entry.focus_set()
                    valid = False
                if valid:
                    if self.minute_entry.get().isnumeric():
                        minute = int(self.minute_var.get())
                        if not 0 <= minute <= 60:
                            self.minute_var.set('')
                            self.minute_entry.select_range(0, END)
                            self.minute_entry.focus_set()
                            valid = False
                    else:
                        self.minute_var.set('')
                        self.minute_entry.select_range(0, END)
                        self.minute_entry.focus_set()
                        valid = False
            else:
                self.hour_var.set('')
                self.hour_entry.select_range(0, END)
                self.hour_entry.focus_set()
                valid = False
            if valid:
                if self.next_entry is not None:
                    self.next_entry.focus_set()
                self.error = False
            else:
                if not self.error:
                    dialogs.Messagebox.ok("Time entered is not valid.", "Time Entry Error")
                    self.error = True

    def get_time(self) -> Optional[time]:
        """
        Builds a datetime.time instance using the values entered to the hour and minute entry fields.
        :return: datetime.time instance
        """
        if len(self.hour_var.get().strip()) == 0 or len(self.minute_var.get().strip()) == 0:
            return None
        else:
            hour: int = int(self.hour_var.get())
            minute: int = int(self.minute_var.get())
            ampm: str = self.ampm_var.get()
            if ampm == "PM":
                if hour < 12:
                    hour += 12
            return time(hour=hour, minute=minute)

    def get_datetime(self):
        """
        Returns a datetime instance with a zero date.

        :return: datetime instance
        :rtype: datetime

        """
        dummy = date(year=2022, month=10, day=23)
        return utilities.mk_datetime(dummy, self.get_time())

    def set_time(self, time_value: time) -> None:
        """
        Set the hour, minute and am/pm fields to the provided time

        :param time_value: the new value for the time widget
        :type time_value: time
        :return: None

        """
        hour: int = time_value.hour
        minute: int = time_value.minute
        ampm: str = 'AM'
        if hour >= 12:
            hour -= 12
            ampm = 'PM'
        self.hour_var.set(str(hour))
        self.minute_var.set(str(minute))
        self.ampm_var.set(ampm)

    def set_datetime(self, dt_value: datetime):
        dt, tm = utilities.split_datetime(dt_value)
        self.set_time(tm)


