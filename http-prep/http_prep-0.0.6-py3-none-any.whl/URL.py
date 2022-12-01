from .OverloadDict import OverloadDict
import urllib.parse
import dataclasses
import typing


class NO_CHECK:
    """A placeholder value to indicate that a value will not be checked in
    `URL.build`.
    
    """


@dataclasses.dataclass
class URLComponents:
    """Contains the components of a URL.
    
    """
    protocol: str
    username: str
    password: str
    subdomain: str
    domain: str
    top_level_domain: str
    port: typing.Union[str, int]
    path_segments: typing.List[str]
    queries: OverloadDict
    fragment: str

    def copy(self) -> "URLComponents":
        return URLComponents(
            self.protocol,
            self.username,
            self.password,
            self.subdomain,
            self.domain,
            self.top_level_domain,
            self.port,
            self.path_segments,
            self.queries,
            self.fragment
        )


@dataclasses.dataclass
class URLSeparators:
    """Contains the separaters used to separate components of a URL.
    
    """
    protocol_sep: str
    username_password_sep: str
    password_host_sep: str
    domain_sep: str
    host_port_sep: str
    pathsegment_sep: str
    path_query_sep: str
    queryarg_sep: str
    queryarg_eq: str
    fragment_sep: str
    def copy(self) -> "URLSeparators":
        return URLSeparators(
            self.protocol_sep,
            self.username_password_sep,
            self.password_host_sep,
            self.domain_sep,
            self.host_port_sep,
            self.pathsegment_sep,
            self.path_query_sep,
            self.queryarg_sep,
            self.queryarg_eq,
            self.fragment_sep
        )


