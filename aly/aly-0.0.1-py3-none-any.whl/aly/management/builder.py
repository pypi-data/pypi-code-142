import os,re,keyword
from aly.bot import TeleBot

class Builder:

    def __init__(self,name):
        self.name = name

    @classmethod
    def create_settings(cls,project_name,path=f"{os.getcwd()}\\"):
        if path == f"{os.getcwd()}\\":
            path += project_name
        
        settings_file = ""
        settings_structure = ""

        # Read SETTINGS structure
        with open(f"{os.path.dirname(os.path.realpath(__file__))}\\structure\\settings.py") as f:
            settings_structure += f.read()

        
        exists = os.path.exists(f"{path}\\settings.py")
        if not exists:
            with open(f"{path}\\settings.py","w") as file:
                file.write(settings_structure)
            settings_file = settings_structure
        else:
            with open(f"{path}\\settings.py") as file:
                settings_file += file.read()
        
                
        return (settings_file,settings_structure)

    @classmethod
    def create_app(cls,project_name,path=f"{os.getcwd()}\\"):
        if path == f"{os.getcwd()}\\":
            path += project_name
        
        app_file = ""
        app_stucture = ""

        # Read MAIN structure
        with open(f"{os.path.dirname(os.path.realpath(__file__))}\\structure\\app.py") as f:
            app_stucture += f.read()
        
        exists = os.path.exists(f"{path}\\app.py")

        if not exists:        
            with open(f"{path}\\app.py","w") as file:
                file.write(app_stucture)
            app_file = app_stucture
        else:
            with open(f"{path}\\app.py") as file:
                app_file += file.read()
        
            
        return (app_file,app_stucture)
 
    @classmethod
    def create_manage(cls,project_name, path=f"{os.getcwd()}\\"):
        if path == f"{os.getcwd()}\\":
            path += project_name

        manage_structure = ""

        # Read manage.py structure
        with open(f"{os.path.dirname(os.path.realpath(__file__))}\\structure\\manage.py") as f:
            manage_structure += f.read()

        if path.split("\\")[-1] == project_name:

            # Edit manage.py structure variables
            manage_structure = manage_structure.format(project_name=project_name)

            # Create or Edit manage.py file in the project
            with open(f"{path}\\manage.py","w") as file:
                file.write(manage_structure)
        else:
            print("\x1b[1;31m\nError: Make sure you are in the project directory\x1b[1;37m")
            
        return manage_structure
 
    @classmethod
    def build_project(cls,name):
        if not keyword.iskeyword(name):
            if name.isidentifier():
                try:
                    os.mkdir(f'{os.curdir}/{name}')

                    # Create SETTINGS file
                    settings_file,settings_structure = cls.create_settings(name)

                    # Create MAIN file
                    app_file,app_stucture = cls.create_app(name)

                    # Create manage.py
                    manage_structure = cls.create_manage(name)

                    return cls(name)
                except FileExistsError:
                    print("\x1b[1;31m\nError: There is a folder with the same name exists in this directory\x1b[1;37m")
            else:
                print("\x1b[1;31m\nError: Invalid name does not match python variable naming conventions\x1b[1;37m")
        else:
            print("\x1b[1;31m\nError: Invalid name you can not use python keywords as a project name\x1b[1;37m")

    @classmethod
    def check_input(cls,input_msg,error_msg):
        var = input(input_msg)
        while var == "" or var == None:
            print(f"\x1b[1;31m * Error: {error_msg} \x1b[1;37m")
            var = input(input_msg)
        return var

    def add_bot_in_app(self,bot_name,path):
        new_bot = ""
        with open(f"{os.path.dirname(os.path.realpath(__file__))}\\structure\\new_bot.py") as f:
            new_bot += f.read()

        new_bot = new_bot.format(bot_name=bot_name)

        # Edit MAIN file
        app_file,app_stucture = self.create_app(self.name,path)
        with open(f"{path}\\app.py","w") as file:
            file.write(app_file+"\n\n"+new_bot)

    def add_bot_in_settings(self,bot_name,tokens,path):
        # Edit SETTINGS file
        settings_file,settings_structure = self.create_settings(self.name,path)

        with open(f"{path}\\settings.py","w") as file:
            lines = settings_file.splitlines()
            new_code = ""

            for l in lines:
                if "TOKENS" in l and "BOTS" not in l:
                    l = re.sub(r"\{.*?\}|{}",str(tokens) , l)

                elif "BOTS" in l:
                    bots = re.findall(r"\{.*?\}|{}",l)[0][0:-1]
                    comma = ", "
                    if len(bots) == 1:
                        comma = ""

                    l = "BOTS = " + bots + comma

                    l += f"'{bot_name}': TeleBot('{bot_name}',TOKENS['{bot_name}'])" + "}"

                new_code += l+"\n"
                
            file.write(new_code)

    def new_bot(self,BOTS,TOKENS,path):
        bot_name = self.check_input("Bot Name: ","You must write bot name").lower()
        bot_name = self.validate(bot_name,BOTS)
        token = self.check_input("Bot token: ","You must write bot token")

        TOKENS.update({bot_name:token})
        self.add_bot_in_settings(bot_name,TOKENS,path)
        self.add_bot_in_app(bot_name,path)
        return bot_name,token

    # Set webhook
    def set_webhook(self,BOTS):
        bot_name = self.check_input("Bot Name U want to hook: ","You must write bot name").lower()

        while bot_name not in BOTS.keys(): 
            print(f"\x1b[1;31m * Error: This bot doesn't exist in this project try another one \x1b[1;37m")
            bot_name = input("Bot name U want to hook: ")

        
        webhook_url = self.check_input("Web hook url: ","You must write Web hook url")

        r = BOTS[bot_name].set_webhook(webhook_url)

        # Check webhook status
        if r.status_code != 200:
            print(
                f"\x1b[1;31m * Status:"+ str(r.status_code) +" \n * Error:token is not true or website link \x1b[1;37m")
        else:
            print(f"\x1b[1;32m * Status:"+ str(r.status_code) +" \n * OK \x1b[1;37m")
    
    # Validate name
    def validate(self,bot_name,BOTS):
        # Check if there is a bot with same name
        for bot in BOTS.keys():
            while bot_name == bot:
                print("\x1b[1;31m\nError: You can't use the same bot name again in the same project\x1b[1;37m\n")
                bot_name = input("Bot name: ")
        
        # Check if name matches python variable naming conventions
        while not bot_name.isidentifier():
            print("\x1b[1;31m\nError: Invalid name does not match python variable naming conventions so try another one \x1b[1;37m\n")
            bot_name = input("Bot name: ")

        return bot_name
