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
from pprint import pprint
from collections import OrderedDict, UserDict
from .img import get_markdown_images, get_markdown_images_format


def check_loadavg(limit=30):
    avg = os.getloadavg()
    if avg[0] < limit:
        return True
    else:
        return False


def auto_request(payload, api, timeout=600):
    """

    :param api:
    :param payload:
    :param timeout:
    :return:
    """
    # payload = dict(payload)
    # payload = json.dumps(payload, ensure_ascii=False)
    # print("auto_request", json.dumps(payload, ensure_ascii=False))
    # headers = {'accept: application/json'}
    # headers = None
    # response = requests.post(
    #     api, json=payload, headers=headers, timeout=timeout)
    # # print(response.text)

    headers = {
        "content-type": "application/json",
        "Accept": "application/json",
    }
    # response = requests.request("POST", url, json=payload, headers=headers)
    # print(json.dumps(payload))
    response = requests.request("POST",
                                api,
                                data=json.dumps(payload),
                                headers=headers)
    # print(response.text)
    # print(response.status_code)
    assert response.status_code == 200
    return response.json()


# def decode_summary_text(data):
#     data={
#     "results": [
#         [
#         {
#             "summary_text": "Benefits of CBD Oil for Dogs .<n>The Benefits of Coconut Oil for Your Dog .<n>How to Deal with DogAnxiety in Car Rides ."
#         }
#         ]
#     ]
#     }


class SentenceClassification(object):
    """
    # 文本分类 请求接口

    """

    def __init__(self, api, timeout=30, **kwargs):
        self.api_host = api  # 服务器
        self.timeout = timeout  # 超时

    def predict_text_pet(self, text_list=[]):
        """


        :param text_list:  # 需要预测的文章列表
        :param timeout: #设置请求超时
        :return:
        """
        payload = {
            "config": {
                "max_length": 512,  #
            },
            "text": text_list
        }
        api = f"{self.api_host}/predict_text_pet"
        return auto_request(payload, api, self.timeout)


