# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import






from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Apricity test"



# class Main:
#     def __init__(self):
#         self.settings = {}
#         self.data = {}
#         self.set_defaults()

#     def set_defaults(self):
#         self.settings = c.file.import_project_settings("__TITLE__.settings.json")

#     def master(self):
#         print("master")


# if __name__ == '__main__':
#     m = Main()
#     m.master()

if __name__ == '__main__':
    app.run()

