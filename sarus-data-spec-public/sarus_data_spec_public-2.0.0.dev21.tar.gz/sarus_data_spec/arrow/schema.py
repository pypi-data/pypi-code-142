import typing as t

import pyarrow as pa

from sarus_data_spec.type import Type
import sarus_data_spec.arrow.type as arrow_type
import sarus_data_spec.protobuf as sp
import sarus_data_spec.typing as st


def to_arrow(schema: sp.Schema) -> pa.schema:
    """Convert Sarus schema to pyarrow schema."""
    return arrow_schema(Type(schema.type))


def arrow_schema(_type: st.Type) -> pa.Schema:
    """Visitor that returns the schema Arrow given the Sarus Type
    #TODO: Currently only Struct and Unions are supported
    """

    class SchemaVisitor(st.TypeVisitor):
        schema: pa.Schema = pa.schema(fields=[])

        def Integer(self, min: int, max: int, base: st.IntegerBase) -> None:
            pass

        def Float(self, min: float, max: float, base: st.FloatBase) -> None:
            pass

        def Datetime(
            self,
            format: str,
            min: str,
            max: str,
            base: st.DatetimeBase,
        ) -> None:
            pass

        def Date(
            self,
            format: str,
            min: str,
            max: str,
            base: st.DateBase,
        ) -> None:
            pass

        def Time(
            self,
            format: str,
            min: str,
            max: str,
            base: st.TimeBase,
        ) -> None:
            pass

        def Duration(
            self,
            unit: str,
            min: int,
            max: int,
        ) -> None:
            pass

        def Struct(
            self,
            fields: t.Mapping[str, st.Type],
            name: t.Optional[str] = None,
        ) -> None:
            self.schema = pa.schema(
                fields=[
                    pa.field(
                        name=field_name,
                        type=arrow_type.to_arrow(fields[field_name]),
                    )
                    for field_name in fields.keys()
                ]
            )

        def Constrained(
            self,
            type: st.Type,
            constraint: st.Predicate,
            name: t.Optional[str] = None,
        ) -> None:
            pass

        def List(
            self,
            type: st.Type,
            max_size: int,
            name: t.Optional[str] = None,
        ) -> None:
            # TODO
            pass

        def Array(
            self,
            type: st.Type,
            shape: t.Tuple[int, ...],
            name: t.Optional[str] = None,
        ) -> None:
            # TODO
            pass

        def Optional(
            self, type: st.Type, name: t.Optional[str] = None
        ) -> None:
            pass

        def Union(
            self,
            fields: t.Mapping[str, st.Type],
            name: t.Optional[str] = None,
        ) -> None:
            arrow_fields = [
                pa.field(
                    name=field_name,
                    type=arrow_type.to_arrow(field_type),
                )
                for field_name, field_type in fields.items()
            ]
            arrow_fields.append(
                pa.field(name='field_selected', type=pa.string())
            )
            self.schema = pa.schema(fields=arrow_fields)

        def Boolean(self) -> None:
            pass

        def Bytes(self) -> None:
            pass

        def Unit(self) -> None:
            pass

        def Hypothesis(
            self, *types: t.Tuple[st.Type, float], name: t.Optional[str] = None
        ) -> None:
            pass

        def Id(
            self,
            unique: bool,
            reference: t.Optional[st.Path] = None,
            base: t.Optional[st.IdBase] = None,
        ) -> None:
            pass

        def Null(self) -> None:
            pass

        def Enum(
            self,
            name: str,
            name_values: t.Sequence[t.Tuple[str, int]],
            ordered: bool,
        ) -> None:
            pass

        def Text(self, encoding: str) -> None:
            pass

    visitor = SchemaVisitor()
    _type.accept(visitor)
    return visitor.schema
