from platform import system

from AsyncPyWhatKit.ascii_art import image_to_ascii_art
from AsyncPyWhatKit.handwriting import text_to_handwriting
from AsyncPyWhatKit.mail import send_hmail, send_mail
from AsyncPyWhatKit.misc import info, playonyt, search, show_history, take_screenshot
from AsyncPyWhatKit.sc import cancel_shutdown, shutdown
from AsyncPyWhatKit.whats import (
    open_web,
    sendwhatmsg,
    sendwhatmsg_instantly,
    sendwhatmsg_to_group,
    sendwhatmsg_to_group_instantly,
    sendwhats_image,
)

_system = system().lower()
if _system in ("darwin", "windows"):
    from AsyncPyWhatKit.misc import take_screenshot

if _system == "windows":
    from AsyncPyWhatKit.remotekit import start_server