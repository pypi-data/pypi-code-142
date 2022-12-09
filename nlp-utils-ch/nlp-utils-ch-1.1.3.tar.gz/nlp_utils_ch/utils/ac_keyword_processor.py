#!user/bin/python
# _*_ coding: utf-8 _*_
# @Author      :   Jesper
# @Time        :   2022/12/9  10:36
# @Description :

import ahocorasick

class acKeywordProcessor():
    def __init__(self):
        self.actree = None

    def add_words(self, key_words):
        '''
            AC自动机进行关键词匹配
            构造AC trie
        '''
        self.actree = ahocorasick.Automaton()  # 初始化trie树
        for index, word in enumerate(key_words):
            self.actree.add_word(word, (index, word))  # 向trie树中添加单词
        self.actree.make_automaton()  # 将trie树转化为Aho-Corasick自动机
        # self.actree = actree
        return self.actree

    def extract_words(self, text, span_info=False):
        '''
            AC自动机进行关键词匹配
            文本匹配
        '''
        region_wds = []
        if span_info is False:
            for w1 in self.actree.iter(text):
                if len(w1) > 0:
                    region_wds.append(w1[1][1])
        else:
            for end_index, (insert_order, original_value) in self.actree.iter(text):
                start_index = end_index - len(original_value) + 1
                region_wds.append((original_value, start_index, end_index))
        return region_wds



if __name__ == '__main__':
    ac_extractor = acKeywordProcessor()
    ac_extractor.add_words(["ab", "cd", "abc"])
    res = ac_extractor.extract_words("abcde", span_info=True)
    print(res)
