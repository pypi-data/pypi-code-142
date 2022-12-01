import typing
import prepr


class MISSING:
    """A placeholder type for the `remove` argument in `format_dict`,
    `format_list`, and `format_lines`.
    
    """


class _headers:
    WWW_Authenticate: typing.Any
    Authorization: typing.Any
    Proxy_Authenticate: typing.Any
    Proxy_Authorization: typing.Any
    Age: typing.Any
    Cache_Control: typing.Any
    Clear_Site_Data: typing.Any
    Expires: typing.Any
    Pragma: typing.Any
    Warning: typing.Any
    Accept_CH: typing.Any
    Accept_CH_Lifetime: typing.Any
    Sec_CH_UA: typing.Any
    Sec_CH_UA_Arch: typing.Any
    Sec_CH_UA_Bitness: typing.Any
    Sec_CH_UA_Full_Version: typing.Any
    Sec_CH_UA_Full_Version_List: typing.Any
    Sec_CH_UA_Mobile: typing.Any
    Sec_CH_UA_Model: typing.Any
    Sec_CH_UA_Platform: typing.Any
    Sec_CH_UA_Platform_Version: typing.Any
    Content_DPR: typing.Any
    Device_Memory: typing.Any
    DPR: typing.Any
    Viewport_Width: typing.Any
    Width: typing.Any
    Downlink: typing.Any
    ECT: typing.Any
    RTT: typing.Any
    Save_Data: typing.Any
    Last_Modified: typing.Any
    ETag: typing.Any
    If_Match: typing.Any
    If_None_Match: typing.Any
    If_Modified_Since: typing.Any
    If_Unmodified_Since: typing.Any
    Vary: typing.Any
    Connection: typing.Any
    Keep_Alive: typing.Any
    Accept: typing.Any
    Accept_Encoding: typing.Any
    Accept_Language: typing.Any
    Expect: typing.Any
    Max_Forwards: typing.Any
    Cookies: typing.Any
    Cookie: typing.Any
    Set_Cookie: typing.Any
    Access_Control_Allow_Origin: typing.Any
    Access_Control_Allow_Credentials: typing.Any
    Access_Control_Allow_Headers: typing.Any
    Access_Control_Allow_Methods: typing.Any
    Access_Control_Expose_Headers: typing.Any
    Access_Control_Max_Age: typing.Any
    Access_Control_Request_Headers: typing.Any
    Access_Control_Request_Method: typing.Any
    Origin: typing.Any
    Timing_Allow_Origin: typing.Any
    Content_Disposition: typing.Any
    Content_Length: typing.Any
    Content_Type: typing.Any
    Content_Encoding: typing.Any
    Content_Language: typing.Any
    Content_Location: typing.Any
    Forwarded: typing.Any
    X_Forwarded_For: typing.Any
    X_Forwarded_Host: typing.Any
    X_Forwarded_Proto: typing.Any
    Via: typing.Any
    Location: typing.Any
    From: typing.Any
    Host: typing.Any
    Referer: typing.Any
    Referrer_Policy: typing.Any
    User_Agent: typing.Any
    Allow: typing.Any
    Server: typing.Any
    Accept_Ranges: typing.Any
    Range: typing.Any
    If_Range: typing.Any
    Content_Range: typing.Any
    Cross_Origin_Embedder_Policy: typing.Any
    Cross_Origin_Opener_Policy: typing.Any
    Cross_Origin_Resource_Policy: typing.Any
    Content_Security_Policy: typing.Any
    Content_Security_Policy_Report_Only: typing.Any
    Expect_CT: typing.Any
    Feature_Policy: typing.Any
    Origin_Isolation: typing.Any
    Strict_Transport_Security: typing.Any
    Upgrade_Insecure_Requests: typing.Any
    X_Content_Type_Options: typing.Any
    X_Download_Options: typing.Any
    X_Frame_Options: typing.Any
    X_Permitted_Cross_Domain_Policies: typing.Any
    X_Powered_By: typing.Any
    X_XSS_Protection: typing.Any
    Sec_Fetch_Site: typing.Any
    Sec_Fetch_Mode: typing.Any
    Sec_Fetch_User: typing.Any
    Sec_Fetch_Dest: typing.Any
    Service_Worker_Navigation_Preload: typing.Any
    Last_Event_ID: typing.Any
    NEL: typing.Any
    Ping_From: typing.Any
    Ping_To: typing.Any
    Report_To: typing.Any
    Transfer_Encoding: typing.Any
    TE: typing.Any
    Trailer: typing.Any
    Sec_WebSocket_Key: typing.Any
    Sec_WebSocket_Extensions: typing.Any
    Sec_WebSocket_Accept: typing.Any
    Sec_WebSocket_Protocol: typing.Any
    Sec_WebSocket_Version: typing.Any
    Accept_Push_Policy: typing.Any
    Accept_Signature: typing.Any
    Alt_Svc: typing.Any
    Date: typing.Any
    Early_Data: typing.Any
    Large_Allocation: typing.Any
    Link: typing.Any
    Push_Policy: typing.Any
    Retry_After: typing.Any
    Signature: typing.Any
    Signed_Headers: typing.Any
    Server_Timing: typing.Any
    Service_Worker_Allowed: typing.Any
    SourceMap: typing.Any
    Upgrade: typing.Any
    X_DNS_Prefetch_Control: typing.Any
    X_Firefox_Spdy: typing.Any
    X_Pingback: typing.Any
    X_Requested_With: typing.Any
    X_Robots_Tag: typing.Any
    X_UA_Compatible: typing.Any
    __map = {
        "WWW_Authenticate": "WWW-Authenticate",
        "Authorization": "Authorization",
        "Proxy_Authenticate": "Proxy-Authenticate",
        "Proxy_Authorization": "Proxy-Authorization",
        "Age": "Age",
        "Cache_Control": "Cache-Control",
        "Clear_Site_Data": "Clear-Site-Data",
        "Expires": "Expires",
        "Pragma": "Pragma",
        "Warning": "Warning",
        "Accept_CH": "Accept-CH",
        "Accept_CH_Lifetime": "Accept-CH-Lifetime",
        "Sec_CH_UA": "Sec-CH-UA",
        "Sec_CH_UA_Arch": "Sec-CH-UA-Arch",
        "Sec_CH_UA_Bitness": "Sec-CH-UA-Bitness",
        "Sec_CH_UA_Full_Version": "Sec-CH-UA-Full-Version",
        "Sec_CH_UA_Full_Version_List": "Sec-CH-UA-Full-Version-List",
        "Sec_CH_UA_Mobile": "Sec-CH-UA-Mobile",
        "Sec_CH_UA_Model": "Sec-CH-UA-Model",
        "Sec_CH_UA_Platform": "Sec-CH-UA-Platform",
        "Sec_CH_UA_Platform_Version": "Sec-CH-UA-Platform-Version",
        "Content_DPR": "Content-DPR",
        "Device_Memory": "Device-Memory",
        "DPR": "DPR",
        "Viewport_Width": "Viewport-Width",
        "Width": "Width",
        "Downlink": "Downlink",
        "ECT": "ECT",
        "RTT": "RTT",
        "Save_Data": "Save-Data",
        "Last_Modified": "Last-Modified",
        "ETag": "ETag",
        "If_Match": "If-Match",
        "If_None_Match": "If-None-Match",
        "If_Modified_Since": "If-Modified-Since",
        "If_Unmodified_Since": "If-Unmodified-Since",
        "Vary": "Vary",
        "Connection": "Connection",
        "Keep_Alive": "Keep-Alive",
        "Accept": "Accept",
        "Accept_Encoding": "Accept-Encoding",
        "Accept_Language": "Accept-Language",
        "Expect": "Expect",
        "Max_Forwards": "Max-Forwards",
        "Cookies": "Cookies",
        "Cookie": "Cookie",
        "Set_Cookie": "Set-Cookie",
        "Access_Control_Allow_Origin": "Access-Control-Allow-Origin",
        "Access_Control_Allow_Credentials": "Access-Control-Allow-Credentials",
        "Access_Control_Allow_Headers": "Access-Control-Allow-Headers",
        "Access_Control_Allow_Methods": "Access-Control-Allow-Methods",
        "Access_Control_Expose_Headers": "Access-Control-Expose-Headers",
        "Access_Control_Max_Age": "Access-Control-Max-Age",
        "Access_Control_Request_Headers": "Access-Control-Request-Headers",
        "Access_Control_Request_Method": "Access-Control-Request-Method",
        "Origin": "Origin",
        "Timing_Allow_Origin": "Timing-Allow-Origin",
        "Content_Disposition": "Content-Disposition",
        "Content_Length": "Content-Length",
        "Content_Type": "Content-Type",
        "Content_Encoding": "Content-Encoding",
        "Content_Language": "Content-Language",
        "Content_Location": "Content-Location",
        "Forwarded": "Forwarded",
        "X_Forwarded_For": "X-Forwarded-For",
        "X_Forwarded_Host": "X-Forwarded-Host",
        "X_Forwarded_Proto": "X-Forwarded-Proto",
        "Via": "Via",
        "Location": "Location",
        "From": "From",
        "Host": "Host",
        "Referer": "Referer",
        "Referrer_Policy": "Referrer-Policy",
        "User_Agent": "User-Agent",
        "Allow": "Allow",
        "Server": "Server",
        "Accept_Ranges": "Accept-Ranges",
        "Range": "Range",
        "If_Range": "If-Range",
        "Content_Range": "Content-Range",
        "Cross_Origin_Embedder_Policy": "Cross-Origin-Embedder-Policy",
        "Cross_Origin_Opener_Policy": "Cross-Origin-Opener-Policy",
        "Cross_Origin_Resource_Policy": "Cross-Origin-Resource-Policy",
        "Content_Security_Policy": "Content-Security-Policy",
        "Content_Security_Policy_Report_Only": "Content-Security-Policy-Report-O"
        "nly",
        "Expect_CT": "Expect-CT",
        "Feature_Policy": "Feature-Policy",
        "Origin_Isolation": "Origin-Isolation",
        "Strict_Transport_Security": "Strict-Transport-Security",
        "Upgrade_Insecure_Requests": "Upgrade-Insecure-Requests",
        "X_Content_Type_Options": "X-Content-Type-Options",
        "X_Download_Options": "X-Download-Options",
        "X_Frame_Options": "X-Frame-Options",
        "X_Permitted_Cross_Domain_Policies": "X-Permitted-Cross-Domain-Policies"
        ,
        "X_Powered_By": "X-Powered-By",
        "X_XSS_Protection": "X-XSS-Protection",
        "Sec_Fetch_Site": "Sec-Fetch-Site",
        "Sec_Fetch_Mode": "Sec-Fetch-Mode",
        "Sec_Fetch_User": "Sec-Fetch-User",
        "Sec_Fetch_Dest": "Sec-Fetch-Dest",
        "Service_Worker_Navigation_Preload": "Service-Worker-Navigation-Preload"
        ,
        "Last_Event_ID": "Last-Event-ID",
        "NEL": "NEL",
        "Ping_From": "Ping-From",
        "Ping_To": "Ping-To",
        "Report_To": "Report-To",
        "Transfer_Encoding": "Transfer-Encoding",
        "TE": "TE",
        "Trailer": "Trailer",
        "Sec_WebSocket_Key": "Sec-WebSocket-Key",
        "Sec_WebSocket_Extensions": "Sec-WebSocket-Extensions",
        "Sec_WebSocket_Accept": "Sec-WebSocket-Accept",
        "Sec_WebSocket_Protocol": "Sec-WebSocket-Protocol",
        "Sec_WebSocket_Version": "Sec-WebSocket-Version",
        "Accept_Push_Policy": "Accept-Push-Policy",
        "Accept_Signature": "Accept-Signature",
        "Alt_Svc": "Alt-Svc",
        "Date": "Date",
        "Early_Data": "Early-Data",
        "Large_Allocation": "Large-Allocation",
        "Link": "Link",
        "Push_Policy": "Push-Policy",
        "Retry_After": "Retry-After",
        "Signature": "Signature",
        "Signed_Headers": "Signed-Headers",
        "Server_Timing": "Server-Timing",
        "Service_Worker_Allowed": "Service-Worker-Allowed",
        "SourceMap": "SourceMap",
        "Upgrade": "Upgrade",
        "X_DNS_Prefetch_Control": "X-DNS-Prefetch-Control",
        "X_Firefox_Spdy": "X-Firefox-Spdy",
        "X_Pingback": "X-Pingback",
        "X_Requested_With": "X-Requested-With",
        "X_Robots_Tag": "X-Robots-Tag",
        "X_UA_Compatible": "X-UA-Compatible"
    }


