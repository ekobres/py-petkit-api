"""Dataclasses for cloud-connected water fountains."""

from datetime import datetime
from typing import Any, ClassVar

from pydantic import BaseModel, Field

from pypetkitapi.const import DEVICE_DATA, DEVICE_RECORDS, W7H, PetkitEndpoint
from pypetkitapi.containers import (
    CloudProduct,
    Device,
    FirmwareDetail,
    UserDevice,
    Wifi,
)


class SettingsCloudWaterFountain(BaseModel):
    """Dataclass for cloud water fountain settings."""

    manual_lock: int | None = Field(None, alias="manualLock")
    click_ok_enable: int | None = Field(None, alias="clickOkEnable")
    language: str | None = None
    languages: list[str] | None = None
    disturb_mode: int | None = Field(None, alias="disturbMode")
    disturb_config: int | None = Field(None, alias="disturbConfig")
    distrub_multi_range: list[list[int]] | None = Field(None, alias="distrubMultiRange")
    camera: int | None = None
    camera_config: int | None = Field(None, alias="cameraConfig")
    camera_multi_range: list[dict[str, Any]] | None = Field(
        None, alias="cameraMultiRange"
    )
    microphone: int | None = None
    night: int | None = None
    time_display: int | None = Field(None, alias="timeDisplay")
    camera_light: int | None = Field(None, alias="cameraLight")
    micro_light: int | None = Field(None, alias="microLight")
    smart_frame: int | None = Field(None, alias="smartFrame")
    highlight: int | None = None
    auto_product: int | None = Field(None, alias="autoProduct")
    upload: int | None = None
    pre_live: int | None = Field(None, alias="preLive")
    live_encrypt: int | None = Field(None, alias="liveEncrypt")
    pet_detection: int | None = Field(None, alias="petDetection")
    drink_detection: int | None = Field(None, alias="drinkDetection")
    flush_notify: int | None = Field(None, alias="flushNotify")
    water_change_notify: int | None = Field(None, alias="waterChangeNotify")
    clean_water_lack_notify: int | None = Field(None, alias="cleanWaterLackNotify")
    clean_water_empty_notify: int | None = Field(None, alias="cleanWaterEmptyNotify")
    waste_water_full_notify: int | None = Field(None, alias="wasteWaterFullNotify")
    pet_notify: int | None = Field(None, alias="petNotify")
    pet_notify_interval: int | None = Field(None, alias="petNotifyInterval")
    drink_notify: int | None = Field(None, alias="drinkNotify")
    add_water_notify: int | None = Field(None, alias="addWaterNotify")
    light_mode: int | None = Field(None, alias="lightMode")
    light_config: int | None = Field(None, alias="lightConfig")
    light_multi_range: list[list[int]] | None = Field(None, alias="lightMultiRange")
    light_assist: int | None = Field(None, alias="lightAssist")
    tone_mode: int | None = Field(None, alias="toneMode")
    tone_multi_range: list[list[int]] | None = Field(None, alias="toneMultiRange")
    tone_config: int | None = Field(None, alias="toneConfig")
    system_sound_enable: int | None = Field(None, alias="systemSoundEnable")
    volume: int | None = None
    flush_intensity: int | None = Field(None, alias="flushIntensity")
    auto_flush: int | None = Field(None, alias="autoFlush")
    flush_cycle: int | None = Field(None, alias="flushCycle")
    flush_time: int | None = Field(None, alias="flushTime")
    fountain_mode: int | None = Field(None, alias="fountainMode")
    fountain_time: int | None = Field(None, alias="fountainTime")
    sleep_time: int | None = Field(None, alias="sleepTime")
    heater_switch: int | None = Field(None, alias="heaterSwitch")
    heater_temp: int | None = Field(None, alias="heaterTemp")
    auto_water_change: int | None = Field(None, alias="autoWaterChange")
    water_change_cycle: int | None = Field(None, alias="waterChangeCycle")
    water_change_time: int | None = Field(None, alias="waterChangeTime")
    add_water_switch: int | None = Field(None, alias="addWaterSwitch")
    add_water_mode: int | None = Field(None, alias="addWaterMode")
    aw_disturb_mode: int | None = Field(None, alias="awDisturbMode")
    aw_disturb_multi_range: list[list[int]] | None = Field(
        None, alias="awDisturbMultiRange"
    )
    clean_water_lack_light: int | None = Field(None, alias="cleanWaterLackLight")
    clean_water_empty_light: int | None = Field(None, alias="cleanWaterEmptyLight")
    waste_water_full_light: int | None = Field(None, alias="wasteWaterFullLight")
    wl_disturb_mode: int | None = Field(None, alias="wlDisturbMode")
    wl_disturb_multi_range: list[list[int]] | None = Field(
        None, alias="wlDisturbMultiRange"
    )
    distribution_diagram: int | None = Field(None, alias="distributionDiagram")
    control_settings: int | None = Field(None, alias="controlSettings")
    log_switch: int | None = Field(None, alias="logSwitch")


