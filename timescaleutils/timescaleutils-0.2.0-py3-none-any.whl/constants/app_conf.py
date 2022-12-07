import configparser
config = configparser.ConfigParser()
config.read('application.conf')

# ---------------------------SECTIONS----------------------------------
DB_SECTION = 'PSQL'
TIME_SECTION = 'TIME'
LOGGER_SECTION_NAME = 'LOG'
# ---------------------------DB----------------------------------
DB_HOST = config.get(DB_SECTION, "host")
DB_PORT = str(config.getint(DB_SECTION, "port"))
DB_USER_NAME = config.get(DB_SECTION, "user_name")
DB_PASSWORD = config.get(DB_SECTION, "password", fallback=None)
DB_NAME = config.get(DB_SECTION, "db_name")
TBL_NAME = config.get(DB_SECTION, "tbl_name")
connection = "postgresql://" + DB_USER_NAME + ":" + DB_PASSWORD + "@" + DB_HOST + ":" + DB_PORT + "/" + DB_NAME
# ---------------------------TIME----------------------------------
TIME_ZONE = config.get(TIME_SECTION, "timezone")
# ---------------------------LOGGER----------------------------------
LOG_LEVEL = config.get(LOGGER_SECTION_NAME, 'log_level', fallback="INFO")
LOG_BASE_PATH = config.get(LOGGER_SECTION_NAME, 'base_path', fallback="logs")
LOG_FILE_NAME = LOG_BASE_PATH + config.get(LOGGER_SECTION_NAME, 'file_name', fallback='ilens_utils')
LOG_HANDLERS = config.get(LOGGER_SECTION_NAME, 'handlers')
LOGGER_NAME = config.get(LOGGER_SECTION_NAME, 'logger_name')
