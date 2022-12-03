#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""
data_record_path = '../data/test.mindrecord'
from mindspore.mindrecord import FileWriter
import troubleshooter as ts


@ts.proposal(write_file_path="/tmp/")
def main():
    writer = FileWriter(file_name=data_record_path, shard_num=4)

    # 定义schema
    data_schema = {"file_name": {"type": "string"}, "label": {"type": "int32"}, "data": {"type": "bytes"}}
    writer.add_schema(data_schema, "test_schema")

    # 数据准备
    file_name = "../../../data/000000581721.jpg"
    with open(file_name, "rb") as f:
        bytes_data = f.read()
    data = [{"file_name": "transform.jpg", "label": 1, "data": bytes_data}]

    indexes = ["file_name", "label"]
    writer.add_index(indexes)

    # 数据写入
    writer.write_raw_data(data)

    # 生成本地数据
    writer.commit()


if __name__ == '__main__':
    main()
