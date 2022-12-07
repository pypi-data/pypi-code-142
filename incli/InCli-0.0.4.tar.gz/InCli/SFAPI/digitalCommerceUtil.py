from . import restClient, objectUtil,digitalCommerce,utils,thread
import time
import sys

def _getItemAtPath(obj,path,field='ProductCode'):
    for p in path.split(':'):
        obj = objectUtil.getSibling(obj,field,p)  
    return obj

def updateOfferField(offerDetails,path,field,value,pathField='ProductCode'):
    obj = _getItemAtPath(offerDetails,path,pathField)
    if obj == '':
        raise ValueError(f'Object does not contain element by path {path}')
    if field in obj:
        obj[field] = value
    else:
        raise ValueError(f'Object does not contain field {field} by path {path}')

    return offerDetails

def updateOfferAttribute(offerDetails,path,AttributeCategory,productAttribute,value):
    obj = _getItemAtPath(offerDetails,path)
    obj = _getItemAtPath(obj,AttributeCategory,field='Code__c')
    obj = _getItemAtPath(obj,productAttribute,field='code')

    obj['userValues'] = value
 
    return offerDetails

def getBasketProductAttributes(basket,path):
    obj = _getItemAtPath(basket,path)
    obj = obj['attributeCategories']

    return obj

def getAction(basket,path,method='addChildBasketAction'):

    lpath = path.split(':')
    xpath = ":".join(lpath[:-1])
    offer = lpath[-1]


    obj = _getItemAtPath(basket,xpath)
    action = _getItemAtPath(obj,method,field='method')

    action['params']['offer'] = offer
    action['link'] = f"/services/apexrest/{restClient.getNamespace()}{action['link']}"



    return action


def checkOffers(path=None,quantity=None):

    catalogs = digitalCommerce.getCatalogs()
    print()
    print('Catalogs in the Org:')
    utils.printFormated(catalogs,"Name:vlocity_cmt__CatalogCode__c:vlocity_cmt__IsActive__c%Active:vlocity_cmt__Description__c")
    print()

    catOffers = []
    numOffersList = []

    print("Getting offfers per catalog.")
    getOfferTimes = []
    def getOffersPerCatalog(catalog):
        if catalog['vlocity_cmt__IsActive__c'] == False:
            return 
        try:
            times = {
                'name':catalog['vlocity_cmt__CatalogCode__c'],
                'Error':'',
                "__color__":utils.CEND
            }
            offers = digitalCommerce.getOfferByCatalogue(catalog['vlocity_cmt__CatalogCode__c'])
            times['elapsed'] = restClient.getLastCallTime()
            l = len(offers) if offers is not None else 0
            numOffersList.append(l)
            times['# Offers'] = l

        except Exception as e:
            times['elapsed'] = restClient.getLastCallTime()
            times['Error'] = e.args[0]['error']
            times['__color__'] = utils.CRED
            getOfferTimes.append(times)
            return   

        if offers == None:
            times['Error'] = "Has no offers."
            times['__color__'] = utils.CYELLOW
            getOfferTimes.append(times)
            return 

        catOffer = {
            'catCode':catalog['vlocity_cmt__CatalogCode__c'],
            'offers':offers
        }
        catOffers.append(catOffer)
        getOfferTimes.append(times)

    thread.processList(getOffersPerCatalog,catalogs,1)
    utils.printFormated(getOfferTimes)
    totalOffers = sum(numOffersList)
    print()

    print(f"Getting offerDetails, createBasket, createBasket with config per offer. total offers {totalOffers}")

    offersList = []
    for catOffer in catOffers:
        for offerCount,offer in enumerate(catOffer['offers']):
            _offer = {
                'catalogCode':catOffer['catCode'],
                'offerCode':digitalCommerce.getOfferCode(offer)
            }
            offersList.append(_offer)

    thread.processList(dba,offersList,50)
    print()
    newlist = sorted(_theTimes, key=lambda d: f"{d['catalog']}{d['offerCode']}")
    utils.printFormated(newlist)

    print()

_theTimes = []
def dba(offerCodes):
    try:
        offerCode = offerCodes['offerCode']
        catalogCode = offerCodes['catalogCode']
        times = {
            'catalog':catalogCode,
            'offerCode':offerCode,
            '__color__':utils.CEND
        }

        if offerCode == 'PROMO_NOS_OFFER_007':
            print()
        details = digitalCommerce.getOfferDetails(catalogCode,offerCode)
        times['details'] = restClient.getLastCallTime()

        basket = digitalCommerce.createBasket(catalogCode,offerCode)
        times['createBasket'] = restClient.getLastCallTime()
        times['basket contextKey']=basket['cartContextKey']

        offerDetails = updateOfferField(details,'0001','Quantity',4,'lineNumber')

        basket2 = digitalCommerce.createBasketAfterConfig(catalogCode,offerDetails)
        times['afterConfig'] = restClient.getLastCallTime()

    except Exception as e:
        times['error']=e.args[0]['error']
        times['__color__'] = utils.CRED

    _theTimes.append(times)

