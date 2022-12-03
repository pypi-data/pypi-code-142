from dataclasses import dataclass, field, fields
from .baseclass_dataclass import EmptyClass


@dataclass
class Kanji_CharacterStandard(EmptyClass):
    value: str  # cp_value
    v_type: str  # cp_type


@dataclass
class Kanji_Radical(EmptyClass):
    value: str  # rad_value
    v_type: str  # rad_type


@dataclass
class Kanji_Description_Variant(EmptyClass):
    value: str  # variant
    v_type: str  # var_type


@dataclass
class Kanji_Description(EmptyClass):
    grade: int | None  # grade?
    stroke_count: field(default_factory=list[int])  # stroke_count+
    variant: field(default_factory=list[Kanji_Description_Variant])  # variant*
    frequency: int | None  # freq?
    radical_name: field(default_factory=list[str])  # rad_name*
    jlpt: int | None  # jlpt?


@dataclass
class Kanji_DictionaryNumber(EmptyClass):
    value: str  # dic_ref
    v_type: str  # dr_type
    volume: int | None  # m_vol
    page: int | None  # m_page


@dataclass
class Kanji_QueryCode(EmptyClass):
    value: str  # q_code
    v_type: str  # qc_type
    misclassification: str | None  # skip_misclass


@dataclass
class Kanji_RNM_Reading(EmptyClass):
    value: str  # reading
    v_type: str  # r_type #REQUIRED
    status: str | None  # r_status


@dataclass
class Kanji_RNM_Meaning(EmptyClass):
    value: str  # meaning
    v_type: str  # m_lang #IMPLIED


@dataclass
class Kanji_RNM_group(EmptyClass):
    reading: list[Kanji_RNM_Reading]  # reading*
    meaning: list[Kanji_RNM_Meaning]  # meaning*


@dataclass
class Kanji_RNM(EmptyClass):
    rmn_group: field(default_factory=list[Kanji_RNM_group])  # rmgroup*
    names_readings: field(default_factory=list[str])  # nanori*


@dataclass
class Kanji(EmptyClass):
    """Kanji class to describe kanji from kanjidic2"""
    kanji: str  # literal
    standard: field(default_factory=list[Kanji_CharacterStandard])  # codepoint (cp_value+)
    radical: field(default_factory=list[Kanji_Radical])  # radical (rad_value+)
    description: field(default_factory=list[Kanji_Description])  # misc (grade?, stroke_count+, variant*, freq?, rad_name*,jlpt?)
    dictionary_number: field(default_factory=list[Kanji_DictionaryNumber])  # dic_number?
    query_code: field(default_factory=list[Kanji_QueryCode])  # query_code? (q_code+)
    rnm: field(default_factory=list[Kanji_RNM])  # reading_meaning? (rmgroup*, nanori*)
