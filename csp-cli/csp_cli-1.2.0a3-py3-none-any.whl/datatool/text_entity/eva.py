#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/4/27 9:50
# @Author  : xgy
# @Site    : 
# @File    : eva.py
# @Software: PyCharm
# @python version: 3.7.4
"""

import os
import sys
import json
# import pandas as pd
# import numpy as np
from loguru import logger

from csp.common.utils import RunSys, read_jsonl


class EntityEva:

    def __init__(self, pre_path, eval_path, long_text_categories=None, output=None):
        self.pre_path = pre_path
        self.eval_path = eval_path
        self.long_text_categories = long_text_categories
        self.output = output

    @staticmethod
    def list_category_values(category, df):
        """
        将tag中一个元素（{}）转为字符串，用于后续匹配判断正误
        拼接元素包含 "id + mention + start"
        :return:
        """
        values = []
        df_category = df[df["category"] == category].reset_index(drop=True)
        len_category = len(df_category)
        for _, row in df_category.iterrows():
            key = str(row["id"]) + str(row["mention"]) + str(row["start"])
            values.append(key)

        return values, len_category

    @staticmethod
    def calculate(y_true, y_pred, len_true, len_pred):
        """
        计算 precision, recall
        """
        precision = 0
        recall = 0

        tp_count = 0
        if y_true and y_pred:
            for pred in y_pred:
                if pred in y_true:
                    tp_count += 1

            precision = round(tp_count / len_pred, 6)
            recall = round(tp_count / len_true, 6)

        return precision, recall

    def df_proc(self, df):
        import pandas as pd
        df_source_spilt = self.df_source[["id", "content"]]
        df = pd.merge(df, df_source_spilt, left_on="id", right_on='id', how="inner")
        return df

    def evaluate(self, output_eval):
        import pandas as pd
        series = []
        final_precision = 0
        final_recall = 0
        final_f_score = 0
        for category in self.categories:

            y_true, len_true = self.list_category_values(category, self.df_true)
            y_pred, len_pred = self.list_category_values(category, self.df_pred)

            if not len_true:
                logger.warning("标签 {} 在 {} 中不存在".format(category, self.eval_path))
            if not len_pred:
                logger.warning("标签 {} 在 {} 中不存在".format(category, self.pre_path))

            if len_true and len_pred:
                precision, recall = self.calculate(y_true, y_pred, len_true, len_pred)
            else:
                precision, recall = 0, 0

            final_precision += precision
            final_recall += recall
            f_score = 0
            if (precision + recall) > 0:
                f_score = 2 * precision * recall / (precision + recall)
            final_f_score += f_score
            result = {"category": category,
                      "precision": precision,
                      "recall": recall,
                      "f_score": f_score}
            series.append(result)
        final_precision = round(final_precision / len(self.categories), 6)
        final_recall = round(final_recall / len(self.categories), 6)
        final_f_score = round(final_f_score / len(self.categories), 6)
        result = {"category": "total",
                  "precision": final_precision,
                  "recall": final_recall,
                  "f_score": final_f_score}
        series.append(result)

        result_df = pd.DataFrame(series)
        # print(result_df)
        result_df.to_csv(output_eval, sep=",", encoding="utf-8", index=False)

        title_dict = {"类别": "category", "召回率": "recall", "准确率": "precision", "f1": "f_score"}
        result_dict = {"data": series}
        from csp.common.utils import format
        format(result_dict, title_dict)

    def get_data(self):
        import pandas as pd
        # 固定列顺序
        true_data = read_jsonl(self.eval_path)
        pred_data = read_jsonl(self.pre_path)

        categories = []
        true_tags = []
        text_sources = []
        for item in true_data:
            tags = item["tags"]
            text = item["text"]
            for tag in tags:
                tag["id"] = item["id"]
                true_tags.append(tag)
                category = tag["category"]
                if category not in categories:
                    categories.append(category)
            result_sources = {"id": item["id"], "content": text}
            text_sources.append(result_sources)

        pred_tags = []
        for item in pred_data:
            tags = item["tags"]
            for tag in tags:
                tag["id"] = item["id"]
                pred_tags.append(tag)

        true_raw = pd.DataFrame(true_tags)[["id", "category", "start", "mention"]]
        pred_raw = pd.DataFrame(pred_tags)[["id", "category", "start", "mention"]]
        df_source = pd.DataFrame(text_sources)[["id", "content"]]

        self.true_raw = true_raw
        self.pred_raw = pred_raw
        self.df_source = df_source
        self.categories = categories

        return true_raw, pred_raw

    def data_filter_by_igcategory(self):
        logger.info("以下长文本字段将被忽略 {}".format(self.long_text_categories))

        if not self.long_text_categories:
            self.df_true = self.true_raw
            self.df_pred = self.pred_raw
        else:
            for item in self.long_text_categories:
                self.df_true = self.true_raw[self.true_raw["category"] != item]
            for item in self.long_text_categories:
                self.df_pred = self.pred_raw[self.pred_raw["category"] != item]

    def get_badcase(self):
        import pandas as pd
        list_good = []
        list_bad = []
        true_keys = []
        for _, row_true in self.df_true.iterrows():
            row_true_split = list(row_true)[1:4]
            row_true_str = []
            for item in row_true_split:
                item_str = str(item)
                row_true_str.append(item_str)
            key_true = "_".join(row_true_str)
            true_keys.append(key_true)

        for _, row_pred in self.df_pred.iterrows():
            row_pred_split = list(row_pred)[1:4]
            row_pred_str = []
            for item in row_pred_split:
                item_str = str(item)
                row_pred_str.append(item_str)
            key_pred = "_".join(row_pred_str)

            if key_pred in true_keys:
                list_good.append(list(row_pred))
            else:
                list_bad.append(list(row_pred))

        col_names = ["id", "category", "start", "mention"]
        df_good = self.df_proc(pd.DataFrame(list_good, columns=col_names))
        df_bad = self.df_proc(pd.DataFrame(list_bad, columns=col_names))

        return df_good, df_bad

    @staticmethod
    def df2files(df, output_json, output_excel):
        df.to_json(output_json, orient="records", force_ascii=False, indent=4)
        df.to_excel(output_excel, index=False)


def print_error_msg(msg, code):
    result_json = {}
    result_json['error_msg'] = msg
    result_json['error_code'] = code
    # result_json['usage'] = usage
    print(json.dumps(result_json, ensure_ascii=False))


def entity_eva(pre_path, eval_path, output, long_text_categories=None):
    try:
        import pandas as pd
    except ImportError:
        logger.error("未检测到 pandas 尝试安装, pip install pandas")
        install_cmd = "pip install pandas"
        RunSys(command=install_cmd).run_cli()

    if not os.path.exists(pre_path) or not os.path.isfile(pre_path):
        print_error_msg(("未找到待评估的预测结果文件: %s" % pre_path), 1001)
        sys.exit(1)

    if not os.path.exists(eval_path) or not os.path.isfile(eval_path):
        print_error_msg(("未找到标注测试集文件: %s" % eval_path), 1002)
        sys.exit(1)

    os.makedirs(output, exist_ok=True)

    file_good_json = "good" + ".json"
    file_bad_json = "bad" + ".json"
    file_good_excel = "good" + ".xlsx"
    file_bad_excel = "bad" + ".xlsx"
    file_eval = "eval" + ".csv"
    output_good_json = os.path.join(output, file_good_json)
    output_bad_json = os.path.join(output, file_bad_json)
    output_good_excel = os.path.join(output, file_good_excel)
    output_bad_excel = os.path.join(output, file_bad_excel)
    output_eval = os.path.join(output, file_eval)

    entityeva = EntityEva(pre_path, eval_path, long_text_categories, output=output)
    entityeva.get_data()
    entityeva.data_filter_by_igcategory()
    df_good, df_bad = entityeva.get_badcase()

    entityeva.df2files(df_good, output_good_json, output_good_excel)
    entityeva.df2files(df_bad, output_bad_json, output_bad_excel)

    entityeva.evaluate(output_eval)


if __name__ == '__main__':
    print("start")

