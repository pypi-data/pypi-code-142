from pyhttpx.http2 import Http2Session

if __name__ == '__main__':

    sess = Http2Session()
    proxies = None
    headers={
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
}

    #54.166.148.227
    #url='https://httpbin.org/get'
    #url = 'https://httpbin.org/post'
    #205.185.123.167
    url = 'https://tls.peet.ws/api/all'
    sess = Http2Session()
    for i in range(1):

        #r = sess.get(url, headers=headers)
        r = sess.post(url, headers=headers,data={'a':1})
        print(r.status_code)
        print(r.text)