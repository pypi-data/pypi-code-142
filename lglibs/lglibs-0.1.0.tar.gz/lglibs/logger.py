from . import color
import json
import sys
import os

Info = info = INFO = 0
Warning = warning = WARNING = 1
Error = error = ERROR = 2

_config = \
{
    "default-level": None,
    "Info-Rendering-end": color.green,
    "disInfo-Rendering-end": color.green.dark,
    "Warning-Rendering-end": color.yellow.normal,
    "disWarning-Rendering-end": color.yellow.dark,
    "Error-Rendering-end": color.red.normal,
    "disError-Rendering-end": color.red.dark,
    "messages-Warning": color.yellow.normal,
    "messages-Error": color.red.normal,
    "Info-head": color.green,
    "Warning-head": color.yellow.normal,
    "Error-head": color.red.normal
}

class __config__:
    def __init__(self):
        self.default_level = _config["default-level"]
        self.Info_Rendering_end = _config["Info-Rendering-end"]
        self.disInfo_Rendering_end = _config["disInfo-Rendering-end"]
        self.Warning_Rendering_end = _config["Warning-Rendering-end"]
        self.disWarning_Rendering_end = _config["disWarning-Rendering-end"]
        self.Error_Rendering_end = _config["Error-Rendering-end"]
        self.disError_Rendering_end = _config["disError-Rendering-end"]
        self.messages_Warning = _config["messages-Warning"]
        self.messages_Error = _config["messages-Error"]
        self.Info_head = _config["Info-head"]
        self.Warning_head = _config["Warning-head"]
        self.Error_head = _config["Error-head"]

    def set_Rendering(self, level, color, dark=None):
        if level == INFO:
            self.Info_Rendering_end = color
            self.Info_head = color
            if dark is not None:
                self.disInfo_Rendering_end = dark
        elif level == WARNING:
            self.Warning_Rendering_end = color
            self.Warning_head = color
            self.messages_Warning = color
            if dark is not None:
                self.disWarning_Rendering_end = dark
        elif level == ERROR:
            self.Error_Rendering_end = color
            self.Error_head = color
            self.messages_Error = color
            if dark is not None:
                self.disError_Rendering_end = dark
        else: Log("set Readering Error, existing level ({}, {}, {})".format("INFO", "WARNING", "ERROR"), level=ERROR)
    
    def save(self, path="./", file_name="config.json"):
        old_config = Logger.get.config()
        Logger.set.config(self)
        for key, value in _config.copy().items():
            if _config[key] is None: _config[key] = ""
            try: _config[key] = value.__str__()
            except: continue
        with open(os.path.join(path, file_name), "w") as file:
            json.dump(_config, file, indent=4)
        Logger.set.config(old_config)
    
    def load(self, path="./config.json", auto_set=False):
        with open(path, "r") as file:
            load_config = json.load(file)
        if auto_set: 
            for key, value in load_config.copy().items():
                if bool(value) is False: # 为了增强可读性，将其写成是False
                    load_config[key] = None
            Logger.set.config_dict(load_config)
        else: 
            for key, value in load_config.copy().items():
                if bool(value) is False: # 为了增强可读性，将其写成是False
                    load_config[key] = None
            return load_config

