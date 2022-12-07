import subprocess, json, socket, time, base64, requests, re, ast, datetime, os
from hashlib import md5
import logging


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64':base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


class Win:
    waitTimeout = 5.0  # 秒，超时
    intervalTimeout = 0.5  # 秒，轮询间隔
    driverPath = r"C:\Aibote\Aibote_cloud\WebDriver.exe"
    socket.setdefaulttimeout(20)  # sock超时设置
    base_path = "/storage/emulated/0/Android/data/com.aibot.client/files/"

    def __init__(self, port=52121):
        self.log = logging
        # 设置日志存放路径
        path = '.\\log\\'
        if not os.path.exists(path):
            os.mkdir(path)
        today_date = str(datetime.date.today())  # 获取今天的日期 格式2019-08-01
        # 定义日志
        self.log.basicConfig(filename=path + 'log_' + today_date + '.txt', level=logging.DEBUG, filemode='a',
                            format='【%(asctime)s】 【%(levelname)s】 >>>  %(message)s', datefmt='%Y-%m-%d %H:%M')
        #

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = str(port)
        subprocess.Popen([self.driverPath, self.port])
        self.sock.connect(('127.0.0.1', port))

    def setSendData(self, *arrArgs):
        strData = ""
        tempStr = ""
        for args in arrArgs:
            if args is None:
                args = ""
            if args is True:
                args = 'true'  # js的bool是小写
            elif args is False:
                args = 'false'  # js的bool是小写
            tempStr += str(args)
            strData += str(len(str(args)))  # 与移动端解析方式不同
            # print(str(args),str(len(str(args))))
            strData += '/'
        strData = strData[:-1]  # 去掉最后一个/
        strData += '\n'
        strData += tempStr
        strData = strData.encode()
        # print('格式化',strData)
        self.log.debug(('setSendData方法', 'strData',strData))
        return strData

    def sendData(self, strData):
        self.log.debug(('sendData方法', '发送tcp', strData))
        self.sock.send(strData)
        data_length, data = self.sock.recv(int(self.port)).split(b"/", 1)
        while int(data_length) > len(data):
            data += self.sock.recv(int(self.port))
        data = data.decode("utf8").strip()
        self.log.debug(('sendData方法', 'recv', data))
        return data

    def setImplicitTimeout(self, waitMs, intervalMs = 0.5):
        # 设置隐式等待
        self.waitTimeout = waitMs
        self.intervalTimeout = intervalMs

    def findWindow(self, className, windowNmae):
        """
        查找窗口句柄
        :param className:窗口类名
        :param windowNmae:窗口名
        :return:成功返回窗口句柄，失败返回None
        """
        strData = self.setSendData("findWindow", className, windowNmae)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet

    def findWindows(self, className, windowNmae):
        """
        查找窗口句柄数组
        :param className: 窗口类名
        :param windowNmae: 窗口名
        :return: 成功返回窗口句柄数组，失败返回None
        """
        strData = self.setSendData("findWindows", className, windowNmae)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet.split("|")

    def findSubWindow(self, curHwnd, className, windowNmae):
        """
        查找子窗口句柄
        :param curHwnd:当前窗口句柄
        :param className:窗口类名
        :param windowNmae:窗口名
        :return:成功返回窗口句柄，失败返回None
        """
        strData = self.setSendData("findSubWindow", curHwnd, className, windowNmae)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet

    def findParentWindow(self, curHwnd):
        """
        查找父窗口句柄
        :param curHwnd: 当前窗口句柄
        :return:成功返回窗口句柄，失败返回None
        """
        strData = self.setSendData("findParentWindow", curHwnd)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet

    def getWindowName(self, hwnd):
        """
        获取窗口名称
        :param hwnd:窗口句柄
        :return:成功返回窗口名称，失败返回None
        """
        strData = self.setSendData("getWindowName", hwnd)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet

    def showWindow(self, hwnd, isShow):
        """
        显示/隐藏窗口
        :param hwnd:窗口句柄
        :param isShow:显示窗口 True， 隐藏窗口 False
        :return:成功返回True，失败返回False
        """
        if isShow is True:
            isShow = "true"
        elif isShow is False:
            isShow = "false"
        strData = self.setSendData("showWindow", hwnd, isShow)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def setWindowTop(self, hwnd, isTop):
        """
        设置窗口到最顶层
        :param hwnd:窗口句柄
        :param isTop:是否置顶，True置顶， False取消置顶
        :return:成功返回True，失败返回False
        """
        if isTop is True:
            isTop = "true"
        elif isTop is False:
            isTop = "false"
        strData = self.setSendData("setWindowTop", hwnd, isTop)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def getWindowPos(self, hwnd):
        """
        获取窗口位置
        :param hwnd:窗口句柄
        :return: {'left':number, 'top':number, 'width':number, 'height':number}成功返回窗口位置，失败返回None
        """
        strData = self.setSendData('getWindowPos', hwnd)
        strRet = self.sendData(strData)
        if strRet == "-1|-1|-1|-1":
            return None
        arrRet = strRet.split("|")
        return {'left': int(arrRet[0]), 'top': int(arrRet[1]), 'width': int(arrRet[2]),
                'height': int(arrRet[3])}

    def setWindowPos(self, hwnd, left, top, width, height):
        """
        设置窗口位置
        :param hwnd:窗口句柄
        :param left:左上角横坐标
        :param top:左上角纵坐标
        :param width:窗口宽度
        :param height:窗口高度
        :return: 成功返回True 失败返回 False
        """
        strData = self.setSendData('setWindowPos', hwnd, left, top, width, height)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def moveMouse(self, hwnd, x, y, options={}):
        """
        移动鼠标
        :param hwnd:窗口句柄
        :param x:横坐标
        :param y:纵坐标
        :param options:{mode:boolean, elementHwnd:string|number} options 操作模式，后台 True，前台 False。默认前台操作。
        :如果mode值为true且目标控件有单独的句柄，则需要通过getElementWindow获得元素句柄，指定elementHwnd的值(极少应用窗口由父窗口响应消息，则无需指定
        :return: 总是返回True
        """
        mode = 'false'
        elementHwnd = 0
        if 'mode' in options:
            mode = options["mode"]
            if mode is True:
                mode = 'true'
            elif mode is False:
                mode = 'false'
        if 'elementHwnd' in options:
            elementHwnd = options["elementHwnd"]
        strData = self.setSendData("moveMouse", hwnd, x, y, mode, elementHwnd)
        strRet = self.sendData(strData)
        if strRet == 'true':
            return True
        return strRet

    def moveMouseRelative(self, hwnd, x, y, mode=False):
        """
        移动鼠标(相对坐标)
        :param hwnd:窗口句柄
        :param x:相对横坐标
        :param y:相对纵坐标
        :param mode:操作模式，后台 True，前台 False。默认前台操作
        :return:总是返回True
        """
        if mode is False:
            mode = 'false'
        elif mode is True:
            mode = 'true'
        strData = self.setSendData("moveMouseRelative", hwnd, x, y, mode)
        strRet = self.sendData(strData)
        if strRet == 'true':
            return True
        return strRet

    def rollMouse(self, hwnd, x, y, dwData, mode=False):
        """
        滚动鼠标
        :param hwnd:窗口句柄
        :param x:横坐标
        :param y:纵坐标
        :param dwData:鼠标滚动次数,负数下滚鼠标,正数上滚鼠标
        :param mode:操作模式，后台 True，前台 False。默认前台操作
        :return:总是返回True
        """
        if mode is False:
            mode='false'
        elif mode is True:
            mode = 'true'
        strData = self.setSendData("rollMouse", hwnd, x, y, dwData, mode)
        strRet = self.sendData(strData)
        if strRet == 'true':
            return True
        return strRet

    def clickMouse(self, hwnd, x, y, msg, options={}):
        """
        鼠标点击
        :param hwnd:窗口句柄
        :param x:横坐标
        :param y:纵坐标
        :param msg:单击左键:1 单击右键:2 按下左键:3 弹起左键:4 按下右键:5 弹起右键:6 双击左键:7 双击右键:8
        :param options:{mode:boolean, elementHwnd:string|number} options 操作模式，后台 True，前台 False。默认前台操作。
        :如果mode值为true且目标控件有单独的句柄，则需要通过getElementWindow获得元素句柄，指定elementHwnd的值(极少应用窗口由父窗口响应消息，则无需指定)
        :return:总是返回True。后台模式下连续点击同一个控件，可能会间断性失效
        """
        mode = 'false'
        elementHwnd = 0
        if mode in options:
            mode = options["mode"]
            if mode is False:
                mode = 'false'
            elif mode is True:
                mode = 'true'
        if elementHwnd in options:
            elementHwnd = options["elementHwnd"];
        # print("clickMouse" + str(hwnd) + str(x) + str(y) + str(msg) + str(mode) + str(elementHwnd))
        strData = self.setSendData("clickMouse", hwnd, x, y, msg, mode, elementHwnd)
        strRet = self.sendData(strData)
        if strRet == 'true':
            return True
        return strRet

    def sendKeys(self, text):
        """
        输入文本
        :param text:输入的文本
        :return:总是返回True
        """
        strData = self.setSendData("sendKeys", text)
        strRet = self.sendData(strData)
        if strRet == 'true':
            return True
        return strRet

    def sendKeysByHwnd(self, hwnd, text):
        """
        后台输入文本
        :param hwnd:窗口句柄，如果目标控件有单独的句柄，需要通过getElementWindow获得句柄
        :param text:输入的文本
        :return:总是返回True
        """
        strData = self.setSendData("sendKeysByHwnd", hwnd, text)
        strRet = self.sendData(strData)
        if strRet == 'true':
            return True
        return strRet

    def sendVk(self, bVk, msg):
        """
        输入虚拟键值(VK)
        :param bVk:VK键值，例如：回车对应 VK键值 13
        :param msg:按下弹起:1 按下:2 弹起:3
        :return:总是返回True
        """
        strData = self.setSendData("sendVk", bVk, msg)
        strRet = self.sendData(strData)
        if strRet == 'true':
            return True
        return strRet

    def sendVkByHwnd(self, hwnd, bVk, msg):
        """
        后台输入虚拟键值(VK)
        :param hwnd:窗口句柄，如果目标控件有单独的句柄，需要通过getElementWindow获得句柄
        :param bVk:VK键值，例如：回车对应 VK键值 13
        :param msg:按下弹起:1 按下:2 弹起:3
        :return:总是返回True。若是后台组合键，可使用sendVk 按下控制键(Alt、Shift、Ctrl...)，再组合其他按键
        """
        strData = self.setSendData("sendVkByHwnd", hwnd, bVk, msg)
        strRet = self.sendData(strData)
        if strRet == 'true':
            return True
        return strRet

    def saveScreenshot(self, hwnd, savePath, options={}):
        """
        截图保存
        :param hwnd:窗口句柄
        :param savePath:保存的位置
        :param options:{region:[left:number, top:number, right:number, bottom:number], threshold:[thresholdType:number, thresh:number, maxval:number], mode:boolean} options 可选参数
        :region截图区域 [10, 20, 100, 200]，region默认  hwnd对应的窗口
        : threshold二值化图片, thresholdType算法类型：
            0   THRESH_BINARY算法，当前点值大于阈值thresh时，取最大值maxva，否则设置为0
            1   THRESH_BINARY_INV算法，当前点值大于阈值thresh时，设置为0，否则设置为最大值maxva
            2   THRESH_TOZERO算法，当前点值大于阈值thresh时，不改变，否则设置为0
            3   THRESH_TOZERO_INV算法，当前点值大于阈值thresh时，设置为0，否则不改变
            4   THRESH_TRUNC算法，当前点值大于阈值thresh时，设置为阈值thresh，否则不改变
            5   ADAPTIVE_THRESH_MEAN_C算法，自适应阈值
            6   ADAPTIVE_THRESH_GAUSSIAN_C算法，自适应阈值
            thresh阈值，maxval最大值，threshold默认保存原图。thresh和maxval同为255时灰度处理
        : mode操作模式，后台 true，前台 false。默认前台操作
        :return: bool
        """
        left = 0; top = 0; right = 0; bottom = 0
        thresholdType = 0; thresh = 0; maxval = 0
        mode = 'false'
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if 'threshold' in options:
            thresholdType = options["threshold"][0]
            if thresholdType == 5 or thresholdType == 6:
                thresh = 127
                maxval = 255
            else:
                thresh = options["threshold"][1]
                maxval = options["threshold"][2]

        if 'mode' in options:
            mode = options["mode"]
            if mode is True:
                mode = 'true'
            elif mode is False:
                mode = 'false'

        strData = self.setSendData("saveScreenshot", hwnd, savePath, left, top, right, bottom, thresholdType, thresh, maxval, mode)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def getColor(self, hwnd, x, y, mode = False):
        """
        获取指定坐标点的色值
        :param hwnd:窗口句柄
        :param x:横坐标
        :param y:纵坐标
        :param mode:操作模式，后台 true，前台 false。默认前台操作
        :return:成功返回#开头的颜色值，失败返回None
        """
        if mode is False:
            mode = 'false'
        elif mode is True:
            mode = 'true'
        strData = self.setSendData("getColor", hwnd, x, y, mode)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet

    def findImage(self, hwnd, imagePath, options={}):
        """
        找图
        :param hwnd:窗口句柄
        :param imagePath:小图片路径
        :param options:{region:[left:number, top:number, right:number, bottom:number], sim:number, threshold:[thresholdType:number, thresh:number, maxval:number], multi:number, mode:boolean} options 可选参数
        :region 指定区域找图 [10, 20, 100, 200]，region默认 hwnd对应的窗口
        : sim浮点型 图片相似度 0.0-1.0，sim默认0.95
        : threshold二值化图片, thresholdType算法类型：
            0   THRESH_BINARY算法，当前点值大于阈值thresh时，取最大值maxva，否则设置为0
            1   THRESH_BINARY_INV算法，当前点值大于阈值thresh时，设置为0，否则设置为最大值maxva
            2   THRESH_TOZERO算法，当前点值大于阈值thresh时，不改变，否则设置为0
            3   THRESH_TOZERO_INV算法，当前点值大于阈值thresh时，设置为0，否则不改变
            4   THRESH_TRUNC算法，当前点值大于阈值thresh时，设置为阈值thresh，否则不改变
            5   ADAPTIVE_THRESH_MEAN_C算法，自适应阈值
            6   ADAPTIVE_THRESH_GAUSSIAN_C算法，自适应阈值
            thresh阈值，maxval最大值，threshold默认保存原图。thresh和maxval同为255时灰度处理
        : multi 找图数量，默认为1 找单个图片坐标
        : mode 操作模式，后台 True，前台 Flse。默认前台操作
        :return:成功返回 单坐标点[{x:number, y:number}]，多坐标点[{x1:number, y1:number}, {x2:number, y2:number}...] 失败返回None
        """
        left = 0; top = 0; right = 0; bottom = 0
        sim = 0.95
        thresholdType = 0; thresh = 0; maxval = 0
        multi = 1
        mode = 'false'
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if 'sim' in options:
            sim = options["sim"]
        if 'threshold' in options:
            thresholdType = options["threshold"][0]
            if thresholdType == 5 or thresholdType == 6:
                thresh = 127
                maxval = 255
            else:
                thresh = options["threshold"][1]
                maxval = options["threshold"][2]
        if 'multi' in options:
            multi = options["multi"]
        if 'mode' in options:
            mode = options["mode"]
            if mode is True:
                mode = 'true'
            elif mode is False:
                mode = 'false'
        strData = self.setSendData("findImage", hwnd, imagePath, left, top, right, bottom, sim, thresholdType, thresh, maxval, multi, mode)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "-1|-1":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "-1|-1":
            return None
        arrPoints = strRet.split("/")
        pointCount = len(arrPoints)
        arrRet = []
        for i in range(pointCount):
            arrPoint = arrPoints[i].split("|")
            arrRet[i] = {'x': int(arrPoint[0]), 'y': int(arrPoint[1])}
        return arrRet

    def findAnimation(self, hwnd, frameRate, options={}):
        """
        找动态图
        :param hwnd:窗口句柄
        :param frameRate:前后两张图相隔的时间，单位秒
        :param options:{region:[left:number, top:number, right:number, bottom:number], mode:boolean} options 可选参数
        :region 指定区域找图 [10, 20, 100, 200]，region默认 hwnd对应的窗口
        :mode 操作模式，后台 True，前台 False。默认前台操作
        :return:成功返回 单坐标点[{x:number, y:number}]，多坐标点[{x1:number, y1:number}, {x2:number, y2:number}...] 失败返回None
        """
        frameRate = frameRate/1000
        left = 0; top = 0; right = 0; bottom = 0
        mode = 'false'
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if 'mode' in options:
            mode = options["mode"]
            if mode is True:
                mode = 'true'
            elif mode is False:
                mode = 'false'
        strData = self.setSendData("findAnimation", hwnd, frameRate, left, top, right, bottom, mode)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "-1|-1":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "-1|-1":
            return None
        arrPoints = strRet.split("/")
        pointCount = arrPoints.length
        arrRet = []
        for i in range(pointCount):
            arrPoint = arrPoints[i].split("|")
            arrRet[i] = {'x': int(arrPoint[0]), 'y': int(arrPoint[1])}
        return arrRet

    def findColor(self, hwnd, strMainColor, options={}):
        """
        查找指定色值的坐标点
        :param hwnd:窗口句柄
        :param strMainColor:#开头的色值
        :param options:{subColors:[[offsetX:number, offsetY:number, strSubColor:string], ...], region:[left:number, top:number, right:number, bottom:number], sim:number, mode:boolean} options 可选参数
        :subColors 相对于strMainColor 的子色值，[[offsetX, offsetY, "#FFFFFF"], ...]，subColors默认为null
        : region 指定区域找色 [10, 20, 100, 200]，region默认 hwnd对应的窗口
        : sim相似度0.0-1.0，sim默认为1
        : mode 操作模式，后台 true，前台 false。默认前台操作
        :return:成功返回{x:number, y:number} 失败返回None
        """
        strSubColors = "null"
        left = 0; top = 0; right = 0; bottom = 0
        sim = 1
        mode = 'false'
        if 'subColors' in options:
            strSubColors = ""
            arrLen = len(options["subColors"])
            for i in range(arrLen):
                strSubColors += options["subColors"][i][0] + "/"
                strSubColors += options["subColors"][i][1] + "/"
                strSubColors += options["subColors"][i][2]
                if i < arrLen - 1:
                    strSubColors += "\n"
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if 'sim' in options:
            sim = options["sim"]
        if 'mode' in options:
            mode = options["mode"]
            if mode is True:
                mode = 'true'
            elif mode is False:
                mode = 'false'
        strData = self.setSendData("findColor", hwnd, strMainColor, strSubColors, left, top, right, bottom, sim, mode)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "-1|-1":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "-1|-1":
            return None
        arrRet = strRet.split("|")
        return {'x': int(arrRet[0]), 'y': int(arrRet[1])}

    def compareColor(self, hwnd, mainX, mainY, strMainColor, options={}):
        """
        比较指定坐标点的颜色值
        :param hwnd:窗口句柄
        :param mainX:主颜色所在的X坐标
        :param mainY:主颜色所在的Y坐标
        :param strMainColor:#开头的色值
        :param options:{subColors:[[offsetX:number, offsetY:number, strSubColor:string], ...], region:[left:number, top:number, right:number, bottom:number], sim:number, mode:boolean} options 可选参数
        :subColors 相对于strMainColor 的子色值，[[offsetX, offsetY, "#FFFFFF"], ...]，subColors默认为null
        : region 指定区域找色 [10, 20, 100, 200]，region默认 hwnd对应的窗口
        : sim相似度0.0-1.0，sim默认为1
        : mode 操作模式，后台 True，前台 False。默认前台操作
        :return:成功返回True 失败返回 False
        """
        strSubColors = "null"
        left = 0; top = 0; right = 0; bottom = 0
        sim = 1
        mode = 'false'
        if 'subColors' in options:
            strSubColors = ""
            arrLen = len(options["subColors"])
            for i in range(arrLen):
                strSubColors += options["subColors"][i][0] + "/"
                strSubColors += options["subColors"][i][1] + "/"
                strSubColors += options["subColors"][i][2]
                if i < arrLen - 1:
                    strSubColors += "\n"
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if 'sim' in options:
            sim = options["sim"]
        if 'mode' in options:
            mode = options["mode"]
            if mode is True:
                mode = 'true'
            elif mode is False:
                mode = 'false'
        strData = self.setSendData("compareColor", hwnd, mainX, mainY, strMainColor, strSubColors, left, top, right, bottom, sim, mode)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "false":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "false":
            return False
        else:
            return True

    ############
    #  OCR系统  #
    ############
    def splitOcr(self, strOcr):
        """
        解析ocr
        :param strOcr:
        :return:
        """
        # print('strOcr',strOcr)
        wordsResult = []
        pattern = re.compile(r'(\[\[\[).+?(\)])')
        matches = pattern.finditer(strOcr)
        text_info_list = []
        for match in matches:
            result_str = match.group()
            text_info = ast.literal_eval(result_str)
            text_info_list.append(text_info)

        for i in text_info_list:
            j = {'location': i[0], 'words': i[1][0], 'interval': i[1][1]}
            wordsResult.append(j)
        return wordsResult

    def ocr(self,hwnd, left, top, right, bottom, mode = False):
        """
        ocr
        :param hwnd:窗口句柄
        :param left:左上角x点
        :param top:左上角y点
        :param right:右下角 x点
        :param bottom:右下角 y点
        :param mode:操作模式，后台 True，前台 False。默认前台操作
        :return:失败返回None，成功返回数组形式的识别结果
        """
        if mode is False:
            mode = 'false'
        elif mode is True:
            mode = 'true'
        strData = self.setSendData("ocr", hwnd, left, top, right, bottom, mode)
        strRet = self.sendData(strData)
        if strRet == "null" or strRet == "":
            return None
        else:
            return self.splitOcr(strRet)

    def ocrByFile(self,imagePath, left, top, right, bottom):
        """
        ocrByFile
        :param imagePath:图片路径
        :param left:左上角x点
        :param top:左上角y点
        :param right:右下角 x点
        :param bottom:右下角 y点
        :return:失败返回None，成功返回数组形式的识别结果
        """
        strData = self.setSendData("ocrByFile", imagePath, left, top, right, bottom)
        strRet = self.sendData(strData)
        if strRet == "null" or strRet == "":
            return None
        else:
            return self.splitOcr(strRet)

    def getWords(self, hwndOrImagePath, options={}):
        """
        获取屏幕文字
        :param hwndOrImagePath:窗口句柄或者图片路径
        :param options:{region:[left:number, top:number, right:number, bottom:number], mode:boolean} options 可选参数
        :region 指定区域 [10, 20, 100, 200]，region默认全图
        :mode 操作模式，后台 True，前台 False。默认前台操作, 仅适用于hwnd
        :return:失败返回None，成功返窗口上的文字
        """
        hwndOrImagePath=str(hwndOrImagePath)
        left = 0; top = 0; right = 0; bottom = 0
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if "." not in hwndOrImagePath:
            mode = 'false'
            if 'mode' in options:
                mode = options["mode"]
                if mode is True:
                    mode = 'true'
                elif mode is False:
                    mode = 'false'
            wordsResult = self.ocr(hwndOrImagePath, left, top, right, bottom, mode)
        else:
            wordsResult = self.ocrByFile(hwndOrImagePath, left, top, right, bottom)
        self.log.debug(('wordsResult ', wordsResult))
        if wordsResult is None:
            return None
        words = ""
        i = 0 # 避免下面len(wordsResult)-1为0，i就没定义
        for i in range(len(wordsResult)-1):
            words += wordsResult[i]['words'] + "\n"
        words += wordsResult[i]['words']
        self.log.debug(('words ',words))
        return words

    def findWords(self, hwndOrImagePath, words, options={}):
        """
        查找文字
        :param hwndOrImagePath:窗口句柄或者图片路径
        :param words:要查找的文字
        :param options:{region:[left:number, top:number, right:number, bottom:number], mode:boolean}  options 可选参数
        :region 指定区域 [10, 20, 100, 200]，region默认全图
        :mode 操作模式，后台 True，前台 False。默认前台操作, 仅适用于hwnd
        :return:失败返回None，成功返回数组[{x:number, y:number}, ...]，文字所在的坐标点
        """
        hwndOrImagePath=str(hwndOrImagePath)
        left = 0; top = 0; right = 0; bottom = 0
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if "." not in hwndOrImagePath:
            mode = 'false'
            if 'mode' in options:
                mode = options["mode"]
                if mode is True:
                    mode = 'true'
                elif mode is False:
                    mode = 'false'
            wordsResult = self.ocr(hwndOrImagePath, left, top, right, bottom, mode)
        else:
            wordsResult = self.ocrByFile(hwndOrImagePath, left, top, right, bottom)
        self.log.debug(wordsResult)
        if wordsResult is None:
            return None
        points = []
        for i in range(len(wordsResult)):
            if words in wordsResult[i]['words']:
                self.log.debug(words)
                index = wordsResult[i]['words'].index(words)
                localLeft = wordsResult[i]['location'][0][0]
                localTop = wordsResult[i]['location'][0][1]
                localRight = wordsResult[i]['location'][2][0]
                localBottom = wordsResult[i]['location'][2][1]
                width = localRight - localLeft
                height = localBottom - localTop

                wordWidth = width / len(wordsResult[i]['words'])
                offsetX = wordWidth * (index + len(words) / 2)
                offsetY = height / 2
                x = int(localLeft + offsetX + left)
                y = int(localTop + offsetY + top)
                points.append({"x": x, "y": y})
        self.log.debug(str(points))
        self.log.debug(0000)
        if len(points) == 0:
            return None
        else:
            return points

    def getElementName(self, hwnd, xpath):
        """
        获取指定元素名称
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :return:成功返回元素名称，失败返回None
        """
        strData = self.setSendData('getElementName', hwnd, xpath)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "null":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "null":
            return None
        else:
            return strRet

    def getElementValue(self, hwnd, xpath):
        """
        获取指定元素文本
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :return:成功返回元素文本
        """
        strData = self.setSendData('getElementValue', hwnd, xpath)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "null":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "null":
            return None
        else:
            return strRet

    def getElementRect(self,hwnd, xpath):
        """
        获取指定元素矩形大小
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :return:成功返回元素位置，失败返回None,{left:number, top:number, right:number, bottom:number}
        """
        strData = self.setSendData('getElementRect', hwnd, xpath)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "-1|-1|-1|-1":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "-1|-1|-1|-1":
            return None
        arrRet = strRet.split("|")
        return {'left': int(arrRet[0]), 'top': int(arrRet[1]), 'right': int(arrRet[2]), 'bottom': int(arrRet[3])}

    def getElementWindow(self, hwnd, xpath):
        """
        获取元素窗口句柄
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :return:成功返回元素窗口句柄，失败返回None
        """
        strData = self.setSendData('getElementWindow', hwnd, xpath)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "null":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "null":
            return None
        else:
            return strRet

    def clickElement(self, hwnd, xpath, msg):
        """
        点击元素
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :param msg:单击左键:1 单击右键:2 按下左键:3 弹起左键:4 按下右键:5 弹起右键:6 双击左键:7 双击右键:8
        :return:成功返回True 失败返回 False
        """

        strData = self.setSendData('clickElement', hwnd, xpath, msg)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "false":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "false":
            return False
        else:
            return True

    def setElementFocus(self, hwnd, xpath):
        """
        设置指定元素作为焦点
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :return:成功返回True 失败返回 False
        """
        strData = self.setSendData('setElementFocus', hwnd, xpath)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "false":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "false":
            return False
        else:
            return True

    def setElementValue(self, hwnd, xpath, value):
        """
        设置元素文本
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :param value:要设置的内容
        :return: 成功返回True 失败返回 False
        """
        strData = self.setSendData('setElementValue', hwnd, xpath, value)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "false":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "false":
            return False
        else:
            return True

    def setElementScroll(self, hwnd, xpath, horizontalPercent, verticalPercent):
        """
        滚动元素
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :param horizontalPercent:水平百分比 -1不滚动
        :param verticalPercent:垂直百分比 -1不滚动
        :return:成功返回True 失败返回 False
        """
        strData = self.setSendData('setElementScroll', hwnd, xpath, horizontalPercent, verticalPercent)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "false":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "false":
            return False
        else:
            return True

    def closeWindow(self, hwnd, xpath):
        """
        关闭窗口
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :return:成功返回True 失败返回 False
        """
        strData = self.setSendData('closeWindow', hwnd, xpath)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def setWindowState(self,hwnd, xpath, state):
        """
        设置窗口状态
        :param hwnd:窗口句柄
        :param xpath:元素路径
        :param state: 0正常 1最大化 2 最小化
        :return:成功返回True 失败返回 False
        """
        strData = self.setSendData('setWindowState', hwnd, xpath, state)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def setClipboardText(self, text):
        """
        设置剪切板文本
        :param text:设置的文本
        :return:成功返回True 失败返回 False
        """
        strData = self.setSendData('setClipboardText', text)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def getClipboardText(self):
        """
        获取剪切板文本
        :return:返回剪切板文本
        """
        strData = self.setSendData('getClipboardText')
        strRet = self.sendData(strData)
        return strRet

    def startProcess(self, commandLine, showWindow=True, isWait=False):
        """
        启动指定程序
        :param commandLine:启动命令行
        :param showWindow:是否显示窗口。可选参数,默认显示窗口
        :param isWait:是否等待程序结束。可选参数,默认不等待
        :return:成功返回True,失败返回False
        """
        if isWait is True:
            isWait='true'
        elif isWait is False:
            isWait = 'false'
        strData = self.setSendData('startProcess', commandLine, showWindow, isWait)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def executeCommand(self, command, waitTimeout=0.3):
        """
        执行cmd命令
        :param command: cmd命令，不能含 "cmd"字串
        :param waitTimeout:可选参数，等待结果返回超时，单位毫秒，默认0.3秒
        :return:返回cmd执行结果
        """
        waitTimeout = waitTimeout *1000
        strData = self.setSendData('executeCommand', command, waitTimeout)
        strRet = self.sendData(strData)
        return strRet

    def downloadFile(self, url, filePath, isWait):
        """
        指定url下载文件
        :param url:文件地址
        :param filePath:文件保存的路径
        :param isWait:是否等待.为true时,等待下载完成
        :return:总是返回True
        """
        if isWait is True:
            isWait = 'true'
        elif isWait is False:
            isWait = 'false'
        strData = self.setSendData('downloadFile', url, filePath, isWait)
        return self.sendData(strData)

    def openExcel(self, excelPath):
        """
        打开excel文档
        :param excelPath: excle路径
        :return:成功返回excel对象，失败返回None
        """
        strData = self.setSendData('openExcel', excelPath)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return json.loads(strRet)

    def openExcelSheet(self, excelObject, sheetName):
        """
        打开excel表格
        :param excelObject: excel对象
        :param sheetName: 表名
        :return: 成功返回sheet对象，失败返回None
        """
        strData = self.setSendData('openExcelSheet', excelObject['book'], excelObject['path'], sheetName)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet

    def saveExcel(self, excelObject):
        """
        保存excel文档
        :param excelObject: excel对象
        :return:成功返回True，失败返回False
        """
        strData = self.setSendData('saveExcel', excelObject['book'], excelObject['path'])
        strRet = self.sendData(strData)
        if strRet == 'false':
            return False
        elif strRet == 'true':
            return True
        else:
            return strRet

    def writeExcelNum(self, sheetObject, row, col, value):
        """
        写入数字到excel表格
        :param sheetObject: sheet对象
        :param row: 行
        :param col: 列
        :param value: 写入的值
        :return: 成功返回True，失败返回False
        """
        strData = self.setSendData('writeExcelNum', sheetObject, row, col, value)
        strRet = self.sendData(strData)
        if strRet == 'false':
            return False
        elif strRet == 'true':
            return True
        else:
            return strRet

    def writeExcelStr(self, sheetObject, row, col, strValue):
        """
        写入字符串到excel表格
        :param sheetObject: sheet对象
        :param row: 行
        :param col: 列
        :param strValue: 写入的值
        :return: 成功返回True，失败返回False
        """
        strData = self.setSendData('writeExcelStr', sheetObject, row, col, strValue)
        strRet = self.sendData(strData)
        if strRet == 'false':
            return False
        elif strRet == 'true':
            return True
        else:
            return strRet

    def readExcelNum(self, sheetObject, row, col):
        """
        读取excel表格数字
        :param sheetObject: sheet对象
        :param row: 行
        :param col: 列
        :return: 返回读取到的数字
        """
        strData = self.setSendData('readExcelNum', sheetObject, row, col)
        strRet = self.sendData(strData)
        return float(strRet)

    def readExcelStr(self, sheetObject, row, col):
        """
        读取excel表格字串
        :param sheetObject: sheet对象
        :param row: 行
        :param col: 列
        :return: 返回读取到的字符
        """
        strData = self.setSendData('readExcelStr', sheetObject, row, col)
        strRet = self.sendData(strData)
        return strRet

    def removeExcelRow(self, sheetObject, rowFirst, rowLast):
        """
        删除excel表格行
        :param sheetObject: sheet对象
        :param rowFirst: 起始行
        :param rowLast: 结束行
        :return: 成功返回True，失败返回False
        """
        strData = self.setSendData('removeExcelRow', sheetObject, rowFirst, rowLast)
        strRet = self.sendData(strData)
        if strRet == 'false':
            return False
        elif strRet == 'true':
            return True
        else:
            return strRet

    def removeExcelCol(self, sheetObject, colFirst, colLast):
        """
        删除excel表格列
        :param sheetObject: sheet对象
        :param colFirst: 起始列
        :param colLast: 结束列
        :return: 成功返回True，失败返回False
        """
        strData = self.setSendData('removeExcelCol', sheetObject, colFirst, colLast)
        strRet = self.sendData(strData)
        if strRet == 'false':
            return False
        elif strRet == 'true':
            return True
        else:
            return strRet
