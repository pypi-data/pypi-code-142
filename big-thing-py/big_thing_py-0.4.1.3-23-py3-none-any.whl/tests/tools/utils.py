from big_thing_py.tests.tools.common import *
from big_thing_py.utils import *
from pathlib import Path
import yaml
import toml
import datetime
import random


def SOPTEST_LOG_DEBUG(msg: str, error: int, e: Exception = None):
    # error = 0  : PASS ✅
    # error = 1  : WARN ⚠ -> use b'\xe2\x9a\xa0\xef\xb8\x8f'.decode()
    # error = -1 : FAIL ❌
    log_msg = ''
    WARN_emoji = b'\xe2\x9a\xa0\xef\xb8\x8f'.decode()

    if error == 0:
        log_msg = f'[PASS✅] {msg} --> {str(e)}'
        SOPLOG_DEBUG(log_msg, 'green')
    elif error == 1:
        log_msg = f'[WARN{WARN_emoji} ] {msg} --> {str(e)}'
        SOPLOG_DEBUG(log_msg, 'yellow')
    elif error == -1:
        log_msg = f'[FAIL❌] {msg} --> {str(e)}'
        SOPLOG_DEBUG(log_msg, 'red')
        return e


def topic_seperator(topic: SoPProtocolType, back_num: int):
    topic_slice = topic.value.split('/')
    for _ in range(back_num):
        topic_slice.pop()

    result = '/'.join(topic_slice)
    return result


def get_mapped_thing_list(schedule_info: Dict, function_name: str = None, all_prefix: bool = False):
    if function_name:
        for mapping_info in schedule_info:
            if not all_prefix:
                if mapping_info['service'].split('.')[1] == function_name:
                    return mapping_info['things']
            elif mapping_info['service'].split('.')[1] == function_name and '*' in mapping_info['service']:
                return mapping_info['things']
    else:
        return [
            {
                'function_name': mapping_info['service'].split('.')[1],
                'thing_list': [thing['id'] for thing in mapping_info['things']]
            } for mapping_info in schedule_info
        ]


def len_no_ansi(string):
    import re
    return len(re.sub(
        r'[\u001B\u009B][\[\]()#;?]*((([a-zA-Z\d]*(;[-a-zA-Z\d\/#&.:=?%@~_]*)*)?\u0007)|((\d{1,4}(?:;\d{0,4})*)?[\dA-PR-TZcf-ntqry=><~]))', '', string))


def len_ansi(string):
    import re
    return len(string) - len(re.sub(
        r'[\u001B\u009B][\[\]()#;?]*((([a-zA-Z\d]*(;[-a-zA-Z\d\/#&.:=?%@~_]*)*)?\u0007)|((\d{1,4}(?:;\d{0,4})*)?[\dA-PR-TZcf-ntqry=><~]))', '', string))


def home_dir_append(path: str, user: str = None) -> str:
    if '~' in path:
        if user:
            return path.replace('~', f'/home/{user}')
        else:
            return path.replace('~', os.path.expanduser('~'))
    else:
        return path


def get_upper_path(path: str):
    path = Path(path)
    return path.parent.absolute()


def unixtime_to_date(unixtime: float = None):
    return datetime.datetime.fromtimestamp(0)


def exception_wrapper(func: Callable = None,
                      empty_case_func: Callable = None,
                      key_error_case_func: Callable = None,
                      else_case_func: Callable = None,
                      final_case_func: Callable = None,):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Empty as e:
            print_error(e)
            if empty_case_func:
                return empty_case_func()
        except KeyError as e:
            print_error(e)
            if key_error_case_func:
                return key_error_case_func()
        except KeyboardInterrupt as e:
            print('KeyboardInterrupt')
            if self.__class__.__name__ == 'Simulator':
                self.wrapup()
        except Exception as e:
            if e is Empty:
                if empty_case_func:
                    return empty_case_func()
            elif e in [ValueError, IndexError, TypeError, KeyError]:
                print_error(e)
            else:
                if self.__class__.__name__ == 'Simulator':
                    self.wrapup()
            print_error(e)
            raise e
        finally:
            if final_case_func:
                final_case_func()
    return wrapper


def check_result_payload(payload: dict = None, element: str = None, name: str = None, action: str = None, check_error_code: bool = True):
    if payload is not None:
        if check_error_code:
            error_code = payload.get('error', None)
            error_string = payload.get('error_string', None)
            if error_code in [0, -4]:
                SOPTEST_LOG_DEBUG(
                    f'{element} {name} {action} checked!', 0)
                return True
            else:
                SOPTEST_LOG_DEBUG(
                    f'error_code: {error_code}, error_string : {error_string}', -1)
                return False
        else:
            return True
    else:
        SOPTEST_LOG_DEBUG(
            f'Payload is None!!!', -1)
        return False


