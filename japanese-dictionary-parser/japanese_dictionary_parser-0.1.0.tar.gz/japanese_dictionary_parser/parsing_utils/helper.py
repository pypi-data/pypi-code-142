from .parsing_dataclass import Entry, Kanji
import xml.etree.ElementTree as ET
import logging
import pathlib


def print_node(node) -> None:
    for child_node in ET.tostring(node).decode('utf-8').split('\n'):
        if child_node:
            print(child_node)
    return


def get_text(node, xpath):
    text = node.find(xpath)
    if text:
        return text.text
    return ''


def extract_text(node, default=None) -> str | None:
    if node is not None:
        return node.text
    else:
        return default


def get_all_text(node, xpath):
    all_text = []
    for child_node in node.findall(xpath):
        if child_node.text:
            all_text.append(
                child_node.text
            )
    return all_text


def get_node_names(xml_node):
    name = xml_node.tag
    attributes = '__'.join((f'{k}={v}' for k, v in xml_node.attrib.items()))
    return f'{name}___{attributes}'


def is_child_node(xml_node, xpath: str) -> bool:
    return True if xml_node.find(xpath) is not None else False


def add_to_dict_if_exist(dictionary: dict, key: str, xml_node, xpath: str) -> None:
    if is_child_node(xml_node, xpath):
        dictionary[key] = get_text(xml_node, xpath)


def parse_xml(path, parsing_func, offset: int = 0, logger=None, test=False):
    tree = ET.parse(path)
    root = tree.getroot()

    elements = []
    for elem in root[offset:]:
        elements.append(
            parsing_func(elem, logger)
        )
        if test:
            return elements.pop()
    return elements


def _log(logger: logging, _method: str, message: str | Exception):
    if logger:
        if _method == 'critical':
            logging.critical(message, exc_info=True)
        else:
            _log_method = getattr(logging, _method)
            _log_method(message)
    else:
        print(message)


class ParsingBase:
    def __init__(self, path: str | pathlib.Path, logger: logging = None):
        self.path = path
        self.logger = logger
        self.offset = None
        self._modify_offset()

    def _parse_elem(self, elem, logger) -> Entry | Kanji:
        pass

    def _modify_offset(self) -> None:
        pass

    def __iter__(self):
        tree = ET.parse(self.path)
        root = tree.getroot()

        for idx, elem in enumerate(root[self.offset:]):
            _log(self.logger, 'info', f'Parsing element - {idx}')
            try:
                entry = self._parse_elem(elem, self.logger)
                item_status = entry.children_status
                for _status in item_status:
                    _log(self.logger, 'info', _status)
                _log(self.logger, 'info', f'Parsed element: {entry}')
            except Exception as e:
                entry = None
                _log(self.logger, 'critical', e)

            yield entry

