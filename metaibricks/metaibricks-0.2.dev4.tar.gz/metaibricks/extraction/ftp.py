import itertools
import ftplib
import re
from typing import Any, Optional, List, Tuple, Dict, Iterator
from multiprocessing import Pool
from functools import partial
import time

from pydantic import Field

from metaibricks.settings import Logger, log_error
from metaibricks.extraction.base import ExtractorBase, SessionBase

LOGGER = Logger(name="extraction.ftp")


class FTPSession(SessionBase):
    """Model used for handling FTP sessions

    Attrs:
        host (str):  Host's name
        username (Optional[str]): user's name used to log in. If not provided,
            the one given in .netrc will be used.
        password (Optional[SecretStr]): password associated to the username. If not
            provided, the one given in the .netrc will be used.

    Private Attrs:
        _handler (ftplib.FTP): FTP handler. It is used as a private attribute
            in order to prevent timeouts by using it through the "handler" property.

    Example:
        >>> os.listdir("my_dir")
        []
        >>> cat ~/.netrc
        machine toto.meteo.fr login my_login password my_password
        >>> session = FTPSession(host="toto.meteo.fr")
        >>> session
        FTPSession(
            host="toto.meteo.fr",
            username="my_login",
            password=SecretStr("********")
        )
        >>> session.password.get_secret_value()
        "my_password"
        >>> session.get("/my/remote/file.txt", "my_dir/file.txt")
        >>> os.listdir("my_dir")
        ["file.txt"]
    """

    host: str
    _handler: Optional[ftplib.FTP] = None
    _activation_time: float = time.time()

    class Config:
        underscore_attrs_are_private = True
        arbitrary_types_allowed = True

    @property
    def handler(self) -> ftplib.FTP:
        """property to activate then expose the FTP handler associated with the given
        credentials.

        Returns:
            ftplib.FTP: FTP Handler
        """
        activate = False
        try:
            self._handler.pwd()  # just verifying if activated
            if time.time() - self._activation_time > 20:
                activate = True
        except (
            AttributeError,
            ftplib.error_perm,
            ftplib.error_temp,
            EOFError,
            BrokenPipeError,
            TimeoutError,
        ):
            activate = True
        if activate:
            self._handler = ftplib.FTP(
                host=self.host,
                user=self.username,
                passwd=self.password.get_secret_value(),
            )
            self._activation_time = time.time()
            LOGGER.info("FTP handler activation", host=self.host, user=self.username)
        return self._handler

    def download(self, src_filename: str, tmp_filename: str) -> None:
        """Method to download a file from a remote machine using FTP protocol.

        Args:
            src_filename (str): Remote source file's name.
            tmp_filename (str): Local destination temporary file's name.
        """
        with open(tmp_filename, "wb") as fp:
            self.handler.retrbinary(f"RETR {src_filename}", fp.write)

    def get_subfolders_and_files(self, dirname: str) -> List[str]:
        """Method to retrieve the list of subfolders and files of the directory
        "dirname", from a remote machine using FTP protocol.

        Args:
            dirname (str): Name of the directory

        Returns:
            List[str]: List of subdirectories and files.
        """
        if dirname == "":
            dirname = "/"  # dirname root case

        try:
            self.handler.cwd(dirname)
        except ftplib.error_perm:
            LOGGER.warning(
                "Given pattern and directory's name matches with a file",
                host=self.host,
                dirname=dirname,
            )
            return []

        tries = 2
        for i in range(tries):
            try:
                filelist = self.handler.nlst()
            except TimeoutError:
                if i < tries - 1:
                    continue
                else:
                    LOGGER.warning(
                        "TimeOut Error while retrieving list of files : ignoring folder"
                    )
                    return []
            break
        return filelist


class FTPExtractorBase(ExtractorBase):
    """Abstract class for defining an FTPExtractor

    Attrs:
        kind (str): Extractor's kind. Constant "FTP".
    """

    kind: str = Field("FTP", const=True)


class FTPFiles(FTPExtractorBase):
    """Extractor used for extracting multiple given files using FTP.

    Attrs:
        kind (str): Constant "FTP"
        session (FTPSession): FTP session to use for extracting multiple files.
        files (List[Tuple[str, str]]): List of files to get. Each element of
            the list is a tuple containing the source file's name and the destination
            file's name.
        n_workers (Optional[int]): Numbers of workers to use to parallelize the
            extraction.

    Example:
        >>> os.listdir("my_dir")
        []
        >>> extr = FTPFiles(
                session={"host": "toto.meteo.fr"},
                files=[
                    ("/my/remote/file1.txt", "./my_dir/file1.txt"),
                    ("/my/remote/file2.txt", "./my_dir/file2.txt"),
                ]
            )
        >>> extr.run()
        >>> os.listdir("my_dir")
        ["file1.txt", "file2.txt"]
    """

    session: FTPSession
    files: List[Tuple[str, str]]

    def run(self) -> bool:
        """Main method to get all self.files.

        Returns:
            bool: Whether the extraction is alright or not.
        """
        if self.n_workers <= 1:
            return all([self.session.get(src, dst) for src, dst in self.files])
        result = []
        pool = Pool(self.n_workers)
        for src, dst in self.files:
            pool.apply_async(
                FTPSession(**self.session.dict()).get,
                args=(
                    src,
                    dst,
                ),
                callback=result.append,
                error_callback=partial(log_error, log=LOGGER),
            )
        pool.close()
        pool.join()
        return all(result)


