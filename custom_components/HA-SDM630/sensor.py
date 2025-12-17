from homeassistant.components.sensor import SensorEntity, SensorStateClass, SensorDeviceClass
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN, REGISTER_MAP
from .coordinator import SDM630Coordinator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    coordinator: SDM630Coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    for key, info in REGISTER_MAP.items():
        entities.append(
            SDM630Sensor(
                coordinator=coordinator,
                entry=entry,
                key=key,
                info=info,
            )
        )

    async_add_entities(entities)


class SDM630Sensor(SensorEntity):
    def __init__(self, coordinator: SDM630Coordinator, entry: ConfigEntry, key: str, info: dict):
        self._coordinator = coordinator
        self._key = key
        self._attr_unique_id = f"{entry.entry_id}_{key}"
        self._attr_name = f"{entry.title} {info['name']}"
        self._attr_native_unit_of_measurement = info.get("unit")
        self._attr_device_class = info.get("device_class")
        self._attr_state_class = info.get("state_class")

    @property
    def native_value(self):
        return self._coordinator.data.get(self._key)

    async def async_added_to_hass(self):
        self._coordinator.async_add_listener(self.async_write_ha_state)
