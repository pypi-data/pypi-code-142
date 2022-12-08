import itertools
import re
from typing import Any, Optional, List, Tuple, Dict, Iterator
from multiprocessing import Pool
from functools import partial
import requests
from bs4 import BeautifulSoup
import urllib3

from pydantic import Field

from metaibricks.settings import Logger, log_error
from metaibricks.extraction.base import ExtractorBase, SessionBase

LOGGER = Logger(name="extraction.HTTP")


class HTTPSession(SessionBase):
    """Model used for handling HTTP sessions

    Attrs:
        host (Optional[str]):  Host's name
        username (Optional[str]): user's name used to log in. If not provided,
            the one given in .netrc will be used.
        password (Optional[str]): password associated to the username. If not
            provided, the one given in the .netrc will be used.
        verify_ssl (Optional[bool]): whether to verify the SSL certificates
        certificate (Optional[str]): path to SSL certificate

    Private Attrs:
        _handler (requests.Session): HTTP handler. It is used as a private attribute
            in order to prevent timeouts by using it through the "handler" property.

    Example:
        >>> os.listdir("my_dir")
        []
        >>> cat ~/.netrc
        machine toto.meteo.fr login my_login password my_password
        >>> session = HTTPSession(host="toto.meteo.fr")
        >>> session
        HTTPSession(
            host="toto.meteo.fr",
            username="my_login",
            password=SecretStr("********")
        )
        >>> session.password.get_secret_value()
        "my_password"
        >>> session.get("https://toto.meteo.fr/my/remote/file.txt", "my_dir/file.txt")
        >>> os.listdir("my_dir")
        ["file.txt"]
    """

    verify_ssl: Optional[bool]
    certificate: Optional[str]
    _handler: Optional[requests.Session] = None

    class Config:
        underscore_attrs_are_private = True
        arbitrary_types_allowed = True

    @property
    def handler(self) -> requests.Session:
        """property to activate then expose the HTTP handler associated with the given
        credentials.

        Returns:
            requests.Session: HTTP Handler
        """
        try:
            self._handler.get(
                "https://meteofrance.com/", verify=self.verify_ssl
            )  # just verifying if activated
        except (AttributeError):
            self._handler = requests.Session()
            if not self.verify_ssl:
                urllib3.disable_warnings()
            if self.certificate:
                self._handler.cert = self.certificate
            if self.username is not None:
                self._handler.auth = requests.auth.HTTPDigestAuth(
                    self.username, self.password.get_secret_value()
                )
            LOGGER.info("HTTP handler activation", user=self.username)
        return self._handler

    def download(self, src_filename: str, tmp_filename: str) -> None:
        """Method to download a file from a remote machine using HTTP protocol.

        Args:
            src_filename (str): Remote source file's name.
            tmp_filename (str): Local destination temporary file's name.
        """
        with open(tmp_filename, "wb") as fp:
            fp.write(self.handler.get(src_filename, verify=self.verify_ssl).content)

    def get_subfolders_and_files(self, dirname: str) -> List[str]:
        """Method to retrieve the list of subfolders and files of the directory
        "dirname", from a remote machine, by parsing the HTML webpage.

        Args:
            dirname (str): Name of the directory

        Returns:
            List[str]: List of subdirectories and files.
        """
        # retrieve subfolders and files
        htmlpage = self.handler.get(dirname, verify=self.verify_ssl).text
        soup = BeautifulSoup(htmlpage, "html.parser")
        list_links = [link.get("href") for link in soup.find_all("a")]
        # remove parent links
        list_links = [link for link in list_links if not link.startswith("/")]
        # remove end backslash in subfolders
        links = []
        for link in list_links:
            if link.endswith("/"):
                link = link[:-1]
            links.append(link)
        return links


class HTTPExtractorBase(ExtractorBase):
    """Abstract class for defining an HTTPExtractor

    Attrs:
        kind (str): Extractor's kind. Constant "HTTP".
    """

    kind: str = Field("HTTP", const=True)


class HTTPFiles(HTTPExtractorBase):
    """Extractor used for extracting multiple given files using HTTP.

    Attrs:
        kind (str): Constant "HTTP"
        session (HTTPSession): HTTP session to use for extracting multiple files.
        files (List[Tuple[str, str]]): List of files to get. Each element of
            the list is a tuple containing the source file's name and the destination
            file's name.
        n_workers (Optional[int]): Numbers of workers to use to parallelize the
            extraction.

    Example:
        >>> os.listdir("my_dir")
        []
        >>> extr = HTTPFiles(
                session={"host": "toto.meteo.fr"},
                files=[
                    ("https://toto.meteo.fr/my/remote/file1.txt", "my_dir/file1.txt")
                    ("https://toto.meteo.fr/my/remote/file2.txt", "my_dir/file2.txt")
                ]
            )
        >>> extr.run()
        >>> os.listdir("my_dir")
        ["file1.txt", "file2.txt"]
    """

    session: HTTPSession
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
                HTTPSession(**self.session.dict()).get,
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


