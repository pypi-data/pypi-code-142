import sys, traceback
from jennie.events.exceptionhandler import ExceptionHanlder
from jennie.events.setup.setup import Setup
from jennie.events.colorprinting import ColorPrinting
from jennie.events.utils.logger import LogginMixin
from jennie.events.utils.command_handler import map_inputs
from jennie.protocols import AutomationHelper, UILibHelper, UbuntuAutomation
from jennie.events.constants import KEY_STACK_ANGULAR_UI_LIB, \
    KEY_STACK_ANGULAR_AUTOMATION, KEY_STACK_DJANGO_AUTOMATIONS

def check_login_state(logger):
    setup_controller = Setup(logger)
    is_user_logger_in = False
    userinfo = setup_controller.get_logged_in_user()
    if userinfo != None:
        is_user_logger_in = True
    return userinfo, is_user_logger_in, setup_controller

def init_session():
    commands = sys.argv[1:]
    final_command_list = []
    debug = False
    for command in commands:
        if command == "--v" or command == "--verbose":
            debug = True
        else:
            final_command_list.append(command)

    logger = LogginMixin(debug)
    return logger, final_command_list

def execute_for_logged_in_user(userinfo, setup_controller, logger, commands):
    updated_command_list = map_inputs(commands)
    logger.debug ("User Info : ", userinfo)
    logger.debug ("Final Command List ", {"args": updated_command_list})

    if updated_command_list[0] == "logout":
        logger.debug ("Logout from jennie")
        return setup_controller.logout()

    elif updated_command_list[0] == "version" or  updated_command_list[0] == "--version":
        return  setup_controller.show_version()

    # print ("Running commands", updated_command_list)

    elif updated_command_list[0] == "ubuntu":
        return UbuntuAutomation().execute(commands)

    if len(updated_command_list) < 2:
        raise Exception ("Invalid Command {}".format(" ".join(commands)))

    elif updated_command_list[0] == "angular" and updated_command_list[1] == "ui-lib":
        resp = UILibHelper(
            library_type= KEY_STACK_ANGULAR_UI_LIB, args=updated_command_list[2:],
            logger=logger, user_info=userinfo
        ).execute

        return resp

    elif updated_command_list[0] == "angular" and updated_command_list[1] == "automations":
        resp = AutomationHelper(
            library_type=KEY_STACK_ANGULAR_AUTOMATION, args=updated_command_list[2:],
            logger=logger, user_info=userinfo
        ).execute

    elif updated_command_list[0] == "django" and updated_command_list[1] == "automations":
        resp = AutomationHelper(
            library_type=KEY_STACK_DJANGO_AUTOMATIONS, args=updated_command_list[2:],
            logger=logger, user_info=userinfo
        ).execute
    else:
        raise Exception ("Invalid Command {}".format(" ".join(commands)))

def execute_for_unknowns(setup_controller, commands):

    if len(commands)  > 0:
        if commands[0] == "setup":
            if len(commands) > 1:
                user_email = commands[1]
            else:
                user_email = input("Enter Email Address >> ")
            return setup_controller.setup(user_email)

        elif commands[0] == "version" or commands[0] == "--version":
            return setup_controller.show_version()

    print ("User not logged in, To use jennie kindly login to the software.\n"
       "To Login use command"
       "\n\n\tjennie setup <user-email>\n"
       "Once logged in user can continue using jennie")

def run():
    logger, commands = init_session()
    userinfo, is_user_logger_in, setup_controller = check_login_state(logger)
    logger.debug("Login Status : " + str(is_user_logger_in))
    exception = None
    try:
        if is_user_logger_in:
            exception = ExceptionHanlder(userinfo["token"])
            execute_for_logged_in_user(userinfo, setup_controller, logger, commands=commands)
        else:
            execute_for_unknowns(setup_controller, commands=commands)
    except Exception as e:
        if exception != None:
            exception.handle_error(e, traceback.format_exc(), commands)
            logger.save_session()
        else:
            color_printinglogger = ColorPrinting()
            color_printinglogger.error(str(traceback.format_exc()))

    logger.save_session()