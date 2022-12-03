from dataclasses import dataclass, field
from .baseclass_dataclass import EmptyClass


@dataclass
class Entry_KanjiElement(EmptyClass):
    value: str  # keb
    info: field(default_factory=list[str])  # ke_inf*
    priority: field(default_factory=list[str])  # ke_pri*


@dataclass
class Entry_ReadingElement(EmptyClass):
    value: str  # reb
    no_kanji: bool  # re_nokanji?
    # reading is applied only to a set of KanjiElements
    atk: field(default_factory=list[str])  # re_restr*
    info: field(default_factory=list[str])  # re_inf*
    priority: field(default_factory=list[str])  # re_pri*


@dataclass
class Entry_SourceLanguage(EmptyClass):
    value: str  # lsource
    v_type: str | None  # lsource ls_type
    language: str | None  # lsource xml:lang
    wasei: str | None  # lsource ls_wasei


@dataclass
class Entry_Sense_Gloss(EmptyClass):
    value: str  # gloss
    v_type: str | None  # gloss g_type
    language: str | None  # gloss xml:lang
    wasei: str | None  # gloss g_gend


# @dataclass
# class Entry_Example(EmptyClass):
#     text: str  # ex_text
#     source: str  # ex_srce
#     language: str  # ex_sent xml:lang
#     sent: list[str]  # ex_sent
#     type: str  # ex_srce exsrc_type


@dataclass
class Entry_Sense(EmptyClass):
    # Sense is applied only to a set of Entry_KanjiElement
    aptk: field(default_factory=list[str])  # stagk*
    # Sense is applied only to a set of Entry_ReadingElement
    aptr: field(default_factory=list[str])  # stagr*
    part_of_speech: field(default_factory=list[str])  # pos*
    xref: field(default_factory=list[str])  # xref*
    antonym: field(default_factory=list[str])  # ant*
    use_field: field(default_factory=list[str])  # field*
    miscellaneous: field(default_factory=list[str])  # misc*
    info: field(default_factory=list[str])  # s_inf*
    source_language: field(default_factory=list[Entry_SourceLanguage])  # lsource*
    dialect: field(default_factory=list[str])  # dial*
    gloss: field(default_factory=list[Entry_Sense_Gloss])  # gloss*
    # example: field(default_factory=list[Entry_Example])  # example*


@dataclass
class Entry(EmptyClass):
    entry_sequence: int  # ent_seq
    kanji_element: field(default_factory=list[Entry_KanjiElement])  # k_ele*
    reading_element: field(default_factory=list[Entry_ReadingElement])  # r_ele+
    sense: field(default_factory=list[Entry_Sense])  # sense+

