from .parsing_dataclass import Entry, Entry_Sense, Entry_Sense_Gloss, Entry_SourceLanguage, \
    Entry_KanjiElement, Entry_ReadingElement

JMDICT_OFFSET = 1


def process_jmdict_node(node):
    xml_1998_namespace = "{http://www.w3.org/XML/1998/namespace}"

    # ent_seq
    entry_sequence = node.find("./ent_seq").text

    # k_ele*
    kanji_element = []
    for elem in node.findall("./k_ele"):
        value = elem.find("./keb").text

        info = []
        for sub_elem in elem.findall("./ke_inf"):
            info.append(
                sub_elem.text
            )

        priority = []
        for sub_elem in elem.findall("./ke_pri"):
            priority.append(
                sub_elem.text
            )

        kanji_element.append(
            Entry_KanjiElement(
                value=value,
                info=info,
                priority=priority,
            )
        )

    # r_ele+
    reading_element = []
    for elem in node.findall("./r_ele"):
        value = elem.find("./reb").text
        no_kanji = True if elem.find("./re_nokanji") else False

        atk = []
        for sub_elem in elem.findall("./re_restr"):
            atk.append(
                sub_elem.text
            )

        info = []
        for sub_elem in elem.findall("./re_inf"):
            info.append(
                sub_elem.text
            )

        priority = []
        for sub_elem in elem.findall("./re_pri"):
            priority.append(
                sub_elem.text
            )

        reading_element.append(
            Entry_ReadingElement(
                value=value,
                no_kanji=no_kanji,
                atk=atk,
                info=info,
                priority=priority,
            )
        )

    # sense+
    sense = []
    for elem in node.findall("./sense"):
        aptk = []
        for sub_elem in elem.findall("./stagk"):
            aptk.append(
                sub_elem.text
            )

        aptr = []
        for sub_elem in elem.findall("./stagr"):
            aptr.append(
                sub_elem.text
            )

        part_of_speech = []
        for sub_elem in elem.findall("./pos"):
            part_of_speech.append(
                sub_elem.text
            )

        xref = []
        for sub_elem in elem.findall("./xref"):
            xref.append(
                sub_elem.text
            )

        antonym = []
        for sub_elem in elem.findall("./ant"):
            antonym.append(
                sub_elem.text
            )

        use_field = []
        for sub_elem in elem.findall("./field"):
            use_field.append(
                sub_elem.text
            )

        miscellaneous = []
        for sub_elem in elem.findall("./misc"):
            miscellaneous.append(
                sub_elem.text
            )

        info = []
        for sub_elem in elem.findall("./s_inf"):
            info.append(
                sub_elem.text
            )

        source_language = []
        for sub_elem in elem.findall("./lsource"):
            value = sub_elem.text
            v_type = sub_elem.get('ls_type', default=None)
            language = sub_elem.get(f'{xml_1998_namespace}lang', default=None)
            wasei = sub_elem.get('ls_wasei', default=None)

            source_language.append(
                Entry_SourceLanguage(
                    value=value,
                    v_type=v_type,
                    language=language,
                    wasei=wasei,
                )
            )

        dialect = []
        for sub_elem in elem.findall("./dial"):
            dialect.append(
                sub_elem.text
            )

        gloss = []
        for sub_elem in elem.findall("./gloss"):
            value = sub_elem.text
            v_type = sub_elem.get('g_type', default=None)
            language = sub_elem.get(f'{xml_1998_namespace}lang', default=None)
            wasei = sub_elem.get('g_gend', default=None)

            gloss.append(
                Entry_Sense_Gloss(
                    value=value,
                    v_type=v_type,
                    language=language,
                    wasei=wasei,
                )
            )

        # NO EXAMPLES FOUND IN JMDICT (Version 1.0 / Rev 1.09)
        # example = []
        # for sub_elem in elem.findall("./example"):
        #     text = sub_elem.text
        #     source = sub_elem.get('g_type', default=None)
        #     language = sub_elem.get('xml:lang', default=None)
        #     sent = []
        #     for sub2_elem in elem.findall("./sent"):
        #         sent.append(
        #             sub2_elem.text
        #         )
        #
        #     example.append(
        #         Entry_Example(
        #             text=text,
        #             source=source,
        #             language=language,
        #             logger=logger
        #         )
        #     )

        sense.append(
            Entry_Sense(
                aptk=aptk,
                aptr=aptr,
                part_of_speech=part_of_speech,
                xref=xref,
                antonym=antonym,
                use_field=use_field,
                miscellaneous=miscellaneous,
                info=info,
                source_language=source_language,
                dialect=dialect,
                gloss=gloss,
            )
        )

    entry = Entry(
        entry_sequence=entry_sequence,
        kanji_element=kanji_element,
        reading_element=reading_element,
        sense=sense,
    )

    return entry
