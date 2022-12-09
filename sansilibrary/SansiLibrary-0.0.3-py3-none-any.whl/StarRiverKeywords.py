# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @email: maoyongfan@163.com
# @Date:   2022-12-05 13:48:02
# @Last Modified by:   yongfanmao
# @Last Modified time: 2022-12-08 09:20:54
import os
import datetime
import time

from robot.api import logger
from robot.api.deco import keyword
from SansiLibrary.CommonKeywords import CommonKeywords
from SansiLibrary.RequestsSessionKeywords import RequestsSessionKeywords
from SansiLibrary.commonDecorator import savePic

class StarRiverKeywords(object):

	@keyword("Take Screenshots During Playback")
	def take_screenshots_during_playback(self,playerName,playerID,programDuration,\
		picType="snapshot",hostUrl = "",cookies={},path="D:\\runRecord"):
		"""
		必传:
			playerName: 播放器名称
			playerID:  播放器ID
			programDuration:	节目播放时长毫秒
		非必传
			picType:  截图类型
			hostUrl:  截图地址的host
			cookies:  所需cookies
			path:     保存图片的基础路径

		"""
		programDuration  = int(int(programDuration)/1000) + 5

		ck = CommonKeywords()
		dateDir = ck.get_time_format(formatStyle="%Y_%m_%d_%H_%M_%S")
		for second in range(1,programDuration+1):
			logger.info(second)
			self._snapshot(playerName,playerID,second,picType=picType,\
				hostUrl = hostUrl,cookies=cookies,path=path,dateDir=dateDir)
			time.sleep(1)


	@savePic
	def _snapshot(self,playerName,playerID,num,picType="",hostUrl = "",cookies={},path='',dateDir=''):
		rs  = RequestsSessionKeywords(url = hostUrl, cookies = cookies)
		if picType == "snapshot":
			uri = "/api/media/players/{playerID}/snapshot".format(playerID=playerID)
		elif picType == "thumbnail":
			uri = "/api/storage/players/{playerID}/thumbnail/download".format(playerID=playerID)
		else:
			uri = "/api/media/players/{playerID}/snapshot".format(playerID=playerID)	
		response = rs.session_get(uri)
		status_code = response.status_code 
		if status_code == 200:
			return (playerName,playerID,response.content,path,num,dateDir)
		elif status_code == 406:
			logger.error(response.text)
			logger.error("截图超时")
			return False
		else:
			logger.error(response.text)
			logger.warn("当前错误返回码为:",status_code)
			return False




