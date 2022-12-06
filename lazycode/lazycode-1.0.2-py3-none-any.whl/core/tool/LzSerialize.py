import pickle


class LzSerialize(object):

    @staticmethod
    def dump_to_file(obj: object, file_path: str) -> None:
        with open(file_path, mode='wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def dump(obj: object) -> bytes:
        return pickle.dumps(obj)

    @staticmethod
    def load_from_file(file_path: str) -> object:
        res = None
        with open(file_path, mode='rb') as f:
            res = pickle.load(f)
        return res

    @staticmethod
    def load(data: bytes) -> object:
        return pickle.loads(data)

#
# dic = {
#     'k1': 'v1',
#     'k2': 'v2'
# }
# # LzSerialize.dump_to_file(dic, './temp.pk')
#
# print(LzSerialize.load_from_file('./temp.pk'))
#
