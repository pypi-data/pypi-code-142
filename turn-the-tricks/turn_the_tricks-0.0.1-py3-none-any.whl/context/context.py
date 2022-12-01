# -*- coding: utf-8 -*-

from overrides import overrides
from typing import Final, Tuple

from PIL import Image

from arcade import (
    Sound,
    Window,
    Texture,
    set_background_color,
    draw_rectangle_filled,
    draw_rectangle_outline,
)
from arcade import run as arcade_run
from arcade import exit as arcade_exit
from arcade.gui import (
    UIAnchorWidget,
    UIBoxLayout,
    UIFlatButton,
    UIManager,
    UIMessageBox,
    UILabel,
    UITextureButton,
)
from arcade.key import R as ARCADE_KEY_R
from arcade.key import P as ARCADE_KEY_P
from arcade.key import N as ARCADE_KEY_N
from arcade.key import LEFT as ARCADE_KEY_LEFT
from arcade.key import RIGHT as ARCADE_KEY_RIGHT
from arcade.key import UP as ARCADE_KEY_UP
from arcade.key import DOWN as ARCADE_KEY_DOWN
from arcade.key import SPACE as ARCADE_KEY_SPACE

from t3.assets.path import (
    EXIT_RUN_NORMAL_PATH,
    EXIT_RUN_HOVERED_PATH,
    EXIT_RUN_PRESSED_PATH,
    FUI_PING_TRIPLET_ECHO_PATH,
    BEATS_A_PATH,
    MAGICAL_FOREST_PATH,
)
from t3.objects.game import Game
from t3.theme.flat import FlatTheme
from t3.variables.block import BLOCK_WIDTH, BLOCK_HEIGHT, BLOCK_MARGIN
from t3.variables.board import BOARD_ROWS, BOARD_COLS
from t3.variables.fonts import GOWUN_DODUM_FONT

SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 800
SCREEN_TITLE: Final[str] = "Turn The Tricks"

MUSIC_VOLUME: Final[float] = 0.3

BACKGROUND_COLOR: Final[Tuple[int, int, int, int]] = (0x0c, 0x1b, 0x23, 0xFF)


# def remove_row(board, row):
#     del board[row]
#     return [[0 for _ in range(BOARD_COLS)]] + board


