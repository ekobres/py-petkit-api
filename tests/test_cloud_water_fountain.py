import json
import unittest
from pathlib import Path

from pypetkitapi import (
    BleWaterFountain,
    CloudWaterFountain,
    CloudWaterFountainCommand,
    CloudWaterFountainRecord,
    W7H,
    WaterFountain,
)
from pypetkitapi.cloud_water_fountain_container import (
    SettingsCloudWaterFountain,
    StateCloudWaterFountain,
)
from pypetkitapi.command import ACTIONS_MAP, DeviceAction, DeviceCommand, FountainCommand
from pypetkitapi.client import PetKitClient
from pypetkitapi.const import DEVICES_CLOUD_WATER_FOUNTAIN, PetkitEndpoint
from pypetkitapi.containers import Device
from pypetkitapi.water_fountain_container import (
    WaterFountainRecord,
    SettingsFountain,
)


def _load_device_detail_fixture() -> dict:
    har_path = Path(__file__).resolve().parents[1] / (
        "doc/captures/api.petkit.com.latest.w7h.20260626-0701.har"
    )
    with har_path.open(encoding="utf-8") as har_file:
        har = json.load(har_file)
    for entry in har["log"]["entries"]:
        if "device_detail" in entry["request"]["url"]:
            import base64

            content = entry["response"]["content"]
            text = content.get("text", "")
            if content.get("encoding") == "base64":
                text = base64.b64decode(text).decode("utf-8")
            payload = json.loads(text)
            return payload.get("result", payload)
    raise AssertionError("device_detail fixture not found in HAR")


class TestCloudWaterFountain(unittest.TestCase):
    """Tests for cloud water fountain models and routing."""

    @classmethod
    def setUpClass(cls):
        cls.device_detail = _load_device_detail_fixture()

    def test_cloud_water_fountain_parses_device_detail(self):
        fountain = CloudWaterFountain(**self.device_detail)
        self.assertEqual(fountain.name, "EVERSWEET ULTRA AI")
        self.assertEqual(fountain.firmware, "412")
        self.assertIsInstance(fountain.settings, SettingsCloudWaterFountain)
        self.assertIsInstance(fountain.state, StateCloudWaterFountain)
        self.assertEqual(fountain.settings.fountain_mode, 3)
        self.assertEqual(fountain.state.filter_left_days, 30)

    def test_cloud_water_fountain_endpoint(self):
        self.assertEqual(
            CloudWaterFountain.get_endpoint(W7H),
            PetkitEndpoint.DEVICE_DETAIL,
        )

    def test_cloud_water_fountain_query_param(self):
        device = Device(
            createdAt=1672531200,
            deviceId=10000468,
            deviceName="eversweet_ultra_ai",
            deviceType=W7H,
            groupId=1,
            type=29,
            typeCode=0,
            uniqueId="unique_10000468",
        )
        params = CloudWaterFountain.query_param(device)
        self.assertEqual(params, {"id": 10000468})

    def test_cloud_water_fountain_record_endpoint(self):
        self.assertEqual(
            CloudWaterFountainRecord.get_endpoint(W7H),
            PetkitEndpoint.GET_DEVICE_RECORD,
        )

    def test_cloud_water_fountain_record_query_param(self):
        device = Device(
            createdAt=1672531200,
            deviceId=10000468,
            deviceName="eversweet_ultra_ai",
            deviceType=W7H,
            groupId=1,
            type=29,
            typeCode=0,
            uniqueId="unique_10000468",
        )
        params = CloudWaterFountainRecord.query_param(device)
        self.assertIn("timestamp", params)
        self.assertEqual(params["deviceId"], 10000468)
        self.assertEqual(params["type"], "0")

    def test_cloud_water_fountain_command_values(self):
        self.assertEqual(CloudWaterFountainCommand.DRAIN_FLUSH, 1)
        self.assertEqual(CloudWaterFountainCommand.REFILL, 2)
        self.assertEqual(CloudWaterFountainCommand.DRAIN, 3)
        self.assertEqual(CloudWaterFountainCommand.DEEP_CLEAN, 4)

    def test_filter_reset_in_actions_map(self):
        self.assertIn(FountainCommand.FILTER_RESET, ACTIONS_MAP)
        action = ACTIONS_MAP[FountainCommand.FILTER_RESET]
        self.assertEqual(action.endpoint, PetkitEndpoint.FILTER_RESET)
        self.assertEqual(action.supported_device, DEVICES_CLOUD_WATER_FOUNTAIN)

    def test_control_device_supports_cloud_fountain(self):
        action = ACTIONS_MAP[DeviceCommand.CONTROL_DEVICE]
        self.assertIn(W7H, action.supported_device)

    def test_control_device_start_action_payload(self):
        action = ACTIONS_MAP[DeviceCommand.CONTROL_DEVICE]
        device = type(
            "Device",
            (object,),
            {
                "id": 10000468,
                "device_nfo": type(
                    "DeviceInfo", (object,), {"device_type": W7H}
                )(),
            },
        )
        params = action.params(
            device,
            {DeviceAction.START: CloudWaterFountainCommand.REFILL},
        )
        self.assertEqual(params["id"], 10000468)
        self.assertEqual(params["type"], "start")
        self.assertIn("start_action", params["kv"])

    def test_add_cloud_water_fountain_task_appends_media(self):
        device = Device(
            createdAt=1672531200,
            deviceId=10000468,
            deviceName="eversweet_ultra_ai",
            deviceType=W7H,
            groupId=1,
            type=29,
            typeCode=0,
            uniqueId="unique_10000468",
        )
        media_tasks: list = []

        class StubClient:
            async def _fetch_media(self, fetch_device: Device) -> None:
                return None

        client = StubClient()
        PetKitClient._add_cloud_water_fountain_task_by_type(
            client,
            media_tasks,
            W7H,
            device,
        )
        self.assertEqual(len(media_tasks), 1)


class TestBleWaterFountainCompatibility(unittest.TestCase):
    """Tests for BLE water fountain compatibility aliases."""

    def test_water_fountain_is_ble_water_fountain(self):
        self.assertIs(WaterFountain, BleWaterFountain)

    def test_water_fountain_record_is_ble_water_fountain_record(self):
        from pypetkitapi.ble_water_fountain_container import BleWaterFountainRecord

        self.assertIs(WaterFountainRecord, BleWaterFountainRecord)

    def test_settings_fountain_is_settings_ble_water_fountain(self):
        from pypetkitapi.ble_water_fountain_container import SettingsBleWaterFountain

        self.assertIs(SettingsFountain, SettingsBleWaterFountain)


if __name__ == "__main__":
    unittest.main()
