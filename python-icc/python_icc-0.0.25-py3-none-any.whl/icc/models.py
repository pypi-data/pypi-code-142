from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from pydantic.json import ENCODERS_BY_TYPE

""" Model Groundwork """


class PydanticObjectId(ObjectId):
    """
    Object Id field. Compatible with Pydantic.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return PydanticObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema: dict):
        field_schema.update(
            type="string",
        )


ENCODERS_BY_TYPE[PydanticObjectId] = str


class IccBaseModel(BaseModel):
    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data


""" Enums and global dicts """


class DeviceType:
    Lighting: str = "Lighting"
    Power: str = "Power"


class LightingDeviceType:
    KasaBulb: str = "Kasa Bulb"
    CustomLedStrip: str = "Custom Led Strip"
    KasaLedStrip: str = "Kasa Led Strip"


class PowerDeviceType:
    KasaPlug: str = "Kasa Plug"


class DisplayDeviceType:
    Chromecast: str = "Chromecast"


class ServiceUrls:
    LIGHTING_SERVICE_URL = "http://.default.svc.cluster.local:8000"
    POWER_SERVICE_URL = "http://power-service-cluster-ip.default.svc.cluster.local:8000"
    SCENE_SERVICE_URL = "http://scene-service-cluster-ip.default.svc.cluster.local:8000"
    DEVICE_SERVICE_URL = "http://device-service-cluster-ip.default.svc.cluster.local:8000"
    DISPLAY_SERVICE_URL = "http://display-service-cluster-ip.default.svc.cluster.local:8000"
    MEDIA_DRIVE_SERVICE_URL = "http://media-drive-service-cluster-ip.default.svc.cluster.local:8000"
    CHROMECAST_CONTROLLER_URL = "http://chromecast-controller-cluster-ip.default.svc.cluster.local:8000"
    KASA_LED_STRIP_CONTROLLER_URL = "http://kasa-led-strip-controller-cluster-ip.default.svc.cluster.local:8000"
    KASA_BULB_CONTROLLER_URL = "http://kasa-bulb-controller-cluster-ip.default.svc.cluster.local:8000"
    KASA_PLUG_CONTROLLER_URL = "http://kasa-plug-controller-cluster-ip.default.svc.cluster.local:8000"


class DeviceControllerProxy:
    device_model_to_url = {
        LightingDeviceType.KasaBulb: ServiceUrls.KASA_BULB_CONTROLLER_URL,
        LightingDeviceType.KasaLedStrip: ServiceUrls.KASA_LED_STRIP_CONTROLLER_URL,
        PowerDeviceType.KasaPlug: ServiceUrls.KASA_PLUG_CONTROLLER_URL,
        DisplayDeviceType.Chromecast: ServiceUrls.CHROMECAST_CONTROLLER_URL
    }


""" DTOs """


class LightingRequest(IccBaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    target: Optional[PydanticObjectId]
    name: Optional[str]
    operation: str
    h: int = 0
    s: int = 100
    v: int = 50
    brightness: int = None
    temperature: int = None
    date: datetime = datetime.utcnow().isoformat()


class PowerRequest(IccBaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    target: Optional[PydanticObjectId]
    name: Optional[str]
    operation: str


class SceneRequestDto(IccBaseModel):
    name: str


class ChromecastRequest(IccBaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    target: PydanticObjectId
    path: str


class LightingRequestDto(IccBaseModel):
    target_id: PydanticObjectId
    operation: str
    h: int | None
    s: int | None
    v: int | None
    brightness: int | None
    temperature: int | None


class PowerRequestDto(IccBaseModel):
    target_id: PydanticObjectId
    operation: str


class SceneDto(IccBaseModel):
    name: str
    lighting_requests: Optional[list[LightingRequestDto]]
    power_requests: Optional[list[PowerRequestDto]]


class DeviceDto(IccBaseModel):
    name: str
    ip: str
    type: str
    model: str


""" Analytics Record Models """


class LightingRequestRecord(IccBaseModel):
    target_id: PydanticObjectId
    operation: str
    h: int | None
    s: int | None
    v: int | None
    brightness: int | None
    temperature: int | None
    time: str


class SceneRequestRecord(IccBaseModel):
    name: str
    time: str


""" Entitity Models """


class Device(IccBaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    name: str
    type: str
    model: str
    ip: str


class SceneModel(IccBaseModel):
    id: PydanticObjectId = Field(None, alias="_id")
    name: str
    lighting_requests: Optional[list[LightingRequestDto]]
    power_requests: Optional[list[PowerRequestDto]]


class DeviceModel(IccBaseModel):
    id: PydanticObjectId = Field(None, alias="_id")
    name: str
    ip: str
    type: str
    model: str
