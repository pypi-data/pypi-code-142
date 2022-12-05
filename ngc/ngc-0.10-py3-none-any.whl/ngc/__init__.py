
import os
import sys
import shutil
import re
import json
import csv
import urllib
import html
import requests

def dirlist(path, ext="", containDir=False, depth=1,pureFilename=False):
    '''
    traverse folder
    '''
    if type(path) is list:
        return path
    allfiles=[]
    rsl=os.walk(path, topdown=True)
    for root, dirs, files in rsl:
        if depth<0 or root.replace(path,"").count("\\")<depth:
            for name in files:
                if name.endswith(ext):
                    if pureFilename:
                        allfiles.append(name)
                    else:
                        allfiles.append(os.path.join(root, name).replace("\\","/"))
            if containDir:
                for name in dirs:
                    if pureFilename:
                        allfiles.append(name)
                    else:
                        allfiles.append(os.path.join(root, name).replace("\\","/"))
    return allfiles

def getline(lines,noret = None):
    '''
    yield line from lines
    '''
    for line in lines:
        yield line
    while True:
        yield noret

## OS
makedir = os.makedirs
'''os make directory'''
getdir=lambda src:os.path.split(src)[0]
'''get dirname of file'''
getname = lambda src,incsuff=True:os.path.split(src)[1] if incsuff else os.path.splitext(os.path.split(src)[1])[0]
'''get filename'''
copyfile = lambda srcfile, dstfile,force=False:shutil.copyfile(srcfile,dstfile) if not os.path.exists(dstfile) or force else None
'''copy file'''
copydir = lambda srcdir,dstdir,force=False:list(makedir(y) if os.path.isdir(x) else copyfile(x,y,force) for [x,y] in dirstruct_copy(srcdir,dstdir))
'''copy directory'''
copy = lambda src,dst,force=False:copyfile(src,dst,force) if os.path.isfile(src) else copydir(src,dst,force)
'''copy file or directory'''
dirstruct_copy=lambda srcdir,dstdir: list([x,x.replace(srcdir,dstdir)] for x in dirlist(srcdir,containDir=1,depth=-1))
'''return the same path list replaced'''
rename = os.rename
'''rename'''
PathAdd = lambda src,ex = "_new":os.path.join(os.path.split(src)[0] + ex, os.path.split(src)[1])
'''replace to directory-relative pathname'''
NameAdd = lambda src,ex = "_new":os.path.join(os.path.splitext(src)[0]+ex, os.path.splitext(src)[1])
'''replace to filename-relative pathname'''

## file
filenameFormat = lambda x:[list(x:=x.replace(z,'') for z in '\\/:*?"<>|'),x][1]
'''format filename'''
readfile = lambda src,srccoding="utf-8" : open(src,"rb").read().decode(srccoding)
'''read text file content'''
writefile = lambda cnt,dst,dstcoding="utf-8" : open(dst,"wb").write(cnt.encode(dstcoding))
'''write text file content'''
readalllines = lambda src,srccoding="utf-8": open(src,'r',encoding=srccoding).read().splitlines()
'''read text file content to lines'''
writealllines = lambda lines,src,srccoding="utf-8": open(src,'w',encoding=srccoding).writelines(lines)
'''write text lines to file'''
jsonload = lambda src,srccoding="utf-8" : json.load(open(src, "r", encoding=srccoding))
'''load json from file'''
jsondump = lambda dic,dst,srccoding='utf-8',sort=False : json.dump(dic, open(dst, "w", encoding=srccoding), ensure_ascii=False, sort_keys=sort, indent=4)
'''dump json to file'''
csvload = lambda src,srccoding='utf-8',dem=',' : list(csv.reader(open(src, "r", encoding=srccoding),delimiter=dem))
'''load double list from csv file'''
csvdump = lambda dic,dst,srccoding='utf-8-sig',dem=',' : csv.writer(open(dst, 'w', encoding=srccoding),delimiter=dem).writerows(dic)
'''dump double list to csv file'''
loadFileHex = lambda src:list(open(src,'rb').read())
'''load hex list from binary file'''
dumpFileHex = lambda iter,dst:open(dst,'wb').write(bytes(iter))
'''dump hex list to binary file'''

## calculate
between = lambda x,a,b: x>=a and x<=b
'''whether a <= x <= b'''

## string solve
replaceAll = lambda x, replis:[list(x:=x.replace(y[0],y[1]) for y in replis),x][1]
'''replace item from double list'''
afterDecodeSJIS = lambda x, replis:[list(x:=x.replace(y[0],y[1]) for y in [['〜','～'],['‖','∥'],['−','－']]),x][1]
'''fix sjis content read with python'''
beforeEncodeSJIS = lambda x, replis:[list(x:=x.replace(y[0],y[1]) for y in [['·','・'],['～','〜'],['∥','‖'],['－','−']]),x][1]
''''''
is_En = lambda char : char >= '\u0000' and char <= '\u007F'
'''is a char ascii'''
is_enline = lambda line : not sum(not is_En(ch) for ch in line)
'''is a string ascii'''
strQ2B = lambda ustring : ''.join(list(chr(ord(u)-65248 if between(u,32+65248,126+65248) else u) if u!='　' else ' ' for u in ustring))
'''convert full width to half width'''
strB2Q = lambda ustring : ''.join(list(chr(ord(u)+65248 if between(u,32,126) else u) if u!=' ' else '　' for u in ustring))
'''convert half width to full width'''

## struct
prlis = lambda lis:list(print(x) for x in lis)
'''print item from list'''
mergeDict = lambda d1, d2:d1.copy().update(d2)
'''merge dict'''
cvtLis2Dic = lambda lis1,lis2 : dict([[x[0],x[1]] for x in list(zip(lis1,lis2))])
'''convert list to dict'''
revertDic = lambda dic: dict([[v,k] for k, v in dic.items()])
'''revert dict item'''
flipLis = lambda lis: list(x.reverse() for x in lis)
'''revert double list'''
sortList = lambda lis,i=1,rev=False : sorted(lis, key=(lambda x: x[i]),reverse=rev) if type(lis) is list else lis
'''sort list with item'''
sortLisDict = lambda dic,rev=False : sorted(dic.items(), key=lambda d: d[1], reverse=rev) if type(dic) is dict else dic
'''sort dict with value'''
fLoop = lambda func,argvs:[list(x:=func(x,z) for z in argvs),x][1]
'''loop function with iterator'''
cvtCsv2Dic = lambda lines : dict(list([line[0],dict(list([lines[0][i+1],v] for i,v in enumerate(line[1:])))] for line in lines[1:]))
'''convert csv's double list to dict'''

## web solve
url_encode = urllib.parse.quote
'''urllib.parse.quote'''
url_decode = urllib.parse.unquote
'''html.escape'''
html_encode = html.escape
'''html.escape'''
html_decode = html.unescape
'''html.unescape'''
downloadDic = lambda url,data={}: json.loads(requests.post(url,data).text)
'''get dict from url posted'''
download = lambda url,dst : open(dst, "wb").write(requests.get(url).content)
'''download file from url got'''

if __name__=='__main__':
    pass
