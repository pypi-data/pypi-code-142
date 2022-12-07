import random
import subprocess, json, socket, time, base64, requests,ast,re


class And:
    waitTimeout = 3  # 超时，秒
    intervalTimeout = 0.5  # 间隔，秒
    socket.setdefaulttimeout(5)  # sock超时设置
    base_path = "/storage/emulated/0/Android/data/com.aibot.client/files/"

    def __init__(self, port=3333):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.server_socket.bind(('', port))
        self.server_socket.listen(5)
        self.sock, self.client_addr = self.server_socket.accept()

    def sock_and_recv_test(self, strData, port=None):
        """
        sock测试
        :param strData: b'4\nhome'
        :param port: self.port
        :return: sock接收到的包
        """
        print(self.sock.send(strData))
        if port is None:
            print(self.sock.recv(self.port))
        else:
            print(self.sock.recv(port))

    def setSendData(self, *arrArgs):
        """
        格式化数据数据包8/3/3\ngetColor100200
        """
        # print('传入', *arrArgs)
        strData = ""
        tempStr = ""
        for args in arrArgs:
            if args == None:
                args = ""
            tempStr += str(args)
            strData += str(len(str(args)))
            strData += '/'
        strData = strData[:-1] #为了去掉最后一个"/"
        strData += '\n'
        strData += tempStr
        strData = strData.encode()
        # print('格式化',strData)
        return strData

    def setSendFile(self, functionName: str, androidFilePath: str, fileData: bytes):
        strData = ""
        strData += str(len(bytes(functionName, 'utf8')))
        strData += "/"
        strData += str(len(bytes(androidFilePath, 'utf8')))
        strData += "/"
        strData += len(fileData)
        strData += "\n"
        strData += functionName
        strData += androidFilePath
        byteData = bytes(strData, 'utf8') + bytes(functionName, 'utf8') + bytes(androidFilePath, 'utf8') + fileData
        return byteData

    def sendData(self, strData):
        """
        : sendData("getColor", 100, 200)
        : http://www.ai-bot.net/aiboteProtocol.html
        """
        # print('发送tcp', strData)
        strRet = self.sock.send(strData)
        data_length, data = self.sock.recv(self.port).split(b"/", 1)
        while int(data_length) > len(data):
            data += self.sock.recv(int(self.port))
        strRet = data.decode("utf8").strip()  # bytes转字符串,去除移除字符串头尾空格
        return strRet

    def setImplicitTimeout(self, waitMs, intervalMs = 0.5):
        # 设置隐式等待
        self.waitTimeout = waitMs
        self.intervalTimeout = intervalMs

    ############
    # 图片与颜色 #
    ############
    def saveScreenshot(self,savePath, options = {}) -> bool:
        """
        截图保存
        :param savePath:保存的位置
        :param options:{region:[left:number, top:number, right:number, bottom:number], threshold:[thresholdType:number, thresh:number, maxval:number]}
        :region截图区域 [10, 20, 100, 200]，region默认全屏
        :threshold二值化图片, thresholdType算法类型：
            0   THRESH_BINARY算法，当前点值大于阈值thresh时，取最大值maxva，否则设置为0
            1   THRESH_BINARY_INV算法，当前点值大于阈值thresh时，设置为0，否则设置为最大值maxva
            2   THRESH_TOZERO算法，当前点值大于阈值thresh时，不改变，否则设置为0
            3   THRESH_TOZERO_INV算法，当前点值大于阈值thresh时，设置为0，否则不改变
            4   THRESH_TRUNC算法，当前点值大于阈值thresh时，设置为阈值thresh，否则不改变
            5   ADAPTIVE_THRESH_MEAN_C算法，自适应阈值
            6   ADAPTIVE_THRESH_GAUSSIAN_C算法，自适应阈值
            thresh阈值，maxval最大值，threshold默认保存原图。thresh和maxval同为255时灰度处理
        :return: bool
        """
        left = 0; top = 0; right = 0; bottom = 0
        thresholdType = 0; thresh = 0; maxval = 0
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if "threshold" in options:
            thresholdType = options["threshold"][0]
            if thresholdType == 5 or thresholdType == 6:
                thresh = 127
                maxval = 255
            else:
                thresh = options["threshold"][1]
                maxval = options["threshold"][2]
        strData = self.setSendData("saveScreenshot", savePath, left, top, right, bottom, thresholdType, thresh,
                                       maxval)
        strRet = self.sendData(strData)
        if strRet=="false":
            return False
        else:
            return True

    # ##########
    #  色值相关  #
    # ##########
    def getColor(self, x,y):
        """
        获取指定坐标点的色值
        :param x:横坐标
        :param y:纵坐标
        :return:成功返回#开头的颜色值，失败返回None
        """
        strData = self.setSendData("getColor", x, y)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet

    def findImage(self, imagePath, options={}):
        """
        找图
        :param imagePath:小图片路径（手机）
        :param options:{region:[left:number, top:number, right:number, bottom:number], sim:number, threshold:[thresholdType:number, thresh:number, maxval:number]}
        : region 指定区域找图 [10, 20, 100, 200]，region默认全屏
        : sim浮点型 图片相似度 0.0-1.0，sim默认1。该值不宜设置太低，否则查找速度会非常慢
        : threshold二值化图片, thresholdType算法类型：
            0   THRESH_BINARY算法，当前点值大于阈值thresh时，取最大值maxva，否则设置为0
            1   THRESH_BINARY_INV算法，当前点值大于阈值thresh时，设置为0，否则设置为最大值maxva
            2   THRESH_TOZERO算法，当前点值大于阈值thresh时，不改变，否则设置为0
            3   THRESH_TOZERO_INV算法，当前点值大于阈值thresh时，设置为0，否则不改变
            4   THRESH_TRUNC算法，当前点值大于阈值thresh时，设置为阈值thresh，否则不改变
            5   ADAPTIVE_THRESH_MEAN_C算法，自适应阈值
            6   ADAPTIVE_THRESH_GAUSSIAN_C算法，自适应阈值
            thresh阈值，maxval最大值，threshold默认保存原图。thresh和maxval同为255时灰度处理
        :return: 成功返回{"x":number, "y":number} 失败返回None
        """
        left = 0; top = 0; right = 0; bottom = 0
        sim = 1
        thresholdType = 0; thresh = 0; maxval = 0
        if "region" in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if "sim" in options:
            sim = options["sim"]
        if "threshold" in options:
            thresholdType = options["threshold"][0]
            if thresholdType == 5 or thresholdType == 6:
                thresh = 127
                maxval = 255
            else:
                thresh = options["threshold"][1]
                maxval = options["threshold"][2]
        strData = self.setSendData("findImage", imagePath, left, top, right, bottom, sim, thresholdType, thresh, maxval)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "-1.0|-1.0":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if strRet == "-1.0|-1.0":
            return None
        arrRet = strRet.split("|")
        return {'x': int(arrRet[0]), 'y': int(arrRet[1])}

    def matchTemplate(self, imagePath, options = {}):
        """
        找图2
        :param imagePath:小图片路径（手机）
        :param options:{{region:[left:number, top:number, right:number, bottom:number], sim:number, threshold:[thresholdType:number, thresh:number, maxval:number], multi:number}} options 可选参数
        : region 指定区域找图 [10, 20, 100, 200]，region默认全屏
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
        :return:成功返回 单坐标点[{'x':number, 'y':number}]，多坐标点[{'x1':number, 'y1':number}, {'x2':number, 'y2':number}...] 失败返回None
        """
        left = 0; top = 0; right = 0; bottom = 0
        sim = 0.95
        thresholdType = 0; thresh = 0; maxval = 0
        multi = 1
        if "region" in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if "sim" in options:
            sim = options["sim"]
        if "threshold" in options:
            thresholdType = options["threshold"][0]
            if thresholdType == 5 or thresholdType == 6:
                thresh = 127
                maxval = 255
            else:
                thresh = options["threshold"][1]
                maxval = options["threshold"][2]
        if "multi" in options:
            multi = options["multi"]
        strData = self.setSendData("matchTemplate", imagePath, left, top, right, bottom, sim, thresholdType, thresh,
                                   maxval, multi)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "-1.0|-1.0":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()

        if strRet == "-1.0|-1.0":
            return None

        arrPoints = strRet.split("/")
        pointCount = len(arrPoints)
        arrRet = []
        for i in range(pointCount):
            arrPoint = arrPoints[i].split("|")
            arrRet.append({'x': int(arrPoint[0]), 'y': int(arrPoint[1])})
        return arrRet

    def findAnimation(self, frameRate, options = {}):
        """
        找动态图
        :param frameRate:前后两张图相隔的时间,单位秒
        :param options:{region:[left:number, top:number, right:number, bottom:number]}
        :region 指定区域找图 [10, 20, 100, 200]，region默认全屏
        :return:成功返回 单坐标点[{x:number, y:number}]，多坐标点[{x1:number, y1:number}, {x2:number, y2:number}...] 失败返回None
        """
        frameRate=frameRate/1000

        left = 0; top = 0; right = 0; bottom = 0
        if "region" in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        strData = self.setSendData("findAnimation", frameRate, left, top, right, bottom)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            byteRet = self.sendData(strData)
            strRet = byteRet.toString()
            if strRet == "-1.0|-1.0":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime=time.time()
        if strRet == "-1.0|-1.0":
            return None

        arrPoints = strRet.split("/")
        pointCount = len(arrPoints)
        arrRet = []
        for i in range(pointCount):
            arrPoint = arrPoints[i].split("|")
            arrRet[i] = {'x': int(arrPoint[0]), 'y': int(arrPoint[1])}
        return arrRet

    def findColor(self, strMainColor, options = {}):
        """
        查找指定色值的坐标点
        :param strMainColor: #开头的色值
        :param options:{subColors:[[offsetX:number, offsetY:number, strSubColor:string], ...], region:[left:number, top:number, right:number, bottom:number], sim:number}
        :subColors 相对于strMainColor 的子色值，[[offsetX, offsetY, "#FFFFFF"], ...]，subColors默认为null
        : region 指定区域找色 [10, 20, 100, 200]，region默认全屏
        : sim相似度0.0-1.0，sim默认为1
        :return:成功返回{'x':number, 'y':number} 失败返回None
        """
        strSubColors = "null"
        left = 0; top = 0; right = 0; bottom = 0
        sim = 1
        if 'subColors' in options:
            strSubColors = ""
            arrLen = len(options["subColors"])
            for i in range(arrLen):
                strSubColors += options["subColors"][i][0] + "/"
                strSubColors += options["subColors"][i][1] + "/"
                strSubColors += options["subColors"][i][2]
                if i < arrLen - 1:
                    strSubColors += "\n"
        if "region" in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if "sim" in options:
            sim = options["sim"]
        strData = self.setSendData("findColor", strMainColor, strSubColors, left, top, right, bottom, sim)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "-1.0|-1.0":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime=time.time()
        if strRet == "-1.0|-1.0":
            return None
        arrRet = strRet.split("|")
        return {'x': int(arrRet[0]), 'y': int(arrRet[1])}

    def compareColor(self, mainX, mainY, strMainColor, options = {}):
        """
        比较指定坐标点的颜色值
        :param mainX:主颜色所在的X坐标
        :param mainY:主颜色所在的Y坐标
        :param strMainColor:#开头的色值
        :param options:{subColors:[[offsetX:number, offsetY:number, strSubColor:string], ...], region:[left:number, top:number, right:number, bottom:number], sim:number}
        : subColors 相对于strMainColor 的子色值，[[offsetX, offsetY, "#FFFFFF"], ...]，subColors默认为null
        : region 指定区域找色 [10, 20, 100, 200]，region默认全屏
        : sim相似度0.0-1.0，sim默认为1
        :return:成功返回true 失败返回 false
        """
        strSubColors = "null"
        left = 0; top = 0; right = 0; bottom = 0
        sim = 1
        if "subColors" in options:
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
        strData = self.setSendData("compareColor", mainX, mainY, strMainColor, strSubColors, left, top, right, bottom,
                                   sim)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet=self.sendData(strData)
            if strRet == "false":
                time.sleep(self.intervalTimeout)
            else:
                break
            endTime = time.time()
        if  strRet == "false":
            return False
        else:
            return True

    #############
    #  点击手势  #
    #############
    def press(self, x, y, duration):
        """
        手指按下
        :param x:横坐标
        :param y:纵坐标
        :param duration:按下时长
        :return:成功返回True 失败返回False
        """
        duration=duration/1000
        strData = self.setSendData("press", x, y, duration)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def move(self, x, y, duration):
        """
        手指移动
        :param x:横坐标
        :param y:纵坐标
        :param duration:移动时长
        :return:成功返回True 失败返回False
        """
        duration = duration/1000
        strData = self.setSendData("move", x, y, duration)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True


    def release(self):
        """
        手指释放
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("release")
        strRet =  self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def click(self, x, y):
        """
        点击坐标
        :param x:横坐标
        :param y:纵坐标
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("click", x, y)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def doubleClick(self, x, y):
        """
        双击坐标
        :param x:横坐标
        :param y:纵坐标
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("doubleClick", x, y)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def longClick(self, x, y, duration):
        """
        长按坐标
        :param x:横坐标
        :param y:纵坐标
        :param duration:长按时长
        :return:成功返回True 失败返回False
        """
        duration = duration/1000
        strData = self.setSendData("longClick", x, y, duration)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def swipe(self, startX, startY, endX, endY, duration):
        """
        滑动坐标
        :param startX:起始横坐标
        :param startY:起始纵坐标
        :param endX:结束横坐标
        :param endY:结束纵坐标
        :param duration:滑动时长
        :return:成功返回True 失败返回False
        """
        duration = duration/1000
        strData = self.setSendData("swipe", startX, startY, endX, endY, duration)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def dispatchGesture(self, gesturePath, duration):
        """
        执行手势
        :param gesturePath:[[x:number, y:number], [x1:number, y1:number]...] gesturePath 手势路径
        :param duration:手势时长
        :return:成功返回True 失败返回False
        """
        duration = duration / 1000
        strGesturePath = ""
        arrLen = len(gesturePath)
        for i in range(arrLen):
            strGesturePath += gesturePath[i][0] + "/"
            strGesturePath += gesturePath[i][1] + "/"
            if i < arrLen - 1:
                strGesturePath += "\n"

        strData = self.setSendData("dispatchGesture", strGesturePath, duration)
        strRet = self.sendData(strData)

        if strRet == "false":
            return False
        else:
            return True


    def dispatchGestures(self, gesturesPath):
        """
        执行多个手势
        :param gesturesPath:[[duration:number, [x:number, y:number], [x1:number, y1:number]...],[duration:number, [x:number, y:number], [x1:number, y1:number]...],...] gesturesPath  多点手势路径
        :return:成功返回True 失败返回False
        """
        strGesturesPath = ""
        arrLen1 = gesturesPath.length
        for i in range(arrLen1):
            arrLen2 = len(gesturesPath[i])
            strGesturesPath += gesturesPath[i][0] + "/"
            for j in range(arrLen2):
                strGesturesPath += gesturesPath[i][j][0] + "/"
                strGesturesPath += gesturesPath[i][j][1] + "/"
                if j < arrLen2 - 1:
                    strGesturesPath += "\n"
            if i < arrLen1 - 1:
                strGesturesPath += "\r\n"

        strData = self.setSendData("dispatchGestures", strGesturesPath)
        strRet = self.sendData(strData)

        if strRet == "false":
            return False
        else:
            return True

    ############
    #  发送文本  #
    ############
    def sendKeys(self, text):
        """
        发送文本
        :param text:发送的文本，需要打开aibote输入法
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("sendKeys", text)
        strRet = self.sendData(strData)

        if strRet == "false":
            return False
        else:
            return True

    ############
    #  发送按键  #
    ############
    def sendVk(self, keyCode):
        """
        发送按键
        :param keyCode:发送的虚拟按键，需要打开aibote输入法。例如：最近应用列表：187  回车：66
        : 按键对照表 https://blog.csdn.net/yaoyaozaiye/article/details/122826340
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("sendVk", keyCode)
        strRet = self.sendData(strData)

        if strRet == "false":
            return False
        else:
            return True

    def back(self):
        """
        返回
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("back")
        strRet = self.sendData(strData)

        if strRet == "false":
            return False
        else:
            return True

    def home(self):
        """home
        :return: 成功返回True 失败返回False
        """
        strData = self.setSendData("home")
        strRet = self.sendData(strData)

        if strRet == "false":
            return False
        else:
            return True

    def recents(self):
        """
        显示最近任务
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("recents")
        strRet = self.sendData(strData)

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
        wordsResult = []
        a = '''\[(\[\[\d+\.\d+,.\d+\.\d+\],.\[\d+\.\d+,.\d+\.\d+\],.\[\d+\.\d+,.\d+\.\d+\],.\[\d+\.\d+,.\d+\.\d+\]\]),.\('(.*?)',.\d\.\d{10,20}\)'''
        d = re.findall(a, strOcr)
        for i in d:
            point = i[0]
            words = i[1]
            wordsResult.append({'point': eval(point), 'words': words})
        return wordsResult

    def ocr(self, left, top, right, bottom, scale):
        """
        ocr
        :param left:左上角x点
        :param top:左上角y点
        :param right:右下角 x点
        :param bottom:右下角 y点
        :param scale:图片缩放率, 默认为 1.0 原大小。大于1.0放大，小于1.0缩小，不能为负数。
        :return:失败返回''，成功返回数组形式的识别结果
        """
        strData = self.setSendData("ocr", left, top, right, bottom, scale)
        strRet = self.sendData(strData)
        if strRet == "null" or strRet == "":
            return None
        else:
            return self.splitOcr(strRet)

    def getWords(self, options = {}):
        """
        获取屏幕文字
        :param options: {'region':[left:number, top:number, right:number, bottom:number], 'scale':number}
        : region 指定区域 [10, 20, 100, 200]，region默认全屏
        : scale浮点型 图片缩放率, 默认为 1.0 原大小。大于1.0放大，小于1.0缩小，不能为负数。仅在区域识别有效
        :return: 失败返回None，成功返回手机屏幕上的文字
        """
        left = 0; top = 0; right = 0; bottom = 0
        scale = 1.0
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if 'scale' in options and right!=0: # scale仅在区域识别有效
            scale = options["scale"]
        wordsResult = self.ocr(left, top, right, bottom, scale)
        if wordsResult == None:
            return None

        words = ""
        i = 0  # 避免下面len(wordsResult)-1为0，i就没定义
        for i in range(len(wordsResult)-1):
            words += wordsResult[i]["words"] + "\n"
        words += wordsResult[i]["words"]
        return words

    def findWords(self,words,options = {}):
        """
        查找文字 (本人自行添加了随机参数)
        :param words:要查找的文字
        :param options: options 可选参数, {region:[left:number, top:number, right:number, bottom:number], scale:number}
        : region 指定区域 [10, 20, 100, 200]，region默认全屏
        : scale浮点型 图片缩放率, 默认为 1.0 原大小。大于1.0放大，小于1.0缩小，不能为负数。仅在区域识别有效
        :return: 失败返回None，成功返回数组[{'x':number, 'y':number}, ...]，文字所在的坐标点
        """
        left = 0; top = 0; right = 0; bottom = 0
        scale = 1.0
        if 'region' in options:
            left = options["region"][0]
            top = options["region"][1]
            right = options["region"][2]
            bottom = options["region"][3]
        if 'scale' in options and right != 0 : # scale仅在区域识别有效
            scale = options["scale"]
        wordsResult = self.ocr(left, top, right, bottom, scale)
        if wordsResult==None:
            return None

        points = []
        for i in range(len(wordsResult)):
            if words in wordsResult[i]['words']:
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
                if right != 0: # 缩放图片
                    x = int((localLeft + offsetX) / scale + left)
                    y = int((localTop + offsetY) / scale + top)
                else:
                    x = int((localLeft + offsetX) * 2 + left)
                    y = int((localTop + offsetY) * 2 + top)
                points.append({"x": x + random.uniform(-width,width), "y": y + random.uniform(-height,height)}) # 根据大小添加随机参数
        if len(points) == 0:
            print('无坐标')
            return None
        else:
            return points

    ############
    #  URL请求  #
    ############
    def urlRequest(self, url, requestType, contentType = "null", postData = "null"):
        """
        URL请求
        :param url:请求的地址
        :param requestType:请求类型，GET或者POST
        :param contentType:可选参数，用作POST 内容类型
        :param postData:可选参数，用作POST 提交的数据
        :return:返回请求数据内容
        """
        strData = self.setSendData("urlRequest", url, requestType, contentType, postData)
        strRet = self.sendData(strData)
        return strRet

    ###############
    # Toast消息提示 #
    ###############
    def showToast(self, text):
        """
        Toast消息提示
        :param text:提示的文本
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("showToast", text)
        strRet = self.sendData(strData)

        if strRet == "false":
            return False
        else:
            return True

    ############
    #  启动APP  #
    ############
    def startApp(self, name):
        """
        启动App
        :param name:包名或者app名称
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("startApp", name)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    ############
    #  屏幕大小  #
    ############
    def getWindowSize(self):
        """
        屏幕大小
        :return:成功返回{'width':number, 'height':number}
        """
        strData = self.setSendData("getWindowSize")
        strRet = self.sendData(strData)
        arrRet = strRet.split("|")
        return {'width': int(arrRet[0]), 'height': int(arrRet[1])}

    ############
    #  图片大小  #
    ############
    def getImageSize(self, imagePath):
        """
        图片大小
        :param imagePath:图片路径
        :return:成功返回{'width':number, 'height':number}
        """
        strData = self.setSendData("getImageSize", imagePath)
        strRet = self.sendData(strData)
        arrRet = strRet.split("|")
        return {'width': int(arrRet[0]), 'height': int(arrRet[1])}

    ############
    # 获取安卓ID #
    ############
    def getAndroidId(self):
        strData = self.setSendData("getAndroidId")
        strRet = self.sendData(strData)
        return strRet

    ############
    # 验证码系统 #
    ############
    # ###### #
    #  超级鹰 #
    # ###### #
    def getCaptcha(self, filePath, username, password, softId, codeType, lenMin = 0):
        """
        识别验证码
        :param filePath:图片文件路径
        :param username:用户名
        :param password:密码
        :param softId:软件ID
        :param codeType:图片类型 参考https://www.chaojiying.com/price.html
        :param lenMin:最小位数 默认0为不启用,图片类型为可变位长时可启用这个参数
        :return: 返回JSON {err_no:number, err_str:string, pic_id:string, pic_str:string, md5:string}
        : err_no,(数值) 返回代码  为0 表示正常，错误代码 参考https://www.chaojiying.com/api-23.html
        : err_str,(字符串) 中文描述的返回信息
        : pic_id,(字符串) 图片标识号，或图片id号
        : pic_str,(字符串) 识别出的结果
        : md5,(字符串) md5校验值,用来校验此条数据返回是否真实有效
        """
        strData = self.setSendData("getCaptcha", filePath, username, password, softId, codeType, lenMin)
        strRet = self.sendData(strData)
        return json.loads(strRet)
    def errorCaptcha(self,username, password, softId, picId):
        """
        识别报错返分
        :param username:用户名
        :param password:密码
        :param softId:软件ID
        :param picId:图片ID 对应 getCaptcha返回值的pic_id 字段
        :return:{err_no:number, err_str:string} 返回JSON
        : err_no,(数值) 返回代码
        : err_str,(字符串) 中文描述的返回信息
        """
        strData = self.setSendData("errorCaptcha", username, password, softId, picId)
        strRet = self.sendData(strData)
        return json.loads(strRet)

    def scoreCaptcha(self,username, password):
        """
        查询验证码剩余题分
        :param username:用户名
        :param password:密码
        :return: 返回JSON {err_no:number, err_str:string, tifen:string, tifen_lock:string}
        """
        strData = self.setSendData("scoreCaptcha", username, password)
        strRet = self.sendData(strData)
        return json.loads(strRet)

    # ###### #
    #   图鉴  #
    # ###### #
    def tujian_base64_api(self, uname, pwd, img, typeid):
        """
        使用图鉴识别验证码
        :param uname: 你的图鉴账号
        :param pwd: 图鉴密码
        :param img: 图片路径
        :param typeid: 默认3，数英结合
        : 一、图片文字类型(默认 3 数英混合)：
        : 1 : 纯数字       1001：纯数字2        2 : 纯英文          1002：纯英文2       3 : 数英混合
        : 1003：数英混合2   4 : 闪动GIF       7 : 无感学习(独家)     11 : 计算题         1005:  快速计算题
        : 16 : 汉字       32 : 通用文字识别(证件、单据)  66:  问答题   49 :recaptcha图片识别
        : 二、图片旋转角度类型：
        : 29 :  旋转类型
        : 三、图片坐标点选类型：
        : 19 :  1个坐标            20 :  3个坐标         21 :  3 ~ 5个坐标       22 :  5 ~ 8个坐标
        : 27 :  1 ~ 4个坐标        48 : 轨迹类型
        : 四、缺口识别
        : 18 : 缺口识别（需要2张图 一张目标图一张缺口图）       33 : 单缺口识别（返回X轴坐标 只需要1张图）
        : 五、拼图识别
        : 53：拼图识别
        :return:
        """
        with open(img, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            b64 = base64_data.decode()
        data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
        result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
            return result["message"]

    def reportError(self,id_):
        """
        图鉴识别报错脚本
        :param id_: 成功返回的id
        :return:
        """
        data = {"id": id_}
        result = json.loads(requests.post("http://api.ttshitu.com/reporterror.json", json=data).text)
        if result['success']:
            return "报错成功"
        else:
            return result["message"]


    ############
    #  元素操作  #
    ############
    def getElementRect(self, xpath):
        """
        获取元素位置
        :param xpath:元素路径
        :return:成功返回元素位置，失败返回None, {'left':number, 'top':number, 'right':number, 'bottom':number}
        """
        strData = self.setSendData("getElementRect", xpath)
        startTime = time.time()
        endTime = time.time()
        while endTime - startTime <= self.waitTimeout:
            strRet = self.sendData(strData)
            if strRet == "-1|-1|-1|-1":
                time.sleep(self.intervalTimeout)
            else:
                break
        if strRet == "-1|-1|-1|-1":
            return None
        arrRet = strRet.split("|")
        return {'left': int(arrRet[0]), 'top': int(arrRet[1]), 'right': int(arrRet[2]),
                'bottom': int(arrRet[3])}

    def getElementDescription(self, xpath):
        """
        获取元素描述
        :param xpath:元素路径
        :return:成功返回元素内容，失败返回None
        """
        strData = self.setSendData("getElementDescription", xpath)
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

    def getElementText(self, xpath):
        """
        获取元素文本
        :param xpath:元素路径
        :return:成功返回元素内容，失败返回None
        """
        strData = self.setSendData("getElementText", xpath)
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

    def elementIsVisible(self, xpath):
        """
        判断元素是否可见
        :param xpath:元素路径
        :return:可见 Ture，不可见 False
        """
        windowRect = self.getWindowSize()
        elementRect =  self.getElementRect(xpath)
        if elementRect == None:
            return False
        elementWidth = elementRect['right'] - elementRect['left']
        elementHeight = elementRect['bottom'] - elementRect['top']
        if elementRect['top'] < 0 or elementRect['left'] < 0 or elementWidth > windowRect['width'] or elementHeight > windowRect['height']:
            return False
        else:
            return True

    def setElementText(self, xpath, text):
        strData = self.setSendData("setElementText", xpath, text)
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

    def clickElement(self, xpath):
        """
        点击元素
        :param xpath:元素路径
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("clickElement", xpath)
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

    def scrollElement(self, xpath, direction):
        """
        滚动元素
        :param xpath:元素路径
        :param direction:0 向前滑动， 1 向后滑动
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("scrollElement", xpath, direction)
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

    def existsElement(self, xpath):
        """
        判断元素是否存在
        :param xpath:元素路径
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("existsElement", xpath)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def isSelectedElement(self, xpath):
        """
        判断元素是否选中
        :param xpath:元素路径
        :return:成功返回True 失败返回False
        """
        strData = self.setSendData("isSelectedElement", xpath)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    ############
    #  文件传输  #
    ############
    def pushFile(self, windowsFilePath, androidFilePath):
        """
        上传文件
        :param windowsFilePath: 电脑文件路径，注意电脑路径 "\\"转义问题
        :param androidFilePath: 安卓文件保存路径, 安卓外部存储根目录 /storage/emulated/0/
        :return: 成功返回True 失败返回False
        """
        with open(windowsFilePath, 'rb') as f:
            fileData = f.read()
        byteData = self.setSendFile("pushFile", androidFilePath, fileData)
        strRet =  self.sendData(byteData)
        if strRet == "false":
            return False
        else:
            return True

    def pullFile(self, androidFilePath, windowsFilePath):
        """
        拉取文件
        :param androidFilePath:安卓文件路径，安卓外部存储根目录 /storage/emulated/0/
        :param windowsFilePath:电脑文件保存路径，注意电脑路径 "\\"转义问题
        :return:
        """
        strData = self.setSendData("pullFile", androidFilePath)
        byteRet = self.sendData(strData)
        with open(windowsFilePath,'wb') as f:
            f.write(byteRet)

    #############
    # 安卓文件读写 #
    #############
    def writeAndroidFile(self, androidFilePath, text, isAppend=False):
        """
        写入安卓文件
        :param androidFilePath:androidFilePath 安卓文件路径，安卓外部存储根目录 /storage/emulated/0/
        :param text:写入的内容
        :param isAppend:可选参数，是否追加，默认覆盖文件内容
        :return:成功返回true，失败返回 false
        """
        strData = self.setSendData("writeAndroidFile", androidFilePath, text, isAppend)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def readAndroidFile(self, androidFilePath):
        """
        读取安卓文件
        :param androidFilePath:安卓文件路径，安卓外部存储根目录 /storage/emulated/0/
        :return:成功返回文件内容，失败返回 None
        """
        strData = self.setSendData("readAndroidFile", androidFilePath)
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet

    #############
    # Intent跳转 #
    #############
    def openUri(self, uri):
        """
        跳转uri
        :param uri:跳转链接，例如：打开支付宝扫一扫界面，"alipayqr://platformapi/startapp?saId=10000007"
        :return:成功返回True，失败返回 False
        """
        strData = self.setSendData("openUri", uri)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def callPhone(self, phoneNumber):
        """
        拨打电话
        :param phoneNumber:拨打的电话号码
        :return:成功返回True，失败返回 False
        """
        strData = self.setSendData("callPhone", phoneNumber)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def sendMsg(self, phoneNumber, message):
        """
        发送短信
        :param phoneNumber:发送的电话号码
        :param message:短信内容
        :return:成功返回True，失败返回 False
        """
        strData = self.setSendData("sendMsg", phoneNumber, message)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    ##############
    # 获取包名/窗口 #
    ##############
    def getActivity(self):
        """
        获取当前活动窗口(Activity)
        :return:成功返回当前activity
        """
        strData = self.setSendData("getActivity")
        strRet = self.sendData(strData)
        return strRet

    def getPackage(self):
        """
        获取当前活动包名(Package)
        :return:成功返回当前包名
        """
        strData = self.setSendData("getPackage")
        strRet = self.sendData(strData)
        return strRet

    ############
    # 安卓剪贴板 #
    ############
    def setClipboardText(self, text):
        """
        设置剪切板文本
        :param text:设置的文本
        :return:成功返回True，失败返回 False
        """
        strData = self.setSendData("setClipboardText", text)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def getClipboardText(self):
        """
        获取剪切板文本
        :return:需要打开aibote输入法。成功返回剪切板文本，失败返回None
        """
        strData = self.setSendData("getClipboardText")
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return strRet

    #############
    # 创建脚本控件 #
    #############
    def createTextView(self, id, text, x, y, width, height):
        """
        创建TextView控件
        :param id:控件ID，不可与其他控件重复
        :param text:控件文本
        :param x:控件在屏幕上x坐标
        :param y:控件在屏幕上y坐标
        :param width:控件宽度
        :param height:控件高度
        :return:成功返回True，失败返回 False
        """
        strData = self.setSendData("createTextView", id, text, x, y, width, height)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def createEditText(self, id, hintText, x, y, width, height):
        """
        创建EditText控件
        :param id:控件ID，不可与其他控件重复
        :param hintText:hintText 提示文本
        :param x:控件在屏幕上x坐标
        :param y:控件在屏幕上y坐标
        :param width:控件宽度
        :param height:控件高度
        :return:成功返回True，失败返回 False
        """
        strData = self.setSendData("createEditText", id, hintText, x, y, width, height)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def createCheckBox(self, id, text, x, y, width, height):
        """
        创建CheckBox控件
        :param id:控件ID，不可与其他控件重复
        :param text:控件文本
        :param x:控件在屏幕上x坐标
        :param y:控件在屏幕上y坐标
        :param width:控件宽度
        :param height:控件高度
        :return:成功返回True，失败返回 False
        """
        strData = self.setSendData("createCheckBox", id, text, x, y, width, height)
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def clearScriptControl(self):
        """
        清除脚本控件
        :return:成功返回True，失败返回 False
        """
        strData = self.setSendData("clearScriptControl")
        strRet = self.sendData(strData)
        if strRet == "false":
            return False
        else:
            return True

    def getScriptParam(self):
        """
        获取脚本配置参数
        :return:成功返回{"id":"text", "id":"isSelect"}
        : 此类对象，失败返回None。函数仅返回TextEdit和CheckBox控件值，需要用户点击安卓端 "提交参数" 按钮
        """
        strData = self.setSendData("getScriptParam")
        strRet = self.sendData(strData)
        if strRet == "null":
            return None
        else:
            return json.loads(strRet)