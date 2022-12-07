import hashlib


########################
#DESCRIPTION
#This module obfuscates all predefined personal data of LPLUS REST responses and returns an anonymized response
#The obfuscation method deployes SHA256 algorithm. This one-way encryption ensures irreversable obfuscation of personal data.

#LICENSE
#MIT License

#Copyright (c) 2022 Nils Hernes

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
######################


def traversing_nested_lists(json_response,data_to_obfuscate):
    nested_dict=json_response

    if isinstance(nested_dict,dict):
        for key,item in nested_dict.items():
            if isinstance(item,list) and item==True:
                traversing_nested_lists(item[0],data_to_obfuscate) #When the item to the key is a nested dictionary itself, the function calls itself to access the next layer
            else:
                if key in data_to_obfuscate: #check if dictionary key is part of data to obfuscate
                    item_encrypted=encryption(item) #when true: item to the key gets encrypted
                    nested_dict[key]=item_encrypted #new item to key gets written in the response

def encryption(item):
    item=item

    if isinstance(item,type(None)) or item=="None" or item=="": #Check if item to key contains personal data
        return item #if not, the item is returned unencrypted

    elif isinstance(item,str): #check if item is text string
        item_bytes=bytes(item, 'utf-8')  #string is turned into bytes
    
    elif isinstance(item,int): #check if item is integrer
        item=str(item) #To turn data into hashable bytes, integers are turned into text
        item_bytes=bytes(item,'utf-8') #string is turned into bytes

    print(item_bytes)
    item_encrypted = hashlib.sha256(item_bytes).hexdigest() #item is encrypted with SHA256 algorithm

    return item_encrypted #encrypted item is returned

def obfuscate(rest_response):
    rest_response=rest_response

    data_to_obfuscate=("userName","password","firstName","lastName","dateOfBirth","gender","salutation","title","nativeFirstName","nativeLastName","isoCountryOfBirth","dateOfBirth","cityOfBirth","email","emailConfirmed","street","zipCode","city","pId1","pId2","importKey","photoIdentificationType","identityNumber","idCardIssueDate","passportPhotoFileName","passportPhotoFileData","phone","fax","isoCountry","insuranceNumber","insuranceCompanyLocation","insuranceCompanyName","uasOperatorId","operatorType","reviewerName","managerName","managerName2","ssoUrl") #Define keys to be obfuscated
    
    if isinstance(rest_response,dict): #Some responses are not packed into list. In this instance, the dict is wrapped in a list
        rest_response=[rest_response]

    if isinstance(rest_response,list): 
        json_response=rest_response

        for eintrag in json_response: #The function iterates over the response
            traversing_nested_lists(eintrag,data_to_obfuscate) #This function iterates over all dictionary entries of the REST response

    else:
        return rest_response

    return json_response