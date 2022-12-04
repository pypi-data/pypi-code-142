"""This module provides a class for handling strings: add color, bold, etc."""


class PString:
    """A class for adding styles to string.

    Parameters
    ----------
    first_arg : str
    *args : str
        if more than one argument is given, they are joined together by a space

    Attributes
    ----------
    string : str
        the string with styles added
    """

    def __init__(self, first_arg, *args):
        self.string = str(first_arg)
        for arg in args:
            self.string += " " + str(arg)

        self.string += "\033[0m"

    def __repr__(self):
        return self.string

    def __add__(self, other):
        return PString(self.string + other.string)

    @staticmethod
    def available_styles():
        """Print all available styles

        Returns
        -------
        list
            a list of available styles (method names)
        """

        styles = [func for func in dir(PString)
                  if callable(getattr(PString, func))
                  and not func.startswith("__")
                  and not func == "available_styles"
                  and not func == "print"]

        PString("Available styles:").bold().g().underline().print()
        for style in styles:
            style_desc = getattr(PString, style).__doc__.replace("Make string ", "")
            style_desc_with_style = getattr(PString, style)(PString(style_desc))

            print(PString(f"{style+'()':<15}").bold(), style_desc_with_style)

        return styles

    def print(self, **kwargs):
        """Print string"""
        print(self.string, **kwargs)

    def r(self):
        """Make string red"""
        self.string = "\033[31m" + self.string
        return self

    def g(self):
        """Make string green"""
        self.string = "\033[32m" + self.string
        return self

    def y(self):
        """Make string yellow"""
        self.string = "\033[33m" + self.string
        return self

    def b(self):
        """Make string blue"""
        self.string = "\033[34m" + self.string
        return self

    def w(self):
        """Make string white"""
        self.string = "\033[37m" + self.string
        return self

    def bg_r(self):
        """Make string background red"""
        self.string = "\033[41m" + self.string
        return self

    def bg_g(self):
        """Make string background green"""
        self.string = "\033[42m" + self.string
        return self

    def bg_y(self):
        """Make string background yellow"""
        self.string = "\033[43m" + self.string
        return self

    def bg_b(self):
        """Make string background blue"""
        self.string = "\033[44m" + self.string
        return self

    def bg_w(self):
        """Make string background white"""
        self.string = "\033[47m" + self.string
        return self

    def bold(self):
        """Make string bold"""
        self.string = "\033[1m" + self.string
        return self

    def italic(self):
        """Make string italic"""
        self.string = "\033[3m" + self.string
        return self

    def underline(self):
        """Make string underlined"""
        self.string = "\033[4m" + self.string
        return self
