import pytest

from repo_ranger import filter_repos


def test_filter_repos_no_filtering():
    repos = [
        {"tags": ["web", "frontend"]},
        {"tags": ["api", "backend"]},
        {"tags": ["docs"]},
    ]

    # Test with no filtering
    filtered_repos = filter_repos(repos, None, None)
    assert filtered_repos == repos


def test_filter_repos_include():
    repos = [
        {"tags": ["web", "frontend"]},
        {"tags": ["api", "backend"]},
        {"tags": ["docs"]},
    ]

    # Test with include filtering
    filtered_repos = filter_repos(repos, ["web"], None)
    assert filtered_repos == [{"tags": ["web", "frontend"]}]

    filtered_repos = filter_repos(repos, ["api"], None)
    assert filtered_repos == [{"tags": ["api", "backend"]}]

    filtered_repos = filter_repos(repos, ["frontend", "backend"], None)
    assert filtered_repos == [
        {"tags": ["web", "frontend"]},
        {"tags": ["api", "backend"]},
    ]


def test_filter_repos_exclude():
    repos = [
        {"tags": ["web", "frontend"]},
        {"tags": ["api", "backend"]},
        {"tags": ["docs"]},
    ]

    # Test with exclude filtering
    filtered_repos = filter_repos(repos, None, ["web"])
    assert filtered_repos == [{"tags": ["api", "backend"]}, {"tags": ["docs"]}]

    filtered_repos = filter_repos(repos, None, ["api"])
    assert filtered_repos == [{"tags": ["web", "frontend"]}, {"tags": ["docs"]}]

    filtered_repos = filter_repos(repos, None, ["frontend", "backend"])
    assert filtered_repos == [{"tags": ["docs"]}]


def test_filter_repos_include_exclude():
    repos = [
        {"tags": ["web", "frontend"]},
        {"tags": ["api", "backend"]},
        {"tags": ["docs"]},
    ]

    # Test with include and exclude filtering
    filtered_repos = filter_repos(repos, ["web"], ["docs"])
    assert filtered_repos == [{"tags": ["web", "frontend"]}]

    filtered_repos = filter_repos(repos, ["frontend"], ["backend"])
    assert filtered_repos == [{"tags": ["web", "frontend"]}]

    filtered_repos = filter_repos(repos, ["frontend", "docs"], ["web"])
    assert filtered_repos == [{"tags": ["docs"]}]
