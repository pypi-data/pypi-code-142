# songbook-latex -- python package for generating formatted songs with chords in LaTeX
# Copyright (C) 2022  Karol Ważny

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

def insert_at(text: str, inserted_text: str, starting_index: int) -> str:
    if starting_index <= 0:
        return inserted_text + text
    if starting_index >= len(text):
        return text + inserted_text
    return text[:starting_index] + inserted_text + text[starting_index:]
