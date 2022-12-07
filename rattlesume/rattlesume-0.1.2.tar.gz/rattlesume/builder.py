from dataclasses import dataclass
from pathlib import Path

import yaml

from rattlesume.exceptions import DefinitionError


@dataclass
class Snippet:
    markdown: str
    sulg: dict


def read_markdown(file: Path, depth: int = 0) -> Snippet:
    """
    Reads in a markdown file and applies pre-processing.

    args:
        file: The Markdown file to read.

        depth: The number of headers deep.
            For example, a raw '## header' with a depth of
            3 will be changed to '##### header'
    """
    with open(file) as fp:
        raw_markdown = fp.read().splitlines()

    # Parse Slug
    slug = {}
    if "---" == raw_markdown[0]:
        raw_markdown = raw_markdown[1:]
        end_slug = raw_markdown.index("---")
        raw_slug, raw_markdown = raw_markdown[:end_slug], raw_markdown[end_slug + 1 :]
        slug = yaml.load("\n".join(raw_slug), Loader=yaml.Loader)

    # TODO: Implement depth
    for i, line in enumerate(raw_markdown):
        if line.strip().startswith("#"):
            raw_markdown[i] = "#" * depth + line.strip()

    return Snippet("\n".join(raw_markdown), slug)


def parse_yaml(file: Path) -> dict:
    with open(file) as fp:
        return yaml.load(fp, Loader=yaml.Loader)


def build_document(definition: Path) -> str:
    structure = parse_yaml(definition)
    document = ""
    base_path = definition.parent.parent / "content"
    document += build_header(structure.get("header", {}))
    document += "\n\n"
    document += build_body(structure["resume"], base_path)
    return document


def build_header(structure: list[str]) -> str:
    if not structure:
        return ""
    return "\n".join(structure)


def build_body(structure: dict, base_path: Path):
    document = ""
    for category, snippets in structure.items():
        if not isinstance(snippets, list):
            header = snippets["header"]
            snippets = snippets["snippets"]
        else:
            header = category.strip().capitalize()

        document += f"\n\n# {header}\n\n"
        for snippet in snippets:
            match snippet:
                case "---":
                    document += snippet
                case _:
                    path = base_path / category / snippet
                    if not path.exists():
                        raise DefinitionError(
                            f"{path=} Does not exist, cannot create document"
                        )
                    document += read_markdown(
                        base_path / category / snippet, depth=1
                    ).markdown
            document += "\n\n"
    return document
