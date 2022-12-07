import os
from pathlib import Path
from git import Repo, SymbolicReference
from git.exc import InvalidGitRepositoryError
import traceback

from continual.python.sdk.metadata import Metadata, MetadataManager
from continual.rpc.management.v1 import types


class ContextProvider:
    """Base context provider class."""

    name: str

    def log(self, metadata_manager: MetadataManager) -> Metadata:
        raise NotImplementedError()


class GitContext(ContextProvider):

    name: str = "git_context"

    def log(self, metadata_manager: MetadataManager) -> Metadata:
        if self._is_git_repo():
            try:
                git_context = self._get_git_metadata()
            except Exception as e:
                if metadata_manager.client.config.debug:
                    print(f"Error logging git context: {e}")
                    print(traceback.format_exc())
                return None
            else:
                return metadata_manager.create(
                    key=self.name,
                    type=types.MetadataType.GIT_CONTEXT.to_proto(),
                    data=git_context,
                )

    def _is_git_repo(self) -> bool:
        try:
            _ = Repo(os.getcwd())
            return True
        except InvalidGitRepositoryError:
            return False

    def _get_git_metadata(self) -> dict:
        repo = Repo(os.getcwd(), search_parent_directories=True)
        repo_is_bare = repo.bare

        repository_name_local = ""
        if repo.working_tree_dir:
            repository_name_local = Path(repo.working_tree_dir).parts[-1]

        repository_name_remote_origin = ""
        repository_remote_origin_url = ""
        if repo.remotes and repo.remotes[0].name == "origin":
            # TODO: consider getting this from current branch tracking branch instead
            repository_name_remote_origin = os.path.splitext(
                os.path.basename(repo.remotes.origin.url)
            )[0]
            repository_remote_origin_url = repo.remotes.origin.url

        repository_name = (
            repository_name_remote_origin
            if repository_name_remote_origin
            else repository_name_local
        )

        branch_name = ""
        try:
            branch_name = repo.active_branch.name
        except:
            pass

        current_commit = None
        if not repo_is_bare:
            if isinstance(repo.head, SymbolicReference):
                current_commit = repo.head.commit
            else:
                current_commit = repo.head.reference.commit

        current_ref = None
        try:
            current_ref = repo.head.reference
        except:
            pass

        current_tag_name = ""
        current_tag_name_long = ""
        try:
            current_tag_name = repo.git.describe("--exact-match", "--abbrev=0")
            current_tag_name_long = repo.git.describe("--exact-match", "--long")
        except:
            pass

        reachable_tag_name = ""
        reachable_tag_name_long = ""
        try:
            reachable_tag_name = repo.git.describe("--abbrev=0")
            reachable_tag_name_long = repo.git.describe("--long")
        except:
            pass

        # consider setting untracked_files=True here
        is_dirty = repo.is_dirty()

        return dict(
            repository=dict(
                name=repository_name,
                name_local=repository_name_local,
                name_remote_origin=repository_name_remote_origin,
                is_bare=repo_is_bare,
                remote_origin_url=repository_remote_origin_url
                # default_branch_name
            ),
            branch=dict(name=branch_name),
            tag_current=dict(
                name=current_tag_name, name_describe=current_tag_name_long
            ),
            tag_reachable=dict(
                name=reachable_tag_name, name_describe=reachable_tag_name_long
            ),
            ref=dict(path=current_ref.path if current_ref is not None else ""),
            commit=dict(
                sha=current_commit.hexsha,
                message=current_commit.message,
                authored_datetime=current_commit.authored_datetime,
                author=dict(
                    name=current_commit.author.name, email=current_commit.author.email
                ),
                committed_datetime=current_commit.committed_datetime,
                committer=dict(
                    name=current_commit.committer.name,
                    email=current_commit.committer.email,
                ),
            )
            if current_commit is not None
            else None,
            head=dict(is_detached=repo.head.is_detached),
            is_dirty=is_dirty,
        )
