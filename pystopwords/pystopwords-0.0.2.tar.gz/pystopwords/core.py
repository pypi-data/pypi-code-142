import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, './data')


def stopwords(langs="zh", source="all"):
    """
    Params:
        langs: string，支持的语言，目前仅支持中文(zh)
        source: string, 停用词来源，目前支持
          - baidu: 百度停用词表
          - hit: 哈工大停用词表
          - ict: 中科院计算所停用词表
          - scu: 四川大学机器智能实验室停用词库
          - cn: 广为流传未知来源的中文停用词表
          - marimo: Marimo multi-lingual stopwords collection 内的中文停用词
          - iso: Stopwords ISO 内的中文停用词
          - all: 上述所有停用词并集
    Return:
        a set, 停用词表集合
    """
    if langs != "zh":
        raise NotImplementedError('目前仅支持中文，请使用`stopwords(langs="zh")`')
    supported_source = ["cn", "baidu", "hit",
                        "scu", "marimo", "ict", "iso", "all"]
    if source not in supported_source:
        raise NotImplementedError("请求了未知来源，请使用`help(stopwords)`查看支持的来源")
    filename = os.path.join(DATA_DIR, f"stopwords.{langs}.{source}.txt")
    return set([elem.strip('\n\r') for elem in open(filename)])
