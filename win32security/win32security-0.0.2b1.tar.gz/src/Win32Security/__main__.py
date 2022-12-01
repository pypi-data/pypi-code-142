import os
import sys

import LassaLib

from src.Win32Security import SecurityObject

_types = {
    "SecurityObject": SecurityObject,
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list,
    "tuple": tuple,
    "dict": dict,
}


def edit_config(config_path):
    class Class:
        def __init__(self, data=..., *, name=...):
            if data is ... and name is ...:
                raise AttributeError("No attribute")

            if data is ...:
                self.name = name
                self.data = {}
            else:
                self.name = data.split('(Params):')[0].split('class ')[1][1:-2]
                self.data = {}

                for line in data.split("def __init__(self):")[1].splitlines()[1:]:
                    try:
                        line: str
                        name, value = line.split('self.')[1].split(' = ')
                        type_, value = value[1:-1].split(', ')
                        self.data[name] = (type_, value[1:-1])
                    except IndexError:
                        pass

        def get_attributes(self):
            return f"\n        ".join([f'self.{key} = ({value[0]}, "{value[1]}")' for key, value in self.data.items()])

        def __str__(self):
            return f'''
# <class>
class _{self.name}__(Params):
    """Settings of {self.name}"""

    def __init__(self):
        {self.get_attributes()}
# </class>
'''

    data = open(config_path, 'r').read()

    classes = [Class(class_) for class_ in [class_.split("# </class>")[0] for class_ in data.split('# <class>')[1:]]]

    run = True
    while run:
        os.system('CLS')
        print()
        chx = LassaLib.menu(
            ["Create new class"] + [c.name for c in classes], "Choice of class",
            can_back=True,
            desc="Choose your class to work on.\nAuto-save on exit"
        )

        match chx:
            case 0:
                run = False
            case 1:
                classes.append(Class(name=input("Class name: ").capitalize()))
            case _:
                class_ = classes[chx - 2]
                os.system('CLS')
                print()
                chx2 = LassaLib.menu(
                    ["Rename class", "Delete class", "Create new attribute"] + list(class_.data), f"Menu {class_.name}",
                    can_back=True
                )
                match chx2:
                    case 0:
                        pass
                    case 1:
                        new_name = input("New name: ").capitalize()
                        if LassaLib.enter(f"Rename {class_.name} for {new_name}?\n >> ", bool):
                            class_.name = new_name
                    case 2:
                        if LassaLib.enter(f"Are you sure you want to delete {class_.name}?\n >> ", bool):
                            classes.remove(class_)
                    case 3:
                        os.system('CLS')
                        print()
                        chx3 = LassaLib.menu(
                            _types, f"Menu create new attribute",
                            can_back=True,
                            desc="Choose your type"
                        )
                        if chx3 == 0:
                            break
                        else:
                            chx3 -= 1
                        type_ = _types[list(_types)[chx3]].__name__
                        name = input("Choose the name: ").upper()
                        value = input(f"Value of {name}: ")
                        if type_ == 'SecurityObject':
                            value = SecurityObject(value, True).encrypted_data
                        class_.data[name] = (type_, value)
                    case _:
                        attr_ = list(class_.data.keys())[chx2 - 4]
                        os.system('CLS')
                        print()
                        chx3 = LassaLib.menu(
                            [
                                f"Rename {attr_}",
                                f"Change {attr_}",
                                f"Delete {attr_}",
                                f"View {attr_}"
                            ], f"Menu {class_.name}.{attr_}",
                            can_back=True
                        )
                        match chx3:
                            case 0:
                                pass
                            case 1:
                                new_name = input("New name: ").upper()
                                if LassaLib.enter(f"Rename {attr_} for {new_name}?\n >> ", bool):
                                    class_.data[new_name] = class_.data[attr_]
                                    del class_.data[attr_]
                            case 2:
                                os.system('CLS')
                                print()
                                chx4 = LassaLib.menu(
                                    _types, f"Menu change attribute",
                                    can_back=True,
                                    desc="Choose your type"
                                )
                                if chx4 == 0:
                                    break
                                else:
                                    chx4 -= 1
                                type_ = list(_types.values())[chx4].__name__
                                value = input(f"Value of {attr_}: ")
                                if type_ == 'SecurityObject':
                                    value = SecurityObject(value, True).encrypted_data
                                class_.data[attr_] = (type_, value)
                            case 3:
                                if LassaLib.enter(f"Are you sure you want to delete {class_.name}.{attr_}?\n >> ",
                                                  bool):
                                    del class_.data[attr_]
                            case 4:
                                print(
                                    f"{class_.name}.{attr_} = {str(_types[class_.data[attr_][0]](class_.data[attr_][1]))}")

    doc = "from Win32Security import *\n\n"
    doc = "from src.Win32Security import *\n" + doc
    for class_ in classes:
        print(f"Prepare {class_.name}...", end='')
        try:
            doc += "\n" + str(class_)
            print('OK')
        except Exception as e:
            print(f'KO : {e}')
    print("Prepare complete.")
    print("Save...")
    try:
        open(config_path, 'w').write(doc)
        print("OK")
    except Exception as e:
        print(f"KO : {e}")


if __name__ == '__main__':
    print(sys.argv)