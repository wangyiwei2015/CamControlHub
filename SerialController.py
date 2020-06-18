import serial
import serial.tools.list_ports

class Hardware:
    s = serial.Serial()
    def __init__(self, port: str):
        self.s.port = port
        self.s.baudrate = 115200
        self.s.open()

    def invoke(self, shutter: str):
        self.s.write(shutter.encode())

    @classmethod
    def find(cls) -> list:
        availables = ["请选择设备"]
        for device in serial.tools.list_ports.comports():
            availables.append(device.device)
        return availables