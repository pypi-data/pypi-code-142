from __future__ import annotations

import logging
import pathlib
import sys

import appdirs
import attrs

from . import client, config, db, domain, repository, version


@attrs.define
class App:

    configuration: config.Configuration
    aoc_client: client.IAocClient
    input_repository: repository.InputRepository
    submission_repository: repository.SubmissionRepository
    version: str = attrs.field(init=False)

    def __attrs_post_init__(self) -> None:
        """Set up logging."""
        root_logger = logging.getLogger()
        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setFormatter(logging.Formatter("[easy-aoc] %(message)s"))
        console_handler.setLevel(logging.DEBUG)
        root_logger.addHandler(console_handler)
        root_logger.setLevel(logging.ERROR)

        easy_aoc_logger = logging.getLogger("easy_aoc")
        easy_aoc_logger.setLevel(logging.INFO)

        self.version = version.__version__

    @classmethod
    def get_default_app(cls) -> App:
        configuration = config.Configuration.from_environment()
        aoc_client = client.AocClient(
            session_key=configuration.session_key,
            base_url=configuration.base_url,
            version=version.__version__,
        )
        cache_dir = pathlib.Path(appdirs.user_cache_dir("easy-aoc", "SebastiaanZ"))
        cache_dir.mkdir(parents=True, exist_ok=True)
        db_dir = cache_dir / "cache.db"
        sessionmaker = db.get_sessionmaker(f"sqlite:///{db_dir!s}")
        input_repository = repository.InputRepository(sessionmaker)
        submission_repository = repository.SubmissionRepository(sessionmaker)

        return cls(
            configuration=configuration,
            aoc_client=aoc_client,
            input_repository=input_repository,
            submission_repository=submission_repository,
        )

    def get_puzzle_input(self, puzzle: domain.Puzzle) -> domain.PuzzleInput:
        """Get the puzzle input for a given year and day.

        :param puzzle: The puzzle to get the input of
        :return: The puzzle input
        """
        puzzle_input = self.input_repository.get(puzzle=puzzle)
        if puzzle_input is None:
            puzzle_input = self.aoc_client.get_puzzle_input(puzzle=puzzle)
            self.input_repository.add(puzzle_input)

        return puzzle_input

    def submit_answer(self, answer: domain.Answer) -> domain.Submission:
        if (submission := self.submission_repository.get(answer)) is not None:
            return submission

        correct_submission = self.submission_repository.get_correct_answer(answer.part)
        if correct_submission is not None:
            # There's already a different, correct answer cached. This
            # means the new answer must be incorrect.
            incorrect = domain.Submission(answer=answer, result=domain.Result.INCORRECT)
            self.submission_repository.add(incorrect)
            return incorrect

        # The result can't be determined based on the cache; the answer
        # needs to be submitted to the Advent of Code website.
        return self.aoc_client.submit_answer(answer)
