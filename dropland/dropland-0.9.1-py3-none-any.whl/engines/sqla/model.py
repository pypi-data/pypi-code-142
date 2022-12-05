from functools import partial
from typing import Any, Dict, Mapping, Optional, Sequence, Set, TYPE_CHECKING, Tuple, Union

from sqlalchemy import Column, delete, exists, func, inspect, literal_column, select, tuple_, update
from sqlalchemy.exc import NoInspectionAvailable
from sqlalchemy.orm import DeclarativeMeta, RelationshipProperty, declarative_base, joinedload, selectinload
from sqlalchemy.sql import ColumnCollection

from dropland.data.models.model import SqlModel
from dropland.util import calculate_digest


class SqlaModel(DeclarativeMeta, type(SqlModel)):
    # noinspection PyUnresolvedReferences
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            column_names_map = inspect(cls).c
        except NoInspectionAvailable:
            pass
        else:
            column_names_map = zip([column.name for column in column_names_map], column_names_map.keys())
            cls.Meta._column_names_map = dict(column_names_map)


if TYPE_CHECKING:
    SqlaModelMeta = SqlModel
else:
    SqlaModelMeta = declarative_base(name='SqlaModel', cls=(SqlModel,), metaclass=SqlaModel)


class SqlaModelBase(SqlaModelMeta):
    __abstract__ = True

    class Meta(SqlModel.Meta):
        single_loader = joinedload
        list_loader = selectinload
        _column_names_map = dict()
        _query_opts_cache: Dict[str, list] = dict()

    # noinspection PyUnresolvedReferences
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        meta_dict = dict()
        for t in reversed(cls.Meta.__mro__):
            meta_dict.update({k: v for k, v in vars(t).items() if not k.startswith('__')})
        cls.Meta = type('Meta', (SqlModel.Meta,), meta_dict)

        cls.Meta.private_fields.update({'metadata', 'registry'})
        cls.Meta.non_serializable_fields.update({'metadata', 'registry'})
        cls.Meta._query_opts_cache = dict()

    def get_id_value(self) -> Any:
        return self._get_column_values(self._get_id_columns())

    @classmethod
    def get_columns(cls) -> ColumnCollection:
        return cls.__table__.columns

    @classmethod
    def get_relationships(cls) -> Mapping[str, Any]:
        return cls.__mapper__.relationships.items()

    # noinspection PyProtectedMember
    @classmethod
    def query_options(cls, include: Optional[Set[str]] = None, exclude: Optional[Set[str]] = None):
        args_digest = calculate_digest((include, exclude))

        if args_digest in cls.Meta._query_opts_cache:
            return cls.Meta._query_opts_cache[args_digest]

        result = list()
        suboptions = dict()
        suboptions_functions = dict()

        for rela_name, rela in cls.get_relationships():  # type: str, RelationshipProperty
            include_rela = True
            include_subkeys = {
                key.replace(f'{rela_name}.', '') for key in include if key.startswith(f'{rela_name}.')
            } if isinstance(include, set) else set()
            exclude_subkeys = {
                key.replace(f'{rela_name}.', '') for key in exclude if key.startswith(f'{rela_name}.')
            } if isinstance(exclude, set) else set()

            if include:
                include_rela &= include == '*' or rela_name in include or bool(include_subkeys)
            if include_rela and exclude:
                include_rela &= not (exclude == '*' or (not exclude_subkeys and rela_name in exclude))
            if include_rela:
                options = cls.Meta.list_loader(rela.class_attribute) if rela.uselist \
                    else cls.Meta.single_loader(rela.class_attribute)

                suboptions[rela_name] = options
                new_include, new_exclude = include_subkeys or None, exclude_subkeys or None
                suboptions_function = partial(rela.entity.class_.query_options, new_include, new_exclude)
                suboptions_functions[rela_name] = suboptions_function
                result.append(options)

        cls.Meta._query_opts_cache[args_digest] = result

        for rela_name, sub_rela in suboptions.items():
            subopts = suboptions_functions[rela_name]()
            suboptions[rela_name] = sub_rela.options(*subopts)

        return result

    # noinspection PyUnresolvedReferences,PyProtectedMember
    @classmethod
    def query_for_select(cls, include_rela: Optional[Set[str]] = None,
                         exclude_rela: Optional[Set[str]] = None, **kwargs):
        return select(cls).options(*cls.query_options(include_rela, exclude_rela))

    @classmethod
    def query_for_update(cls, **kwargs):
        return update(cls)

    @classmethod
    def query_for_delete(cls, **kwargs):
        return delete(cls)

    #
    # Query operations
    #

    @classmethod
    def query_get(cls, id_value: Any, query=None, **kwargs):
        cls._check_abstract()
        if not isinstance(id_value, (list, tuple, dict)):
            ident_ = [id_value]
        else:
            ident_ = id_value
        columns = cls._get_id_columns()
        if len(ident_) != len(columns):
            raise ValueError(
                f'Incorrect number of values as primary key: expected {len(columns)}, got {len(ident_)}.')

        clause = query if query is not None else cls.query_for_select(**kwargs)
        for i, c in enumerate(columns):
            try:
                val = ident_[i]
            except KeyError:
                val = ident_[cls._get_field_by_column(c)]
            clause = clause.where(c == val)
        return clause

    @classmethod
    def query_any(cls, indices: Sequence[Any], query=None, **kwargs):
        cls._check_abstract()
        columns = cls._get_id_columns()
        clause = query if query is not None else cls.query_for_select(**kwargs)
        vals_clause = []

        for ident in indices:
            if not isinstance(ident, (list, tuple, dict)):
                ident_ = [ident]
            else:
                ident_ = ident

            if len(ident_) != len(columns):
                raise ValueError(
                    f'Incorrect number of values as primary key: expected {len(columns)}, got {len(ident_)}.')

            vals = []
            for i, c in enumerate(columns):
                try:
                    val = ident_[i]
                except KeyError:
                    val = ident_[cls._get_field_by_column(c)]
                vals.append(val)

            if len(vals) == 1:
                vals_clause.append(vals[0])
            elif len(vals) > 1:
                vals_clause.append((*vals,))

        if len(columns) == 1:
            clause = clause.where(columns[columns.keys()[0]].in_(vals_clause))
        elif len(columns) > 1:
            clause = clause.where(tuple_(*columns).in_(vals_clause))
        return clause

    @classmethod
    def query_list(cls, filters: Sequence[Any], sorting: Sequence[Any],
                   skip: int = 0, limit: int = 0, params: Mapping[str, Any] = None, **kwargs):
        query = cls.query_for_select(**kwargs).offset(skip if skip >= 0 else 0)
        if limit > 0:
            query = query.limit(limit)
        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)
        for s in sorting:
            query = query.order_by(s)
        return query

    # noinspection PyUnresolvedReferences
    @classmethod
    def query_count(cls, filters: Optional[Sequence[Any]] = None, params: Mapping[str, Any] = None, **kwargs):
        if filters:
            query = cls.query_for_select()
            for f in filters:
                query = query.where(f)
            if params:
                query = query.params(**params)
        else:
            query = cls.__table__

        return select([func.count(literal_column('1'))]).select_from(query.alias())

    @classmethod
    def query_exists(cls, id_value: Any, **kwargs):
        return cls.query_get(id_value, query=exists(), **kwargs).select()

    @classmethod
    def query_exists_by(cls, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs):
        query = exists(cls)

        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)

        return query.select()

    @classmethod
    def query_update(cls, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs):
        query = cls.query_for_update(**kwargs)

        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)

        return query

    @classmethod
    def query_delete(cls, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs):
        query = cls.query_for_delete(**kwargs)

        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)

        return query

    #
    # Private
    #

    # noinspection PyUnresolvedReferences
    @classmethod
    def _check_abstract(cls):
        if cls.__table__ is None:
            raise TypeError(f'Model {cls.__name__} is abstract, no table is defined!')

    def __eq__(self, other: 'SqlaModelBase'):
        self._check_abstract()
        return type(self) == type(other) and self.get_id_value() == other.get_id_value()

    def __hash__(self):
        self._check_abstract()
        return self.get_id_value().__hash__()

    @classmethod
    def _get_id_columns(cls) -> ColumnCollection:
        return cls.__table__.primary_key.columns

    # noinspection PyProtectedMember
    @classmethod
    def _get_field_by_column(cls, c: Column) -> str:
        return cls.Meta._column_names_map.get(c.name)

    def _get_column_values(
            self, columns: ColumnCollection, force_tuple: bool = False) -> Union[Any, Tuple[Any]]:
        rv = []
        for c in columns:
            rv.append(getattr(self, self._get_field_by_column(c)))
        return rv[0] if len(rv) == 1 and not force_tuple else tuple(rv)

    @classmethod
    def _get_fk_columns(cls, model) -> ColumnCollection:
        for fk in cls.__table__.foreign_keys:
            if model.__table__ == fk.constraint.referred_table:
                return fk.constraint.columns
        return ColumnCollection()
