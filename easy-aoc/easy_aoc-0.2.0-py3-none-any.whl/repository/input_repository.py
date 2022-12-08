"""Repository for getting puzzle inputs."""
import attrs
from sqlalchemy import orm

from .. import db, domain, utils


class InputRepository:
    """Repository for puzzle inputs."""

    def __init__(self, sessionmaker: orm.sessionmaker[orm.Session]) -> None:
        """Initialize the repository with a SQLAlchemy sessionmaker.

        :param sessionmaker: The sessionmaker to use
        """
        self._sessionmaker = sessionmaker

    def get(self, puzzle: domain.Puzzle) -> domain.PuzzleInput | None:
        """Get the puzzle input.

        If the puzzle input exists in the cache, it is retrieved from
        the cache. Otherwise, it's fetched from the Advent of Code
        website.

        :param puzzle: The puzzle to get the input of
        :return: An instance of PuzzleInput
        """
        with self._sessionmaker() as session:
            puzzle_input = session.get(db.PuzzleInput, attrs.astuple(puzzle))

        if puzzle_input is None:
            return None

        return domain.PuzzleInput(puzzle=puzzle, text=puzzle_input.text)

    def add(self, puzzle_input: domain.PuzzleInput) -> None:
        """Add the puzzle input to the repository.

        :param puzzle_input: The puzzle input to add
        """
        mapped_puzzle_input = db.PuzzleInput(**utils.serialize(puzzle_input))
        with self._sessionmaker() as session:
            session.add(mapped_puzzle_input)
            session.commit()


def _serialize_puzzle_input(puzzle_input: domain.PuzzleInput) -> dict[str, int | str]:
    """Serialize an instance of PuzzleInput.

    :param puzzle_input: The puzzle input to serialize
    :return: A flat dict
    """
    return {**attrs.asdict(puzzle_input.puzzle), "text": puzzle_input.text}
