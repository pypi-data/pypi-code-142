import typing
import prepr


class OverloadList(list):
    """A list subclass.

    """


class OverloadDict(typing.Dict[typing.Any, OverloadList]):
    """Similar to a dictionary, but turns multiple occurances of a key into a
    list of values intead of overwriting the previous value.

    Additionally, multiple keys and values can be set at once, for example:
    ```
    d = OverloadDict()
    d["a", "b", "c"] = 1, 2, 3
    ```
    Unwanted values may be removed through the `remove_values` method, and can
    be converted into a standard `dict` object through the `to_dict` method.

    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def __repr__(self, *args, **kwargs) -> prepr.pstr:
        return prepr.prepr(self).build(*args, **kwargs)


    def __setitem__(self, __k, __v) -> None:
        if type(__k) == tuple and type(__v) not in [tuple, list]:
            return print(f"multiple values must be used if assigning multiple "
                "keys. Expected {len(__k)}, got 1.")
        if type(__k) == tuple:
            for k, v in zip(__k, __v):
                self[k].append(v) if __k in self else super().__setitem__(k,
                    OverloadList([v]))
            return
        return self[__k].append(__v) if __k in self else super().__setitem__(
            __k, OverloadList([__v]))


    def remove_values(self, remove: typing.Any) -> "OverloadDict":
        """Iteratively removes values in each of the contained `OverloadList`
        objects that are equal to `remove` and returns the result as a new
        `OverloadDict`.
        
        """
        new = {}
        for k, v_list in self.items():
            temp = [v for v in v_list if v != remove]
            if temp:
                new[k] = OverloadList(temp)
        return OverloadDict(new)
    

    def to_dict(self, pref: int = 0) -> dict:
        """Iteratively creates a new `dict` object with the contents if this
        OverloadDict. A list index preference may be chosen through the `pref`
        parameter, and must be either `0` (first item) or `-1` (last item).
        
        """
        new = {}
        for k, v_list in self.items():
            temp = v_list[pref] if len(v_list) > 0 else None
            if temp:
                new[k] = temp
        return new
