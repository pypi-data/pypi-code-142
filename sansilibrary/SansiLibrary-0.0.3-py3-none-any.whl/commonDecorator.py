# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @email: maoyongfan@163.com
# @Date:   2022-12-05 16:49:39
# @Last Modified by:   yongfanmao
# @Last Modified time: 2022-12-09 10:00:47
import os
import platform

# from SansiLibrary.CommonKeywords import CommonKeywords

def savePic(func):
	def wrapper(self,*args,**kwargs):
		
		result = func(self,*args,**kwargs)
		if result:
			playerName,playerID,content,path,num,dateDir = result[0],result[1],result[2],result[3],result[4],result[5]

			if platform.system().lower() == "linux":
				path = "/home/sansi/autoTest/runRecord"
			
			save_path = path + os.sep + playerName + "_" + playerID + os.sep + dateDir

			if not os.path.exists(save_path):
				os.makedirs(save_path)

			with open(save_path + os.sep +'{num}.jpg'.format(num=num),'wb') as f:
				f.write(content)
				f.close()
	return wrapper