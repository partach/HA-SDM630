"""Constants for the Eastron SDM630 integration."""
from typing import Dict

DOMAIN = "HA-SDM630"

CONF_SERIAL_PORT = "serial_port"
CONF_SLAVE_ID = "slave_id"
CONF_BAUDRATE = "baudrate"
CONF_NAME = "name"

DEFAULT_SLAVE_ID = 1
DEFAULT_BAUDRATE = 9600

# Full register map based on real working SDM630 configuration
# All values are 32-bit floats (2 registers), big-endian, input registers
REGISTER_MAP = {
    "phase_1_l_n_volts": {
        "address": 0,
        "name": "Phase 1 L/N Volts",
        "unit": "V",
        "device_class": "voltage",
        "state_class": "measurement",
        "precision": 2,
    },
    "phase_2_l_n_volts": {
        "address": 2,
        "name": "Phase 2 L/N Volts",
        "unit": "V",
        "device_class": "voltage",
        "state_class": "measurement",
        "precision": 2,
    },
    "phase_3_l_n_volts": {
        "address": 4,
        "name": "Phase 3 L/N Volts",
        "unit": "V",
        "device_class": "voltage",
        "state_class": "measurement",
        "precision": 2,
    },
    "phase_1_current": {
        "address": 6,
        "name": "Phase 1 Current",
        "unit": "A",
        "device_class": "current",
        "state_class": "measurement",
        "precision": 2,
    },
    "phase_2_current": {
        "address": 8,
        "name": "Phase 2 Current",
        "unit": "A",
        "device_class": "current",
        "state_class": "measurement",
        "precision": 2,
    },
    "phase_3_current": {
        "address": 10,
        "name": "Phase 3 Current",
        "unit": "A",
        "device_class": "current",
        "state_class": "measurement",
        "precision": 2,
    },
    "phase_1_power": {
        "address": 12,
        "name": "Phase 1 Power",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "precision": 2,
    },
    "phase_2_power": {
        "address": 14,
        "name": "Phase 2 Power",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "precision": 2,
    },
    "phase_3_power": {
        "address": 16,
        "name": "Phase 3 Power",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "precision": 2,
    },
    "total_system_power": {
        "address": 52,
        "name": "Total System Power",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "precision": 2,
    },
    "frequency": {
        "address": 70,
        "name": "Frequency",
        "unit": "Hz",
        "device_class": "frequency",
        "state_class": "measurement",
        "precision": 2,
    },
    "import_energy": {
        "address": 72,
        "name": "Import Energy",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "total_increasing",
        "precision": 2,
    },
    "export_energy": {
        "address": 74,
        "name": "Export Energy",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "total_increasing",
        "precision": 2,
    },
    "total_energy": {
        "address": 342,
        "name": "Total Energy",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "total",
        "precision": 2,
    },
    "neutral_current": {
        "address": 224,
        "name": "Neutral Current",
        "unit": "A",
        "device_class": "current",
        "state_class": "measurement",
        "precision": 2,
    },
    # You can add more later – e.g., THD, demand, per-phase energy, etc.
    # We start with the most useful ones
}

def get_validated_register_map() -> Dict[str, dict]:
    """Validate REGISTER_MAP and return it. Raises clear error on bad entries."""
    validated = {}
    required_keys = ["address", "name"]
    optional_keys = ["unit", "device_class", "state_class", "precision"]

    for key, info in REGISTER_MAP.items():
        if not isinstance(info, dict):
            raise ValueError(f"Register '{key}' is not a dict: {info}")

        for req in required_keys:
            if req not in info:
                raise ValueError(f"Register '{key}' missing required key '{req}'")

        if not isinstance(info["address"], int):
            raise ValueError(f"Register '{key}' address must be int: {info['address']}")

        # Set defaults
        validated_info = info.copy()
        validated_info.setdefault("precision", 2)
        validated_info.setdefault("state_class", "measurement")

        validated[key] = validated_info

    return validated

# Export the validated version
VALIDATED_REGISTER_MAP = get_validated_register_map()
