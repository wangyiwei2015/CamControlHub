# v1.0.0

from SerialController import Hardware
from MainWindow import Application
import _thread
from time import sleep

info = '''
'''

def main():
    def run(portIn: str):
        global port
        port = portIn
        _thread.start_new_thread(arduinoLoop,())

    def arduinoLoop():
        arduino = Hardware(port=port)
        app.fire = lambda s: arduino.invoke(s)
        '''while True:
            arduino.invoke(input(info))'''

    devices = Hardware.find()
    app = Application(devices)
    app.callback = lambda port: run(port)
    app.start()

if __name__ == '__main__':
    main()