class Headers(_headers):
    """A set of all standard (current, depreciated and experimental) HTTP
    headers.

    Custom HTTP headers may be set through `__setitem__`, e.g.:
    ```
    h = Headers()
    h["a"] = "b"
    ```
    
    """
    def __repr__(self, *args, **kwargs) -> prepr.pstr:
        return prepr.prepr(self).build(*args, **kwargs)

    def format_dict(self, check=MISSING) -> dict:
        """Format the headers into a `dict` object, e.g.:
        ```
        {"Content-Type":"application/json","Accept":"*/*"}
        ```
        
        Arguments
        ---------
        check : bool
            If True, all headers whose values are equal to `remove` will be
            removed.
        remove : Any, optional, default=MISSING
            See `check` above.

        """
        new = {}
        _map = self._headers__map
        # if check = True
        if check != MISSING:
            for k, v in self.__dict__.items():
                if v != check:
                    new[_map[k] if k in _map else k] = v
            return new
        # if check = False
        for k, v in self.__dict__.items():
            new[_map[k] if k in _map else k] = v
        return new
    

    def format_list(self, check=MISSING) -> dict:
        """Format the headers into a `list` of `tuples` object, e.g.:
        ```
        [("Content-Type","application/json"),("Accept","*/*")]
        ```
        
        Arguments
        ---------
        check : bool
            If True, all headers whose values are equal to `remove` will be
            removed.
        remove : Any, optional, default=MISSING
            See `check` above.

        """
        new = []
        _map = self._headers__map
        # if check = True
        if check != MISSING:
            for k, v in self.__dict__.items():
                if v != check:
                    new.append(((_map[k] if k in _map else k), v))
            return new
        # if check = False
        for k, v in self.__dict__.items():
            new.append(((_map[k] if k in _map else k), v))
        return new
    

    def format_lines(self, check=MISSING) -> typing.List[str]:
        """Format the headers into a `list` of `str` object, e.g.:
        ```
        ["Content-Type: application/json","Accept: */*"]
        ```
        
        Arguments
        ---------
        check : bool
            If True, all headers whose values are equal to `remove` will be
            removed.
        remove : Any, optional, default=MISSING
            See `check` above.

        """
        lines = []
        _map = self._headers__map
        if check != MISSING:
            for k, v in self.__dict__.items():
                if v != check:
                    lines.append((_map[k] if k in _map else k) + ": " + str(v))
            return lines
        # if check = False
        for k, v in self.__dict__.items():
            lines.append((_map[k] if k in _map else k) + ": " + str(v))
        return lines


    def __setitem__(self, __k, __v) -> None:
        self.__dict__[__k] = __v
    

    def __getitem__(self, __k) -> typing.Any:
        return self.__dict__[__k]
