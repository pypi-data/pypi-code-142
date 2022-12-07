import json
from .SFAPI import Sobjects, query,restClient,jsonFile,utils,objectUtil,debugLogs,digitalCommerceUtil
import logging
import simplejson,sys
from operator import itemgetter
from inspect import getmembers, isfunction
import traceback


varsFile = 'confIcli.json'
vars = None


def readVars(field=None):
    global vars
    vars = jsonFile.read(varsFile)

    if field != None:
        return vars[field]
    return vars

def setVar(name,value):

    vars = jsonFile.read(varsFile)
    vars[name]=value
    jsonFile.write(varsFile,vars)
    print(simplejson.dumps(vars, indent=4))

def getParam(argv,key,i=1):
    if key not in argv:
        return None

    ind = argv.index(key)
    if (ind+i <= (len(argv)-1)):
        arg = argv[ind+i]
        if arg[0] == '-':
            return None
        return arg
    return None

def listEnvs():
    cons = restClient.getConfigOrgs()
    cons = sorted(cons,key=itemgetter('name'))
    utils.printFormated(cons,fieldsString='name:isSandBox:instance_url:login.username:login.password:login.bearer')
    env = readVars('environment')
    print(f"Current Environment is {env}")

def _queryAndPrint(q,fields=None,systemFields=True,nullFields=False):

    res = query.queryRecords(q)
    if fields != None:
        res = utils.deleteNulls(res,systemFields==False,nullFields==False)
        if fields=='all':
            utils.printFormated(res)
        else:
            utils.printFormated(res,fields)
    else:
        res = utils.deleteNulls(res,systemFields==False,nullFields==False)
        print(simplejson.dumps(res, indent=4))
    
    print()
    print(f"Null values -> {nullFields}  systemFields --> {systemFields}")

def option_q(args):
    if '-h' in args:
        help = """
        -q "select..." query to execute. 
            -null - will print null values as well
            -system - will print the system fields
            -fields "a:b:c:..."
            -fields all"""
        return help

    #else:
    q = getParam(args,'-q')

    fields = getParam(args,'-fields') if '-fields' in args else None    
    nullFields = True if '-null' in args else False
    systemFields = True if '-system' in args else False

    connectionInit(args)

    _queryAndPrint(q,fields=None,systemFields=True,nullFields=False)

def option_checkCatalogs(args):
    if '-h' in args:
        help = """
        -checkCatalogs 
            Checks the catalogs. Gets all catalogs, does a getOffers, getOfferDetails, basketwithoutconfig and basket with config
            path: the path to a child product to configure. Path = ... ProductCode ... ProdcutCode
            quantity: the quantity for the object""" 
        return help

    connectionInit(args)

   # path = getParam(args,'-checkCatalogs')
   # quantity = getParam(args,'-checkCatalogs',2)

    digitalCommerceUtil.checkOffers()

    print()

def option_d(args):
    help = """
        -d objectName --> Describe an object
            -d objectName:fieldName --> describe a field in the objec"""
    if '-h' in args:
        return help    

    connectionInit(args)

    objectField = getParam(args,'-d')
    if objectField == None:
        print(help)
        return

    ofs = objectField.split(':')

    sObjectName = ofs[0]
    fieldName = ofs[1] if len(ofs) > 1 else None

    res = Sobjects.describe(sObjectName)
    if fieldName == None:
        print(simplejson.dumps(res['fields'], indent=4))
    else:
        sibbling = objectUtil.getSiblingWhere(res['fields'],'name',fieldName)['object']

        print(simplejson.dumps(sibbling, indent=4))

def option_l(args):
    if '-h' in args:
        help = """
        -l --> current org limits consuptions. """
        return help
    connectionInit(args)
    action = '/services/data/v51.0/limits'
    res = restClient.callAPI(action)
    records = []
    for key in res.keys():
        record = {
            'Limit':key,
            'Max':res[key]['Max'],
            'Remaining':res[key]['Remaining'],
        }
        record['Percent Remaining'] =  100 *(res[key]['Remaining']/res[key]['Max']) if res[key]['Max']>0 else 0
        record['__color__'] = ''

        if record['Max'] != 0:
            if record['Percent Remaining']<50:
                record['__color__'] = utils.CYELLOW
            if record['Percent Remaining']<25:
                record['__color__'] = utils.CYELLOW
        records.append(record)

    utils.printFormated(records)

def option_o(args):
    if '-h' in args:
        help = """
        -o --> List all Objects
            -like name
            objectName  --> get one row from the object
            objectName:Id --> get the row especified by the Id"""
        return help
        
    connectionInit(args)

    if '-name' in args:
        obj = getParam(args,'-name')
        chunks = obj.split(':')

        if len(chunks) == 1:
            q = f"select fields(all) from {chunks[0]} limit 1"
        else:
            q = f"select fields(all) from {chunks[0]} where Id='{chunks[1]}'"

        print('pre q:'+q)
        _queryAndPrint(q)
        return
        
    like = getParam(args,'-like') if '-like' in args else None    
    count = True if '-count' in args else False   

    objs = Sobjects.listObjects()
    if like is not None:
        if ':' not in like:
            like = f"name:{like}"        
        ls = like.split(':')
        outs = []
        for obj in objs:
      #      print(f"{str(ls[1])} . {str(obj[ls[0]])}")
            if str(ls[1]).lower() in str(obj[ls[0]]).lower():
                outs.append(obj) 
    else:
        outs = objs

    if count==True:
        for out in outs:
            if out['queryable'] == True:
                print("Quering objects row count.")
                print("", end=".")          
                try:
                    if out['name'] == 'AccountUserTerritory2View':
                        print()
                    c = query.query(f" select count(Id) from {out['name']}",raiseEx=True)
                    out['count'] = c['records'][0]['expr0']
                except Exception as e:
                    out['count'] = 'E'
            else:
                out['count'] = '-'
    
    #print(simplejson.dumps(objs, indent=4))
    utils.printFormated(outs,'name:label:associateParentEntity:associateParentEntity:queryable:count')

