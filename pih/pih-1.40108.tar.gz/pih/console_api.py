import importlib.util
import sys

pih_is_exists = importlib.util.find_spec("pih.pih") is not None
if not pih_is_exists:
    sys.path.append("//self.pih/facade")

from pih import PIH, NotFound, ActionValue, ActionStack
from pih.tools import EnumTool, FullNameTool
from pih.collection import Mark, User, FullName, MarkDivision, UserContainer, LoginPasswordPair
from pih.const import CONST, MarkType, PASSWORD


class ConsoleAppsApi:

    def __init__(self, pih: PIH = None):
        self.pih = pih or PIH
        self.full_name: FullName = None
        self.tab_number: str = None
        self.telephone_number: str = None
        self.division_id: int = None
        self.user_is_exists: bool = False
        self.login: str = None
        self.password: str = None
        self.internal_email: str = None
        self.external_email: str = None
        self.email_password: str = None
        self.polibase_login: str = None
        self.polibase_password: str = None
        self.user_container: UserContainer = None
        self.description: str = None
        self.use_template_user: bool
        self.need_to_create_mark: bool = None

    def send_whatsapp_message(self, telephone_number: str, message: str) -> bool:
        return self.pih.MESSAGE.WHATSAPP.send(
            telephone_number, message, use_alternative=False, wappi_profile_id=CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE_ID.IT.value)

    def who_lost_the_mark(self, tab_number: str = None):
        try:
            tab_number = tab_number or self.pih.INPUT.tab_number()
            if tab_number is not None:
                try:
                    mark: Mark = self.pih.RESULT.MARK.by_tab_number(
                        tab_number).data
                    mark_type: MarkType = EnumTool.get(MarkType, mark.type)
                    if mark_type == MarkType.FREE:
                        self.pih.OUTPUT.good("Это свободная карта доступа")
                    elif mark_type == MarkType.GUEST:
                        self.pih.OUTPUT.good("Это гостевая карта доступа")
                    else:
                        if mark_type == MarkType.TEMPORARY:
                            mark = self.pih.RESULT.MARK.temporary_mark_owner(
                                mark).data
                            tab_number = mark.TabNumber
                            self.pih.OUTPUT.good("Это временная карта доступа")
                        if mark is not None:
                            telephone_number: str = mark.telephoneNumber
                            self.pih.OUTPUT.value(f"Персона", mark.FullName)
                            if not self.pih.CHECK.telephone_number(telephone_number):
                                user: User = self.pih.RESULT.USER.by_mark_tab_number(
                                    tab_number).data
                                if user is not None:
                                    telephone_number = user.telephoneNumber
                            if not self.pih.CHECK.telephone_number(telephone_number):
                                self.pih.OUTPUT.bad(f"Телефон не указан")
                            else:
                                self.pih.OUTPUT.value(
                                    f"Телефон", telephone_number)
                                if self.pih.INPUT.yes_no("Отправить сообщение?", True):
                                    details: str = self.pih.INPUT.input(
                                        f"{self.pih.SESSION.get_user_given_name()}, уточните, где забрать найденную карту")
                                    if self.send_whatsapp_message(
                                            telephone_number, f"День добрый, {FullNameTool.to_given_name(mark.FullName)}, вашу карту доступа ({tab_number}) нашли, заберите ее {details}"):
                                        self.pih.OUTPUT.good(
                                            "Сообщение отправлено")
                                    else:
                                        self.pih.OUTPUT.bad(
                                            "Ошибка при отправке сообщения")
                        else:
                            self.pih.OUTPUT.bad(f"Телефон не указан")
                except NotFound as error:
                    self.pih.OUTPUT.bad(
                        "Карта доступа, с введенным номером не найдена")
        except KeyboardInterrupt:
            pass


    def create_new_mark(self):

        self.full_name = None
        self.tab_number = None
        self.telephone_number = None
        self.division_id = None

        def get_full_name() -> ActionValue:
            self.pih.OUTPUT.new_line()
            self.pih.OUTPUT.head("Заполните ФИО персоны")
            self.full_name = self.pih.INPUT.full_name(True)
            user_is_exsits: bool = not self.pih.CHECK.MARK.exists_by_full_name(
                self.full_name)
            if user_is_exsits:
                self.pih.OUTPUT.bad(
                    "Персона с данной фамилией, именем и отчеством уже есть!")
                if not self.pih.INPUT.yes_no("Продолжить?"):
                    exit()
            return self.pih.OUTPUT.get_action_value("ФИО персоны", FullNameTool.to_string(self.full_name))

        def get_telephone() -> ActionValue:
            self.pih.OUTPUT.new_line()
            self.pih.OUTPUT.head("Заполните номер телефона")
            self.telephone_number = self.pih.INPUT.telephone_number()
            return self.pih.OUTPUT.get_action_value("Номер телефона", self.telephone_number, False)

        def get_tab_number() -> ActionValue:
            self.pih.OUTPUT.new_line()
            self.pih.OUTPUT.head("Выбор группы и номера для карты доступа")
            free_mark: Mark = self.pih.INPUT.MARK.free()
            group_name: str = free_mark.GroupName
            self.tab_number = free_mark.TabNumber
            self.pih.OUTPUT.value("Группа карты доступа", group_name)
            return self.pih.OUTPUT.get_action_value("Номер карты пропуска", self.tab_number)

        def get_division() -> ActionValue:
            self.pih.OUTPUT.new_line()
            self.pih.OUTPUT.head("Выбор подразделения")
            person_division: MarkDivision = self.pih.INPUT.MARK.person_division()
            self.division_id = person_division.id
            return self.pih.OUTPUT.get_action_value("Подразделение, к которому прикреплена персона", person_division.name)

        ActionStack("Данные пользователя",
                    get_full_name,
                    get_division,
                    get_telephone,
                    get_tab_number,
                    input=self.pih.INPUT,
                    output=self.pih.OUTPUT
                    )
        if self.pih.INPUT.yes_no("Создать карту доступа для персоны?", True):
            if self.pih.ACTION.MARK.create(self.full_name, self.division_id, self.tab_number, self.telephone_number):
                self.pih.OUTPUT.good("Карты доступа создана!")
                self.pih.MESSAGE.COMMAND.it_notify_about_create_new_mark(
                    self.full_name)
                if self.pih.INPUT.yes_no("Уведомить персону?", True):
                    self.pih.MESSAGE.WHATSAPP.send(
                        self.telephone_number, f"Сообщение от ИТ отдела Pacific International Hospital: День добрый, {FullNameTool.to_given_name(self.full_name)}, Вам выдана карта доступа с номером {self.tab_number}")
            else:
                self.pih.OUTPUT.bad("Карта доступа не создана!")

    def send_internal_message(self, login: str = None, message: str = None) -> None:
        user: User = None
        while True:
            try:
                if login is None:
                    user = self.pih.INPUT.USER.by_any()
                    login = user.samAccountName
                else:
                    user = self.pih.RESULT.USER.by_login(login).data
                if user is not None:
                    break
            except NotFound as error:
                self.pih.OUTPUT.bad(error.get_details())
        message = message or self.pih.INPUT.message(f"Введите сообщение для {FullNameTool.to_given_name(user)}", f"{FullNameTool.to_given_name(user)}, ")
        self.pih.MESSAGE.WORKSTATION.by_login(login, message)

    def create_new_user(self) -> None:

        self.full_name = None
        self.tab_number = None
        self.telephone_number = None
        self.division_id = None
        self.user_is_exists = False
        self.login = None
        self.password = None
        self.internal_email = None
        self.external_email = None
        self.email_password = None
        self.polibase_login = None
        self.polibase_password = None
        self.user_container = None
        self.description = None
        self.use_template_user = None
        self.need_to_create_mark = None

    
        def get_full_name() -> ActionValue:
            self.pih.OUTPUT.header("Заполнение ФИО пользователя")
            self.full_name = self.pih.INPUT.full_name(True)
            self.user_is_exists = self.pih.CHECK.USER.exists_by_full_name(self.full_name)
            if self.user_is_exists:
                self.pih.OUTPUT.bad(
                    "Пользователем с данной фамилией, именем и отчеством уже есть!")
                if not self.pih.INPUT.yes_no("Продолжить?"):
                    self.pih.SESSION.exit()
            return self.pih.OUTPUT.get_action_value("ФИО пользователя", FullNameTool.to_string(self.full_name))


        def get_login() -> ActionValue:
            self.pih.OUTPUT.header("Создание логина для аккаунта пользователя")
            self.login = self.pih.INPUT.USER.generate_login(self.full_name)
            return self.pih.OUTPUT.get_action_value("Логин пользователя", self.login)

        def get_telephone_number() -> ActionValue:
            self.pih.OUTPUT.header("Заполнение номера телефона")
            self.telephone_number = self.pih.INPUT.telephone_number()
            return self.pih.OUTPUT.get_action_value("Номер телефона", self.telephone_number, False)


        def get_description() -> ActionValue:
            self.pih.OUTPUT.header("Заполнение описания пользователя")
            self.description = self.pih.INPUT.description()
            return self.pih.OUTPUT.get_action_value("Описание", self.description, False)

        def get_template_user_container_or_user_container() -> ActionValue:
            self.pih.OUTPUT.header("Выбор контейнера для пользователя")
            if self.pih.INPUT.yes_no("Использовать шаблон для создания аккаунта пользователя?", True):
                self.user_container, self.use_template_user = (
                    self.pih.INPUT.USER.template(), True)
                return self.pih.OUTPUT.get_action_value("Контейнер пользователя", self.user_container.description)
            else:
                self.user_container, self.use_template_user = (
                   self.pih.INPUT.USER.container(), False)
                return self.pih.OUTPUT.get_action_value("Контейнер пользователя", self.user_container.distinguishedName)

        def get_pc_password() -> ActionValue:
            self.pih.OUTPUT.header("Создание пароля для аккаунта пользователя")
            self.password = self.pih.INPUT.USER.generate_password(
                settings=PASSWORD.SETTINGS.PC)
            return self.pih.OUTPUT.get_action_value("Пароль", self.password, False)

        def get_internal_email() -> ActionValue:
            self.pih.OUTPUT.header("Создание корпоративной электронной почты")
            if self.pih.INPUT.yes_no("Создать", True):
                self.internal_email = self.pih.ACTION.generate_email(self.login)
            return self.pih.OUTPUT.get_action_value("Адресс корпоративной электронной почты пользователя", self.internal_email)

        def get_email_password() -> ActionValue:
            if self.internal_email:
                self.pih.OUTPUT.header("Создание пароля для корпоротивной электронной почты")
                if self.pih.INPUT.yes_no("Использовать пароль от аккаунта пользователя", True):
                    self.email_password = self.password
                else:
                    self.email_password = self.pih.INPUT.USER.generate_password(
                        settings=PASSWORD.SETTINGS.EMAIL)
                return self.pih.OUTPUT.get_action_value("Пароль электронной почты",  self.email_password, False)
            return None

        def get_external_email() -> ActionValue:
            self.pih.OUTPUT.header("Добавление внешней почты")
            if self.pih.INPUT.yes_no("Добавить"):
                self.external_email = self.pih.INPUT.email()
            return self.pih.OUTPUT.get_action_value("Адресс внешней электронной почты пользователя", self.external_email if self.external_email else "Нет", False)

        def get_division() -> ActionValue:
            full_name_string: str = FullNameTool.to_string(self.full_name)
            mark: Mark = self.pih.RESULT.MARK.by_name(full_name_string, True).data
            if mark is not None:
                if self.pih.INPUT.yes_no(
                        f"Найдена карта доступа для персоны {full_name_string} с номером {mark.TabNumber}. Использовать?", True):
                    self.need_to_create_mark = False
                    return None
            self.need_to_create_mark = self.pih.INPUT.yes_no(
                f"Создать карту доступа для персоны '{full_name_string}'", True)
            if self.need_to_create_mark:
                self.pih.OUTPUT.header("Выбор подразделения")
                person_division: MarkDivision = self.pih.INPUT.MARK.person_division()
                self.division_id = person_division.id
                return self.pih.OUTPUT.get_action_value("Подразделение персоны, которой принадлежит карта доступа", person_division.name)
            return None

        def get_tab_number() -> ActionValue:
            if self.need_to_create_mark:
                self.pih.OUTPUT.header("Создание карты доступа")
                free_mark: Mark = self.pih.INPUT.MARK.free()
                group_name: str = free_mark.GroupName
                self.tab_number = free_mark.TabNumber
                self.pih.OUTPUT.value("Группа карты доступа", group_name)
                return self.pih.OUTPUT.get_action_value("Номер карты доступа", self.tab_number)
            return None

        self.pih.OUTPUT.head1("Создание пользователя")
        ActionStack(
            "Данные пользователя",
            get_full_name,
            get_login,
            get_telephone_number,
            get_description,
            get_template_user_container_or_user_container,
            get_pc_password,
            get_internal_email,
            get_email_password,
            get_external_email,
            get_division,
            get_tab_number,  
            input=self.pih.INPUT,
            output=self.pih.OUTPUT
            )
        polibase_login: str = self.login
        polibase_password: str = self.password
        if self.pih.INPUT.yes_no("Создать аккаунт для пользователя", True):
            if self.use_template_user:
                self.pih.ACTION.USER.create_from_template(
                    self.user_container.distinguishedName, self.full_name, self.login, self.password, self.description, self.telephone_number, self.internal_email or self.external_email)
            else:
                self.pih.ACTION.USER.create_in_container(
                    self.user_container.distinguishedName, self.full_name, self.login, self.password, self.description, self.telephone_number, self.internal_email or self.external_email)
            self.tab_number = self.tab_number or self.pih.RESULT.MARK.by_name(
                FullNameTool.to_string(self.full_name), True).data.TabNumber
            if self.need_to_create_mark:
                self.pih.ACTION.MARK.create(
                    self.full_name, self.division_id, self.tab_number, self.telephone_number)
            user_account_document_path: str = self.pih.PATH.USER.get_document_name(
                FullNameTool.to_string(self.full_name), self.login if self.user_is_exists else None)
            if self.pih.ACTION.DOCUMENTS.create_for_user(user_account_document_path, self.full_name, self.tab_number, LoginPasswordPair(self.login, self.password), LoginPasswordPair(
                    polibase_login, polibase_password), LoginPasswordPair(self.internal_email, self.email_password)):
                self.pih.MESSAGE.COMMAND.hr_notify_about_new_employee(self.login)
                self.pih.MESSAGE.COMMAND.it_notify_about_user_creation( self.login, self.password)
                if self.need_to_create_mark:
                    self.pih.MESSAGE.COMMAND.it_notify_about_create_new_mark(
                        self.full_name)
                if self.pih.INPUT.yes_no("Сообщить пользователю о создании документов", True):
                    self.send_whatsapp_message(
                        self.telephone_number, f"Сообщение от ИТ отдела Pacific International Hospital: День добрый, {FullNameTool().to_given_name(self.full_name)}, Вас ожидает документы и карта доступа с номером {self.tab_number} в отделе")
                if self.pih.INPUT.yes_no("Отправить пользователю данные об аккаунте?", True):
                    self.send_whatsapp_message(
                        self.telephone_number, f"Сообщение от ИТ отдела Pacific International Hospital: День добрый, {FullNameTool().to_given_name(self.full_name)}, данные Вашего аккаунта:\nЛогин: {self.login}\nПароль: {self.password}\nЭлектронная почта: {self.internal_email}")
