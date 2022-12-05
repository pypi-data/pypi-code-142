from guardian_sdk.common import constant
import logging
"""
String stringToSign=
HTTPMethod + "\n" +
Accept + "\n" +                //建议显示设置 Accept Header。当 Accept 为空时，部分 Http 客户端会给 Accept 设置默认值为 */*，导致签名校验失败。
Content-MD5 + "\n"
Content-Type + "\n" +
Date + "\n" +
Headers +
Url
"""
lf = "\n"


def build_string_to_sign(method, path, headers, querys, bodys, sign_headers):
    string_to_sign = []
    string_to_sign.append(method)
    string_to_sign.append(lf)

    if constant.HTTP_HEADER_ACCEPT in headers and headers[constant.HTTP_HEADER_ACCEPT]:
        string_to_sign.append(headers[constant.HTTP_HEADER_ACCEPT])
    string_to_sign.append(lf)

    if constant.HTTP_HEADER_CONTENT_MD5 in headers and headers[constant.HTTP_HEADER_CONTENT_MD5]:
        string_to_sign.append(headers[constant.HTTP_HEADER_CONTENT_MD5])
    string_to_sign.append(lf)

    if constant.HTTP_HEADER_CONTENT_TYPE in headers and headers[constant.HTTP_HEADER_CONTENT_TYPE]:
        string_to_sign.append(headers[constant.HTTP_HEADER_CONTENT_TYPE])
    string_to_sign.append(lf)

    if constant.HTTP_HEADER_DATE in headers and headers[constant.HTTP_HEADER_DATE]:
        string_to_sign.append(headers[constant.HTTP_HEADER_DATE])
    string_to_sign.append(lf)

    string_to_sign.append(_build_headers(headers=headers, sign_headers=sign_headers))
    string_to_sign.append(_build_url(path, querys, bodys))

    string_to_sign_str = ''.join(string_to_sign)
    logging.debug(f"string_to_sign:\n{string_to_sign_str}")
    return string_to_sign_str


def _build_headers(headers={}, sign_headers=None):
    build_headers = []
    signature_headers = []
    if sign_headers is not None and len(headers) > 0:
        header_list = list(headers.keys())
        if constant.X_GW_SIGNATURE in header_list:
            header_list.remove(constant.X_GW_SIGNATURE)
        if constant.X_GW_SIGNATURE_HEADERS in header_list:
            header_list.remove(constant.X_GW_SIGNATURE_HEADERS)
        if constant.HTTP_HEADER_ACCEPT in header_list:
            header_list.remove(constant.HTTP_HEADER_ACCEPT)
        if constant.HTTP_HEADER_CONTENT_MD5 in header_list:
            header_list.remove(constant.HTTP_HEADER_CONTENT_MD5)
        if constant.HTTP_HEADER_CONTENT_TYPE in header_list:
            header_list.remove(constant.HTTP_HEADER_CONTENT_TYPE)
        if constant.HTTP_HEADER_DATE in header_list:
            header_list.remove(constant.HTTP_HEADER_DATE)
        header_list.sort()
        for k in header_list:
            if _is_header_to_sign(k, sign_headers):
                build_headers.append(k.lower())
                build_headers.append(":")
                build_headers.append(str(headers[k]))
                build_headers.append(lf)
                signature_headers.append(k.lower())
        # 将需要签名的请求头以,分隔设置到X-Gw-Signature-Headers请求头中
        headers[constant.X_GW_SIGNATURE_HEADERS] = ','.join(signature_headers)
    return "".join(build_headers)


def _build_url(path=None, querys={}, bodys={}):
    build_url = []
    if path:
        build_url.append(path)

    tmp_dict = {}
    if querys:
        for k in querys:
            if k:
                tmp_dict[k] = querys[k]

    if bodys:
        for k in bodys:
            if k:
                tmp_dict[k] = bodys[k]

    tmp_list = []
    if tmp_dict:
        build_url.append("?")
        keys = list(tmp_dict.keys())
        keys.sort()
        for k in keys:
            if k:
                if len(tmp_list) > 0:
                    tmp_list.append("&")
                tmp_list.append(k)
                if tmp_dict[k]:
                    tmp_list.append("=")
                    tmp_list.append(tmp_dict[k])

        build_url = build_url + tmp_list
    return "".join(build_url)


def _is_header_to_sign(header_name: str, sign_headers):
    if not header_name:
        return False
    if header_name.startswith(constant.GW_HEADER_TO_SIGN_PREFIX_SYSTEM):
        return True
    if header_name in sign_headers:
        return True
    else:
        return False


if __name__ == '__main__':
    ret = build_string_to_sign("get", "/guardian/s/weather", {"Content-Type": "text/plain", "Accept": "application/json", "Content-MD5": "md5", "Date":"a","a":""},
                               {"c": "zzz", "d": "mmm"}, {}, ["a"])
    print(f"{ret}")
