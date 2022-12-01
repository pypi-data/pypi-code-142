# -*- coding: utf-8 -*-

from copy import deepcopy
from math import floor
from typing import Optional, Tuple

from PIL import Image

from arcade import Sound, Texture, draw_text, draw_line, draw_rectangle_outline
from arcade.gui import (
    UIAnchorWidget,
    UIBoxLayout,
    UIFlatButton,
    UIManager,
    UIMessageBox,
    UILabel,
    UITextureButton,
)


from t3.assets.path import (
    REFRESH_NORMAL_PATH,
    REFRESH_HOVERED_PATH,
    REFRESH_PRESSED_PATH,
    ARROW_LEFT_NORMAL_PATH,
    ARROW_LEFT_HOVERED_PATH,
    ARROW_LEFT_PRESSED_PATH,
    ARROW_RIGHT_NORMAL_PATH,
    ARROW_RIGHT_HOVERED_PATH,
    ARROW_RIGHT_PRESSED_PATH,
    BUTTON_05_PATH,
    FUI_PING_TRIPLET_ECHO_PATH,
    WALLET_CLOSE_PATH,
    MI_SFX_42_PATH,
)
from t3.objects.block import (
    E,
    Matrix,
    create_block_textures,
    rotate_clockwise,
    is_active_block,
)
from t3.objects.board import Board
from t3.objects.history import History
from t3.stages.stages import create_stages
from t3.theme.flat import FlatTheme
from t3.theme.theme import Theme
from t3.variables.block import BLOCK_WIDTH, BLOCK_HEIGHT, BLOCK_MARGIN
from t3.variables.board import BOARD_COLS, BOARD_ROWS


