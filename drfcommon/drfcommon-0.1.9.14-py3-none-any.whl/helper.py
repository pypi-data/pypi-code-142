
def _handler_err(errors, msg="请检查请求参数") -> str:
    if isinstance(errors, dict):
        for key, value in errors.items():
            if isinstance(value, list):
                value = _handler_err(value)
            if isinstance(value, dict):
                value = _handler_err(value)
            msg = str(value)
            return msg

    if isinstance(errors, list):
        for value in errors:
            if isinstance(value, list):
                value = _handler_err(value)
            if isinstance(value, dict):
                value = _handler_err(value)
            msg = str(value)
            return msg
    return msg


def handler_err(errors) -> str:
    return _handler_err(errors)


def demo_dict():
    errors = {
        # "items": [
        #     "问卷内容不能为空"
        # ],
        "items_dict": [
            {
                # "name": "错误"
                # "name": ["11", "bb"],
                "name": {
                    "abc": ["a", "b"]
                }
            }
        ]
    }
    msg = handler_err(errors)
    print(msg)


def demo_list():
    errors = [
        # "问卷内容不能为空"
        {
            "items_dict": [
                {
                    # "name": "错误"
                    # "name": ["11", "bb"],
                    "name": {
                        # "abc": ["a", "b"]
                        'abc': {
                            # "a": 1,
                            # "a": ["aa", "b"]
                            "a": {
                                "name": "1"
                            }
                        }
                    }
                }
            ]
        }
    ]
    msg = handler_err(errors)
    print(msg)


if __name__ == '__main__':
    demo_dict()
    demo_list()