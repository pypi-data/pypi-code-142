SYSTEM_HEADERS = (
    X_GW_SIGNATURE, X_GW_SIGNATURE_HEADERS, X_GW_TIMESTAMP, X_GW_NONCE, X_GW_KEY, X_GW_ERROR_MESSAGE
) = (
    'X-Gw-Signature', 'X-Gw-Signature-Headers', 'X-Gw-Timestamp', 'X-Gw-Nonce', 'X-Gw-Key', "X-Gw-Error-Message"
)

HTTP_HEADERS = (
    HTTP_HEADER_ACCEPT, HTTP_HEADER_CONTENT_MD5,
    HTTP_HEADER_CONTENT_TYPE, HTTP_HEADER_USER_AGENT, HTTP_HEADER_DATE
) = (
    'Accept', 'Content-MD5',
    'Content-Type', 'User-Agent', 'Date'
)

HTTP_PROTOCOL = (
    HTTP, HTTPS
) = (
    'guardian_sdk.http', 'https'
)

HTTP_METHOD = (
    GET, POST, PUT, DELETE
) = (
    'GET', 'POST', 'PUT', 'DELETE'
)

CONTENT_TYPE = (
    CONTENT_TYPE_FORM, CONTENT_TYPE_STREAM,
    CONTENT_TYPE_JSON, CONTENT_TYPE_XML, CONTENT_TYPE_TEXT
) = (
    'application/x-www-form-urlencoded; charset=UTF-8', 'application/octet-stream; charset=UTF-8',
    'application/json; charset=UTF-8', 'application/xml; charset=UTF-8', 'application/text; charset=UTF-8'
)

BODY_TYPE = (
    FORM, STREAM
) = (
    'FORM', 'STREAM'
)

GW_HEADER_TO_SIGN_PREFIX_SYSTEM = "x-gw-"