class FTPDir(FTPExtractorBase):
    """Extractor used for extracting multiple files using FTP.
    With this extractor file's name are not explicitly specified, but
    the source and destination directories are specified using constraints.

    Attrs:
        kind (str): Extractor's kind. Constant "FTP".
        session (FTPSession): FTP Session to use for extracting all files.
        src (str): Remote source files's pattern. It may contain tags "{}"
            to specify constraints (from self.constraints).
        dst (str): Local destination files's pattern. It also may contain
            tags "{}" to specify constraints (from self.constraints and src groups).
        constraints (Dict[str, List[Any]]): Dictionnary containing the possible values
            of all the tags given in src.
        n_workers (Optional[int]): Numbers of workers to use to parallelize the
            extraction.

    Private Attrs::
        _files (List[Tuple[str, str]]): List of files to retrieve when they have been
            found remotely according to the src description.

    Example:
        >>> os.listdir("my_dir")
        []
        >>> extr = FTPDir(
                session={"host": "toto.meteo.fr"},
                src="/my/remote/{year}/{month:02d}/(?P<basename>.\\w+.txt)",
                dst="my_dir/{year}_{month:02d}/{basename}",
                constraints={
                    "date": [2021],
                    "month": [1, 2, 3],
                }
            )
        >>> list(os.get_constraints_combinations())
        [
            {"year": 2021, "month": 1},
            {"year": 2021, "month": 2},
            {"year": 2021, "month": 3},
        ]
        >>> extr.files
        [
            ("/my/remote/2021/01/file1.txt", "my_dir/2021_01/file1.txt"),
            ("/my/remote/2021/01/file2.txt", "my_dir/2021_01/file2.txt"),
            ("/my/remote/2021/02/file3.txt", "my_dir/2021_02/file3.txt"),
            ("/my/remote/2021/03/file4.txt", "my_dir/2021_03/file4.txt"),
        ]
        >>> extr.run()
        >>> os.listdir("my_dir")
        ["2021_01", "2021_02", "2021_03"]
        >>> os.listdir("my_dir/2021_01")
        ["file1.txt", "file2.txt"]
    """

    kind: str = Field("FTP", const=True)
    session: FTPSession
    src: str
    dst: str
    constraints: Dict[str, List[Any]] = {}
    _files: List[Tuple[str, str]] = None

    def get_constraints_combinations(self) -> Iterator[Dict[str, Any]]:
        """Generator made for creating the possible combinations
        with the given constraints.

        Yields:
            Iterator[Dict[str, Any]]: Iteration of dictionnaries with the name
                of the constraint as key, and its given value.
        """
        for values in itertools.product(*self.constraints.values()):
            yield {k: v for k, v in zip(self.constraints.keys(), values)}

    def get_matching_dst(self, src_filename: str, format_dico: Dict[str, Any]) -> str:
        """Returns the formated dst_filename corresponding to the given src_filename
        and the current constraints, and according to self.src and self.dst.

        Args:
            src_filename (str): Source file's name.
            format_dico (Dict[str, Any]): Dictionnary containing the keys and values
                to format the dst filename.

        Returns:
            str: Formated destination filename

        Example:
            >>> extr = FTPDir(
                session={"host": "toto.meteo.fr"},
                src="/my/remote/{year}/(?P<basename>.\\w+.txt)",
                dst="my_dir/{year}_{basename}",
                constraints={"date": [2021]},
            )
            >>> extr.get_matching_dst("/my/remote/2021/file1.txt", {"year":2021})
            "my_dir/2021_file1.txt"
        """
        reg = re.compile(self.src.format(**format_dico))
        match = reg.match(src_filename)
        if not bool(match):
            dico = {gn: None for gn in reg.groupindex}
        else:
            dico = {gn: match.group(gn) for gn in reg.groupindex}
        dico.update(format_dico)
        return self.dst.format(**dico)

    @property
    def files(self) -> List[Tuple[str, str]]:
        """Property that gives the list of the files found in the FTP session that
        corresponds to the self.src and self.constraints.

        Returns:
            List[Tuple[str, str]]: List of files to get. Each element of
            the list is a tuple containing the source file's name and the destination
            file's name.
        """
        if self._files is not None:
            return self._files
        self._files = []
        LOGGER.debug("Starting to find files.")
        for dico in self.get_constraints_combinations():
            # formatting the directory's name with the constraints
            LOGGER.debug(f"Current constraint dico : {dico}")
            format_src = self.src.format(**dico)
            LOGGER.debug(f"Formated src : {format_src}")
            sources = ["."]
            # finding all source matching the src_dirname pattern by iteration
            for pattern in format_src.split("/"):
                LOGGER.debug(f"Finding pattern {pattern} in {sources}")
                sources = self.session.find_pattern(pattern, sources)
            LOGGER.debug(f"Final sources found: {sources} with {format_src}")
            self._files += [(src, self.get_matching_dst(src, dico)) for src in sources]
        self._files = sorted(self._files)
        LOGGER.debug(f"Final files : {self._files}")
        return self._files

    def to_ftp_extractor(self) -> FTPFiles:
        """Short method for returning the equivalent FTPFiles.

        Returns:
            FTPFiles: FTPFiles equivalent to the given attributes.
        """
        return FTPFiles(
            session=self.session,
            files=self.files,
            n_workers=self.n_workers,
        )

    def run(self) -> bool:
        """Main method to get all self.files.

        Returns:
            bool: Whether the extraction is alright or not.
        """
        return self.to_ftp_extractor().run()
