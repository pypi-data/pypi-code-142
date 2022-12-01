import inspect


def get_all_methods_and_properties(clazz):
    return [name for name, value in inspect.getmembers(clazz)]


def get_methods_and_properties(clazz, dont=False, starts_with=''):
    if starts_with == '':
        return [name for name, value in inspect.getmembers(clazz)]
    if not dont:
        return [name for name, value in inspect.getmembers(clazz) if name.startswith(starts_with)]
    else:
        return [name for name, value in inspect.getmembers(clazz) if not name.startswith(starts_with)]


if __name__ == '__main__':
    from poe import *
    from aspect import TestLogger

    logger = TestLogger(folder='utility', stdout=True)
    logger.info(get_methods_and_properties(ScreenElement))
    logger.warning(get_methods_and_properties(LabelElement, dont=True, starts_with='_'))
    logger.error(get_methods_and_properties(SelectElement, dont=True, starts_with='__'))
    logger.warning(get_methods_and_properties(SectionElement, dont=False, starts_with='_'))
    logger.error(get_methods_and_properties(InputElement, dont=False, starts_with='__'))
