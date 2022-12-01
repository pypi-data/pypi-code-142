from PenguinServices import openFile

class Identifiers:
    def __init__(self):
        self.getGroupIds()
        self.getUserIds()

    def getVal(self, line, slots = [0, 2]):
        line = line.split(":")
        return line[slots[0]], line[slots[1]]

    def getGroupIds(self):
        self.groupId2Name = {}
        self.name2GroupId = {}
        
        for line in openFile("/etc/group"):
            key, val = self.getVal(line)
            self.groupId2Name[val] = key
            self.name2GroupId[key] = val

    def getUserIds(self):
        self.userId2Name = {}
        self.name2UserId = {}

        for line in openFile("/etc/passwd"):
            key, val = self.getVal(line)
            self.userId2Name[val] = key
            self.name2UserId[key] = val

    # options: user or group
    # findName = True means you want the name
    def translate(self, key, option = "user", findName = True):
        try:
            if option == "user":
                if findName:
                    return self.userId2Name[key]
                else:
                    return self.name2UserId[key]
            else:
                if findName:
                    return self.groupId2Name[key]
                else:
                    return self.name2GroupId[key]
        except:
            return f"Could not find the key, {key}, based on the search parameters you chose!"
