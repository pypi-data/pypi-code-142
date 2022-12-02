import pandas as pd


class PycodeSniffer:
    def __init__(self, file):
        self.file = file

    def errors_types(self):
        error_type = []

        with open(self.file, 'r+') as arq:
            arqq = arq.readlines()

        for i in arqq:
            try:
                x, _ = i.split('::')[0][0], i.split('::')[1]
                error_type.append(x)
            except BaseException:
                continue

        return pd.Series(error_type).value_counts()

    def insigth_pylint(self):
        error_code = []

        with open(self.file, 'r+') as _:
            arq = _.readlines()

        for i in arq:
            try:
                x, _ = i.split('::')[0], i.split('::')[1]
                error_code.append(x)
            except BaseException:
                continue

        return pd.Series(error_code).value_counts()

    def pylint_score(self):
        with open(self.file, 'r+') as _:
            arq = _.readlines()
            while '\n' in arq:
                arq.remove('\n')

        return arq[-1].split('/')[0].split()[-1]


print(PycodeSniffer('pylint_errors.txt').insigth_pylint())
print(PycodeSniffer('pylint_errors.txt').pylint_score())
print(PycodeSniffer('pylint_errors.txt').errors_types())
