"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

import re

ASSIGNMENT = re.compile(
    r"""
    # (1) .. location (optional)
    (?P<where>(?:.*?)?)\s?
    # (2) .. time of court date
    (?P<time>\d{2}:\s?\d{2})\s
    # (3) .. docket number
    (?P<docket>\d{2,3}\sU?Js\s\d+\/\d{2})\s
    # (4) .. name(s) of prosecutor(s), namely ..
    (?P<assigned>
        (?:
            # (a) .. last name & doctoral degree (optional)
            (?:(?:Dr\.\s)?[\u00C0-\u017F\w-]+)
            # (b) .. department number (optional)
            (?:\s?(?:\([0-9XIV]+\)))?\s?,\s
            # (c) .. first name
            (?:[\u00C0-\u017F\w-]+)\s?,\s
            # (d) .. official title
            (?:
                (?:
                    Ref|JOI|AAAnw|
                    E?(?:O?StA|O?AA)|
                    (?:RR(?:\'in)?aAA)
                )
                (?:\'in)?
                (?:\s\(ba\))?
            )\s?
        )+
    )
    """,
    re.VERBOSE,
)


EXPRESS = re.compile(
    r"""
    # (1) .. start date
    (?P<from>\d{2}\.\d{2}\.\d{4})\s
    # (2) .. hyphen, followed by whitespace
    (?:-\s)
    # (3) .. end date
    (?P<to>\d{2}\.\d{2}\.\d{4})\s
    # (4) .. name(s) of prosecutor(s), namely ..
    (?P<assigned>
        (?:
            # (a) .. last name & doctoral degree (optional)
            (?:(?:Dr\.\s)?[\u00C0-\u017F\w-]+)
            # (b) .. department number (optional)
            (?:\s(?:\([0-9XIV]+\)))?\s?,\s
            # (c) .. first name
            (?:[\u00C0-\u017F\w-]+)\s?,\s
            # (d) .. official title
            (?:
                (?:
                    Ref|JOI|AAAnw|
                    E?(?:O?StA|O?AA)|
                    (?:RR(?:\'in)?aAA)
                )
                (?:\'in)?
                (?:\s\(ba\))?
            )\s?
        )+
    )
    """,
    re.VERBOSE,
)


PERSON = re.compile(
    r"""
    # (1) .. doctoral degree (optional)
    (?P<doc>(?:Dr\.)?)\s??
    # (2) .. last name
    (?P<last>[\u00C0-\u017F\w-]+)\s?
    # (3) .. department number (optional)
    (?P<department>(?:\([0-9XIV]+\))?)\s?,\s?
    # (4) .. first name
    (?P<first>[\u00C0-\u017F\w-]+)\s?,\s?
    # (5) .. official title, being either ..
    (?P<title>
        (?:
            # (a) .. Rechtsreferendar:in
            # - Ref / Ref'in
            #
            # (b) .. Justizoberinspektor:in
            # - JOI / JOI'in
            #
            # (c) .. Amtsanwaltsanwärter:in
            # - AAAnw / AAAnw'in
            Ref|JOI|AAAnw|

            # (d) .. (Erste:r / Ober-) Staatsanwalt:anwältin
            # - OStA / OStA'in
            # - EStA / EStA'in
            # - StA / StA'in
            # (e) .. (Erste:r) (Oberamts-) Anwalt:Anwältin
            # - EOAA / EOAA'in
            # - OAA / OAA'in
            E?(?:O?StA|O?AA)|

            # (f) .. Regierungsrat:rätin als Amtsanwalt:anwältin
            # - RRaAA / RR'inaAA'in
            (?:RR(?:\'in)?aAA)
        )
        (?:\'in)?
        (?:\s\(ba\))?
    )
    """,
    re.VERBOSE,
)
