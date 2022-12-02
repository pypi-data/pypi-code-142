# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import
import os


# import colemen_utils as c
# import globe
from flask import Flask,Blueprint





class Main:
    '''
        The wrapping class for control the setup of the Flask instance and its routes.

        ----------


        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-02-2022 08:11:08
        `memberOf`: apricity_labs
        `version`: 1.0
        `method_name`: Main
        * @TODO []: documentation for Main
    '''
    force_run:bool = False
    '''If True the development server will be ran\n
        If this is done on the production server, it will throw a fatal error.
    '''
    app:Flask = None
    '''The Flask application instance'''

    def __init__(self):
        self.settings = {}
        self.data = {}
        self.force_run = False
        self.app = Flask(__name__)

    def prep(self):
        master_blueprint = Blueprint('master_blueprint', __name__)
        # master_blueprint.register_blueprint(_services.auth_blueprint)
        # master_blueprint.register_blueprint(_acc.acc_blueprint)

        for bp in services.blue_prints:
            # print(f"bp:{bp}")
            master_blueprint.register_blueprint(bp)

        # @Mstep [] finally, register the master blueprint with flask.
        self.app.register_blueprint(master_blueprint)
        print(self.app.url_map)

    # def set_defaults(self):
        # self.settings = c.file.import_project_settings("__TITLE__.settings.json")

    def start(self):
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
# MAIN.log = a.objects.Log.Log()
# main = main
# LOG = main.log

# ----------------------------- IMPORT ALL ROUTES ---------------------------- #


from apricity import *

# import apricity.services.home.routes as _home
# import apricity.services as _services

# import apricity.services.account.routes as _acc
# import services.auth.routes as _auth





def start():
    main.start()








if __name__ == '__main__':
    main.start()