class URL:
    def __init__(self, components_override: URLComponents = None,
                 protocol_sep: str = "://", username_password_sep: str = ":",
                 password_host_sep: str = "@", domain_sep: str = ".",
                 host_port_sep: str = ":", pathsegment_sep: str = "/",
                 path_query_sep: str = "?", queryarg_sep: str = "&",
                 queryarg_eq: str = "=", fragment_sep: str = "#",
                 protocol: str = None, username: str = None,
                 password: str = None, subdomain: str = None,
                 domain: str = None, top_level_domain: str = None,
                 port: typing.Union[str, int] = None,
                 path_segments: typing.List[str] = ...,
                 queries: OverloadDict = ..., fragment: str = None) -> None:
        """Prepare a URL.

        Arguments
        ---------
        components_override : URLComponents, optional, default=None
            If defined, the provided URLComponents object will be used instead
            of initializing a new object with the given parameters.
        protocol_sep : str, optional, default="://"
            Separates the protocol and the netloc.
            `protocol[://]username:password@subdomain.domain.topleveldomain:1234/pathseg1?qarg1=1&qarg2=2#fragment`
        username_password_sep : str, optional, default=":"
            Separates the username and password.
            `protocol://username[:]password@subdomain.domain.topleveldomain:1234/pathseg1?qarg1=1&qarg2=2#fragment`
        password_host_sep : str, optional, default="@"
            Separates the password and the host.
            `protocol://username:password[@]subdomain.domain.topleveldomain:1234/pathseg1?qarg1=1&qarg2=2#fragment`
        domain_sep : str, optional, default="."
            Separates the subdomain, domain, and top-level domain.
            `protocol://username:password@subdomain[.]domain[.]topleveldomain:1234/pathseg1?qarg1=1&qarg2=2#fragment`
        host_port_sep : str, optional, default=":"
            Separates the host and the port.
            `protocol://username:password@subdomain.domain.topleveldomain[:]1234/pathseg1?qarg1=1&qarg2=2#fragment`
        pathsegment_sep : str, optional, default="/"
            Separates each path segment.
            `protocol://username:password@subdomain.domain.topleveldomain:1234[/]pathseg1?qarg1=1&qarg2=2#fragment`
        path_query_sep : str, optional, default="?"
            Separates the path and the query string.
            `protocol://username:password@subdomain.domain.topleveldomain:1234/pathseg1[?]qarg1=1&qarg2=2#fragment`
        queryarg_sep : str, optional, default="&"
            Separates each query argument.
            `protocol://username:password@subdomain.domain.topleveldomain:1234/pathseg1?qarg1=1[&]qarg2=2#fragment`
        queryarg_eq : str, optional, default="="
            Joins each query string key and value.
            `protocol://username:password@subdomain.domain.topleveldomain:1234/pathseg1?qarg1[=]1&qarg2[=]2#fragment`
        fragment_sep : str, optional, default="#"
            Separates the query string and the fragment.
            `protocol://username:password@subdomain.domain.topleveldomain:1234/pathseg1?qarg1=1&qarg2=2[#]fragment`
        protocol : str, optional, default=None
        username : str, optional, default=None
        password : str, optional, default=None
        subdomain : str, optional, default=None
        domain : str, optional, default=None
        top_level_domain : str, optional, default=None
        port : str | int, optional, default=None
        path_segments : list[str], optional, default=...
            A list of path segments as strings. E.g. ['a', 'b', 'c'] -> '/a/b/c'
        queries : OverloadDict, optional, default=...
            The queries as an OverloadDict or a dict with str keys and list of
            str values (dict[str, list[str]]), where each item in the list
            relates to the given key.
        fragment : str, optional, default=None

        Attributes
        ----------
        separators : URLSeparators
        components : URLComponents
        """
        self.separators = URLSeparators(protocol_sep, username_password_sep,
            password_host_sep, domain_sep, host_port_sep, pathsegment_sep,
            path_query_sep, queryarg_sep, queryarg_eq, fragment_sep)
        self.components = (components_override.copy() if components_override
            else URLComponents(protocol, username, password, subdomain, domain,
            top_level_domain, port, path_segments if path_segments != ... else
            [], queries if queries != ... else OverloadDict(), fragment))

    
    def build(self, port_check=NO_CHECK, path_check=NO_CHECK,
              query_check=NO_CHECK, fragment_check=NO_CHECK) -> str:
        """Build the components and separators into a URL.
        
        Arguments
        ---------
        port_check : any, optional, default=NO_CHECK
            If set to a value, the port will not be included if it is equal to
            the given value.
        path_check : any, optional, default=NO_CHECK
            If set to a value, any path segments that are equal to the given
            value will not be included.
        query_check : any, optional, default=NO_CHECK
            If set to a value, any query that is equal to the given value will
            not be included.
        fragment_check : any, optional, default=NO_CHECK
            If set to a value, the fragment will not be included if it is equal
            to the given value.
        
        Returns
        -------
        str
        
        """
        segments = []
        if self.components.protocol:
            segments.append(self.components.protocol +
                            self.separators.protocol_sep)
        if self.components.username and self.components.password:
            segments.append(self.components.username +
                self.separators.username_password_sep + self.components.password
                + self.separators.password_host_sep)
        if self.components.subdomain:
            segments.append(self.components.subdomain + 
                            self.separators.domain_sep)
        if self.components.domain:
            segments.append(self.components.domain)
        if self.components.top_level_domain:
            segments.append(self.separators.domain_sep +
                            self.components.top_level_domain)
        if self.components.port is not None and (port_check == NO_CHECK or
            port_check != self.components.port):
            segments.append(self.separators.host_port_sep +
                            str(self.components.port))
        if self.components.path_segments:
            if path_check != NO_CHECK:
                segments.extend([self.separators.pathsegment_sep + segment for
                                 segment in self.components.path_segments if
                                 segment != path_check])
            else:
                segments.extend([self.separators.pathsegment_sep + segment for
                                 segment in self.components.path_segments])
        if self.components.queries:
            formatted_queries = []
            if query_check != NO_CHECK:
                for k, v_list in self.components.queries.items():
                    for v in v_list:
                        if v == query_check:
                            continue
                        formatted_queries.append(k + self.separators.queryarg_eq
                                                 + urllib.parse.quote(str(v)))
            else:
                for k, v_list in self.components.queries.items():
                    for v in v_list:
                        formatted_queries.append(k + self.separators.queryarg_eq
                                                 + urllib.parse.quote(str(v)))
            if formatted_queries:
                segments.append(self.separators.path_query_sep +
                    self.separators.queryarg_sep.join(formatted_queries))
        if self.components.fragment and (fragment_check == NO_CHECK or
            fragment_check != self.components.fragment):
            segments.append(self.separators.fragment_sep + str(
                self.components.fragment))
        return "".join(segments)
