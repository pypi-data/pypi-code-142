class DBUtilsSecrets:

    def get(self, **kwargs):
        # print("calling DBUtilsSecrets.get func from dummy dbutils package, and no operation performed.")
        pass

class DBUtilsWidgets:

    def removeAll(self):
        # print("calling DBUtilsWidgets.removeAll func from dummy dbutils package, and no operation performed.")
        pass

    def text(self, *args):
        # print("calling DBUtilsWidgets.text func from dummy dbutils package, and no operation performed.")
        pass

    def get(self, *args):
        # print("calling DBUtilsWidgets.get func from dummy dbutils package, and no operation performed.")
        pass


class DButilsFunctions:

    def ls(self, dir: str):
        # print("calling DButilsFunctions.ls func from dummy dbutils package, and no operation performed.")
        pass

    def mkdirs(self, dir: str):
        # print("calling DButilsFunctions.mkdirs func from dummy dbutils package, and no operation performed.")
        pass

    def mv(self, src: str, tgt: str):
        # print("calling DButilsFunctions.mv func from dummy dbutils package, and no operation performed.")
        pass

    def mounts(self):
        return []

    def mount(self, **kwargs):
        pass 

class DBUtils:

    def __init__(self):
        self.fs = DButilsFunctions()
        self.widgets = DBUtilsWidgets()
        self.secrets = DBUtilsSecrets()

dbutils = DBUtils()

# dbutils.fs.ls("dir")
# dbutils.fs.mkdirs("dir")
# dbutils.fs.mv("src", "tgt")

scope_name = "abd"
key = "acd"
dbutils.secrets.get(scope = f"{scope_name}", key = f"{key}")

