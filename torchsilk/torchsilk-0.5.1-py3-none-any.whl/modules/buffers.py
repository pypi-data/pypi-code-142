"""Functionality related to buffers for torchsilk modules."""
import typing as t

import attrs
import lovely_tensors as lt  # type: ignore
import torch
from rich.console import Console
from rich.table import Table


@attrs.define()
class NamedBuffers(t.Mapping[str, torch.Tensor]):
    """Allows one to access buffers as attributes.

    Example:

    >>> class MyModule(torch.nn.Module):
    ...     def __init__(self):
    ...         super().__init__()
    ...         self.register_buffer("foo", torch.tensor(1))
    ...         self.register_buffer("bar", torch.tensor(2))
    ...     def forward(self, x):
    ...         return x
    ... buffers = NamedBuffers.from_module(MyModule())
    ... assert torch.allclose(buffers.foo, torch.tensor(1))
    ... assert torch.allclose(buffers.bar, torch.tensor(2))
    """

    buffers: t.Mapping[str, torch.Tensor]

    @classmethod
    def from_module(cls, module: torch.nn.Module) -> "NamedBuffers":
        return cls(dict(module.named_buffers()))

    def evolve_from_values(self, values: tuple[torch.Tensor]) -> "NamedBuffers":
        """Create a new NamedBuffers with the same keys but new values."""
        assert len(values) == len(self.buffers)
        return attrs.evolve(self, buffers=dict(zip(self.buffers.keys(), values)))

    def evolve(self, values: dict[str, torch.Tensor]) -> "NamedBuffers":
        """Create a new NamedBuffers with the same keys but new values."""
        return attrs.evolve(self, buffers={**self.buffers, **values})

    def as_table(
        self, name_column_width: int = 24, buffers_column_width: int = 56
    ) -> Table:
        """Return a rich Table representation of the buffer.

        Args:
        -----
            name_column_width: The width of the name column.
            buffers_column_width: The width of the buffers column.
        Returns:
        --------
            A rich Table representation of the buffer.

        Example representation:
        -----------------------
        >>> import torch
        ... import rich
        ... class MyModule(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         generator = torch.Generator().manual_seed(0)
        ...         self.register_buffer("foo", torch.ones(5, 5))
        ...         self.register_buffer("bar", torch.randn(5, 5, generator=generator))
        ...     def forward(self, x):
        ...         return x
        ... buffers = NamedBuffers.from_module(MyModule())
        ... rich.print(buffers.as_table())

        ┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Name        ┃                 Buffers                  ┃
        ┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
        │ foo         │    tensor[5, 5] n=25 x∈[1.000, 1.000]    │
        │             │               μ=1.000 σ=0.               │
        │ bar         │   tensor[5, 5] n=25 x∈[-2.564, 2.014]    │
        │             │             μ=-0.215 σ=1.149             │
        └─────────────┴──────────────────────────────────────────┘
        """
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name", style="dim", width=name_column_width)
        table.add_column(
            "Buffers",
            style="dim",
            width=buffers_column_width,
            justify="center",
        )
        for name, buffer in self.buffers.items():
            table.add_row(name, str(lt.lovely(buffer)))
        return table

    def show(self) -> None:
        """Show a pretty representation of the buffer.

        Example representation:
        -----------------------

        >>> import torch
        ... import rich
        ... class MyModule(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         generator = torch.Generator().manual_seed(0)
        ...         self.register_buffer("foo", torch.ones(5, 5))
        ...         self.register_buffer("bar", torch.randn(5, 5, generator=generator))
        ...     def forward(self, x):
        ...         return x
        ... buffers = NamedBuffers.from_module(MyModule())
        ... buffers.show()

        ┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Name        ┃                 Buffers                  ┃
        ┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
        │ foo         │    tensor[5, 5] n=25 x∈[1.000, 1.000]    │
        │             │               μ=1.000 σ=0.               │
        │ bar         │   tensor[5, 5] n=25 x∈[-2.564, 2.014]    │
        │             │             μ=-0.215 σ=1.149             │
        └─────────────┴──────────────────────────────────────────┘
        """
        console = Console()
        console.print(
            self.as_table(name_column_width=24, buffers_column_width=console.width - 24)
        )

    def __getattr__(self, name: str) -> torch.Tensor:
        try:
            return self.buffers[name]
        except KeyError:
            raise AttributeError(f"Module has no buffer {name}") from None

    def __getitem__(self, name: str) -> torch.Tensor:
        return self.buffers[name]

    def __iter__(self) -> t.Iterator[str]:
        return iter(self.buffers)

    def __len__(self) -> int:
        return len(self.buffers)
