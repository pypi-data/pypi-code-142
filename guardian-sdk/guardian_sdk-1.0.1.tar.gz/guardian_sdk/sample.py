from guardian_sdk.Client import Client
from guardian_sdk.Request import Request
from guardian_sdk.util import md5
from guardian_sdk.common import constant
import json
import logging

logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s %(message)s', level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
)


def test_get():
    bytes_body = json.dumps({"a": "杭州"}).encode("utf-8")
    #headers = {constant.HTTP_HEADER_CONTENT_TYPE: constant.CONTENT_TYPE_JSON,
    #           constant.HTTP_HEADER_CONTENT_MD5: str(md5.get_md5_base64_str(bytes_body), "utf-8")}
    headers = {constant.HTTP_HEADER_CONTENT_TYPE: constant.CONTENT_TYPE_JSON}
    sign_headers = [constant.X_GW_KEY, constant.X_GW_NONCE, constant.X_GW_TIMESTAMP]
    querys = {"appid": "wx000f9aa568ddedc4", "token": "e85cf5eef1104ff9b45a9ba09e67893a"}
    # bodys = {"a": "杭州"}
    bodys = {}

    # 测试GET请求
    request = Request("39690096",
                      "B84A23AB3FCF11ED8B67CD0F1AC241BC",
                      10,
                      constant.GET,
                      "https://gw.ihotel.cn",
                      "/guardian/api/member/getMemberInfoByToken.json",
                      headers,
                      querys,
                      None,
                      None,
                      None,
                      sign_headers)

    resp = Client.execute(request)
    print(resp.get_body())
    print(resp.get_error_message())


# 测试post表单
def test_post_form():
    bodys = {"city": "杭州", "city2": "杭州2"}
    headers = {constant.HTTP_HEADER_CONTENT_TYPE: constant.CONTENT_TYPE_FORM}
    request = Request("50556064",
                      "06B9FEF3E91111EAB8A67907504A7446",
                      10,
                      constant.POST,
                      "http://127.0.0.1:2222",
                      "/guardian/uc/api/login",
                      headers,
                      None,
                      bodys,
                      None,
                      None,
                      None)
    resp = Client.execute(request)
    print(resp.get_body())
    print(resp.get_error_message())


# 测试postJson
def test_post_json():
    bytes_body = json.dumps(
        {"appCode": "UC", "orgCode": "", "userCode": "LJH", "password": "8cc7cad17fd6e855df069bdfbb0f97f5"}).encode(
        "utf-8")
    headers = {constant.HTTP_HEADER_CONTENT_TYPE: constant.CONTENT_TYPE_JSON,
               constant.HTTP_HEADER_CONTENT_MD5: str(md5.get_md5_base64_str(bytes_body), "utf-8")}
    request = Request("50556064",
                      "06B9FEF3E91111EAB8A67907504A7446",
                      10,
                      constant.POST,
                      "http://127.0.0.1:2222",
                      "/guardian/uc/api/login",
                      headers,
                      None,
                      None,
                      None,
                      bytes_body,
                      None)
    resp = Client.execute(request)
    print(resp.get_body())
    print(resp.get_error_message())


# 测试post string
def test_post_string():
    text = "hello python"
    headers = {constant.HTTP_HEADER_CONTENT_TYPE: constant.CONTENT_TYPE_TEXT}
    request = Request("50556064",
                      "06B9FEF3E91111EAB8A67907504A7446",
                      10,
                      constant.POST,
                      "http://127.0.0.1:2222",
                      "/guardian/uc/api/login",
                      headers,
                      None,
                      None,
                      text,
                      None,
                      None)
    resp = Client.execute(request)
    print(resp.get_body())
    print(resp.get_error_message())


if __name__ == "__main__":
     test_get()
    # test_post_json()
    # test_post_form()
    # test_post_string()