class Logger:
    Logged_Info = 0
    Logged_Warning = 0
    Logged_Error = 0
    class set:
        @staticmethod
        def renderer(level, color, dis=False):
            setting_obj = None
            if level == INFO:
                if dis: setting_obj = "disInfo-Rendering-end"
                else: setting_obj = "disInfo-Rendering-end"
            if level == WARNING:
                if dis: setting_obj = "disWarning-Rendering-end"
                else: setting_obj = "Warning-Rendering-end"
            if level == ERROR:
                if dis: setting_obj = "disError-Rendering-end"
                else: setting_obj = "Error-Rendering-end"
            _config[setting_obj] = color
        def config(config):
            _config["default-level"] = config.default_level
            _config["Info-Rendering-end"] = config.Info_Rendering_end
            _config["disInfo-Rendering-end"] = config.disInfo_Rendering_end
            _config["Warning-Rendering-end"] = config.Warning_Rendering_end
            _config["disWarning-Rendering-end"] = config.disWarning_Rendering_end
            _config["Error-Rendering-end"] = config.Error_Rendering_end
            _config["disError-Rendering-end"] = config.disError_Rendering_end
            _config["messages-Warning"] = config.messages_Warning
            _config["messages-Error"] = config.messages_Error
            _config["Info-head"] = config.Info_head
            _config["Warning-head"] = config.Warning_head
            _config["Error-head"] = config.Error_head
        def config_dict(dict_config):
            # 危险行为
            global _config
            _config = dict_config
            
    class get:
        @staticmethod
        def config() -> __config__:
            return __config__()
        def config_dict() -> dict:
            return _config
            
            
class Echo_Mode(object):
    @staticmethod
    def JsonWriter(message, indent=4, **kwargs):
        return json.dumps(message, indent)
    @staticmethod
    def InfoWriter(message, **kwargs):
        if kwargs["messages_type"] == list:
            output_content = str()
            for item in message:
                output_content += str(item) + " "
            return output_content
        else:
            output_content = str()
            for key, value in message.values():
                output_content += f"{key}: {value}\n"
            return output_content

def _Messages_color():
    if not Logger.Logged_Info: Info_color = _config["disInfo-Rendering-end"]
    else: Info_color = _config["Info-Rendering-end"]
    
    if not Logger.Logged_Warning: Warning_color = _config["disWarning-Rendering-end"]
    else: Warning_color = _config["Warning-Rendering-end"]
    
    if not Logger.Logged_Error: Error_color = _config["disError-Rendering-end"]
    else: Error_color = _config["Error-Rendering-end"]
    
    return Info_color, Warning_color, Error_color

def _ColorJoin(render):
    return f"{render[0]}info{color.off}: {render[0]}{Logger.Logged_Info}{color.off}, {render[1]}warning{color.off}: {render[1]}{Logger.Logged_Warning}{color.off}, {render[2]}error{color.off}: {render[2]}{Logger.Logged_Error}{color.off}"

def Log(messages, level=None, writer=Echo_Mode.InfoWriter, **kwargs):
    if "write-mode" not in kwargs: write = sys.stdout.write
    else: write = kwargs["write-mode"]
    if "flush-mode" not in kwargs: flush = sys.stdout.flush
    else: flush = kwargs["flush-mode"]
    if "upper" not in kwargs: upper = True
    else: upper = kwargs["upper"]

    if _config["default-level"] is None: _config["default-level"] = INFO
    if level is None: level = _config["default-level"]
    
    if level == INFO: Logger.Logged_Info += 1
    if level == WARNING: Logger.Logged_Warning += 1
    if level == ERROR: Logger.Logged_Error += 1
    
    level_color = {
        INFO: _config["Info-head"] + "INFO" + color.off,
        WARNING: _config["Warning-head"] + "WARNING" + color.off,
        ERROR: _config["Error-head"] + "ERROR" + color.off
    }[level]
    
    if not upper: level_color = level_color.lower()
    
    if type(messages) in (list, dict):
        render = _Messages_color()
        show_type = {list: "List", dict: "Dictionaries"}[type(messages)]
        write(f"[{level_color}]: {show_type} Information - {_ColorJoin(render)}\n")
        flush()
        write("List: " + writer(messages, messages_type=type(messages)) + "\n")
        flush()
    
    else:
        render = _Messages_color()
        if "WARNING" in level_color:
            messages = _config["messages-Warning"] + messages + color.off
        if "ERROR" in level_color:
            messages = _config["messages-Error"] + messages + color.off
        write(f"[{level_color}]: {messages} - {_ColorJoin(render)}")
        flush()
        write("\n")
        flush()