class AutoReWrite(object):
    """
    # AutoReWrite 自动重写模块





    """

    def __init__(self,
                 api='http://192.168.1.18:3008',
                 api_sbert_host=None,
                 **kwargs):
        self.api_host = api
        if api_sbert_host is not None:
            self.api_sbert_host = api_sbert_host
        else:
            self.api_sbert_host = api
        pass

    def predict_enzh(self, payload, timeout=600):
        """
        生成中文翻译

        示例：

            payload = {"config":{"do_sample": true,
                    "max_length":1024,
                    "num_return_sequences": 5,
                    "temperature":1.5833010652204251,
                    "top_p":1.1544317694512212,
                    "early_stopping":true
                    },
                "text":["Unsupervised pretraining of large neural models has recently revolutionized Natural Language Processing."]}

            out = predict_enzh(payload)
            print(out)


        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_host}/predict_en_zh"
        return auto_request(payload, api, timeout)

    def predict_paraphrase(self, payload, timeout=600):
        """
        生成同义句

        示例：

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            },"text": ["Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
            "than a century ago in Britain. "]}
            out = predict_paraphrase(payload)
            print(out)


        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_host}/predict_paraphrase"
        return auto_request(payload, api, timeout)

    def predict_summary(self, payload, timeout=600):
        """
        生成摘要
        示例：

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            },"text": ["Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
                   "than a century ago in Britain. "]}
            out = predict_summary(payload)
            print(out)


        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_host}/predict_en_summary"
        return auto_request(payload, api, timeout)

    def auto_summary(self,
                     text,
                     auto_sample=False,
                     temperature=1.15,
                     config=None,
                     **kwargs):
        """
        自动生成摘要，设置了默认参数

        获取最好的一个摘要信息



        示例：
            from tkitAutoRewriter import AutoReWrite, SentenceClassification
            text = "The Border Collie is a British breed of herding dog of medium size. They are descended from landrace sheepdogs once found all over the British Isles, but became standardized in the Anglo-Scottish border region. Presently they are used primarily as working dogs to herd livestock, specifically sheep.[1] The Border Collie is considered a highly intelligent, extremely energetic, acrobatic and athletic dog. They frequently compete with great success in sheepdog trials and a range of dog sports like dog obedience, disc dog, herding and dog agility. They are one of the most intelligent domestic dog breeds.[2] Border Collies continue to be employed in their traditional work of herding livestock throughout the world and are kept as pets."
            # rewriter = AutoReWrite(api='http://192.168.1.18:3008')
            rewriter = AutoReWrite(api='http://127.0.0.1:3000')
            out = rewriter.auto_summary(text)
            print(out)
            > {'results': [[{'summary_text': 'Border Collie: Dog Breed Profile, Characteristics, and Development-Worthy of Homeward-Homeward Herding Dogs of the 21st-century Dog-Ages'}]]}

        :param text:
        :return:
        """
        while check_loadavg(limit=30) == False:
            time.sleep(100)

        mi = max(int(len(text.split(" ")) * 0.6), 64)
        # payload = {"config": {
        #     "do_sample": auto_sample,
        #     # "num_beams": 5,
        #     "max_length": min(mi,128),
        #     "temperature":temperature
        #     # "num_return_sequences": 5
        # }, "text": [text]}
        # payload = {"config": {
        #     "do_sample": auto_sample,
        #     # "num_beams": 5,
        #     "max_length": min(mi,128),
        #     "temperature":temperature
        #     # "num_return_sequences": 5
        # }, "text": [text]}

        # 自动调参 https://wandb.ai/terrychanorg/uncategorized/sweeps/j64ghxnf?workspace=user-terrychanorg
        # config={"do_sample": True,
        #             "max_length": min(mi,128),
        #             "early_stopping":True,
        #             "num_return_sequences": 5,
        #             "no_repeat_ngram_size":5,
        #             "num_beams":8,
        #             "temperature":0.7773100411930902,
        #             "top_p":0.7735368770052764,
        #             "top_k": 50
        #             }

        #new1 for cnn
        if config is None:
            config = {
                "do_sample": True,
                "max_length": min(mi, 128),
                "early_stopping": True,
                "num_return_sequences": 5,
                "no_repeat_ngram_size": 5,
                "num_beams": 6,
                "temperature": 0.8532525677925238,
                "top_p": 0.5793650747162632,
                # "top_k": 50
            }
        payload = {"config": config, "text": [text]}
        return self.predict_summary(payload, timeout=600)
        # pass

    def predict_optimize_content(self, payload, timeout=600):
        """
        优化内容接口
        示例：

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            },"text": ["Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
                   "than a century ago in Britain. "]}
            out = predict_summary(payload)
            print(out)


        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        while check_loadavg(limit=30) == False:
            time.sleep(100)
        api = f"{self.api_host}/predict_optimize_content"
        return auto_request(payload, api, timeout)

    def auto_optimize_content(self,
                              text,
                              auto_sample=False,
                              temperature=1.15,
                              config=None,
                              **kwargs):
        """
        自动优化内容，设置了默认参数

        获取最好的一个摘要信息



        示例：
            from tkitAutoRewriter import AutoReWrite, SentenceClassification
            text = "The Border Collie is a British breed of herding dog of medium size. They are descended from landrace sheepdogs once found all over the British Isles, but became standardized in the Anglo-Scottish border region. Presently they are used primarily as working dogs to herd livestock, specifically sheep.[1] The Border Collie is considered a highly intelligent, extremely energetic, acrobatic and athletic dog. They frequently compete with great success in sheepdog trials and a range of dog sports like dog obedience, disc dog, herding and dog agility. They are one of the most intelligent domestic dog breeds.[2] Border Collies continue to be employed in their traditional work of herding livestock throughout the world and are kept as pets."
            # rewriter = AutoReWrite(api='http://192.168.1.18:3008')
            rewriter = AutoReWrite(api='http://127.0.0.1:3000')
            out = rewriter.auto_summary(text)
            print(out)
            > {'results': [[{'summary_text': 'Border Collie: Dog Breed Profile, Characteristics, and Development-Worthy of Homeward-Homeward Herding Dogs of the 21st-century Dog-Ages'}]]}

        :param text:
        :return:
        """
        mi = max(int(len(text.split(" ")) * 0.6), 64)
        # payload = {"config": {
        #     "do_sample": auto_sample,
        #     # "num_beams": 5,
        #     "max_length": min(mi,128),
        #     "temperature":temperature
        #     # "num_return_sequences": 5
        # }, "text": [text]}
        # payload = {"config": {
        #     "do_sample": auto_sample,
        #     # "num_beams": 5,
        #     "max_length": min(mi,128),
        #     "temperature":temperature
        #     # "num_return_sequences": 5
        # }, "text": [text]}

        # 自动调参 https://wandb.ai/terrychanorg/uncategorized/sweeps/j64ghxnf?workspace=user-terrychanorg
        # config={"do_sample": True,
        #             "max_length": min(mi,128),
        #             "early_stopping":True,
        #             "num_return_sequences": 5,
        #             "no_repeat_ngram_size":5,
        #             "num_beams":8,
        #             "temperature":0.7773100411930902,
        #             "top_p":0.7735368770052764,
        #             "top_k": 50
        #             }

        #new1 for cnn
        if config is None:
            config = {
                "do_sample": True,
                "max_length": 1024,
                "early_stopping": True,
                "num_return_sequences": 5,
                # "no_repeat_ngram_size":5,
                "num_beams": 6,
                # "temperature":0.8532525677925238,
                # "top_p":0.5793650747162632,
                # "top_k": 50
            }
        payload = {"config": config, "text": [f"{text}"]}

        # print(payload)
        return self.predict_optimize_content(payload, timeout=600)

    def predict_title(self, payload, timeout=600):
        """
        生成标题

        示例：

            payload = {"config": {
            "num_beams": 5,
            "max_length": 64,
            "num_return_sequences": 5
            },"text": ["Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
            "than a century ago in Britain. "]}
            out = predict_paraphrase(payload)
            print(out)


        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_host}/predict_headline_rewriter"
        return auto_request(payload, api, timeout)

    def auto_title(self, text):
        """
        自动生成标题，设置了默认参数

        示例：
            from tkitAutoRewriter import AutoReWrite, SentenceClassification
            text = "The Border Collie is a British breed of herding dog of medium size. They are descended from landrace sheepdogs once found all over the British Isles, but became standardized in the Anglo-Scottish border region. Presently they are used primarily as working dogs to herd livestock, specifically sheep.[1] The Border Collie is considered a highly intelligent, extremely energetic, acrobatic and athletic dog. They frequently compete with great success in sheepdog trials and a range of dog sports like dog obedience, disc dog, herding and dog agility. They are one of the most intelligent domestic dog breeds.[2] Border Collies continue to be employed in their traditional work of herding livestock throughout the world and are kept as pets."
            # rewriter = AutoReWrite(api='http://192.168.1.18:3008')
            rewriter = AutoReWrite(api='http://127.0.0.1:3000')
            out = rewriter.auto_title(text)
            print(out)
            > {'results': [[{'summary_text': 'Border Collie: Dog Breed Profile, Characteristics, and Development-Worthy of Homeward-Homeward Herding Dogs of the 21st-century Dog-Ages'}]]}

        :param text:
        :return:
        """
        payload = {
            "config": {
                # "do_sample": False,
                "num_beams": 5,
                "max_length": 64,
                "num_return_sequences": 5
            },
            "text": [text]
        }
        return self.predict_title(payload, timeout=600)
        pass

    def predict_paraphrase_sbert(self, payload, timeout=600):
        """
        预测句子相关性

        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_sbert_host}/predict_paraphrase_sbert"
        return auto_request(payload, api, timeout)

    def predict_simplified(self, payload, timeout=600):
        """
        生成同义句

        示例：

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            },"text": ["Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
            "than a century ago in Britain. "]}
            out = predict_paraphrase(payload)
            print(out)


        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_host}/predict"
        return auto_request(payload, api, timeout)

    def auto_simplified(self, payload={}):
        """
        自动简化句子

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            }, "text": [
            "Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
            "than a century ago in Britain. "]}
            auto_paraphrase(payload)

            结果如下

            > {'text': 'Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more than a century ago in Britain. ', 'text_pair': ['The Border Collie was developed more than a century ago in Britain.', 'The Border Collie was developed in Britain more than a century ago.', 'The Border Collie was developed over a century ago in Britain.', 'The Border Collie was developed in Britain over a century ago.', 'The Border Collie was developed more than a century ago in Britain and is a prize for his intelligence, herding instinct and working ability.'], 'out': {'results': {'scores': [0.8412754581989551, 0.8384939168488782, 0.8282370060160626, 0.8268469374505539, 0.9535872264040571], 'best_pair': 'The Border Collie was developed more than a century ago in Britain and is a prize for his intelligence, herding instinct and working ability.', 'best_pair_index': 4}}}


        :param payload:
        :return:
        """
        # http://192.168.1.18:3015/predict
        paraphrase = self.predict_simplified(payload)
        # print("paraphrase['results']", paraphrase['results'])
        # 开始预测相关性最大的句子
        or_text = payload["text"][0]
        text_pair = []
        for it in paraphrase['results'][0][0]:
            # print(it.get("summary_text"))
            tx = it.get("summary_text").replace("\n", '')
            text_pair.append(tx)

        payload = {"text": or_text, "text_pair": list(set(text_pair))}

        out = self.predict_paraphrase_sbert(payload)
        # print("相关性最大的句子：",out)
        #
        # print("最终结果：")
        # print(or_text)
        # print(out['results']['best_pair'])
        payload['out'] = out
        return payload

    def simplified(self,
                   text,
                   simlimit=0.8,
                   num_beams=5,
                   num_return_sequences=5,
                   max_length=128,
                   simlimitmax=1.0,
                   auto_sample=False,
                   temperature=1.25,
                   **kwargs):
        """
        对文本进行简化重写,
        自动将文章拆分成句子，之后逐句生成同义句，
        使用逐句重写方案，后对句子的相关性进行判别

        # 重写模式 ["del summary paraphrase：", "del：", "summary：", "paraphrase：", "del summary paraphrase："]
        :param pre_text:
        :param auto_sample: #是否随机选择，否则选择相关度最高的句子
        :param simlimitmax:  # 限制最大相关度
        :param max_length:  # 句子最大长度
        :param num_return_sequences:  #候选句子个数
        :param num_beams: #
        :param simlimit: # 相关度限制
        :param text:  # 输入的文本内容，不限制字数
        :return new:  返回生成句子列表
        """
        splitter = SentenceSplitter(language='en')

        newdata = []
        images_list = []
        # for p in text.split('\n'):
        # 自动拆分段落，并且对文本中的图像进行分割为单独段落。
        sents = []
        for p in get_markdown_images_format(text)[0]:

            # 判断是否存在图片，如果存在图片则不做重写
            images = get_markdown_images(p)
            if len(images) == 0:
                for sent in tqdm(splitter.split(text=p)):
                    sents.append(sent)
                    images = get_markdown_images(sent)
                    if len(sent) > 5 and len(images) == 0:
                        # print(sent)

                        try:
                            payload = {
                                "config": {
                                    "do_sample": True,
                                    "temperature": temperature,
                                    # "num_beams": num_beams,
                                    "max_length": max_length,
                                    "num_return_sequences":
                                    num_return_sequences,
                                    "early_stopping": True,
                                    "temperature": 0.8532525677925238,
                                    # "top_p":0.5793650747162632,
                                    # "top_k": 50
                                },
                                "text": [sent]
                            }

                            # print("payload", payload)
                            # 预测简化后句子
                            out = self.auto_simplified(payload)
                            # print("out", out)

                            best_pair_index = out['out']['results'][
                                'best_pair_index']
                            #  这里限制 相关度 自动选择第一个
                            if auto_sample == False:
                                newdata.append(
                                    out['out']['results']['best_pair'].replace(
                                        "888-349-8884", ""))
                                # print(newdata[-1])
                            else:
                                # 筛选出匹配的index
                                pair_index = []
                                for i, score in enumerate(
                                        out['out']['results']['scores']):
                                    if simlimitmax > score > simlimit:
                                        pair_index.append(i)
                                if len(pair_index) > 0:
                                    index = random.choice(pair_index)
                                    # print('pair_index:', index)
                                    newdata.append(
                                        out["text_pair"][index].replace(
                                            '\n',
                                            ' ').replace("888-349-8884", ""))
                                else:
                                    newdata.append(sent)

                        except Exception as e:
                            print(e)

                            newdata.append(sent)
                        # print(sent)
                        # print(out[0].replace("888-349-8884", ""))
                    else:
                        newdata.append(sent)
            else:
                sents.append(p)
                newdata.append(p)
                images_list = images_list + images
            newdata.append("\n")
        # print(text, "\n")
        # print("".join(new), "\n")
        return {"items": newdata, "images": images_list, "sents": sents}

    def auto_paraphrase(self, payload={}):
        """
        自动生成同义句并自动筛选

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            }, "text": [
            "Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
            "than a century ago in Britain. "]}
            auto_paraphrase(payload)

            结果如下

            > {'text': 'Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more than a century ago in Britain. ', 'text_pair': ['The Border Collie was developed more than a century ago in Britain.', 'The Border Collie was developed in Britain more than a century ago.', 'The Border Collie was developed over a century ago in Britain.', 'The Border Collie was developed in Britain over a century ago.', 'The Border Collie was developed more than a century ago in Britain and is a prize for his intelligence, herding instinct and working ability.'], 'out': {'results': {'scores': [0.8412754581989551, 0.8384939168488782, 0.8282370060160626, 0.8268469374505539, 0.9535872264040571], 'best_pair': 'The Border Collie was developed more than a century ago in Britain and is a prize for his intelligence, herding instinct and working ability.', 'best_pair_index': 4}}}


        :param payload:
        :return:
        """

        paraphrase = self.predict_paraphrase(payload)
        # print("同义句生成结果：",out)

        # can remove pre words
        # pre_arr = ["del summary paraphrase：", "summary paraphrase:",  "del：", "summary：", "paraphrase：",
        #            "summary paraphrase：", "del paraphrase：", "del summary paraphrase：", "del summary：", "paraphrase : ", "del summary："]
        # pre_arr = ["del summary paraphrase：", "summary paraphrase:", "summary：", "paraphrase：", "summary paraphrase：",
        #            "del paraphrase：", "del summary paraphrase：", "del summary：", "paraphrase : ", "del summary："]
        # 开始预测相关性最大的句子
        or_text = payload["text"][0]
        text_pair = []
        for it in paraphrase['results'][0][0]:
            # print(it.get("summary_text"))
            tx = it.get("generated_text").replace("\n", ' ')
            # 清理头
            # for pre_text in pre_arr:
            #     if tx.startswith(pre_text):
            #         tx = tx.replace(pre_text, '')
            # tx = tx.replace(pre_text, '')
            # print(tx)
            text_pair.append(tx)

        # if type(or_text) == str:
        #     for pre_text in pre_arr:
        #         # print(pre_text)
        #         if or_text.startswith(pre_text):
        #             or_text = or_text.replace(pre_text, "")
        # print(or_text)
        payload = {"text": or_text, "text_pair": text_pair}

        out = self.predict_paraphrase_sbert(payload)
        # print("相关性最大的句子：",out)
        #
        # print("最终结果：")
        # print(or_text)
        # print(out['results']['best_pair'])
        payload['out'] = out
        return payload

    def auto_sent_multiple(self, payload={}, model="paraphrase"):
        """
        自动生成同义句并自动筛选

            # model参数 paraphrase/

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            }, "text": [
            "Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
            "than a century ago in Britain. "]}
            auto_paraphrase(payload)

            结果如下

            > {'text': 'Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more than a century ago in Britain. ', 'text_pair': ['The Border Collie was developed more than a century ago in Britain.', 'The Border Collie was developed in Britain more than a century ago.', 'The Border Collie was developed over a century ago in Britain.', 'The Border Collie was developed in Britain over a century ago.', 'The Border Collie was developed more than a century ago in Britain and is a prize for his intelligence, herding instinct and working ability.'], 'out': {'results': {'scores': [0.8412754581989551, 0.8384939168488782, 0.8282370060160626, 0.8268469374505539, 0.9535872264040571], 'best_pair': 'The Border Collie was developed more than a century ago in Britain and is a prize for his intelligence, herding instinct and working ability.', 'best_pair_index': 4}}}


        :param payload:
        :model参数 paraphrase/simplified 使用简写或者同义句模型
        :return:
        """
        if model == "simplified":
            paraphrase = self.predict_simplified(payload)
            pass
        else:
            paraphrase = self.predict_paraphrase(payload)
        # print("同义句生成结果：",pprint(paraphrase))

        for or_text, item in zip(payload['text'], paraphrase['results'][0]):
            # 开始预测相关性最大的句子
            # or_text = payload["text"][0]
            text_pair = []
            for iitem in item:
                # print(it.get("summary_text"))
                tx = iitem.get("generated_text").replace("\n", ' ')
                text_pair.append(tx)

            data = {"text": or_text, "text_pair": text_pair}

            out = self.predict_paraphrase_sbert(data)
            # print("相关性最大的句子：",out)
            #
            # print("最终结果：")
            # print(or_text)
            # print(out['results']['best_pair'])
            data['out'] = out
            # return payload
            yield data

    def rewriter(self,
                 text,
                 simlimit=0.8,
                 num_beams=5,
                 num_return_sequences=5,
                 max_length=128,
                 simlimitmax=1.0,
                 auto_sample=False,
                 temperature=1.1125,
                 pre_text="",
                 **kwargs):
        """
        对文本进行重写,
        自动将文章拆分成句子，之后逐句生成同义句，
        使用逐句重写方案，后对句子的相关性进行判别


        temperature 建议1.0-1.5之间

        :param pre_text:  # 重写模式 ["del summary paraphrase：", "del：", "summary：", "paraphrase：", "del summary paraphrase："]
        :param auto_sample: #是否随机选择，否则选择相关度最高的句子
        :param simlimitmax:  # 限制最大相关度
        :param max_length:  # 句子最大长度
        :param num_return_sequences:  #候选句子个数
        :param num_beams: #
        :param simlimit: # 相关度限制
        :param text:  # 输入的文本内容，不限制字数
        :return new:  返回生成句子列表
        """
        splitter = SentenceSplitter(language='en')
        # print(splitter.split(text='This is a paragraph. It contains several sentences. "But why," you ask?'))
        # ['This is a paragraph.', 'It contains several sentences.', '"But why," you ask?']
        # ["del summary paraphrase：", "del：", "summary：", "paraphrase：", "del summary paraphrase："]

        newdata = []
        images_list = []

        # for p in text.split('\n'):
        # 自动拆分段落，并且对文本中的图像进行分割为单独段落。
        for p in get_markdown_images_format(text)[0]:
            # 判断是否存在图片，如果存在图片则不做重写
            images = get_markdown_images(p)
            if len(images) == 0:
                for sent in tqdm(splitter.split(text=p)):
                    images = get_markdown_images(sent)
                    if len(sent) > 5 and len(images) == 0:
                        payload = {
                            "config": {
                                "do_sample": True,
                                "early_stopping": True,
                                "temperature": temperature,
                                "max_length": max_length,
                                "num_return_sequences": num_return_sequences
                            },
                            "text": [pre_text + sent]
                        }
                        try:
                            # 预测同义句
                            out = self.auto_paraphrase(payload)
                            # print(out)
                            # print("\n\n")

                            best_pair_index = out['out']['results'][
                                'best_pair_index']
                            #  这里限制 相关度
                            if auto_sample == False and (
                                    simlimitmax > out['out']['results']
                                ['scores'][best_pair_index] > simlimit):
                                # print(out['text'], "\n==>\n", out['out']['results']['best_pair'])
                                newdata.append(
                                    out['out']['results']['best_pair'].replace(
                                        "888-349-8884", ""))
                            elif auto_sample == True:
                                # 筛选出匹配的index
                                pair_index = []
                                for i, score in enumerate(
                                        out['out']['results']['scores']):
                                    if simlimitmax > score > simlimit:
                                        pair_index.append(i)
                                    pass
                                index = random.choice(pair_index)
                                # print('pair_index:', index)
                                newdata.append(out["text_pair"][index].replace(
                                    '\n', ' ').replace("888-349-8884", ""))
                                pass

                            else:
                                # print(out['text'], "\n==>\n", "相关度过低不休改")
                                newdata.append(sent)
                        except Exception as e:
                            print("Exception", e)
                            newdata.append(sent)
                    else:
                        newdata.append(sent)
                    # print(sent)
                    # print(newdata[-1])
            else:
                newdata.append(p)
                images_list = images_list + images
            newdata.append("\n")
        # print(text, "\n")
        # print("".join(new), "\n")
        return {"items": newdata, "images": images_list}

    def rewriter_by_paraphrase(self,
                               text,
                               simlimit=0.8,
                               num_beams=5,
                               num_return_sequences=5,
                               max_length=128,
                               simlimitmax=1.0,
                               auto_sample=False,
                               temperature=1.2197635693677316,
                               pre_text="",
                               **kwargs):
        """
        对文本进行重写,
        自动将文章拆分成句子，之后逐句生成同义句，
        使用逐句重写方案，后对句子的相关性进行判别

        使用

            rewriter = AutoReWrite(api='http://192.168.1.18:3008',api_sbert_host="http://192.168.1.18:3016")
            temperature=1
            for item in  rewriter.rewriter_by_paraphrase(text, simlimit=0.6, simlimitmax=0.999999999, auto_sample=False,temperature=temperature):
                print(item)

        返回格式如下：
            生成器
            {'text': 'An intense and tractable worker, the border dog is a highly energy breed that thrive with vigorous exercise, a job and space to run.', 'original': 'An intense and tractable worker, the Border Collie is a highly energetic breed that thrives with vigorous exercise, a job and space to run.', 'image': None, 'results': {'text': 'An intense and tractable worker, the Border Collie is a highly energetic breed that thrives with vigorous exercise, a job and space to run.', 'text_pair': ['The border dog is an intense and tractable worker that thrive with vigorous exercise, a job and space to run.', 'An intense and tractable worker, the border dog is a highly energy breed that thrive with vigorous exercise, a job and space to run.', 'The border dog is a highly energy breed that thrive with vigorous exercise, a job and space to run an intense tractable worker.', 'The border dog is an intense and tractable worker, a highly energy breed that thrive with vigorous exercise, a job and space to run.', 'An intense and tractable worker, the border dog is a highly energy breed that thrive with vigorous exercise, a job and space to run.'], 'out': {'results': {'scores': [0.8840175084126243, 0.8921903948002754, 0.8680708691438526, 0.8873742224117748, 0.8921903948002754], 'best_pair': 'An intense and tractable worker, the border dog is a highly energy breed that thrive with vigorous exercise, a job and space to run.', 'best_pair_index': 1}}}}

        temperature 建议1.0-1.5之间

        :param pre_text:  # 重写模式 ["del summary paraphrase：", "del：", "summary：", "paraphrase：", "del summary paraphrase："]
        :param auto_sample: #是否随机选择，否则选择相关度最高的句子
        :param simlimitmax:  # 限制最大相关度
        :param max_length:  # 句子最大长度
        :param num_return_sequences:  #候选句子个数
        :param num_beams: #
        :param simlimit: # 相关度限制
        :param text:  # 输入的文本内容，不限制字数
        :return new:  返回生成句子列表
        """
        splitter = SentenceSplitter(language='en')
        # print(splitter.split(text='This is a paragraph. It contains several sentences. "But why," you ask?'))
        # ['This is a paragraph.', 'It contains several sentences.', '"But why," you ask?']
        # ["del summary paraphrase：", "del：", "summary：", "paraphrase：", "del summary paraphrase："]

        newdata = []
        images_list = []

        # for p in text.split('\n'):
        # 自动拆分段落，并且对文本中的图像进行分割为单独段落。
        for p in get_markdown_images_format(text)[0]:
            # 判断是否存在图片，如果存在图片则不做重写
            images = get_markdown_images(p)
            if len(images) == 0:
                for sent in tqdm(splitter.split(text=p)):
                    images = get_markdown_images(sent)
                    if len(sent) > 5 and len(images) == 0:
                        payload = {
                            "config": {
                                "do_sample": True,
                                "num_beams": 8,
                                "early_stopping": True,
                                "temperature":
                                temperature,  # "temperature":1.2197635693677316
                                "max_length": max_length,
                                "num_return_sequences": num_return_sequences
                            },
                            "text": [pre_text + sent]
                        }
                        try:
                            # 预测同义句
                            out = self.auto_paraphrase(payload)
                            # print(out)
                            # print("\n\n")

                            best_pair_index = out['out']['results'][
                                'best_pair_index']
                            #  这里限制 相关度
                            if auto_sample == False and (
                                    simlimitmax > out['out']['results']
                                ['scores'][best_pair_index] > simlimit):
                                new_sent = out["text_pair"][best_pair_index]

                            elif auto_sample == True:
                                # 筛选出匹配的index
                                pair_index = []
                                for i, score in enumerate(
                                        out['out']['results']['scores']):
                                    if simlimitmax > score > simlimit:
                                        pair_index.append(i)
                                    pass
                                index = random.choice(pair_index)
                                new_sent = out["text_pair"][index]

                            else:
                                # print(out['text'], "\n==>\n", "相关度过低不休改")
                                # newdata.append(sent)
                                new_sent = sent
                            results = out
                            # paraphrases=payload['text']

                        except Exception as e:
                            print("Exception:", e)
                            # newdata.append(sent)
                            new_sent = sent
                            results = None
                            # paraphrases=None
                    else:
                        # newdata.append(sent)
                        new_sent = sent
                        results = None
                        # paraphrases=None

                    yield UserDict(text=new_sent,
                                   original=sent,
                                   image=None,
                                   results=results)

            else:
                newdata.append(p)
                images_list = images_list + images
                yield UserDict(text=p, original=p, image=images, results=None)
            # 段落 增加回车
            yield UserDict(text="\n", original="\n", image=None, results=None)
        # print(text, "\n")
        # print("".join(new), "\n")
        # return {"items": newdata, "images": images_list}

    def rewriter_by_summary(self,
                            text,
                            simlimit=0.8,
                            num_beams=5,
                            num_return_sequences=5,
                            max_length=128,
                            simlimitmax=1.0,
                            auto_sample=False,
                            temperature=1.1125,
                            pre_text="",
                            **kwargs):
        """
        对文本进行重写,
        自动将文章拆分成句子，之后逐句生成同义句，
        使用逐句重写方案，后对句子的相关性进行判别


        temperature 建议1.0-1.5之间

        :param pre_text:  # 重写模式 ["del summary paraphrase：", "del：", "summary：", "paraphrase：", "del summary paraphrase："]
        :param auto_sample: #是否随机选择，否则选择相关度最高的句子
        :param simlimitmax:  # 限制最大相关度
        :param max_length:  # 句子最大长度
        :param num_return_sequences:  #候选句子个数
        :param num_beams: #
        :param simlimit: # 相关度限制
        :param text:  # 输入的文本内容，不限制字数
        :return new:  返回生成句子列表
        """

        newdata = []
        # 自动拆分段落，并且对文本中的图像进行分割为单独段落。
        for item in tqdm(auto_cut_markdown(text)):
            if len(item['text']) > 0:
                try:
                    out = self.auto_summary(item['text'],
                                            auto_sample=True,
                                            temperature=temperature)
                except Exception as e:
                    # 失败后返回原文
                    item['results'] = item['text']
                    yield item
                # print(out)
                try:
                    if out.get("results") and type(out) == dict and out[
                            'results'][0][0]['summary_text'] is not None:

                        item["results"] = out['results'][0][0]['summary_text']
                except Exception as e:
                    if type(out) == dict and out['results'][0][0][0][
                            'summary_text'] is not None:

                        item["results"] = out['results'][0][0][0][
                            'summary_text']
            logging.info("rewriter_by_summary:", item)
            yield item
        #     newdata.append(item)

        # return newdata


def rewriter_by_paraphrase(text,
                           simlimit=0.8,
                           num_beams=5,
                           num_return_sequences=5,
                           max_length=128,
                           simlimitmax=1.0,
                           auto_sample=False,
                           temperature=1.2197635693677316,
                           pre_text="",
                           api='http://192.168.1.18:3011',
                           api_sbert_host="http://192.168.1.18:3016",
                           **kwargs):
    """
    """
    rewriter = AutoReWrite(api=api, api_sbert_host=api_sbert_host)
    temperature = 1
    for item in rewriter.rewriter_by_paraphrase(text,
                                                simlimit=0.6,
                                                simlimitmax=0.999999999,
                                                auto_sample=False,
                                                temperature=temperature):
        # print("====")
        # # print(item)
        # print(item['original'])
        # print(item['text'])
        yield item


def rewriter_by_summary(text,
                        auto_sample=False,
                        simlimit=0.6,
                        temperature=1.2,
                        api='http://192.168.1.18:3011',
                        api_sbert_host="http://192.168.1.18:3016",
                        **kwargs):
    """
    自动处理重写任务

    """
    # 自动分段处理
    # text= auto_text_tilling(text)
    rewriter = AutoReWrite(api=api, api_sbert_host=api_sbert_host)
    # for temperature in [1.2]:
    for item in rewriter.rewriter_by_summary(text,
                                             simlimit=0.6,
                                             simlimitmax=0.999999999,
                                             auto_sample=False,
                                             temperature=temperature):
        yield item

    # text="\n ".join(out['items'])
    # text= auto_text_tilling(text)
    # # 提取图片信息
    # text_list,images=get_markdown_images_format(text)
    # return text_list,images
    # return out


def auto_rewriter_by_paraphrases(text,
                                 simlimit=0.8,
                                 num_beams=5,
                                 num_return_sequences=5,
                                 max_length=128,
                                 simlimitmax=1.0,
                                 auto_sample=False,
                                 temperature=1.1125,
                                 pre_text="",
                                 api='http://192.168.1.18:3011',
                                 api_sbert_host="http://192.168.1.18:3016",
                                 **kwargs):
    """
    自动重写全文

    """
    new_text = []
    for item in rewriter_by_paraphrase(text,
                                       api=api,
                                       api_sbert_host=api_sbert_host,
                                       **kwargs):
        # for item in  rewriter_by_paraphrase(text, api='http://127.0.0.1:3000',api_sbert_host="http://192.168.1.18:3016"):
        # print("====")
        # # print(item)
        # print(item['original'])
        # print(item['text'])
        new_text.append(item['text'])
    return " ".join(new_text)

    pass


if __name__ == "__main__":
    # payload = {"config": {
    #     "num_beams": 5,
    #     "max_length": 120,
    #     "num_return_sequences": 5
    # }, "text": [
    #     "Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
    #     "than a century ago in Britain. "]}
    # out=auto_paraphrase(payload)
    # print(out)

    auto = AutoReWrite()
    splitter = SentenceSplitter(language='en')
    # print(splitter.split(text='This is a paragraph. It contains several sentences. "But why," you ask?'))
    # ['This is a paragraph.', 'It contains several sentences.', '"But why," you ask?']
    text = """

    The Border Collie is a British breed of herding dog of medium size. They are descended from landrace sheepdogs once found all over the British Isles, but became standardized in the Anglo-Scottish border region. Presently they are used primarily as working dogs to herd livestock, specifically sheep.[1]

    The Border Collie is considered a highly intelligent, extremely energetic, acrobatic and athletic dog. They frequently compete with great success in sheepdog trials and a range of dog sports like dog obedience, disc dog, herding and dog agility. They are one of the most intelligent domestic dog breeds.[2] Border Collies continue to be employed in their traditional work of herding livestock throughout the world and are kept as pets.


    """

    new = []
    for sent in splitter.split(text=text):
        if len(sent) > 2:
            payload = {
                "config": {
                    "num_beams": 5,
                    "max_length": 120,
                    "num_return_sequences": 5
                },
                "text": [sent]
            }
            out = auto.auto_paraphrase(payload)
            # print(out)
            # print("\n\n")

            best_pair_index = out['out']['results']['best_pair_index']
            #  这里限制 相关度
            if out['out']['results']['scores'][best_pair_index] > 0.92:
                # print(out['text'], "\n==>\n", out['out']['results']['best_pair'])
                new.append(out['out']['results']['best_pair'])
            else:
                # print(out['text'], "\n==>\n", "相关度过低不休改")
                new.append(out['text'])
        else:
            new.append(out['text'])

    print(text, "\n")
    print("".join(new), "\n")

    dff = dff_text(text, "".join(new))
    print(dff, "\n")
