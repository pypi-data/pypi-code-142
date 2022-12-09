from mixpanel import Mixpanel
from polly.constants import MIXPANEL_KEY


class Track:
    """
    This class is used for tracking polly-python services using mixpanel.
    This class will have a unidirectional association relationship with the class which wants to use the tracking service.
    The track function sends the logs to mixpanel.
    For using this feature, make an object in the __init__ function for the class this feature is to be used,
    then use the track function with that object.
    """

    def track_decorator(function):
        def wrapper_function(*args, **kwargs):
            execution_flag = False
            try:
                result = function(*args, **kwargs)
                execution_flag = True
            except Exception as e:
                returned_err = e
            obj = args[0].session
            user_id = obj.user_details.get("user_id")
            properties = {}
            # checking if args is not empty(contains self object apart from arguments)
            if len(args) > 1:
                args_list = []
                for index in range(1, len(args)):
                    args_list.append(args[index])
                properties["arguments"] = args_list
            # checking if kwargs exist
            if kwargs:
                for key, value in kwargs.items():
                    properties[key] = value
            properties["execution_status"] = execution_flag
            mp = Mixpanel(MIXPANEL_KEY)
            mp.track(user_id, function.__name__, properties)
            if execution_flag:
                if result is not None:
                    return result
            else:
                raise returned_err

        return wrapper_function
