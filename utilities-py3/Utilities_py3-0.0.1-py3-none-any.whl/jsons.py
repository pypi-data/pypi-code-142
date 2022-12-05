import json

def save_json(js: dict, name: str) -> str:
    file = open(name,"w")
    json.dump(js,file)
    file.close()
    return name
read_json = lambda name: json.loads(open(name).read())