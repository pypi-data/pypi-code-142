import asyncio
from jija_orm import config, fields


class Executor:
    def __init__(self, model, *operators, use_model=True):
        if isinstance(model, str):
            self.__model = model
        else:
            if use_model:
                self.__model = model
            else:
                self.__model = model.get_name()

        self.__operators = self.sort_operators(operators)
        self.__operators_query = self.prepare()
        self.__query = self.__generate_query()
        self.__params = self.get_params()

    @staticmethod
    def sort_operators(operators):
        return sorted(operators, key=lambda arg: arg.PRIORITY)

    def prepare(self):
        result = {}

        for operator in self.operators:
            operator.prepare(self.model)

            result[operator.get_name()] = operator.calculate()

        return result

    def __generate_query(self):
        return "\n".join(self.operators_query.values())

    def get_params(self):
        params = set()
        for operator in self.__operators:
            params.update(operator.get_params())

        return params

    @property
    def model(self):
        return self.__model

    @property
    def operators(self):
        return self.__operators

    @property
    def operators_query(self):
        return self.__operators_query

    @property
    def params(self):
        return self.__params

    @property
    def query(self):
        return self.__query

    def sync_execute(self, **kwargs):
        result = asyncio.run(self.execute(**kwargs))
        return result

    async def execute(self, **kwargs):
        if self.__params != set(kwargs.keys()):
            raise ValueError()

        connection = await self.get_connection()

        for key in kwargs.keys():
            kwargs[key] = fields.get_validator(kwargs[key]).to_sql(kwargs[key])

        query = self.__query.format(**kwargs)
        query = query.format(**kwargs)
        return self.__serialize(await connection.fetch(query))

    @staticmethod
    async def get_connection():
        return await config.JijaORM.get_connection()

    def __serialize(self, query_set):
        if isinstance(self.__model, str):
            return query_set

        return list(map(lambda record: self.__model(**record), query_set))
