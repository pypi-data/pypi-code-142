from trafilatura import extract
import trafilatura
from goose3 import Goose
import re
import justext
import logging
from delphai_ml_utils.text_processing import remove_emoji_patterns

g = Goose()


def post_processing(sentence: str):
    # handle emojis
    sentence = remove_emoji_patterns(sentence)
    return sentence


def formatting(text: str):
    text = re.sub(r"\n+", "\n", text).strip()
    list_sentences = text.split("\n")
    list_sentences = [post_processing(sentence) for sentence in list_sentences]
    if list_sentences == [""]:
        list_sentences = []
    return list_sentences


def deboilerplating(html: str):
    try:
        result_traf = extract(
            html,
            no_fallback=False,
            include_comments=False,
            include_tables=True,
            include_formatting=False,
        )
        if result_traf is not None:
            result_traf = formatting(result_traf)
        else:
            result_traf = []
    except Exception as e:
        result_traf = []
        logging.info(f"error calling trafilatura: {e}")

    try:
        result_goose = g.extract(raw_html=html)
        result_goose = str(result_goose.cleaned_text)
        if result_goose is not None:
            result_goose = formatting(result_goose)
        else:
            result_goose = []
    except Exception as e:
        result_goose = []
        logging.info(f"error calling goose3: {e}")
    all_sentences = result_traf + result_goose
    sentence_set = list(dict.fromkeys(all_sentences))

    try:
        paragraphs = justext.justext(
            html, justext.get_stoplist("English"), 50, 200, 0.1, 0.2, 0.2, 200, True
        )
        invalid = [
            paragraph.text for paragraph in paragraphs if paragraph.is_boilerplate
        ]
    except Exception as e:
        invalid = []
        logging.info(f"error calling justext: {e}")

    sentence_set = [
        sentence
        for sentence in sentence_set
        if sentence not in invalid or sentence != ""
    ]
    if not sentence_set:
        sentence_set = []
        logging.info("Page not found")

    return dict(
        {
            "set": sentence_set,
            "trafilatura": result_traf,
            "goose": result_goose,
            "justext": invalid,
        }
    )


def get_text_from_html(html: str) -> str:
    result = deboilerplating(html)
    text = " ".join(result["set"])
    return text
