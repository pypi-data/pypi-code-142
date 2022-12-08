import random
import re
import json
import os
import requests
from tqdm.auto import tqdm
from sentence_splitter import SentenceSplitter, split_text_into_sentences
from .diff import dff_text
from .text_tilling import auto_text_tilling
from .cut import auto_cut_markdown
import logging
import time

from collections import OrderedDict, UserDict
from .img import get_markdown_images, get_markdown_images_format
from .api import AutoReWrite
from pprint import pprint


def auto_rewriter_by_paraphrase(
        text,
        is_html=False,
        simlimit=0.8,
        num_beams=5,
        num_return_sequences=5,
        max_length=128,
        simlimitmax=1.0,
        auto_sample=False,
        temperature=1.2197635693677316,
        pre_text="",
        api='http://192.168.1.18:3008',
        api_sbert_host="http://192.168.1.18:3016",
        model="paraphrase",  # model参数 paraphrase/simplified 使用简写或者同义句模型
        **kwargs):
    """
    AutoReWrite by Paraphrase
    :param text:
    :param is_html:
    :param simlimit:
    :param num_beams:
    :param num_return_sequences:
    :param max_length:
    """
    Gen = AutoReWrite(api=api, api_sbert_host=api_sbert_host)
    # 同义句请求参数
    payload = {
        "config": {
            "do_sample": True,
            "early_stopping": True,
            "temperature": temperature,
            "max_length": max_length,
            "num_return_sequences": num_return_sequences
        },
        "text": []
    }

    pre = auto_cut_markdown(text,
                            is_html=is_html,
                            tilling=False,
                            return_sents=True)
    for item in pre:
        sents = []
        for sent in item.get("sents", []):
            if len(sent.split()) > 0:
                # 修改请求数据
                sents.append(sent)

        payload['text'] = sents
        # 生成
        response = Gen.auto_sent_multiple(payload, model)
        # pprint(response)
        for iitem in response:
            yield iitem


if __name__ == "__main__":
    text = """Why?  Basically the reason is the natural instincts of the two are completely incompatible.
    Consider the following situation:  An excited child who was minding his/her own business or was playing with their sweet four legged friend, runs out the front door or into the backyard.  Suddenly, the border collie dogs herding nature kicks in and he wants to re-collect the escaped “sheep”.
    ![]("http://www.world.com/images_list/saaa().jpg")
    He runs full tilt and blocks the child’s path, looking very threatening.


    The child’s natural reaction is to become frightened, scream and run.  Unfortunately, this response only furthers the collie’s desire to put the “livestock” back in line and he will become even more ferocious, nipping at the kid’s heels or grabbing on to them to drag them back into the home.  Though the animal will find nothing wrong with his actions, the poor little boy or girl and any onlooker will be traumatized by the ordeal."""

    res = auto_rewriter_by_paraphrase(
        text,
        is_html=False,
        simlimit=0.8,
        num_beams=5,
        num_return_sequences=5,
        max_length=128,
        simlimitmax=1.0,
        auto_sample=False,
        temperature=1.2197635693677316,
        pre_text="",
        api='http://192.168.1.18:3011',
        api_sbert_host="http://192.168.1.18:3016")

    # for item in res:
    #     print(item)