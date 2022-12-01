"This module contains constansts for Appstream"

from typing import Literal

URL_TYPES_LITERAL = Literal[
    "homepage",
    "bugtracker",
    "faq",
    "help",
    "donation",
    "translate",
    "contact",
    "vcs-browser",
    "contribute"
]

OARS_ATTRIBUTE_TYPES_LITERAL = [
    "violence-cartoon",
    "violence-fantasy",
    "violence-realistic",
    "violence-bloodshed",
    "violence-sexual",
    "violence-desecration",
    "violence-slavery",
    "drugs-alcohol",
    "drugs-narcotics",
    "drugs_tobacco",
    "sex_nudity",
    "sex-themes",
    "language-profanity",
    "language-humor",
    "language-discrimination",
    "money-advertising",
    "money-gambling",
    "money-purchasing",
    "social-chat",
    "social-audio",
    "social-contacts",
    "social-info",
    "social-location"
]

OARS_VALUE_TYPES_LITERAL = [
    "none",
    "mild",
    "moderate",
    "intense"
]

PROVIDES_TYPES_LITERAL = [
    "mediatype",
    "library",
    "binary",
    "font",
    "modalias",
    "firmware",
    "python2",
    "python3",
    "dbus",
    "id"
]

CONTROL_TYPES_LITERAL = Literal[
    "pointing",
    "keyboard",
    "console",
    "tablet",
    "touch",
    "gamepad",
    "tv-remote",
    "voice",
    "vision"
]

INTERNET_RELATION_VALUE_LITERAL = Literal[
    "always"
    "offline-only"
    "first-run"
]

URL_TYPES = list(URL_TYPES_LITERAL)
"All URL types"

OARS_ATTRIBUTE_TYPES = list(OARS_ATTRIBUTE_TYPES_LITERAL)
"All aviable OARS attributes"

OARS_VALUE_TYPES = list(OARS_VALUE_TYPES_LITERAL)
"All ORAS value types"

PROVIDES_TYPES = list(PROVIDES_TYPES_LITERAL)
"The list with all types for provides"

CONTROL_TYPES = list(CONTROL_TYPES_LITERAL)
"The list with all possible values for control"

INTERNET_RELATION_VALUE = list(INTERNET_RELATION_VALUE_LITERAL)
"The list with all possible values for internet"
