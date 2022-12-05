from random import choice, randint

from pandas import DataFrame


def combobox_hierarchy(data: dict | DataFrame) -> str:
    """
        It is a function with generate a random combobox with hierarchy.

        :param data: A dict or DataFrame with the data.

        :return: A random combobox between the present combobox.
        :rtype: str

        :Example:
            >>> combobox_hierarchy({"Estado": ["SP", "SP", "SP", "SC", "SC", "SC"],
            "Cidade": ["São Paulo", "Itatiba", "Campinas", "Chapecó", "Xaxim", "Xanxerê"]})
    """
    if isinstance(data, dict):
        df = DataFrame(data)
        check_hierarchy(df)
        first, second = set_choices(df)
        return f'{df.columns[0]} {first} e {df.columns[1]} {second}'
    elif isinstance(data, DataFrame):
        check_hierarchy(data)
        first, second = set_choices(data)
        return f'{data.columns[0]} {first} e {data.columns[1]} {second}'
    else:
        raise TypeError('The data must be a dict or a DataFrame')


def set_choices(df: DataFrame) -> tuple[str, str]:
    """
        It is a function to set the choices of the combobox.

        :param df: A DataFrame with the data.

        :return: A tuple with the choices.
        :rtype: tuple[str, str]

        :Example:
            >>> set_choices(df)
    """
    first = choice(df.iloc[:, 0])
    df = df[df.iloc[:, 0] == first]
    second = randint(0, len(df) - 1)
    return first, df.iloc[second, 1]


def check_hierarchy(df: DataFrame) -> bool:
    """
        It is a function to check if the DataFrame has hierarchy.

        :param df: A DataFrame with the data.

        :return: True if the DataFrame has hierarchy, False if not.
        :rtype: bool

        :Example:
            >>> check_hierarchy(df)
    """
    if len(df.iloc[:, 0]) != len(set(df.iloc[:, 0])):
        return True
    else:
        raise ValueError('The DataFrame must have hierarchy')
