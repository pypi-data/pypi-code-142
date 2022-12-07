
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import logging as log



class ScrapEvent:

    def __init__(self,location,event) -> None:
        log.info('<--------Inside Constructor----------->')
        self.loc = location
        self.event = event


    def __removeTag(self,a):
        b = a.split('>')[1].split('<')[0]
        return b


    def __scrapping(self,myUrl):


        uClient = uReq(myUrl)
        pageSoup = soup(uClient.read().decode('utf-8', 'ignore'), 'html.parser')

        containers = pageSoup.find_all('div',{'class':'search-event-card-wrapper'})

        name = []
        price = []
        time = []
        location = []


        for i in containers:
            strName = str(i.find('div', {'class': 'eds-is-hidden-accessible'}))
            strTime = str(i.find('div', {
            'class': 'eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm'}))
            strPrice = str(
            i.find_all('div', {'class': 'eds-event-card-content__sub eds-text-bm eds-text-color--ui-600 eds-l-mar-top-1'}))
            strLocation = str(i.find('div', {'data-subcontent-key': 'location'}))



            name.append(self.__removeTag(strName))
            price.append(self.__removeTag(strPrice))
            time.append(self.__removeTag(strTime))
            location.append(self.__removeTag(strLocation))

        df = pd.DataFrame(zip(name, time, location, price))

        return df




    def __str__(self) :
        log.info('<-----------Inside String function ------------->')
        return 'This class is used to scrap data from eventbrite.ie'




    def getData(self):
        log.info('<--------------Inside getData ---------------->')
        myUrl = 'https://www.eventbrite.ie/d/ireland--{0}/{1}/?page={2}'
        
        myList = []

        finalDf = pd.DataFrame()

        for i in range(1,3):
            df2 = pd.DataFrame()
            df2 = self.__scrapping(myUrl.format(self.loc,self.event,i))
            myList.append(df2)


        finalDf = pd.concat(myList)
        finalDf.columns=['name', 'time', 'location', 'price']

        return finalDf


          
