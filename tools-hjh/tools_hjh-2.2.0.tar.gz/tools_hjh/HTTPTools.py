# coding:utf-8
from tools_hjh import other as tools
import os
import time
from tools_hjh.ThreadPool import ThreadPool
from tools_hjh.HTTPRequest import HTTPRequest

    
def main():
    url = 'https://data.elsbbus.com/list.php?name=d9890e5f8eb6cce4014cffc01f008656'
    text = HTTPTools.get_page(url)
    print(text)


class HTTPTools():

    @staticmethod
    def get_page(url, headers=None, data=None, proxies=None, encoding='UTF-8'):
        req = HTTPRequest()
        req.connect(url, headers, data, proxies, encoding=encoding)
        text = req.get_text()
        req.close()
        return text

    @staticmethod
    def download(url, dstfile, headers=None, data=None, proxies=None, maxRetryCount=5, nowRetryCount=0, minSize=1024):
        """ 重新指定url等参数，执行下载 """
        url = url.strip()
        req = HTTPRequest()
        statusCode = req.connect(url=url, headers=headers, data=data, proxies=proxies)
        if statusCode != 200 and maxRetryCount > nowRetryCount:
            nowRetryCount = nowRetryCount + 1
            req.close()
            time.sleep(0.2)
            size = HTTPTools.download(url, dstfile, headers, data, proxies, maxRetryCount=maxRetryCount, nowRetryCount=nowRetryCount, minSize=minSize)
        elif statusCode != 200 and maxRetryCount <= nowRetryCount:
            size = 0
        elif statusCode == 200:
            size = req.download(dstfile, if_check_size=True)
            if size < minSize and maxRetryCount > nowRetryCount:
                nowRetryCount = nowRetryCount + 1
                req.close()
                time.sleep(0.2)
                size = HTTPTools.download(url, dstfile, headers, data, proxies, maxRetryCount=maxRetryCount, nowRetryCount=nowRetryCount, minSize=minSize)
            elif size < minSize and maxRetryCount <= nowRetryCount:
                tools.rm(dstfile)
                size = 0
        return size
    
    @staticmethod
    def download_m3u8(url, dstfile, headers=None, data=None, proxies=None, maxRetryCount=5, nowRetryCount=0, minSize=1024, theadnum=32, maxFailRate=0.015):
        url = HTTPTools.get_last_m3u8(url, headers, data, proxies)
        # 获取上下文
        page = HTTPTools.get_text(url, headers, data, proxies)
        # 修正路径
        dstfile = dstfile.replace('\\', '/')
        # 创建临时文件存放文件夹
        if '/' in dstfile and '.' in dstfile:
            m3u8TmpFileDir = dstfile.rsplit('.', 1)[0]
        elif '/' not in dstfile and '.' in dstfile:
            m3u8TmpFileDir = dstfile.split('.')[0]
        elif '/' not in dstfile and '.' not in dstfile:
            m3u8TmpFileDir = dstfile
        tools.mkdir(m3u8TmpFileDir)
        # 取得url的开头网址和url的不包含文件名的url
        urlSplits = url.split('/')
        urlHead = urlSplits[0] + '//' + urlSplits[2]
        urlPath = url.rsplit('/', 1)[0] + '/'
        # 对上下文最换行拆分分析
        lines = page.split('\n')
        key = None
        mode = None
        tsUrls = []
        for idx in range(len(lines)):
            # 如果是加密的ts，得到key
            if lines[idx].startswith('#EXT-X-KEY:'):
                from Crypto.Cipher import AES
                # keyMode = lines[idx].split('METHOD=')[1].split(',')[0]
                keyUrl = lines[idx].split('URI="')[1].split('"')[0]
                if not keyUrl.startswith('http'):
                    keyUrl = urlHead + keyUrl
                key = HTTPTools.get_text(keyUrl, headers, data, proxies)
                mode = AES.MODE_CBC
            # 得到tsUrl
            if lines[idx].startswith('#EXTINF:'):
                ts = lines[idx + 1]
                if not ts.startswith('http'):
                    if ts.startswith('/'):
                        ts = urlHead + ts
                    else:
                        ts = urlPath + ts
                tsUrls.append(ts)
                
        # 下载ts文件，记录下载文件路径
        tp = ThreadPool(theadnum)
        tsFilePaths = []
        for idx in range(len(tsUrls) - 1):
            tsfile = m3u8TmpFileDir + '/' + str(idx)
            tp.run(HTTPTools.download, (tsUrls[idx], tsfile, headers, data, proxies, maxRetryCount, nowRetryCount, minSize))
            tsFilePaths.append(tsfile)
        tp.wait()
        
        # 根据成功下载文件的数量判断是否下载完整，定义一个失败率
        downloadedFileNumber = len(os.listdir(m3u8TmpFileDir))
        # print(downloadedFileNumber)
        if len(tsUrls) == 0:
            raise Exception("需要下载的ts文件数量为" + str(len(tsUrls)))
        elif downloadedFileNumber / len(tsUrls) < 1 - maxFailRate:
            raise Exception("需要下载的ts文件数量为" + str(len(tsUrls)) + "，而下载成功的ts文件数量为" + str(downloadedFileNumber))
        
        # 解密并合并文件
        size = 0
        dstfile = open(dstfile, 'wb')
        for tsFilePath in tsFilePaths:
            if os.path.exists(tsFilePath):
                tsfile = open(tsFilePath, "rb")
                tsfileRead = tsfile.read()
                if key is not None:
                    tsfileRead = HTTPTools.aes_decrypt(tsfileRead, key, mode)
                size = size + dstfile.write(tsfileRead)
                tsfile.close()
        tools.rm(m3u8TmpFileDir)
        dstfile.close()
        return size

    @staticmethod
    def get_last_m3u8(url, headers=None, data=None, proxies=None):
        urlSplits = url.split('/')
        urlHead = urlSplits[0] + '//' + urlSplits[2]
        urlPath = url.rsplit('/', 1)[0] + '/'
        page = HTTPTools.get_text(url, headers, data, proxies=proxies)
        for line in page.split('\n'):
            if line.endswith('.m3u8'):
                url = line
                if not url.startswith('http'):
                    if url.startswith('/'):
                        url = urlHead + url
                    else:
                        url = urlPath + url
                url = HTTPTools.get_last_m3u8(url, headers=headers, data=data, proxies=proxies)
        return url
    
    @staticmethod
    def get_size(url, headers=None, data=None, proxies=None):
        req = HTTPRequest()
        req.connect(url, headers, data, proxies)
        size = req.get_size()
        req.close()
        return size
    
    @staticmethod
    def get_status_code(url, headers=None, data=None, proxies=None):
        req = HTTPRequest()
        req.connect(url, headers, data, proxies)
        statusCode = req.get_status_code()
        req.close()
        return statusCode
    
    @staticmethod
    def get_size_m3u8(url, headers=None, data=None, proxies=None):
        tp_save_size = ThreadPool(128)
        file_sizes = []
        page = HTTPTools.get_text(url, headers, data, proxies)
        urlSplits = url.split('/')
        urlHead = urlSplits[0] + '//' + urlSplits[2]
        urlPath = url.rsplit('/', 1)[0] + '/'
        lines = page.split('\n')
        tsUrls = []
        for idx in range(len(lines)):
            if lines[idx].startswith('#EXTINF:'):
                ts = lines[idx + 1]
                if not ts.startswith('http'):
                    if ts.startswith('/'):
                        ts = urlHead + ts
                    else:
                        ts = urlPath + ts
                tsUrls.append(ts)
    
        def save_size(tsUrl, headers, data, proxies):
            try:
                fileSize = HTTPTools.get_size(tsUrl, headers, data, proxies)
            except:
                fileSize = HTTPTools.get_size(tsUrl, headers, data, proxies)
            file_sizes.append(fileSize)
        
        for tsUrl in tsUrls:
            tp_save_size.run(save_size, (tsUrl, headers, data, proxies))
            
        while(len(file_sizes) < len(tsUrls)):
            time.sleep(0.5)
            
        tp_save_size.wait()
        
        return sum(file_sizes)
    
    @staticmethod
    def get_ts_urls(url, headers=None, data=None, proxies=None):
        page = HTTPTools.get_text(url, headers, data, proxies)
        urlSplits = url.split('/')
        urlHead = urlSplits[0] + '//' + urlSplits[2]
        urlPath = url.rsplit('/', 1)[0] + '/'
        lines = page.split('\n')
        tsUrls = []
        for idx in range(len(lines)):
            if lines[idx].startswith('#EXTINF:'):
                ts = lines[idx + 1]
                if not ts.startswith('http'):
                    if ts.startswith('/'):
                        ts = urlHead + ts
                    else:
                        ts = urlPath + ts
                tsUrls.append(ts)
        return tsUrls
    
    @staticmethod
    def aes_decrypt(b, key, mode):
        """ 根据指定的key和mode使用AES解密字节码 """
        from Crypto.Cipher import AES
        key = key.encode('utf-8')
        aes = AES.new(key, mode)
        return aes.decrypt(b)
    
    @staticmethod
    def N_m3u8DL_CLI(url, dstfile, theadnum=32, exePath='N_m3u8DL-CLI'):
        workDir = os.path.abspath(os.path.dirname(__file__)) + '/' + dstfile.rsplit('/', 1)[0]
        dstfile = dstfile.split('/')[-1]
        cmd = exePath + ' --enableDelAfterDone --workDir ' + workDir + ' --saveName ' + dstfile + ' --maxThreads ' + str(theadnum) + ' ' + url
        os.popen(cmd)


if __name__ == '__main__':
    main()
