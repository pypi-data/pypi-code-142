# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import
import os


import colemen_utils as c
from flask import Flask,redirect,url_for,request,Blueprint

import settings as _s
import modules.Log as _log

main = None

# def equari_api():
    


class Main:
    log:_log.Log = None
    def __init__(self):
        self.settings = {}
        self.data = {}
        self.force_run = False
        self.app = Flask(__name__)
        
    def prep(self):
        master_blueprint = Blueprint('master_blueprint', __name__)
        master_blueprint.register_blueprint(_auth.auth_blueprint)
        master_blueprint.register_blueprint(_home.home_blueprint)
        # master_blueprint.register_blueprint(_user.user_blueprint)
        # self.set_defaults()

        # @Mstep [] finally, register the master blueprint with flask.
        self.app.register_blueprint(master_blueprint)
    # def set_defaults(self):
        # self.settings = c.file.import_project_settings("__TITLE__.settings.json")

    def master(self):
        print("master")
        self.prep()
        # @Mstep [IF] if this is the main file.
        # This is necessary for use with pythonanywhere, otherwise it will cause a fatal error.
        if __name__ == '__main__' or self.force_run:
            # @Mstep [] run the development server.
            self.app.debug = True
            self.app.run()



# ------------------------- INSTANTIATE MAIN INSTANCE ------------------------ #
main = Main()
main.log = _log.Log()


# ----------------------------- IMPORT ALL ROUTES ---------------------------- #



import services.home.routes as _home
import services.auth.routes as _auth
# import services.auth.routes as _auth












if __name__ == '__main__':
    main.master()