class HTTPDir(HTTPExtractorBase):
    """Extractor used for extracting multiple files using HTTP.
    With this extractor file's name are not explicitly specified, but
    the source and destination directories are specified using constraints.

    Attrs:
        kind (str): Extractor's kind. Constant "HTTP".
        session (HTTPSession): HTTP Session to use for extracting all files.
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
        >>> extr = HTTPDir(
                session={"host": "toto.meteo.fr"},
                src="https://toto.meteo.fr/{year}/{month:02d}/(?P<basename>.\\w+.txt)",
                dst="my_dir/{year}_{month:02d}/{basename}",
                constraints={
                    "date": [2021],
                    "month": [1, 2, 3],
                }
            )
        >>> list(extr.get_constraints_combinations())
        [
            {"year": 2021, "month": 1},
            {"year": 2021, "month": 2},
            {"year": 2021, "month": 3},
        ]
        >>> extr.files
        [
            ("https://toto.meteo.fr/2021/01/file1.txt", "my_dir/2021_01/file1.txt"),
            ("https://toto.meteo.fr/2021/01/file2.txt", "my_dir/2021_01/file2.txt"),
            ("https://toto.meteo.fr/2021/02/file3.txt", "my_dir/2021_02/file3.txt"),
            ("https://toto.meteo.fr/2021/03/file4.txt", "my_dir/2021_03/file4.txt"),
        ]
        >>> extr.run()
        >>> os.listdir("my_dir")
        ["2021_01", "2021_02", "2021_03"]
        >>> os.listdir("my_dir/2021_01")
        ["file1.txt", "file2.txt"]
    """

    kind: str = Field("HTTP", const=True)
    session: HTTPSession
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
            >>> extr = HTTPDir(
                session={"host": "toto.meteo.fr"},
                src="https://toto.meteo.fr/{year}/(?P<basename>.\\w+.txt)",
                dst="my_dir/{year}_{basename}",
                constraints={"date": [2021]},
            )
            >>> extr.get_matching_dst(
                    "https://toto.meteo.fr/2021/file1.txt", {"year":2021}
                )
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
        """Property that gives the list of the files found in the HTTP session that
        corresponds to the self.src and self.constraints.

        Returns:
            List[Tuple[str, str]]: List of files to get. Each element of
            the list is a tuple containing the source file's name and the destination
            file's name.
        """
        if self._files is not None:
            return self._files
        self._files = []
        regex = re.compile("[a-zA-Z0-9_/.:-]*")
        LOGGER.debug("Starting to find files.")
        for dico in self.get_constraints_combinations():
            # formatting the directory's name with the constraints
            LOGGER.debug(f"Current constraint dico : {dico}")
            format_src = self.src.format(**dico)
            LOGGER.debug(f"Formated src : {format_src}")
            regmatch = regex.match(format_src)
            baseurl = regmatch.group()
            last_slash = baseurl.rfind("/")
            if last_slash < len(baseurl) - 1:
                baseurl = baseurl[: last_slash + 1]
                endurl = format_src[last_slash + 1 :]
            else:
                endurl = format_src[regmatch.end() :]
            LOGGER.debug(f"Base URL : {baseurl}")
            sources = [baseurl]
            # finding all source matching the src_dirname pattern by iteration
            for pattern in endurl.split("/"):
                LOGGER.debug(f"Finding pattern {pattern} in {sources}")
                sources = self.session.find_pattern(pattern, sources)
            LOGGER.debug(f"Final sources found: {sources} with {format_src}")
            self._files += [(src, self.get_matching_dst(src, dico)) for src in sources]
        self._files = sorted(self._files)
        LOGGER.debug(f"Final files : {self._files}")
        return self._files

    def to_HTTP_extractor(self) -> HTTPFiles:
        """Short method for retruning the equivalent HTTPFiles.

        Returns:
            HTTPFiles: HTTPFiles equivalent to the given attributes.
        """
        return HTTPFiles(
            session=self.session,
            files=self.files,
            n_workers=self.n_workers,
        )

    def run(self) -> bool:
        """Main method to get all self.files.

        Returns:
            bool: Whether the extraction is alright or not.
        """
        return self.to_HTTP_extractor().run()
