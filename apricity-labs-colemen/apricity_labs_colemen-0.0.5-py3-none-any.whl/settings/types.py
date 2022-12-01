




from typing import TypeVar as _TypeVar
from typing import Union as _Union
from typing import Iterable as _Iterable
from typing import TYPE_CHECKING
# from dataclasses import dataclass, field
# from typing import List,Dict
# import modules.Log as _log

# from modules.ControlPanel import ControlPanel as _control_panel

INFLECT_ENGINE = None


_config = None
_main_type = None
_log_type = None
_database_type = None
_result_type = None
_request_type = None
_response_type = None




# ControlPanel = _control_panel.ControlPanel()

if TYPE_CHECKING:
    import modules.Database as _db
    _database_type = _TypeVar('_database_type', bound=_db.Database)
    # import modules.Result as _result
    # _result_type = _TypeVar('_result_type', bound=_result.Result)


    # import modules.Request as _request
    # _request_type = _TypeVar('_request_type', bound=_request.Request)


    # import modules.Response as _response
    # _response_type = _TypeVar('_response_type', bound=_response.Response)

    import main as _main
    _main_type = _TypeVar('_main_type', bound=_main.Main)

    import modules.Log as _log
    _log_type = _TypeVar('_log_type', bound=_log.Main)