class StateCloudWaterFountain(BaseModel):
    """Dataclass for cloud water fountain runtime state."""

    wifi: Wifi | None = None
    pim: int | None = None
    ota: int | None = None
    overall: int | None = None
    power: int | None = None
    heat_install: int | None = Field(None, alias="heatInstall")
    stg_install: int | None = Field(None, alias="stgInstall")
    cwt_install: int | None = Field(None, alias="cwtInstall")
    wt_install: int | None = Field(None, alias="wtInstall")
    heat_state: int | None = Field(None, alias="heatState")
    lift_valve_state: int | None = Field(None, alias="liftValveState")
    lift_live_state: int | None = Field(None, alias="liftLiveState")
    pump_state: int | None = Field(None, alias="pumpState")
    water_pump_state: int | None = Field(None, alias="waterPumpState")
    cwt_state: int | None = Field(None, alias="cwtState")
    wt_state: int | None = Field(None, alias="wtState")
    add_water_state: int | None = Field(None, alias="addWaterState")
    flush_state: int | None = Field(None, alias="flushState")
    drink_time: int | None = Field(None, alias="drinkTime")
    pet_time: int | None = Field(None, alias="petTime")
    pet_close_time: int | None = Field(None, alias="petCloseTime")
    lift_reset_state: int | None = Field(None, alias="liftResetState")
    stg_full_state: int | None = Field(None, alias="stgFullState")
    disinfect_time: int | None = Field(None, alias="disinfectTime")
    heat_left_time: int | None = Field(None, alias="heatLeftTime")
    heat_status_time: int | None = Field(None, alias="heatStatusTime")
    disinfect_state: int | None = Field(None, alias="disinfectState")
    filter_left_days: int | None = Field(None, alias="filterLeftDays")
    filter_updated_at: int | None = Field(None, alias="filterUpdatedAt")
    heat_real_temp: int | None = Field(None, alias="heatRealTemp")
    add_water_frequent: int | None = Field(None, alias="addWaterFrequent")
    camera_status: int | None = Field(None, alias="cameraStatus")


class CloudWaterFountainRecordContent(BaseModel):
    """Dataclass for cloud water fountain event content."""

    start_time: int | None = Field(None, alias="startTime")
    event_start: int | None = Field(None, alias="eventStart")
    event_end: int | None = Field(None, alias="eventEnd")
    mark: int | None = None
    upload: int | None = None
    media: int | None = None
    drink_time: int | None = Field(None, alias="drinkTime")


