import jieba
import pandas as pd


df = pd.read_csv(r"cmfd_civictech.csv")

moral_dict = {}
for word in set(df['chinese'].tolist()):
    jieba.add_word(word)

for category, df_item in df.groupby(by=['foundation']):
    moral_dict[category] = df_item['chinese'].tolist()


def get_moral_dict():
    return moral_dict


def moral_quantity(text, duplicate=True, normalize=True, with_word=False):
    """
     Calculate the number or proportion of moral dictionaries in Chinese text
    :param text: chinese text
    :param duplicate: keep repeated moral words
    :param normalize: calculate the ratio
    :param with_word: output with moral words
    :return:
    """
    if isinstance(text, str):
        # The total number of matched moral words
        word_total = 0
        # dict of moral word
        moral_word = {}
        # Store the number corresponding to the moral vocabulary
        moral_num = {}
        if duplicate:
            for key in moral_dict.keys():
                moral_word[key] = []
            for word in jieba.cut(text):
                for key in moral_dict.keys():
                    if word in moral_dict[key]:
                        moral_word[key].append(word)
        else:
            for key in moral_dict.keys():
                moral_word[key] = set()

            for word in jieba.cut(text):
                for key in moral_dict.keys():
                    if word in moral_dict[key]:
                        moral_word[key].add(word)

        for key in moral_word.keys():
            word_total += len(moral_word[key])

        if word_total == 0:
            return None

        if normalize:
            for key in moral_word.keys():
                moral_num[key] = len(moral_word[key]) / word_total
        else:
            moral_num[key] = len(moral_word[key])
        if with_word:
            moral_word_num = {}
            for key in moral_dict.keys():
                moral_word_num[key] = {}
                moral_word_num[key]['num'] = moral_num[key]
                moral_word_num[key]['word'] = ";".join(moral_word[key])
            return moral_word_num
        else:
            return moral_num
    return None