class Game:
    def __init__(
        self,
        board_cols=BOARD_COLS,
        board_rows=BOARD_ROWS,
        block_width=BLOCK_WIDTH,
        block_height=BLOCK_HEIGHT,
        block_margin=BLOCK_MARGIN,
        theme: Optional[Theme] = None,
    ):
        self._theme = theme if theme else FlatTheme()
        self._block_textures = create_block_textures(
            block_width,
            block_height,
            self._theme,
        )

        self._sfx_volume = 0.5

        self._board = Board(
            board_cols,
            board_rows,
            block_width,
            block_height,
            block_margin,
            self._block_textures,
        )

        self._total_delta = 0.0
        self._drop_delta = 0.0
        self._drop_threshold = 1.0

        self._stage_clear = False
        self._stage_failed = False
        self._game_over = False
        self._paused = False

        self._cursor_board: Optional[Board] = None
        self._cursor_x = 0
        self._cursor_y = 0

        self._drop_matrix: Optional[Matrix] = None
        self._drop_x = 0
        self._drop_y = 0

        self._stages = create_stages()
        self._stage = 0

        self._buttons = self._create_buttons()
        self._buttons.enable()

        self._history = History(
            self._theme.history_size,
            self._board.block_width,
            self._board.block_height,
            self._board.block_margin,
            self._theme.history_cap_width,
            self._block_textures,
        )

        self.reset()

        self._move_sound = Sound(WALLET_CLOSE_PATH)
        self._error_sound = Sound(MI_SFX_42_PATH)
        self._drop_sound = Sound(BUTTON_05_PATH)

    @property
    def stage_clear(self) -> bool:
        return self._stage_clear

    @property
    def stage_failed(self) -> bool:
        return self._stage_failed

    def is_empty_more_stage(self) -> bool:
        return self._stage == 10

    def enable_buttons(self) -> None:
        return self._buttons.enable()

    def disable_buttons(self) -> None:
        return self._buttons.disable()

    def _create_buttons(self) -> UIManager:
        refresh_normal = Texture("RefreshNormal", Image.open(REFRESH_NORMAL_PATH))
        refresh_hovered = Texture("RefreshHovered", Image.open(REFRESH_HOVERED_PATH))
        refresh_pressed = Texture("RefreshPressed", Image.open(REFRESH_PRESSED_PATH))
        refresh_button = UITextureButton(
            texture=refresh_normal,
            texture_hovered=refresh_hovered,
            texture_pressed=refresh_pressed,
        )

        @refresh_button.event("on_click")
        def on_click_refresh(event):
            self.reset()

        # right_normal = Texture("RightNormal", Image.open(ARROW_RIGHT_NORMAL_PATH))
        # right_hovered = Texture("RightHovered", Image.open(ARROW_RIGHT_HOVERED_PATH))
        # right_pressed = Texture("RightPressed", Image.open(ARROW_RIGHT_PRESSED_PATH))
        # right_button = UITextureButton(
        #     texture=right_normal,
        #     texture_hovered=right_hovered,
        #     texture_pressed=right_pressed,
        # )

        # left_normal = Texture("LeftNormal", Image.open(ARROW_LEFT_NORMAL_PATH))
        # left_hovered = Texture("LeftHovered", Image.open(ARROW_LEFT_HOVERED_PATH))
        # left_pressed = Texture("LeftPressed", Image.open(ARROW_LEFT_PRESSED_PATH))
        # left_button = UITextureButton(
        #     texture=left_normal,
        #     texture_hovered=left_hovered,
        #     texture_pressed=left_pressed,
        # )

        v_box = UIBoxLayout(vertical=True, align="center")
        v_box.add(refresh_button)
        # v_box.add(right_button.with_space_around(top=4))
        # v_box.add(left_button.with_space_around(top=4))

        top_padding = (refresh_normal.height // 2) * len(v_box.children)
        right_padding = (refresh_normal.width // 2) + self._theme.margin_width
        align_x = -1 * (self._board.half_width + right_padding)
        align_y = self._board.half_height - top_padding

        anchor = UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            align_x=align_x,
            align_y=align_y,
            child=v_box,
        )

        uis = UIManager()
        uis.add(anchor)
        return uis

    def reset(self) -> None:
        self.change_stage(self._stage)

    def change_next_stage(self) -> None:
        if self._stage + 1 >= len(self._stages):
            return
        self._stage += 1
        self.change_stage(self._stage)

    def change_prev_stage(self) -> None:
        if self._stage - 1 < 0:
            return
        self._stage -= 1
        self.change_stage(self._stage)

    def change_stage(self, stage_index: int) -> None:
        self._stage_clear = False
        self._stage_failed = False

        stage = self._stages[stage_index]
        self._board.set_matrix(deepcopy(stage.board[::-1]))
        self._history.set_history(deepcopy(stage.history))
        self.next_block()

    def resize(self, width: float, height: float) -> None:
        half_width = width // 2
        half_height = height // 2
        x = floor(half_width - self._board.half_width)
        y = floor(half_height - self._board.half_height)
        offset_x = x if x > 0 else 0
        offset_y = y if y > 0 else 0

        self._board.update_offset(offset_x, offset_y)
        self._history.update_offset(
            self._board.right + self._theme.margin_width,
            self._board.bottom,
        )
        self.update_cursor()
        self.update_hard_drop_matrix()

    def update(self, delta_time: float) -> None:
        self._total_delta += delta_time

    def _draw_border(self) -> None:
        left = self._board.left - self._board.block_margin
        right = self._board.right + self._board.block_margin
        top = self._board.top - self._board.block_margin
        bottom = self._board.bottom + self._board.block_margin

        draw_line(
            start_x=left,
            start_y=top,
            end_x=left,
            end_y=bottom,
            color=self._theme.foreground,
            line_width=self._theme.border_width,
        )

        draw_line(
            start_x=right,
            start_y=top,
            end_x=right,
            end_y=bottom,
            color=self._theme.foreground,
            line_width=self._theme.border_width,
        )

    def _draw_right_panel(self) -> None:
        x = self._board.right + self._theme.margin_width
        top = self._board.top - self._board.block_margin

        draw_text(
            text=f"STAGE {self._stage}",
            start_x=x + (self._board.block_margin * 2),
            start_y=top,
            color=self._theme.foreground,
            font_size=self._theme.subtitle_size,
            font_name=self._theme.font_name,
            bold=True,
            anchor_x="left",
            anchor_y="top",
        )

        next_top = top - 30
        draw_text(
            text=f"REMAIN {self._history.size}",
            start_x=x + (self._board.block_margin * 2),
            start_y=next_top,
            color=self._theme.foreground,
            font_size=self._theme.subtitle_size,
            font_name=self._theme.font_name,
            bold=True,
            anchor_x="left",
            anchor_y="top",
        )

    def draw(self):
        self._board.draw()
        self._draw_border()
        self._draw_right_panel()
        self._history.draw()

        if self._cursor_board:
            self._cursor_board.draw()

        if self._drop_matrix is not None:
            self._draw_drop_matrix()

        self._buttons.draw()

    def _draw_drop_matrix(self) -> None:
        assert self._drop_matrix is not None

        left = self._board.left
        bottom = self._board.bottom

        for row in range(len(self._drop_matrix)):
            for col in range(len(self._drop_matrix[0])):
                value = self._drop_matrix[row][col]
                if not is_active_block(value):
                    continue

                x = self._drop_x + col
                y = self._drop_y + row
                center = self._board.measure_block_center(x, y)
                width = self._board.block_width
                height = self._board.block_height

                draw_rectangle_outline(
                    left + center[0],
                    bottom + center[1],
                    width,
                    height,
                    self._theme.accent,
                )

    def next_block(self) -> None:
        self._cursor_board = self._history.pop()

        half_cols = self._board.cols // 2
        half_cursor_block_cols = self._cursor_board.cols // 2
        self._cursor_x = half_cols - half_cursor_block_cols
        self._cursor_y = 0

        self.update_cursor()
        self.update_hard_drop_matrix()

    def update_cursor(self) -> None:
        left = self._board.left
        bottom = self._board.bottom
        block_width = self._board.block_width
        block_margin = self._board.block_margin
        offset_x = left + (block_width + block_margin) * self._cursor_x
        offset_y = bottom

        self._cursor_board.update_offset(offset_x, offset_y)

    def move(self, delta_x: int) -> None:
        if self._cursor_board is None:
            return

        board_cols = self._board.cols
        cursor_block_cols = self._cursor_board.cols
        max_x = board_cols - cursor_block_cols
        next_x = self._cursor_x + delta_x

        stop_flag = False

        if next_x < 0:
            next_x = 0
            stop_flag = True
        if next_x > max_x:
            next_x = max_x
            stop_flag = True

        cursor_matrix = self._cursor_board.matrix
        if not self._board.check_collision(cursor_matrix, next_x, self._cursor_y):
            self._cursor_x = next_x
            self.update_cursor()
            self.update_hard_drop_matrix()

        if stop_flag:
            self.play_error_sound()
        else:
            self.play_move_sound()

    def update_hard_drop_matrix(self) -> None:
        hard_drop_position = self.get_hard_drop_position()
        if hard_drop_position is not None:
            self._drop_matrix = deepcopy(self._cursor_board.matrix)
            self._drop_x = hard_drop_position[0]
            self._drop_y = hard_drop_position[1]
        else:
            self._drop_matrix = None
            self._drop_x = 0
            self._drop_y = 0

    def rotate(self):
        rotated_block = rotate_clockwise(self._cursor_board.matrix)
        rotated_block_width = len(rotated_block[0])

        board_cols = self._board.cols
        if self._cursor_x + rotated_block_width >= board_cols:
            next_x = board_cols - rotated_block_width
        else:
            next_x = self._cursor_x
        if not self._board.check_collision(rotated_block, next_x, self._cursor_y):
            self._cursor_board.set_matrix(rotated_block)
            self._cursor_x = next_x
            self.update_cursor()
            self.update_hard_drop_matrix()
            self.play_move_sound()
        else:
            self.play_error_sound()

    def get_hard_drop_position(self) -> Optional[Tuple[int, int]]:
        cursor_matrix = self._cursor_board.matrix
        x = self._cursor_x
        max_y = self._board.rows - self._cursor_board.rows
        for y in range(self._cursor_y, max_y + 1, 1):
            if self._board.check_intersection(cursor_matrix, x, y):
                if self._board.check_insertable(cursor_matrix, x, y):
                    return x, y
                else:
                    return None
        return None

    def play_move_sound(self) -> None:
        self._move_sound.play(self._sfx_volume)

    def play_error_sound(self) -> None:
        self._error_sound.play(self._sfx_volume)

    def play_drop_sound(self) -> None:
        self._drop_sound.play(self._sfx_volume)

    def hard_drop(self) -> None:
        if self._drop_matrix is None:
            return

        self.play_drop_sound()

        self._board.fill_matrix(self._drop_matrix, self._drop_x, self._drop_y, E)
        self._board.update_textures()

        self._drop_matrix = None
        self._drop_x = 0
        self._drop_y = 0

        if self._history.size >= 1:
            self.next_block()
            self._history.update_textures()
        else:
            self._cursor_board = None
            self._cursor_x = 0
            self._cursor_y = 0

            if self._board.is_all_inactive():
                self.on_stage_clear()
            else:
                self.on_stage_failed()

    def on_stage_clear(self) -> None:
        self._stage_clear = True
        self._stage_failed = False

    def on_stage_failed(self) -> None:
        self._stage_clear = False
        self._stage_failed = True