def generate_random_words(word_num: int = None, word_len: tuple = None, custom_words_file: List[str] = [], ban_word_list: List[str] = []) -> List[str]:
    picked_words = []
    whole_words = []

    if not custom_words_file:
        response = requests.get(
            "https://www.mit.edu/~ecprice/wordlist.10000")
        whole_words = response.content.splitlines()
        for word in ban_word_list:
            try:
                whole_words.remove(word)
            except Exception:
                pass
    else:
        file: List[str] = read_file(custom_words_file)
        whole_words = [line.strip() for line in file]
        return whole_words

    while len(picked_words) < word_num:
        picked_word = random.choice(whole_words)
        if picked_word in picked_words:
            continue

        if isinstance(picked_word, bytes):
            picked_word = picked_word.decode('utf-8')

        if word_len:
            if len(picked_word) >= word_len[0] and len(picked_word) <= word_len[1]:
                picked_words.append(picked_word)
        else:
            picked_words.append(picked_word)

    return picked_words


def get_middleware_list_recursive(middleware: object = None) -> List[object]:
    middleware_list = [middleware]

    for child_middleware in middleware.child_middleware_list:
        middleware_list.extend(
            get_middleware_list_recursive(child_middleware))

    middleware_list = sorted(
        middleware_list, key=lambda x: x.level, reverse=True)
    return middleware_list


def get_thing_list_recursive(middleware: object = None) -> List[object]:
    thing_list = [thing for thing in middleware.thing_list]

    for child_middleware in middleware.child_middleware_list:
        thing_list.extend(get_thing_list_recursive(child_middleware))

    thing_list = sorted(
        thing_list, key=lambda x: x.level, reverse=True)
    return thing_list


def get_scenario_list_recursive(middleware: object = None) -> List[object]:
    scenario_list = [scenario for scenario in middleware.scenario_list]

    for child_middleware in middleware.child_middleware_list:
        scenario_list.extend(get_scenario_list_recursive(child_middleware))

    scenario_list = sorted(
        scenario_list, key=lambda x: x.level, reverse=True)
    return scenario_list


# TODO: Fix it. 어떤 element는 안 찾아지고 None이 반환되는 문제가 있다.
def find_element_recursive(middleware: object, element: object):

    def inner(middleware: object, element: object):
        if middleware == element:
            return middleware, None

        for thing in middleware.thing_list:
            if thing == element:
                return thing, middleware
        for scenario in middleware.scenario_list:
            if scenario == element:
                return scenario, middleware
        for child_middleware in middleware.child_middleware_list:
            if child_middleware == element:
                return child_middleware, middleware

        for child_middleware in middleware.child_middleware_list:
            result = inner(
                child_middleware, element)
            if result:
                return result[0], result[1]
            else:
                inner(
                    child_middleware, element)

    result = inner(middleware, element)
    if result:
        return result[0], result[1]
    else:
        return None, None


def find_element_by_name_recursive(middleware: object, element_name: str):

    def inner(middleware: object, element_name: str):
        if middleware.name == element_name:
            return middleware, None

        for thing in middleware.thing_list:
            if thing.name == element_name:
                return thing, middleware
        for scenario in middleware.scenario_list:
            if scenario.name == element_name:
                return scenario, middleware
        for child_middleware in middleware.child_middleware_list:
            if child_middleware.name == element_name:
                return child_middleware, middleware

        for child_middleware in middleware.child_middleware_list:
            result = inner(child_middleware, element_name)
            if result:
                return result[0], result[1]
            else:
                inner(child_middleware, element_name)

    result = inner(middleware, element_name)
    if result:
        return result[0], result[1]
    else:
        return None, None


def test_find_element_recursive(middleware: object):
    thing_list = get_thing_list_recursive(middleware)
    for thing in thing_list:
        result = find_element_recursive(
            middleware, thing)
        print(
            f'{thing.name} was found!! {result[0].name}-{result[1].name}')

    scneario_list = get_scenario_list_recursive(
        middleware)
    for scenario in scneario_list:
        result = find_element_recursive(
            middleware, scenario)
        print(
            f'{scenario.name} was found!! {result[0].name}-{result[1].name}')

    middleware_list = get_middleware_list_recursive(
        middleware)
    for middleware in middleware_list:
        result = find_element_recursive(
            middleware, middleware)
        print(
            f'{middleware.name} was found!! {result[0].name}-{result[1].name if result[1] else "No Parent(TOP)"}')


def test_find_element_by_name_recursive(middleware: object):
    thing_list = get_thing_list_recursive(middleware)
    for thing in thing_list:
        result = find_element_by_name_recursive(
            middleware, thing.name)
        print(
            f'{thing.name} was found!! {result[0].name}-{result[1].name}')

    scneario_list = get_scenario_list_recursive(
        middleware)
    for scenario in scneario_list:
        result = find_element_by_name_recursive(
            middleware, scenario.name)
        print(
            f'{scenario.name} was found!! {result[0].name}-{result[1].name}')

    middleware_list = get_middleware_list_recursive(
        middleware)
    for middleware in middleware_list:
        result = find_element_by_name_recursive(
            middleware, middleware.name)
        print(
            f'{middleware.name} was found!! {result[0].name}-{result[1].name if result[1] else "No Parent(TOP)"}')


def append_indent(code: str, indent: int = 1):
    code_lines = code.split('\n')
    tabs = '    ' * indent
    for i, code_line in enumerate(code_lines):
        code_lines[i] = tabs + code_lines[i] + '\n'
    return ''.join(code_lines)


def load_toml(path: str) -> dict:
    config = toml.load(path)
    return config


def load_yaml(path: str) -> dict:
    with open(path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
