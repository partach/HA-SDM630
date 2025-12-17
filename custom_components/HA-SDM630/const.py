"""Constants for the SDM630 integration."""

DOMAIN = "HA-SDM630"

CONF_SERIAL_PORT = "serial_port"
CONF_SLAVE_ID = "slave_id"
CONF_BAUDRATE = "baudrate"
CONF_UPDATE_INTERVAL = "update_interval"

DEFAULT_SLAVE_ID = 1
DEFAULT_BAUDRATE = 9600
DEFAULT_UPDATE_INTERVAL = 30  # Seconds

# Standard SDM630 holding registers (float, address in decimal)
REGISTER_MAP = {
    "voltage_l1": {"address": 0, "name": "Voltage L1", "unit": "V", "device_class": "voltage"},
    "voltage_l2": {"address": 2, "name": "Voltage L2", "unit": "V", "device_class": "voltage"},
    "voltage_l3": {"address": 4, "name": "Voltage L3", "unit": "V", "device_class": "voltage"},
    "current_l1": {"address": 6, "name": "Current L1", "unit": "A", "device_class": "current"},
    "current_l2": {"address": 8, "name": "Current L2", "unit": "A", "device_class": "current"},
    "current_l3": {"address": 10, "name": "Current L3", "unit": "A", "device_class": "current"},
    "power_l1": {"address": 12, "name": "Power L1", "unit": "W", "device_class": "power"},
    "power_l2": {"address": 14, "name": "Power L2", "unit": "W", "device_class": "power"},
    "power_l3": {"address": 16, "name": "Power L3", "unit": "W", "device_class": "power"},
    "total_power": {"address": 52, "name": "Total Power", "unit": "W", "device_class": "power"},
    "import_energy": {"address": 72, "name": "Import Energy", "unit": "kWh", "device_class": "energy"},
    "export_energy": {"address": 74, "name": "Export Energy", "unit": "kWh", "device_class": "energy"},
    # Add more as needed from SDM630 manual (e.g., frequency at 70, PF at 30-44)
}
