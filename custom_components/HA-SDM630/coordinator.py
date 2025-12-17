import struct
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from pymodbus.client import ModbusSerialClient

from .const import REGISTER_MAP

class SDM630Coordinator(DataUpdateCoordinator):
    def __init__(self, hass, port, slave_id, baudrate):
        super().__init__(
            hass,
            _LOGGER,
            name="SDM630",
            update_interval=timedelta(seconds=10),  # Adjustable later via options
        )
        self.client = ModbusSerialClient(
            port=port,
            baudrate=baudrate,
            parity="N",
            stopbits=1,
            bytesize=8,
            timeout=5,
        )
        self.slave_id = slave_id

    async def async_test_connection(self) -> bool:
        try:
            await self.hass.async_add_executor_job(self._read_registers, 0, 2)
            return True
        except:
            return False

    def _read_registers(self, start_addr: int, count: int):
        if not self.client.connected:
            self.client.connect()
        rr = self.client.read_input_registers(start_addr, count, slave=self.slave_id)
        if rr.isError():
            raise Exception(f"Modbus read error: {rr}")
        return rr.registers

    async def _async_update_data(self):
        try:
            new_data = {}
            for key, info in REGISTER_MAP.items():
                registers = await self.hass.async_add_executor_job(
                    self._read_registers, info["address"], 2
                )
                # Convert two 16-bit registers to 32-bit big-endian float
                raw = struct.pack(">HH", registers[0], registers[1])
                value = struct.unpack(">f", raw)[0]

                # Apply precision
                precision = info.get("precision", 2)
                if value is not None:
                    value = round(value, precision)

                new_data[key] = value

            return new_data
        except Exception as err:
            raise UpdateFailed(f"Failed to update SDM630 data: {err}")
