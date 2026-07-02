"""BLE water fountain models (compatibility import path)."""

from pypetkitapi.ble_water_fountain_container import (
    BleWaterFountain,
    BleWaterFountainRecord,
    Electricity,
    Schedule,
    SettingsBleWaterFountain,
    StatusBleWaterFountain,
    Type,
)

WaterFountain = BleWaterFountain
WaterFountainRecord = BleWaterFountainRecord
SettingsFountain = SettingsBleWaterFountain
Status = StatusBleWaterFountain

__all__ = [
    "BleWaterFountain",
    "BleWaterFountainRecord",
    "Electricity",
    "Schedule",
    "SettingsBleWaterFountain",
    "SettingsFountain",
    "Status",
    "StatusBleWaterFountain",
    "Type",
    "WaterFountain",
    "WaterFountainRecord",
]
