
from cjutils.cmd import *
from cjutils.utils import *
from inspect import isgenerator


class cmd(cmd_base):
    def __init__(self, prog=None) -> None:
        super().__init__([
            ('j', 'json', 'format json file, multiple file separate with ","', "", False),
            ('J', 'Json', 'format dir all json files', ".", False),
            ('p', 'python', 'format python file, multiple file separate with ","', "", False),
            ('P', 'Python', 'format dir all python files', ".", False),
            ('f', 'fiddler', 'format fiddler request to python code', "", False),
            ('F', 'Fiddler', 'format fiddler request to FULL python code', "", False),
            ('i', 'in-place', 'make changes to files in place', False, False),
            ('o', 'output', 'output result to file', "", False),
            ('c', 'clipboard', 'output result to clipboard', False, False)
        ], prog=prog, description='a simple formatter', enable_plugins=False)

    def __from_fiddler_text_to_code(self, text: bytes):
        tmp = text.decode().split('\r\n\r\n')
        assert len(tmp) <= 2, f'format error:\n{text}'
        if len(tmp) == 1:
            header = tmp[0]
            body = None
        else:
            header, body = tmp
        header_lines = header.split('\r\n')
        mode, url, _ = header_lines[0].split()
        code = f"req_url = '{url}'\nreq_headers = {{\n"
        for line in header_lines[1:-1]:
            key, *val = line.split(':')
            key = key.replace('\\', '\\\\')
            val = ':'.join(val).replace('\\', '\\\\').strip()
            code += f"    '{key}': '{val}',\n"
        key, *val = header_lines[-1].split(':')
        key = key.replace('\\', '\\\\')
        val = ':'.join(val).replace('\\', '\\\\').strip()
        code += f"    '{key}': '{val}'\n"
        code += '}\n'
        if mode == 'POST':
            body = body.replace('\\', '\\\\').strip('\r\n')
            code += f"req_body = '{body}'\n"
            code += f'\nreq = requests.post(url = req_url, headers = req_headers, data = req_body, verify = False)\n'
        elif mode == 'GET':
            code += f'\nreq = requests.get(url = req_url, headers = req_headers, verify = False)\n'
        else:
            assert False, f'unknown mode: {mode}'
        return code

    def __format_fiddler(self, file=None, content=None):
        if content:
            if isinstance(content, str):
                content = content.encode()
            return self.__from_clipboard, self.__from_fiddler_text_to_code(content)
        with open(file, 'rb') as f:
            return file, self.__from_fiddler_text_to_code(f.read())

    def __format_fiddler_full(self, file=None, content=None):
        file, code = self.__format_fiddler(file, content)
        code_lines = code.split('\n')
        for idx, _ in enumerate(code_lines):
            code_lines[idx] = '    ' + code_lines[idx]
        code_lines.append('    print(req.text)')
        code_lines.append('')
        code_lines.append('    break')
        code = 'import requests\nimport urllib3\nurllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)\n\nwhile True:\n' + '\n'.join(
            code_lines)
        return file, code

    def __format_json(self, file=None, content=None):
        if content:
            info(f'formating {self.__from_clipboard}...')
            return self.__from_clipboard, dump_json(json.loads(content))[1:]
        info(f'formating {file}...')
        with open(file, 'r', encoding='utf-8') as f:
            return file, dump_json(json.load(f))[1:]

    def __format_jsons(self, dir):
        assert pexist(dir), f"{dir} not exist"
        for file in list_all_file(dir):
            if file.endswith('.json'):
                yield self.__format_json(file)

    def __format_py(self, file=None, content=None):
        mod = import_module('autopep8')
        if content:
            info(f'formating {self.__from_clipboard}...')
            return self.__from_clipboard, mod.fix_code(content)
        info(f'formating {file}...')
        with open(file, 'r', encoding='utf-8') as f:
            return file, mod.fix_code(f.read(), options={'ignore': ['E402']})

    def __format_pys(self, dir):
        assert pexist(dir), f"{dir} not exist"
        for file in list_all_file(dir):
            if file.endswith('.py'):
                yield self.__format_py(file)

    def __format(self):
        def check_and_format(option, format_func):
            if self.get_opt(option) is not None:
                args = [d for d in self.get_opt(
                    option).split(',') if len(d) > 0]
                if len(args) == 0:
                    info('try to use clipboard')
                    self.__res_list.append(
                        format_func(content=get_clipboard()))
                for arg in args:
                    if not pexist(arg):
                        warn(f'{arg} not exist')
                        continue
                    res = format_func(arg)
                    if isgenerator(res):
                        for d in res:
                            self.__res_list.append(d)
                    else:
                        self.__res_list.append(res)

        check_and_format('j', self.__format_json)
        check_and_format('J', self.__format_jsons)
        check_and_format('p', self.__format_py)
        check_and_format('P', self.__format_pys)
        check_and_format('f', self.__format_fiddler)
        check_and_format('F', self.__format_fiddler_full)

    def main(self):
        self.__res_list = []
        self.__from_clipboard = 'from clipboard'
        self.__format()
        for file, res in self.__res_list:
            if self.get_opt('i') and file != self.__from_clipboard:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(res)
            else:
                print(f'{file:-^80}')
                print(res)

            if self.get_opt('o'):
                with open(self.get_opt('o'), 'a', encoding='utf-8') as f:
                    f.write(res)

            if not self.get_opt('c') and is_windows():
                set_clipboard(res)

            if self.get_opt('c'):
                set_clipboard(res)

        if len(self.__res_list) == 0:
            info('nothing to do')
        return 0
