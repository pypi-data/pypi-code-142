# Imports from other packages
import email
import logging
from email import utils
from email.message import Message
from typing import Optional, List, Callable

from imapclient import IMAPClient, SEEN
from imapclient.response_types import SearchIds

from .constans import EXCLUDED_FLAGS_FOLDERS
from .email_processing import write_txt_file
from .helpers import (
    calc_timeout,
    get_time,
)
from .structs import EmailListenerSettings

logger = logging.getLogger(__name__)


class EmailListener:
    folders: List = []

    __server: Optional[IMAPClient] = None
    __settings: EmailListenerSettings = None
    __func_is_double: Optional[Callable[[dict], bool]] = None

    def __init__(self, settings: EmailListenerSettings):
        self.__settings = settings
        self.__login()
        self.__prepare_folder()

    def scrape(self, folder: str = 'inbox', move=None, unread=False, delete=False):
        """
        Scrape unread emails from the current folder.
        A list of the file paths to each scraped email.
        :param folder:
        :param move:
        :param unread:
        :param delete:
        """
        self.__select_folder(folder, readonly=False)
        messages = self.__server.search("UNSEEN")
        return self.__processing(ids=messages, move=move, unread=unread, delete=delete)

    def get_all_msq(self, folder: str = 'Inbox', move=None, unread=False, delete=False,
                    func_check: Callable[[dict], bool] = None):
        logger.info('Getting all messages')
        self.__func_is_double = func_check
        self.__select_folder(folder, readonly=False)
        messages = self.__server.search()
        return self.__processing(ids=messages, move=move, unread=unread, delete=delete)

    def listen(self, timeout, process_func=write_txt_file, **kwargs):
        """Listen in an email folder for incoming emails, and process them.

        Args:
            timeout (int or list): Either an integer representing the number
                of minutes to timeout in, or a list, formatted as [hour, minute]
                of the local time to timeout at.
            process_func (function): A function called to further process the
                emails. The function must take only the list of file paths
                returned by the scrape function as an argument. Defaults to the
                example function write_txt_file in the email_processing module.
            **kwargs (dict): Additional arguments for processing the email.
                Optional arguments include:
                    move (str): The folder to move emails to. If not set, the
                        emails will not be moved.
                    unread (bool): Whether the emails should be marked as unread.
                        If not set, emails are kept as read.
                    delete (bool): Whether the emails should be deleted. If not
                        set, emails are not deleted.

        Returns:
            None

        """
        # Get the timeout value
        outer_timeout = calc_timeout(timeout)

        # Run until the timeout is reached
        while get_time() < outer_timeout:
            self.__idle(process_func=process_func, **kwargs)
        return

    def __processing(self, ids: SearchIds, *, move=None, unread=False, delete=False):
        answer = []
        for uid, message_data in self.__server.fetch(ids, 'RFC822').items():
            msg = self.__decode_email_message(uid, message_data)
            self.__execute_options(uid, move, unread, delete)
            if self.__func_is_double and not self.__func_is_double(msg) or not self.__func_is_double:
                answer.append(msg)
        return answer

    @staticmethod
    def __get_from(email_message: Message):
        """Helper function for getting who an email message is from.

        Args:
            email_message (email.message): The email message to get sender of.

        Returns:
            A string containing the from email address.

        """

        from_raw = email_message.get_all('From', [])
        from_list = utils.getaddresses(from_raw)
        if len(from_list[0]) == 1:
            return from_list[0][0]
        elif len(from_list[0]) == 2:
            return from_list[0][1]
        else:
            return "UnknownEmail"

    @staticmethod
    def __get_subject(email_message):
        # Get the subject
        subject = email_message.get("Subject")
        # If there isn't a subject
        return "No Subject" if subject is None else subject

    @staticmethod
    def __parse_multi_part_message(email_message: Message, val_dict):
        """Helper function for parsing multipart email messages.

        Args:
            email_message (email.message): The email message to parse.
            val_dict (dict): A dictionary containing the message data from each
                part of the message. Will be returned after it is updated.

        Returns:
            The dictionary containing the message data for each part of the
            message.

        """

        # For each part
        for part in email_message.walk():
            file_name = part.get_filename()
            if bool(file_name):
                attachment_list = val_dict.get("attachments") or []
                attachment_list.append({
                    "name": file_name,
                    "content": part.get_payload(decode=True)
                })
                val_dict["attachments"] = attachment_list
            elif part.get_content_type() == 'text/html':
                val_dict["HTML"] = part.get_payload()
            elif part.get_content_type() == 'text/plain':
                val_dict["Plain_Text"] = part.get_payload()

        return val_dict

    @staticmethod
    def __parse_single_part_message(email_message: Message, val_dict):
        """Helper function for parsing singlepart email messages.

        Args:
            email_message (email.message): The email message to parse.
            val_dict (dict): A dictionary containing the message data from each
                part of the message. Will be returned after it is updated.

        Returns:
            The dictionary containing the message data for each part of the
            message.

        """

        # Get the message body, which is plain text
        val_dict["Plain_Text"] = email_message.get_payload()
        return val_dict

    def __execute_options(self, uid, move, unread, delete):
        """Loop through optional arguments and execute any required processing.

        Args:
            uid (int): The email ID to process.
            move (str): The folder to move the emails to. If None, the emails
                are not moved. Defaults to None.
            unread (bool): Whether the emails should be marked as unread.
                Defaults to False.
            delete (bool): Whether the emails should be deleted. Defaults to
                False.

        Returns:
            None

        """

        # If the message should be marked as unread
        if bool(unread):
            self.__server.remove_flags(uid, [SEEN])

        # If a move folder is specified
        if move is not None:
            try:
                # Move the message to another folder
                self.__server.move(uid, move)
            except Exception as _:
                # Create the folder and move the message to the folder
                self.__server.create_folder(move)
                self.__server.move(uid, move)
        # If the message should be deleted
        elif bool(delete):
            # Move the email to the trash
            self.__server.set_gmail_labels(uid, "\\Trash")
        return

    def __idle(self, process_func=write_txt_file, **kwargs):
        """Helper function, idles in an email folder processing incoming emails.

        Args:
            process_func (function): A function called to further process the
                emails. The function must take only the list of file paths
                returned by the scrape function as an argument. Defaults to the
                example function write_txt_file in the email_processing module.
            **kwargs (dict): Additional arguments for processing the email.
                Optional arguments include:
                    move (str): The folder to move emails to. If not set, the
                        emails will not be moved.
                    unread (bool): Whether the emails should be marked as unread.
                        If not set, emails are kept as read.
                    delete (bool): Whether the emails should be deleted. If not
                        set, emails are not deleted.

        Returns:
            None

        """

        # Set the relevant kwarg variables
        move = kwargs.get('move')
        unread = bool(kwargs.get('unread'))
        delete = bool(kwargs.get('delete'))

        # Start idling
        self.__server.idle()
        print("Connection is now in IDLE mode.")
        # Set idle timeout to 5 minutes
        inner_timeout = get_time() + 60 * 5
        # Until idle times out
        while get_time() < inner_timeout:
            # Check for a new response every 30 seconds
            responses = self.__server.idle_check(timeout=30)
            print("Server sent:", responses or "nothing")
            # If there is a response
            if responses:
                # Suspend the idling
                self.__server.idle_done()
                # Process the new emails
                msgs = self.scrape(move=move, unread=unread, delete=delete)
                # Run the process function
                process_func(self, msgs)
                # Restart idling
                self.__server.idle()
        # Stop idling
        self.__server.idle_done()
        return

    def __check_folder_exists(self, folder):
        for el in map(lambda x: x['label'], self.folders):
            if el.upper() == folder.upper():
                return el
        raise ValueError(f'Invalid folder: {folder}')

    def __select_folder(self, folder: str, readonly: bool = False):
        self.__check_folder_exists(folder)
        self.__server.select_folder(folder, readonly=readonly)

    def __decode_email_message(self, uid, message_data):
        email_message = email.message_from_bytes(message_data[b'RFC822'])
        from_email = self.__get_from(email_message)
        logger.info(f"PROCESSING: Email UID = {uid} from {from_email}")
        val_dict = {"subject": self.__get_subject(email_message).strip(),
                    'headers': self.__extract_headers(email_message)}
        if email_message.is_multipart():
            val_dict = self.__parse_multi_part_message(email_message, val_dict)
        else:
            val_dict = self.__parse_single_part_message(email_message, val_dict)
        return val_dict

    def __extract_headers(self, message_data):
        return {key: self.__erase_header_value(value) for key, value in message_data.items()}

    @staticmethod
    def __erase_header_value(value):
        return value.strip().replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')

    def __prepare_folder(self):
        for el in self.__server.list_folders():
            self.folders.append(dict(zip(["label", "populate_name", "parent_name"], self.__extract_label(el))))

    @staticmethod
    def __extract_label(item) -> tuple:
        populate_name = item[-1]
        parent_name = item[1].decode()
        label = next((ell.decode() for ell in item[0] if ell not in EXCLUDED_FLAGS_FOLDERS), populate_name)
        return label, populate_name, parent_name

    def __login(self):
        self.__server = IMAPClient('imap.gmail.com')
        self.__server.login(self.__settings.email, self.__settings.password)
        # self.__server.select_folder(self.__settings.folder, readonly=False)

    def __logout(self):
        self.__server.logout()
        self.__server = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__logout()