class CloudWaterFountainRecord(BaseModel):
    """Dataclass for cloud water fountain device record data."""

    data_type: ClassVar[str] = DEVICE_RECORDS

    aes_key: str | None = Field(None, alias="aesKey")
    avatar: str | None = None
    content: CloudWaterFountainRecordContent | None = None
    device_id: int | None = Field(None, alias="deviceId")
    duration: int | None = None
    enum_event_type: str | None = Field(None, alias="enumEventType")
    event_id: str | None = Field(None, alias="eventId")
    event_type: int | None = Field(None, alias="eventType")
    expire: int | None = None
    media_api: str | None = Field(None, alias="mediaApi")
    pet_id: str | None = Field(None, alias="petId")
    pet_name: str | None = Field(None, alias="petName")
    preview: str | None = None
    storage_space: int | None = Field(None, alias="storageSpace")
    sub_content: list | None = Field(None, alias="subContent")
    timestamp: int | None = None
    user_id: str | None = Field(None, alias="userId")

    @classmethod
    def get_endpoint(cls, device_type: str) -> str | None:
        """Get the endpoint URL for the given device type."""
        if device_type == W7H:
            return PetkitEndpoint.GET_DEVICE_RECORD
        return None

    @classmethod
    def query_param(
        cls,
        device: Device,
        device_data: Any | None = None,
        request_date: str | None = None,
    ) -> dict:
        """Generate query parameters including request_date."""
        if device.device_type == W7H:
            return {
                "timestamp": int(datetime.now().timestamp()),
                "deviceId": device.device_id,
                "type": "0",
            }
        raise ValueError(f"Invalid device type: {device.device_type}")


class CloudWaterFountain(BaseModel):
    """Dataclass for cloud water fountain data.
    Supported devices = W7H
    """

    data_type: ClassVar[str] = DEVICE_DATA

    auto_upgrade: int | None = Field(None, alias="autoUpgrade")
    bt_mac: str | None = Field(None, alias="btMac")
    cloud_product: CloudProduct | None = Field(None, alias="cloudProduct")
    created_at: str | None = Field(None, alias="createdAt")
    cwt_tip: int | None = Field(None, alias="cwtTip")
    device_records: list[CloudWaterFountainRecord] | None = None
    drink_count: int | None = Field(None, alias="drinkCount")
    drink_time_avg: int | None = Field(None, alias="drinkTimeAvg")
    firmware: str
    firmware_details: list[FirmwareDetail] | None = Field(None, alias="firmwareDetails")
    frequency_pet_tip: int | None = Field(None, alias="frequencyPetTip")
    hardware: int
    id: int
    is_pet_drink_tips: int | None = Field(None, alias="isPetDrinkTips")
    locale: str | None = None
    mac: str | None = None
    model_code: int | None = Field(None, alias="modelCode")
    multi_config: bool | None = Field(None, alias="multiConfig")
    name: str | None = None
    next_flush_time: str | None = Field(None, alias="nextFlushTime")
    next_water_change_time: str | None = Field(None, alias="nextWaterChangeTime")
    p2p_type: int | None = Field(None, alias="p2pType")
    pet_drink_tips: list | None = Field(None, alias="petDrinkTips")
    secret: str | None = None
    service_status: int | None = Field(None, alias="serviceStatus")
    settings: SettingsCloudWaterFountain | None = None
    share_open: int | None = Field(None, alias="shareOpen")
    signup_at: str | None = Field(None, alias="signupAt")
    sn: str
    state: StateCloudWaterFountain | None = None
    temp_range: list[int] | None = Field(None, alias="tempRange")
    timezone: float | None = None
    too_many_pets: int | None = Field(None, alias="tooManyPets")
    user: UserDevice | None = None
    wt_tip: int | None = Field(None, alias="wtTip")
    device_nfo: Device | None = None
    medias: list | None = None

    @classmethod
    def get_endpoint(cls, device_type: str) -> str:
        """Get the endpoint URL for the given device type."""
        return PetkitEndpoint.DEVICE_DETAIL

    @classmethod
    def query_param(
        cls,
        device: Device,
        device_data: Any | None = None,
    ) -> dict:
        """Generate query parameters."""
        return {"id": int(device.device_id)}
