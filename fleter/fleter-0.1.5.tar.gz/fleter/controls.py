import flet
from typing import Optional, Literal
from flet import icons, TextAlign
from flet.control import Control
from flet.dropdown import Option
from fleter import buttons

__all__ = [
    "animation_show",
    "empty",
    "enabled_harmonysans",
    "enable_material3_theme",
    "disable_material3_theme",
    "AudioControlBar",
    "ComboBox",
    "Editor",
    "HeaderBar",
    "Manage",
    "NoteBook",
    "SpinBox",
    "Time",
]


def animation_show(container: flet.Container, time=300):
    container.animate_opacity = 0
    container.opacity = False
    container.animate_opacity = time
    container.opacity = True
    container.update()


def empty(_1=None, _2=None, _3=None, _4=None, _5=None):
    pass


def enabled_harmonysans(page: flet.Page):
    from pathlib import Path
    harmony_sans = str(Path(__file__).parent).replace("\\", "//") + "//font//HarmonySans.ttc"
    harmony_sans_bold = str(Path(__file__).parent).replace("\\", "//") + "//font//HarmonySansBold.ttc"
    harmony_sans_light = str(Path(__file__).parent).replace("\\", "//") + "//font//HarmonySansLight.ttc"
    page.fonts = {
        "HarmonySans": harmony_sans,
        "HarmonySans Bold": harmony_sans_bold,
        "HarmonySans Light": harmony_sans_light,
    }
    page.theme = flet.Theme(font_family="HarmonySans")


def enable_material3_theme(page: flet.Page):
    theme = flet.theme.Theme()
    theme.use_material3 = True
    page.theme = theme


def disable_material3_theme(page: flet.Page):
    theme = flet.theme.Theme()
    theme.use_material3 = False
    page.theme = theme


class AudioControlBar(flet.Row):
    def __init__(self):
        super().__init__()

        self._play_button = flet.IconButton()


class ComboBox(flet.Dropdown):
    def __init__(self,
                 #
                 # DropDown Specific
                 #
                 value: Optional[str] = None,
                 autofocus: Optional[bool] = None,
                 options: Optional[str] = [""],
                 on_change=None,
                 on_focus=None,
                 on_blur=None,
                 ):
        super(ComboBox, self).__init__()

        self._option = []
        self._options = options

        self.option = self._options

    @property
    def option(self):
        return self._option

    @option.setter
    def option(self, list):
        self._options = list

        for item in self._options:
            item_type = type(item).__name__
            if item_type == "list" or item_type == "tuple":
                disabled = item[1]
                self._option.append(Option(item[0], disabled=disabled))
            else:
                self._option.append(Option(item))
        self.options = self._option


class Editor(flet.TextField):
    def __init__(self):
        super().__init__(min_lines=100000, expand=True, multiline=True)