class Context(Window):
    def __init__(
        self,
        fullscreen=False,
        resizable=False,
        fps=60,
        antialiasing=False,
        vsync=False,
        center_window=False,
        debug=False,
        verbose=0,
    ):
        self._update_rate = 1.0 / fps
        self._debug = debug
        self._verbose = verbose

        super().__init__(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            title=SCREEN_TITLE,
            fullscreen=fullscreen,
            resizable=resizable,
            update_rate=self._update_rate,
            antialiasing=antialiasing,
            vsync=vsync,
            center_window=center_window,
        )

        set_background_color(BACKGROUND_COLOR)

        self._theme = FlatTheme()
        self._game = Game(
            BOARD_COLS,
            BOARD_ROWS,
            BLOCK_WIDTH,
            BLOCK_HEIGHT,
            BLOCK_MARGIN,
        )

        # window_width, window_height = self.get_size()
        # self._game.resize(window_width, window_height)

        # self._music = Sound(CATWALK_OGG_PATH, streaming=True)
        # self._current_player = self._music.play(MUSIC_VOLUME, loop=True)

        self._show_exit_alert = False
        self._exit_alert = self._exit_alert_ui()

        self._main_buttons = self._create_ui()
        self._main_buttons.enable()

        self._stage_clear_uis = self._create_stage_clear_ui()
        self._stage_failed_uis = self._create_stage_failed_ui()
        self._stage_complete_uis = self._create_stage_complete_ui()

        self._sfx_volume = 0.5
        self._error_sound = Sound(FUI_PING_TRIPLET_ECHO_PATH)

        # self._bgm_volume = 0.1
        # self._bgm = Sound(MAGICAL_FOREST_PATH).play(self._bgm_volume, loop=True)

    def play_error_sound(self) -> None:
        self._error_sound.play(self._sfx_volume)

    def _exit_alert_ui(self) -> UIManager:
        uis = UIManager()
        v_box = UIBoxLayout(x=0, y=0, vertical=True, align="center")
        title = UILabel(
            text="Quit the game?",
            font_name=GOWUN_DODUM_FONT,
            font_size=self._theme.title_size,
            text_color=self._theme.foreground,
            bold=True,
        )
        v_box.add(title)

        ok_button = UIFlatButton(
            text="Ok",
            width=200,
            style={"font_name": GOWUN_DODUM_FONT},
        )
        v_box.add(ok_button.with_space_around(top=24, bottom=8))

        @ok_button.event("on_click")
        def on_click_ok(event):
            self.close()

        cancel_button = UIFlatButton(
            text="Cancel",
            width=200,
            style={"font_name": GOWUN_DODUM_FONT},
        )
        v_box.add(cancel_button)

        @cancel_button.event("on_click")
        def on_click_exit(event):
            self.hide_exit_alert_dialog()

        anchor = UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=v_box.with_space_around(left=8, top=8),
        )
        uis.add(anchor)
        return uis

    def _create_stage_clear_ui(self) -> UIManager:
        uis = UIManager()
        v_box = UIBoxLayout(x=0, y=0, vertical=True, align="center")
        title = UILabel(
            text="Complete !",
            font_name=GOWUN_DODUM_FONT,
            font_size=self._theme.title_size,
            text_color=self._theme.foreground,
            bold=True,
        )
        v_box.add(title)

        message = UILabel(
            text="Press any key to go to the next stage",
            font_name=GOWUN_DODUM_FONT,
            font_size=self._theme.subtitle_size,
            text_color=self._theme.foreground,
            bold=True,
        )
        v_box.add(message.with_space_around(top=8))

        anchor = UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=v_box.with_space_around(left=8, top=8),
        )
        uis.add(anchor)
        return uis

    def _create_stage_failed_ui(self) -> UIManager:
        uis = UIManager()
        v_box = UIBoxLayout(x=0, y=0, vertical=True, align="center")
        title = UILabel(
            text="Failure",
            font_name=GOWUN_DODUM_FONT,
            font_size=self._theme.title_size,
            text_color=self._theme.foreground,
            bold=True,
        )
        v_box.add(title)

        message = UILabel(
            text="Press any key to restart",
            font_name=GOWUN_DODUM_FONT,
            font_size=self._theme.subtitle_size,
            text_color=self._theme.foreground,
            bold=True,
        )
        v_box.add(message.with_space_around(top=8))

        anchor = UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=v_box.with_space_around(left=8, top=8),
        )
        uis.add(anchor)
        return uis

    def _create_stage_complete_ui(self) -> UIManager:
        uis = UIManager()
        v_box = UIBoxLayout(x=0, y=0, vertical=True, align="center")
        title = UILabel(
            text="Thanks for playing",
            font_name=GOWUN_DODUM_FONT,
            font_size=self._theme.title_size,
            text_color=self._theme.foreground,
            bold=True,
        )
        v_box.add(title)

        message = UILabel(
            text="Press any key to exit",
            font_name=GOWUN_DODUM_FONT,
            font_size=self._theme.subtitle_size,
            text_color=self._theme.foreground,
            bold=True,
        )
        v_box.add(message.with_space_around(top=8))

        anchor = UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=v_box.with_space_around(left=8, top=8),
        )
        uis.add(anchor)
        return uis

    def _create_ui(self) -> UIManager:
        uis = UIManager()
        v_box = UIBoxLayout(x=0, y=0, vertical=True, align="left")
        exit_run_normal = Texture("ExitRunNormal", Image.open(EXIT_RUN_NORMAL_PATH))
        exit_run_hovered = Texture("ExitRunHovered", Image.open(EXIT_RUN_HOVERED_PATH))
        exit_run_pressed = Texture("ExitRunPressed", Image.open(EXIT_RUN_PRESSED_PATH))
        exit_button = UITextureButton(
            texture=exit_run_normal,
            texture_hovered=exit_run_hovered,
            texture_pressed=exit_run_pressed,
        )
        v_box.add(exit_button.with_space_around(bottom=8))

        @exit_button.event("on_click")
        def on_click_exit(event):
            self.show_exit_alert_dialog()

        title_menu = UIAnchorWidget(
            anchor_x="left",
            anchor_y="top",
            child=v_box.with_space_around(left=8, top=8),
        )
        uis.add(title_menu)
        return uis

    def show_exit_alert_dialog(self) -> None:
        self._show_exit_alert = True
        self._main_buttons.disable()
        self._exit_alert.enable()
        self.play_error_sound()

    def hide_exit_alert_dialog(self) -> None:
        self._show_exit_alert = False
        self._main_buttons.enable()
        self._exit_alert.disable()

    def _draw_result_panel(self) -> None:
        window_width, window_height = self.get_size()
        window_half_width = window_width // 2
        window_half_height = window_height // 2

        panel_width = window_width + 10
        panel_height = 200

        draw_rectangle_filled(
            center_x=window_half_width,
            center_y=window_half_height,
            width=panel_width,
            height=panel_height,
            color=self._theme.background,
        )
        draw_rectangle_outline(
            center_x=window_half_width,
            center_y=window_half_height,
            width=panel_width,
            height=panel_height,
            color=self._theme.foreground,
        )

    @property
    def debug(self) -> bool:
        return self._debug

    @property
    def verbose(self) -> int:
        return self._verbose

    @overrides
    def on_resize(self, width: float, height: float) -> None:
        super().on_resize(width, height)
        self._main_buttons.on_resize(width, height)
        self._game.resize(width, height)

    @overrides
    def on_update(self, delta_time: float) -> None:
        self._main_buttons.on_update(delta_time)
        self._game.update(delta_time)

        if self._game.stage_clear:
            self._main_buttons.disable()
            self._game.disable_buttons()
        elif self._game.stage_failed:
            self._main_buttons.disable()
            self._game.disable_buttons()

    def next_stage(self) -> None:
        if self._game.is_empty_more_stage():
            self.close()
        else:
            self._game.change_next_stage()
            self._main_buttons.enable()
            self._game.enable_buttons()

    def reset_stage(self) -> None:
        self._game.reset()
        self._main_buttons.enable()
        self._game.enable_buttons()

    @overrides
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if self._show_exit_alert:
            return

        if self._game.stage_clear:
            self.next_stage()
            return

        if self._game.stage_failed:
            self.reset_stage()
            return

    @overrides
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        # self._main_buttons.on_key_press(symbol, modifiers)
        # self._exit_alert.on_key_press(symbol, modifiers)
        # self._stage_clear_uis.on_key_press(symbol, modifiers)
        # self._stage_failed_uis.on_key_press(symbol, modifiers)

        if self._show_exit_alert:
            return

        if self._game.stage_clear:
            self.next_stage()
            return

        if self._game.stage_failed:
            self.reset_stage()
            return

        if symbol == ARCADE_KEY_R:
            self._game.reset()
        if symbol == ARCADE_KEY_P:
            self._game.change_prev_stage()
        if symbol == ARCADE_KEY_N:
            self._game.change_next_stage()
        if symbol == ARCADE_KEY_LEFT:
            self._game.move(-1)
        elif symbol == ARCADE_KEY_RIGHT:
            self._game.move(1)
        elif symbol == ARCADE_KEY_DOWN or symbol == ARCADE_KEY_SPACE:
            self._game.hard_drop()
        elif symbol == ARCADE_KEY_UP:
            self._game.rotate()

    @overrides
    def on_draw(self) -> None:
        self.clear()

        if self._show_exit_alert:
            self._exit_alert.draw()
            return

        self._main_buttons.draw()
        self._game.draw()

        if self._game.stage_clear:
            self._draw_result_panel()
            if self._game.is_empty_more_stage():
                self._stage_complete_uis.draw()
            else:
                self._stage_clear_uis.draw()
        elif self._game.stage_failed:
            self._draw_result_panel()
            self._stage_failed_uis.draw()

    def run(self) -> None:
        arcade_run()


def run_context(
    fullscreen=False,
    resizable=False,
    fps=60,
    antialiasing=False,
    vsync=False,
    center_window=False,
    debug=False,
    verbose=0,
) -> None:
    context = Context(
        fullscreen=fullscreen,
        resizable=resizable,
        fps=fps,
        antialiasing=antialiasing,
        vsync=vsync,
        center_window=center_window,
        debug=debug,
        verbose=verbose,
    )
    context.run()
