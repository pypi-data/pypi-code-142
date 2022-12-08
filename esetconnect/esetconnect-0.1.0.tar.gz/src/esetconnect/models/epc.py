import pydantic


class GetSyslogConfigurationRequest(pydantic.BaseModel):
    config_options: str


class GetSyslogConfigurationResponse(pydantic.BaseModel):
    config_data_json: str