def option_default(args):
    help = """
        -default:set key value --> defaults the specified key-value
        -default:del key    --> deletes the default
        -default:get key    --> displays the current value
        """

    if '-h' in args:
        return help   

    if "-default:del" in args:
        key = getParam(args,'-default:del',1)
        if key == None:
            restClient.glog().info(f'Key not found in the provided arguments. {args}')
            return 
        restClient.delConfigVar(key)
        return

    if "-default:set" in args: 
        key = getParam(args,'-default:set',1)
        value = getParam(args,'-default:set',2)
        if key == None or value==None:
            print(help)
            return

        restClient.setConfigVar(key,value)
        print(f"Default value for {key} is {value}")

    if "-default:get" in args: 
        key = getParam(args,'-default:get',1)
        value =restClient.getConfigVar(key)
        print(f"Default value for {key} is {value}")

def option_history(args):
    if '-h' in args:
        help = """
        -history"""
        return help
    print()
    print('HISTORY:')
    vars = jsonFile.read(varsFile)
    for line in vars['history']:
        print(line)

def option_logs(args):
    help = """
        -logs:ls --> list last logs
            -limit how many, default 50 max 200
            -user "field:value", filter for specified user. The user can be specified by any field in the User Object. Examples:
                    "Id:XXXXXXXX"
                    "name:Onboarding Site Guest User"
                    "FirstName:Onboarding"
                    "ProfileId:00e3O000000IHneQAG"
        -logs --> parse logs
            -logs Id --> parse the logs with the provided Id
            -logs -last:X --> parses the last X logs. 
        """

    if '-h' in args:
        return help

    if '-logs:ls' in args:
        user = getParam(args,'-user') 
        last = getParam(args,'-last') 
        lim = 50 if last == None else last

        connectionInit(args)

        id = None
        if user != None:
            chunks = user.split(":")
            key = chunks[0]
            value = chunks[1]
            id = query.queryField(f"Select Id from User where {key}='{value}'") if key.lower()!='id' else value
        debugLogs.printLogs(logUserId=id,limit=lim)
    else:
        logId = getParam(args,'-logs')    
        last = getParam(args,'-last')    

        if logId == None and last == None:
            print(help)
            return

        connectionInit(args)
        debugLogs.parseLog(logId,lastN=last)

    return
    printLimits = False if '-nolimits' in args else True
    userDebug = False if '-userDebug' in args else True
    last = True if '-last' in args else False
    lastN = getParam(args,'-last')  if last == True else 1

    isLogUserId = True if '-userId' in args else False
    logUserId = getParam(args,'-userId')  if isLogUserId == True else None

    if last == True:
        logId = None
        
    if logId == 'latest':
        logId = None

    debugLogs.parseLog(logId,printLimits=printLimits,userDebug=userDebug,lastN=lastN,logUserId=logUserId)

def option_h(args):
    module = __import__('InCli')

    funcs = getmembers(sys.modules[__name__], isfunction)
    functions = [func[0] for func in funcs if func[0].startswith('option_')]

    for f in functions:
        if f == 'option_h':
            continue

        print(eval(f'{f}(args)'))      

def connectionInit(argsIn):

    userName_or_ofgAlias = getParam(argsIn,'-u') 
    restClient.init(userName_or_ofgAlias)

def main(argsIn):
    try:
    #    restClient.setConfigFile('/Users/uormaechea/Documents/Dev/python/Industries/config/ConnectionsParams.json')
    #    restClient.initWithConfig('DEVNOSCAT2')

        restClient.setLoggingLevel(logging.INFO)
      #  connectionInit(argsIn)

        # "uormaechea.devnoscat3@nos.pt"
        if '-h' in argsIn:
            help = """
        -u --> username or org alias to be used to log into the org. 
               Can be set to a default value --> -set u "xx"adas.com"
        """
            print(help)

        funcs = getmembers(sys.modules[__name__], isfunction)
        functions = [func[0] for func in funcs if func[0].startswith('option_')]

        args = []
        for argv in argsIn:
            if argv == '|':
                break
            args.append(argv)

        for arg in args:
            ar = arg.split(':')[0][1:]
            ar = f"option_{ar}"
            if ar in functions:
         #       module = __import__('InCli')
                eval(f'{ar}(args)')
          #      func = getattr(module, ar)
          #      func(args)

        if '-h' in argsIn:
            print()
            print("SFDX Commands:")
            print(" - sfdx force:org:list --verbose --all --> to list all authorized Orgs and Connection Status")
            print(" - sfdx auth:web:login -r 'Instance Url' -a 'Alias' --> to re-authorize")
            print(" - sfdx auth:web:login -u 'userName'  -a 'alias' --> to authorize and Org")
            print()

    except Exception as e:
        utils.printException(e)
        traceback.format_exc()

if __name__ == '__main__':
    main(sys.argv)

