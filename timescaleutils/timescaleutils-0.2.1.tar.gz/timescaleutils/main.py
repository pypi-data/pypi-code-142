from timescaleutils.timescale import TimeScaleUtils

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
utils = TimeScaleUtils()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # utils.test()
    # utils.create_index('edge_data')
    # print(utils.check_timescale())
    # print(utils.array_agg({"start": "2022-11-21 14:54:00", "end": "2022-11-21 14:55:00"},
    #                       {"name": "where", "condition": {"l1": "site_888"}}, [], "", [], [5, 4]))
    # utils.create_index()
    # utils.create_hypertable("live_data_ilens","date_time")
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    utils.generate_md()
    # print(utils.selectgroupdata("avg", {"start": "2022-11-21 14:54:00", "end": "2022-11-21 14:55:00"},
    #                             {"name": "where", "condition": {"l1": "site_888"}}, "", [], [], [5, 4]))
    # utils.create_table("tbl_name", [{"column": 'id', "datatype": "bigint", "length": "0"},{"column": 'names',
    #     "datatype": "varchar", "length": "200"},{"column": 'date_time', "datatype": "timestamp", "length": "0"}])
