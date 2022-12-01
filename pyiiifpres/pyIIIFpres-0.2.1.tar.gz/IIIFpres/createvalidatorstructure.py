from . import iiifpapi3

manifestattr = dir(iiifpapi3.Manifest)
for i in manifestattr:
    if i.startswith('set_'):
        field = i.replace('set_','')
        print(f"assign(amanifest.{i},obj,'{field}')")
    if i.startswith('add_'):
        field = i.replace('add_','')
        print(f"validate_{field}(obj,amanifest)")


def printvalidation(obj,key):
    manifestattr = dir(obj)
    for i in manifestattr:
        if i.startswith('set_'):
            field = i.replace('set_','')
            print(f"assign({key}.{i},obj,'{field}')")
        if i.startswith('add_'):
            field = i.replace('add_','')
            print(f"validate_{field}(obj,{key})")
    for i in manifestattr:
        if i.startswith('add_'):
            field = i.replace('add_','')
            print(f"def validate_{field}(obj):")
            print(f"    pass")

printvalidation(iiifpapi3.Manifest,'amanifest')
    