class HeaderBar(flet.Row):
    def __init__(self,
                 page: flet.Page,
                 has_close: bool = True,
                 has_maximize: bool = False,
                 has_minimize: bool = False,
                 frameless: bool = False,
                 title: str = "",
                 title_align: TextAlign = "center",
                 ):
        """

        :param page: 为被设置页面窗口
        :param has_close: 决定是否有关闭按钮
        :param title: 设置标题栏的标题
        :param title_align: 设置标题栏的标题对齐
        """
        super(HeaderBar, self).__init__()
        self._page = page
        if frameless:
            self._page.window_frameless = True
        else:
            self._page.window_title_bar_hidden = True
            self._page.window_title_bar_buttons_hidden = True

        self._title = title
        self._page.title = title

        self._title_widget = flet.Text(title, size=18, text_align=title_align)
        self._title_area = flet.Container(self._title_widget, padding=15)
        self._darg_area = flet.WindowDragArea(self._title_area, expand=True)

        self.controls.append(
            self._darg_area,
        )

        self._has_close = has_close

        self._has_maximize = has_maximize

        self._has_minimize = has_minimize

        self._close_button = None

        self._maximize_button = None

        self._minimize_button = None

        if has_minimize:
            self._minimize_button = buttons.MinimizeButton(self._page)
            self.controls.append(
                self._minimize_button
            )

        if has_maximize:
            self._maximize_button = buttons.MaximizeButton(self._page)
            self.controls.append(
                self._maximize_button
            )

        if has_close:
            self._close_button = buttons.CloseButton(self._page)
            self.controls.append(
                self._close_button
            )

    @property
    def title_align(self):
        return self._title_widget.text_align

    @title_align.setter
    def title_align(self, align: TextAlign = "center"):
        self._title_widget.text_align = align

    @property
    def has_close(self):
        return self._has_close

    @has_close.setter
    def has_close(self, has: bool):
        if self._has_close:
            if not has:
                try:
                    self.controls.remove(self._close_button)
                except:
                    pass
        elif not self._has_close:
            if has:
                self._close_button = buttons.CloseButton(self._page)
                self.controls.append(
                    self._close_button
                )
        self._has_close = has

    @property
    def has_maximize(self):
        return self._has_maximize

    @has_maximize.setter
    def has_maximize(self, has: bool):
        if self._has_maximize:
            if not has:
                try:
                    self.controls.remove(self._maximize_button)
                except:
                    pass
        elif not self._has_maximize:
            if has:
                self._maximize_button = buttons.MaximizeButton(self._page)
                self.controls.append(
                    self._maximize_button
                )
        self._has_maximize = has

    @property
    def has_minimize(self):
        return self._has_minimize

    @has_minimize.setter
    def has_minimize(self, has: bool):
        if self._has_minimize:
            if not has:
                try:
                    self.controls.remove(self._minimize_button)
                except:
                    pass
        elif not self._has_minimize:
            if has:
                self._minimize_button = buttons.MinimizeButton(self._page)
                self.controls.append(
                    self._minimize_button
                )
        self._has_minimize = has

    @property
    def title(self):
        return self._title_widget.value

    @title.setter
    def title(self, title: str):
        self._title_widget.value = title

    @property
    def title_widget(self):
        return self._title_widget

    @title_widget.setter
    def title_widget(self, widget):
        self._title_widget = widget

    @property
    def title_area(self):
        return self._title_area

    @property
    def darg_area(self):
        return self._darg_area

    @property
    def close_button(self) -> Control:
        try:
            return self._close_button
        except:
            return None

    @close_button.setter
    def close_button(self, control: Control):
        self._close_button = control

    @property
    def maximize_button(self) -> Control:
        try:
            return self._maximize_button
        except:
            return None

    @maximize_button.setter
    def maximize_button(self, control: Control):
        self._maximize_button = control

    @property
    def minimize_button(self) -> Control:
        try:
            return self._minimize_button
        except:
            return None

    @minimize_button.setter
    def minimize_button(self, control: Control):
        self._minimize_button = control

    def show(self):
        self._page.add(self)


class Manage(object):
    def __init__(self, page: flet.Page):
        self.build(page)

    def build(self, page: flet.Page):
        self._page = page
        self._page.update()

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page: flet.Page):
        self.page = page

    def resize(self, width: int = None, height: int = None):
        if width is not None:
            self._page.window_width = width
        if height is not None:
            self._page.window_height = height

    def create_titlebar(self, has_close: bool = True,
                        title: str = "",
                        title_align: Literal["left", "right", "center", "justify", "start", "end"] | None = "left"):
        titlebar = HeaderBar(self._page, has_close=has_close, title=title, title_align=title_align)
        titlebar.show()
        return titlebar


class NoteBook(flet.Tabs):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create(self, text: str = "", content=None, note_content=None, icon=None):
        tab = flet.Tab(text=text, content=content, tab_content=note_content, icon=icon)
        return tab

    def create_with_can_close(self, text: str = "", content=None, tooltip="close control", on_close=None, icon=None,
                              close_tip: bool = False, close_tip_title="Close tab",
                              close_tip_shape=flet.CountinuosRectangleBorder(radius=18),
                              close_tip_message="Are you sure you want to close this tab", close_tip_yes="Yes",
                              close_tip_no="No"):
        if on_close is None:
            if close_tip:
                def close(evt):
                    def close_dialog(evt=None):
                        ok.open = False
                        self.page.update()

                    def remove(evt):
                        self.remove(tab)
                        ok.open = False
                        self.page.update()

                    ok = flet.AlertDialog(
                        title=flet.Text(value=close_tip_title),
                        content=flet.Text(value=close_tip_message),
                        shape=close_tip_shape,
                        actions=[
                            flet.TextButton(close_tip_yes, on_click=remove),
                            flet.TextButton(close_tip_no, on_click=close_dialog),
                        ],
                        on_dismiss=close_dialog,
                        actions_alignment="end",
                    )
                    self.page.dialog = ok
                    ok.open = True
                    self.page.update()

                on_close = close
            else:
                def close(evt):
                    self.remove(tab)

                on_close = close
        row = flet.Row(
            [
                flet.Text(value=text),
                flet.IconButton(icon=icons.CLOSE_ROUNDED, tooltip=tooltip, icon_size=15, on_click=on_close)
            ]
        )
        tab = self.create(content=content,
                          note_content=row
                          )
        return tab

    def create_with_add(self, *args, **kwargs):
        self.add(self.create(*args, **kwargs))

    def create_with_add_can_close(self, *args, **kwargs):
        self.add(self.create_with_can_close(*args, **kwargs))

    def add_control(self, text: str = "", content=None, note_content=None):
        self.add(self.create(text=text, content=content, note_content=note_content))

    def add_control_with_can_close(self, text: str = "", content=None, tooltip="close control", on_close=None,
                                   close_tip: bool = False, close_tip_title="Close tab",
                                   close_tip_shape=flet.CountinuosRectangleBorder(radius=18),
                                   close_tip_message="Are you sure you want to close this tab",
                                   close_tip_yes="Yes", close_tip_no="No",
                                   *args, **kwargs):
        self.add(self.create_with_can_close(text=text, content=content, tooltip=tooltip, on_close=on_close,
                                            close_tip=close_tip, close_tip_title=close_tip_title,
                                            close_tip_shape=close_tip_shape,
                                            close_tip_message=close_tip_message,
                                            close_tip_yes=close_tip_yes, close_tip_no=close_tip_no))

    def add(self, tab):
        self.tabs.append(tab)

    def insert(self, index, tab):
        self.tabs.insert(index, tab)
        self.update()

    def clear(self):
        self.tabs.clear()

    def remove(self, tab):
        self.tabs.remove(tab)
        self.update()


