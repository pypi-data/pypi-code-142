import math
from typing import TypeVar, Generic, List

from springdata.domain.pageable import Pageable

T = TypeVar("T")


class Page(Generic[T]):
    """
    A page is a sublist of a list of objects. It allows gain information about the position of it in the containing
    entire list.
    """

    def __init__(self, content: List[T], pageable: Pageable = None, total: int = None):
        """
        Creates a new :class:`Page`.

        :param content: the content of this page, must not be None.
        :param pageable: the paging information, default to unpaged.
        :param total: the total amount of items available, default to content length. The total might be
                               adapted considering the length of the content given, if it is going to be the content of
                               the last page. This is in place to mitigate inconsistencies.
        """
        if content is None:
            raise ValueError("Content must not be None")
        self.content = content
        self.pageable = pageable or Pageable.unpaged()
        if total is None:
            self.total_elements = len(content)
        elif (
            len(content) > 0
            and self.pageable.is_paged()
            and self.pageable.offset + self.pageable.page_size > total
        ):
            self.total_elements = self.pageable.offset + len(content)
        else:
            self.total_elements = total

    @classmethod
    def empty(cls, pageable: Pageable = None) -> "Page":
        """
        Creates a new empty :class:`Page`.

        :return:
        """
        return Page([], pageable, 0)

    @property
    def number(self) -> int:
        """
        Returns the number of the current :class:`Page`.

        :return: the number of the current :class:`Page`.
        """
        return self.pageable.page_number if self.pageable.is_paged() else 0

    @property
    def number_of_elements(self) -> int:
        """
        Returns the number of elements currently on this :class:`Page`.

        :return: the number of elements currently on this :class:`Page`.
        """
        return len(self.content)

    @property
    def size(self) -> int:
        """
        Returns the size of the :class:`Page`.

        :return: the size of the :class:`Page`.
        """
        return (
            self.pageable.page_size if self.pageable.is_paged() else len(self.content)
        )

    @property
    def total_pages(self) -> int:
        """
        Returns the number of total pages.

        :return: the number of total pages.
        """
        return (
            1
            if self.size == 0 or self.total_elements is None
            else math.ceil(self.total_elements / self.size)
        )

    def has_content(self) -> bool:
        """
        Returns if the :class:`Page` has content at all.

        :return:
        """
        return bool(self.content)

    def has_next(self) -> bool:
        """
        Returns if there is a next :class:`Page`.

        :return: if there is a next :class:`Page`.
        """
        return self.number + 1 < self.total_pages

    def has_previous(self) -> bool:
        """
        Returns if there is a previous :class:`Page`.

        :return: if there is a previous :class:`Page`.
        """
        return self.number > 0

    def is_first(self) -> bool:
        """
        Returns if the current :class:`Page` is the first one.

        :return:
        """
        return not self.has_previous()

    def is_last(self) -> bool:
        """
        Returns if the current :class:`Page` is the last one.

        :return:
        """
        return not self.has_next()

    def next_pageable(self) -> Pageable:
        """
        Returns the :class:`Pageable` to request the next :class:`Page`.

        :return:
        """
        return self.pageable.next() if self.has_next() else Pageable.unpaged()

    def previous_pageable(self) -> Pageable:
        """
        Returns the :class:`Pageable` to request the previous :class:`Page`.

        :return:
        """
        return (
            self.pageable.previous_or_first()
            if self.has_previous()
            else Pageable.unpaged()
        )
