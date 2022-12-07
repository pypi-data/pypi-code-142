from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import time
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import pymysql
from urllib.request import urlopen
import json

class getJson:
   """
   getJson from url
   """

   def __init__(self):
      self.nada=0

   def readJsonUrlToDf(self,url):
       continuar=True
       intentos=0
       intentosMax=6
       result=pd.DataFrame()
       while(continuar):
           try:
               with urlopen(url,timeout=28) as response:
                   body = response.read()
                   data = json.loads(body)
               result=pd.DataFrame(data)
               if(int(result.shape[0])>0):
                   continuar=False
           except Exception as e:
               print('err readJsonUrlToDf;',e)

           intentos=intentos+1
           if(intentos<=intentosMax):
               continuar=False
           if(~continuar):
               return result
       return result

   def readJsonUrlToInfoData(self,url):
       continuar=True
       intentos=0
       intentosMax=6
       result=pd.DataFrame()
       while(continuar):
           try:
               with urlopen(url,timeout=28) as response:
                   body = response.read()
                   info = json.loads(body)["info"]
                   data = json.loads(body)["data"]
                   #print(info)
                   #print(data)
               result=pd.DataFrame(data)
               if(int(result.shape[0])>0):
                   continuar=False
           except Exception as e:
               print('err readJsonUrlToInfoData;',e)

           intentos=intentos+1
           if(intentos<=intentosMax):
               continuar=False
           if(~continuar):
               return info,result
       return info,result

class hora:
   """
   Retorna la Hora
   """

   def __init__(self):
      self.nada=0

   def get(self,asString=True):
      """
      :return: la hora
      :rtype: string
      """
      if(asString):
         return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      else:
         return datetime.now()


   def hoy(self,asString=True):
      """
      :return: la fecha actual
      :rtype: string
      """
      now = datetime.now().strftime("%Y-%m-%d")
      if(asString):
         return now
      else:
         return datetime.strptime(now,"%Y-%m-%d")

   def ayer(self,asString=True):
      """
      :return: la fecha de ayer
      :rtype: string
      """
      yesterday = datetime.now() - timedelta(days=1)
      yesterday = yesterday.strftime("%Y-%m-%d")
      if(asString):
         return yesterday
      else:
         return datetime.strptime(yesterday,"%Y-%m-%d")


   def diasAtras(self,dias,asString=True):
      """
      :return: la fecha de ayer
      :rtype: string
      """
      yesterday = datetime.now() - timedelta(days=dias)
      yesterday = yesterday.strftime("%Y-%m-%d")
      if(asString):
         return yesterday
      else:
         return datetime.strptime(yesterday,"%Y-%m-%d")

   def mesesAtras(self,mesesAtras,asString=True):
      hoy = date.today()
      fromx = hoy - relativedelta(months=mesesAtras)
      fromx = fromx.strftime("%Y-%m-01")
      tox = hoy - relativedelta(months=(mesesAtras-1))
      tox = tox.strftime("%Y-%m-01")
      if(asString):
         return {"fromx":fromx, "tox":tox}
      else:
         return {"fromx":datetime.strptime(fromx,"%Y-%m-%d"), "tox":datetime.strptime(tox,"%Y-%m-%d")}
hora=hora()

class out:
   """
   escribe log modo append
   :param filename: nombre del archivo
   :type filename: string
   """

   def __init__(self,filename='/dev/null'):
      self.filename = filename

   def log(self,text):
      """
      :param text: texto a escribir
      :type text: string
      """
      horax=hora.get()
      f = open(self.filename, "a")
      f.write(horax + "; " + text + "\n")
      f.close()

   def print(self,text):
      """
      :param text: texto a imprimir
      :type text: string
      """
      horax=hora.get()
      print(horax + "; " + text)

outx=out()

class mysql:
   """
   queries mysql db
   :param servidor: ip
   :type servidor: string

   :param user: user
   :type user: string

   :param pass: ip
   :type pass: string

   :param db: ip
   :type db: string
   """

   def __init__(self,servidorx,userx,passx,dbx,port=3306):
      self.servidorx=servidorx
      self.userx=userx
      self.passx=passx
      self.dbx=dbx
      self.port=port

   def insert(self,query):
      connectionObject   = pymysql.connect(host=self.servidorx, port=self.port, user=self.userx, password=self.passx,db=self.dbx,local_infile=True)
      try:
         cursorObject            = connectionObject.cursor()
         x=cursorObject.execute(query)
         #print('rows:',x)
         connectionObject.commit()
      except Exception as e:
         out().print("Exeception occured:{}".format(e))
      else:
         connectionObject.close()

   def query(self,q,intentos=3,sleepStep=1):
      looper=0
      intentos=int(intentos)
      valid=False
      while looper < intentos:
          if looper>1:
              time.sleep(sleepStep*looper)
          looper+=1
          try:
              df=self.mysqlQuerySilent(q)
              if isinstance(df, pd.DataFrame):
                  valid=True
                  break
          except Exception as e:
              falla='Err mysql; Check Install sqlalchemy pymysql pandas ;'+str(e)
              out().print(falla)
              nada=0

      if(valid):
        #out().print('intentos:' + str(looper) + '; df.shape:' + str(df.shape) )
        return {'result':1,'data':df}
      else:
        #out().print('Err mysql; intentos:' + str(looper) )
        return {'result':0,'data':pd.DataFrame()}


   def mysqlQuerySilent(self,query):
      df='err:'
      try:
         sqlEngine       = create_engine('mysql+pymysql://'+self.userx+':'+self.passx+'@'+self.servidorx)
         dbConnection    = sqlEngine.connect()
         frame           = pd.read_sql(query, dbConnection);
         dbConnection.close()
         return frame
      except OperationalError as e:
         out().print('Err mysql; ' + str(e))
         return ''
      except Exception as e:
         out().print('Err mysql; ' + str(e))
         return ''
      finally:
         dbConnection.close()

