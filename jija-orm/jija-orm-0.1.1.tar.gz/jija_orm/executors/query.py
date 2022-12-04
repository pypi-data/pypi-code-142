from jija_orm.executors import operators, executors


class QueryManager:
    def __init__(self, model_class, class_operators=None):
        self.__model_class = model_class
        self.__operators = self.fix_operators(class_operators)

    def __add_templates(self, *new_templates) -> 'QueryManager':
        class_operators = self.__operators.copy()
        class_operators.extend(new_templates)
        return self.__class__(self.__model_class, class_operators)

    @staticmethod
    def fix_operators(class_templates):
        if not class_templates:
            return []

        templates_dict = {}
        for template in class_templates:
            if templates_dict.get(template.PRIORITY):
                if template.COMPARABLE is False:
                    templates_dict[template.PRIORITY] = template
                else:
                    raise NotImplementedError()

            else:
                templates_dict[template.PRIORITY] = template

        return list(templates_dict.values())

    @property
    def model(self):
        return self.__model_class

    @property
    def templates(self):
        return self.__operators

    def select(self, *args, **kwargs) -> 'QueryManager':
        return self.__add_templates(operators.Select(*args, **kwargs))

    def update(self, **kwargs) -> 'QueryManager':
        return self.__add_templates(operators.Update(**kwargs))

    def insert(self, **kwargs) -> 'QueryManager':
        return self.__add_templates(operators.Insert(**kwargs))

    def multiple_insert(self, rows) -> 'QueryManager':
        return self.__add_templates(operators.MultipleInsert(rows))

    def delete(self):
        return self.__add_templates(operators.Delete())

    def where(self, *args, **kwargs) -> 'QueryManager':
        if self.__operators:
            new_operators = []
        else:
            new_operators = [operators.Select()]

        new_operators.append(operators.Where(*args, **kwargs))
        return self.__add_templates(*new_operators)

    def __await__(self):
        async def wrapper():
            executor = executors.Executor(self.__model_class, *self.__operators)
            return await executor.execute()

        return wrapper().__await__()