class SpinBox(flet.Row):
    def __init__(self, value: int = 0, plus=1, minus=1, max_value: int = None, min_value: int = None):
        super().__init__()
        self._max_value = max_value
        self._min_value = min_value

        self._plus_button = flet.IconButton(icon=icons.ADD_ROUNDED, on_click=self.plus_value)
        self._minus_button = flet.IconButton(icon=icons.REMOVE_ROUNDED, on_click=self.minus_value)

        self._plus = plus
        self._minus = minus

        self._value = value

        self._sphin_text = flet.TextField(value=value, border_radius=50, text_align="center", width=160, height=55)

        if self._min_value > self._value:
            self.sphin_text.value = self._max_value

        if self._max_value < self._value:
            self.sphin_text.value = self._max_value

        self.controls = (
            self._minus_button,
            self._sphin_text,
            self._plus_button,
        )

    def plus_value(self, *args, **kwargs) -> None:
        if self._max_value is not None:
            if self._sphin_text.value < self._max_value:
                self._sphin_text.value = self._sphin_text.value + self._plus
        else:
            self._sphin_text.value = self._sphin_text.value + self._plus
        self._sphin_text.update()

    def minus_value(self, *args, **kwargs) -> None:
        if self._min_value is not None:
            if self._sphin_text.value > self._min_value:
                self._sphin_text.value = self._sphin_text.value - self._minus
        else:
            self._sphin_text.value = self._sphin_text.value - self._minus
        self._sphin_text.update()

    @property
    def plus(self):
        return self._plus

    @plus.setter
    def plus(self, value: int):
        self._plus = value

    @property
    def minus(self):
        return self._minus

    @minus.setter
    def minus(self, value: int):
        self._minus = value

    @property
    def sphin_text(self) -> flet.TextField:
        return self._sphin_text

    @property
    def plus_button(self) -> flet.IconButton:
        return self._plus_button

    @property
    def minus_button(self) -> flet.IconButton:
        return self._minus_button

    @property
    def value(self):
        return self._sphin_text.value

    @value.setter
    def value(self, value: int):
        self._sphin_text.value = value

    @property
    def max_value(self):
        return self._max_value

    @max_value.setter
    def max_value(self, value: int):
        self._max_value = value

    @property
    def min_value(self):
        return self._min_value

    @min_value.setter
    def min_value(self, value: int):
        self._min_value = value


class Time(object):
    def __init__(self, on_tick=empty):
        self.build(on_tick)

    @property
    def on_tick(self):
        return self._on_tick

    @on_tick.setter
    def on_tick(self, function):
        self._on_tick = function

    def start(self, id: int or str = 0, time: int = 10):
        from threading import Thread
        from time import sleep

        def main():
            for _time in range(time):
                sleep(1)
                self._on_tick(id, _time + 1)

        Thread(target=main).start()

    def build(self, on_tick=None):
        self._on_tick = on_tick


class Widget(flet.UserControl):
    def build(self):
        pass


if __name__ == '__main__':
    def main(page: flet.Page):
        enabled_harmonysans(page)
        notebook = NoteBook()
        tab1 = notebook.create("Hello")
        tab2 = notebook.create_with_can_close()
        notebook.add(tab1)

        page.add(
            notebook
        )
        page.update()


    flet.app(target=main)
