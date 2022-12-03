from .helper import extract_text
from .parsing_dataclass import Kanji_CharacterStandard, Kanji_Radical, Kanji_Description_Variant, Kanji_RNM_group, \
    Kanji_Description, Kanji_DictionaryNumber, Kanji_QueryCode, Kanji_RNM_Reading, Kanji_RNM_Meaning, Kanji_RNM, Kanji

KANJIDIC_OFFSET = 1


def process_kanjidic_node(node):
    # kanji
    kanji = node.find("./literal").text

    # codepoint (cp_value+)
    standard = []
    for elem in node.findall("./codepoint/cp_value"):
        standard.append(
            Kanji_CharacterStandard(
                v_type=elem.get('cp_type'),
                value=elem.text,
            )
        )

    # radical (rad_value+)
    radical = []
    for elem in node.findall("./radical/rad_value"):
        radical.append(
            Kanji_Radical(
                v_type=elem.get('rad_type'),
                value=elem.text,
            )
        )

    # misc (grade?, stroke_count+, variant*, freq?, rad_name*,jlpt?)
    grade = extract_text(node.find("./misc/grade"))

    stroke_count = []
    for elem in node.findall("./misc/stroke_count"):
        stroke_count.append(
            elem.text
        )

    variant = []
    for elem in node.findall("./misc/variant"):
        stroke_count.append(
            Kanji_Description_Variant(
                v_type=elem.get('var_type'),
                value=elem.text,
            )
        )

    frequency = extract_text(node.find("./misc/freq"))

    radical_name = []
    for elem in node.findall("./misc/rad_name"):
        radical_name.append(
            elem.text
        )

    jlpt = extract_text(node.find("./misc/jlpt"))

    description = Kanji_Description(
        grade=grade,
        stroke_count=stroke_count,
        variant=variant,
        frequency=frequency,
        radical_name=radical_name,
        jlpt=jlpt,
    )

    # dic_number?
    dictionary_reference = []
    for elem in node.findall("./dic_number/dic_ref"):
        dictionary_reference.append(
            Kanji_DictionaryNumber(
                value=extract_text(elem),
                v_type=elem.get('dr_type'),
                volume=elem.get('m_vol', default=None),
                page=elem.get('m_page', default=None),
            )
        )

    # query_code? (q_code+)
    query_code = []
    for elem in node.findall("./query_code/q_code"):
        query_code.append(
            Kanji_QueryCode(
                value=extract_text(elem),
                v_type=elem.get('qc_type'),
                misclassification=elem.get('skip_misclass', default=None),
            )
        )

    # reading_meaning? (rmgroup*, nanori*)
    rnm = []
    for elem in node.findall("./reading_meaning"):
        rnm_group = []
        for sub_elem in elem.findall("./rmgroup"):
            reading = []
            for sub2_elem in sub_elem.findall("./reading"):
                reading.append(
                Kanji_RNM_Reading(
                    value=extract_text(sub2_elem),
                    v_type=sub2_elem.get('r_type', default=None),
                    status=sub2_elem.get('status', default=None),
                )
                )

            meaning = []
            for sub2_elem in sub_elem.findall("./meaning"):
                meaning.append(
                    Kanji_RNM_Meaning(
                        value=extract_text(sub2_elem),
                        v_type=sub2_elem.get('m_lang', default=None),
                    )
                )

            rnm_group.append(
                Kanji_RNM_group(
                    reading=reading,
                    meaning=meaning,
                )
            )

        nanori = []
        for sub_elem in elem.findall("./nanori"):
            nanori.append(
                sub_elem.text
            )

        rnm.append(
            Kanji_RNM(
                rmn_group=rnm_group,
                names_readings=nanori,
            )

        )

    entry = Kanji(
        kanji=kanji,
        standard=standard,
        radical=radical,
        description=description,
        dictionary_number=dictionary_reference,
        query_code=query_code,
        rnm=rnm,
    )

    return entry
