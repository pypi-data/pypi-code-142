from enum import Enum, auto
from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass
from typing_extensions import Literal

from .exceptions import UnexpectedFormatError
from .utils import get_public_vars


class NiceEnum(Enum):
    # https://github.com/pydantic/pydantic/issues/598#issuecomment-503032706
    # config pydantic to get enum from string key.
    @classmethod
    def __get_validators__(cls):
        cls.lookup = {v: k.value for v, k in cls.__members__.items()}
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            if isinstance(v, cls):
                return v
            return cls[v]
        except KeyError as e:
            raise ValueError(
                f"Invalid value '{v}' not one of: {[x.name for x in cls]}"
            ) from e


class ComparisonResult(NiceEnum):
    equal = auto()
    conflict = auto()
    push = auto()
    pull = auto()
    ignore = auto()


class StatusUpdate(NiceEnum):
    published = auto()
    hidden = auto()
    draft = auto()
    trashed = auto()
    excluded = auto()


@dataclass
class ValidFilters:
    tag: Optional[str] = None
    slug: Optional[str] = None
    status: Optional[str] = None
    result: Optional[ComparisonResult] = None


# @dataclass
# class PubliiPostViewSettings:
#     display_author: Optional[bool] = Field(alias="displayAuthor")
#     display_date: Optional[bool] = Field(alias="displayDate")
#     display_modified_date: Optional[bool] = Field(alias="displayUpdatedDate")
#     display_share_buttons: Optional[bool] = Field(alias="displayShareButtons")
#     display_tags: Optional[bool] = Field(alias="displayTags")
#     display_author_bio: Optional[bool] = Field(alias="displayAuthorBio")
#     display_post_navigation: Optional[bool] = Field(alias="displayPostNavigation")
#     display_related_posts: Optional[bool] = Field(alias="displayRelatedPosts")
#     display_comments: Optional[bool] = Field(alias="displayComments")

#     def to_publii_metadata(self) -> str:
#         _field_map: Dict[str, str] = {
#             "display_author": "displayAuthor",
#             "display_date": "displayDate",
#             "display_modified_date": "displayUpdatedDate",
#             "display_share_buttons": "displayShareButtons",
#             "display_tags": "displayTags",
#             "display_author_bio": "displayAuthorBio",
#             "display_post_navigation": "displayPostNavigation",
#             "display_related_posts": "displayRelatedPosts",
#             "display_comments": "displayComments",
#         }
#         return json.dumps(
#             {
#                 _field_map[k]: {
#                     **{"type": "select"},
#                     **({} if v is None else {"value": str(int(v))}),
#                 }
#                 for k, v in get_public_vars(self).items()
#             },
#             indent=None,
#             separators=(",", ":"),
#         )


@dataclass
class PubliiPost:
    id: int
    slug: str
    author: str
    created_at: int
    modified_at: int
    status: str  # Literal["published", "hidden", "draft", "trashed"]
    status_all: str
    # view_settings: Union[Json[PubliiPostViewSettings], PubliiPostViewSettings]
    main_tag: str
    text_format: Literal["md", "json", "html"]
    text: str

    def compare(
        self,
        file_path_expected: Path,
        file_path_actual: Optional[Path],
        force_pull: bool = False,
        force_push: bool = False,
    ) -> "PubliiPostComparison":
        return PubliiPostComparison(
            file_path_expected=file_path_expected,
            file_path=file_path_actual,
            force_pull=force_pull,
            force_push=force_push,
            **get_public_vars(self),
        )


@dataclass
class PubliiPostComparison(PubliiPost):
    file_path_expected: Path
    file_path: Optional[Path] = None
    force_push: bool = False
    force_pull: bool = False
    file_modified_at: Optional[int] = Field(None, init=False)
    file_text: Optional[str] = Field(None, init=False)
    result: Optional[ComparisonResult] = Field(None, init=False)

    def __post_init__(self) -> None:
        if self.force_push and self.force_pull:
            raise ValueError(
                "Parameters `force_push` and `force_pull` are mutually exclusive."
            )

        if not self.file_path or not self.file_path.exists():
            self.result = (
                ComparisonResult.pull
                if not self.force_push
                else ComparisonResult.ignore
            )
        else:
            self.file_modified_at = int(self.file_path.stat().st_mtime * 1000)

            self.file_text = self.file_path.read_text()

            if self.file_path.suffix.lower() != f".{self.text_format}":
                raise UnexpectedFormatError(
                    f"Expected extension {self.text_format} for file:"
                    f" {self.file_path.name}"
                )

            if self.force_pull or self.modified_at > self.file_modified_at:
                self.result = ComparisonResult.pull
            elif self.force_push or self.modified_at < self.file_modified_at:
                self.result = ComparisonResult.push
            elif self.text == self.file_text:
                self.result = ComparisonResult.equal
            else:
                self.result = ComparisonResult.conflict
