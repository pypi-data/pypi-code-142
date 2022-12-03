"""
Тайпинги параметров Yandex Cloud Functions
https://cloud.yandex.ru/docs/functions/concepts/function-invoke
"""

from typing import Literal, TypedDict, Dict, List, Protocol, Optional

HttpMethod = Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']


class Identity(TypedDict):
    # Адрес, с которого был сделан запрос
    sourceIp: str
    # Содержимое HTTP-заголовка User-Agent исходного запроса
    userAgent: str


class ApiGateway(TypedDict):
    # Словарь с контекстом операции, описанным в спецификации API-шлюза
    operationContext: dict


class RequestContext(TypedDict):
    # Набор пар ключ:значение для аутентификации пользователя
    identity: Identity
    # DELETE, GET, HEAD, OPTIONS, PATCH, POST или PUT
    httpMethod: HttpMethod
    # ID запроса, генерируется в роутере
    requestId: str
    # Время запроса в формате CLF
    requestTime: str
    # Время запроса в формате Unix
    requestTimeEpoch: str
    # Словарь с контекстом авторизации
    authorizer: dict
    # Словарь со специфичными данными, передаваемыми API-шлюзом при вызове функции
    apiGateway: ApiGateway
    # Идентификатор веб-сокетного соединения
    connectionId: str
    # Время подключения веб-сокетного соединения
    connectedAt: str
    # Тип события или операции с веб-сокетом: CONNECT, MESSAGE, DISCONNECT
    eventType: Literal['CONNECT', 'MESSAGE', 'DISCONNECT']
    # Идентификатор сообщения, полученного из веб-сокета
    messageId: str
    # Статус-код закрытия веб-сокета
    disconnectStatusCode: str
    # Текстовое описание причины закрытия веб-сокета
    disconnectReason: str


class Event(TypedDict):
    """
    Входящий запрос в Yandex Cloud Function
    https://cloud.yandex.ru/docs/functions/concepts/function-invoke#request
    """
    body: str
    # Название HTTP-метода
    httpMethod: HttpMethod
    # Словарь строк, содержащий HTTP-заголовки запроса и их значения.
    # Если один и тот же заголовок передан несколько раз,
    #   словарь содержит последнее переданное значение.
    headers: Dict[str, str]
    # Словарь, содержащий HTTP-заголовки запроса и списки с их значениями.
    # Он содержит те же самые ключи, что и словарь headers,
    #   но если какой-либо заголовок повторялся несколько раз,
    #   список для него будет содержать все переданные значения для данного заголовка.
    # Если заголовок был передан всего один раз, он включается в этот словарь,
    #   и список для него будет содержать одно значение.
    multiValueHeaders: Dict[str, List[str]]
    # Словарь, содержащий параметры запроса.
    # Если один и тот же параметр указан несколько раз,
    #   словарь содержит последнее указанное значение.
    queryStringParameters: Dict[str, str]
    # Словарь, содержащий для каждого параметра запроса список со всеми указанными значениями.
    # Если один и тот же параметр указан несколько раз, словарь содержит все указанные значения.
    multiValueQueryStringParameters: Dict[str, List[str]]
    requestContext: RequestContext
    # Если body содержит данные закодированные в Base64,
    #   то Cloud Functions установит значение параметра в true.
    isBase64Encoded: bool


class Context(TypedDict):
    """
    Служебные данные
    https://cloud.yandex.ru/docs/functions/concepts/function-invoke#service-data
    """
    # Идентификатор запроса к функции, генерируется при обращении к функции и
    #   отображается в журнале вызова функции.
    requestId: str
    # Идентификатор функции.
    functionName: str
    # Идентификатор версии функции.
    functionVersion: str
    # Объем памяти, указанный для версии функции, МБ.
    memoryLimitInMB: str
    # IAM-токен сервисного аккаунта, указанного для версии функции.
    # Актуальное значение генерируется автоматически.
    # Используется для работы с API Yandex Cloud.
    # Поле присутствует, только если для версии функции указан корректный сервисный аккаунт.
    token: str


# https://cloud.yandex.ru/docs/functions/concepts/function-invoke#http-state
StatusCode = Literal[
    # 200 OK — функция успешно выполнена.
    200,
    # 400 BadRequest — ошибка в параметрах HTTPS-запроса.
    400,
    # 403 Forbidden — запрос не может быть выполнен из-за ограничений в доступе для клиента к функции.
    403,
    # 404 Not Found — по указанному URL не найдена функция.
    404,
    # 413 Payload Too Large — превышение лимита на размер JSON-структуры запроса превышает 3,5 МБ.
    413,
    # 429 TooManyRequests — слишком высокая интенсивность вызова функции:
    #   Превышение квоты на количество выполняемых запросов.
    #   Текущий запрос не был выполнен, так как все исполнители уже перегружены
    #       существующими запросами к данной функции.
    429,
    # 500 Internal Server Error — внутренняя ошибка сервера.
    500,
    # 502 BadGateway — ошибка в коде функции или в формате возвращаемого JSON-ответа.
    502,
    # 503 Service Unavailable — недоступность сервиса Cloud Functions.
    503,
    # 504 Gateway Timeout — превышено максимальное время выполнения функции до таймаута.
    504,
]


class Resp(TypedDict, total=False):
    """
    Результат выполнения Cloud Function
    https://cloud.yandex.ru/docs/functions/concepts/function-invoke#response
    """
    # Код состояния HTTP, по которому клиент узнаёт результаты запроса.
    statusCode: StatusCode
    # Содержимое ответа в виде строки.
    # Для работы с бинарными данными содержимое может быть закодировано в формат Base64.
    # В этом случае установите параметр isBase64Encoded: true.
    body: str
    # Если body закодирован в формат Base64, установите значение параметра в true.
    isBase64Encoded: bool
    # Словарь строк, содержащий HTTP-заголовки ответа и их значения.
    headers: Dict[str, str]
    # Словарь, в котором для HTTP-заголовков ответа можно указать одно или несколько значений в виде списка.
    # Если один и тот же заголовок указан и в headers, и в multiValueHeaders, содержимое headers игнорируется.
    multiValueHeaders: Dict[str, List[str]]


class Handler(Protocol):
    """Cloud Function обработчик"""

    def __call__(
        self,
        event: Event,
        context: Optional[Context] = None,
    ) -> Resp:
        ...
