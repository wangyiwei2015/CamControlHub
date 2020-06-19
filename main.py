# v1.0.0

from SerialController import Hardware
from MainWindow import Application
import _thread
from time import sleep

info = '''
'''


class Instance:
    arduino = None
    port = None
    app = None

    def __init__(self):
        devices = Hardware.find()
        self.app = Application(devices)
        self.app.callback = lambda p: self.run(p)
        self.app.start()

    def run(self, portIn: str):
        self.port = portIn
        _thread.start_new_thread(self.arduinoLoop, ())

    def arduinoLoop(self):
        self.arduino = Hardware(port=self.port)
        self.app.fire = lambda s: self.arduino.invoke(s)


def main():
    Instance()


if __name__ == '__main__':
    main()
