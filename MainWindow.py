import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkmsg


class Application:
    window = None
    box = None
    button = None

    def __init__(self, devices: list):
        self.window = tk.Tk()
        self.window.title('CamControlHub')
        self.window.geometry("250x105")

        if len(devices) < 2:
            self.errorWindow("设备未连接")

        self.box = ttk.Combobox(self.window)
        self.box.pack(padx=40, pady=15)
        deviceList = devices
        self.box['value'] = tuple(deviceList)
        self.box.current(0)

        self.button = ttk.Button(self.window,
                                 text='连接',
                                 command=self.onConnectAction)
        self.button.pack(padx=40, pady=10)

        for i in range(1, 11):
            ttk.Button(self.window,
                       text='1/' + str(10 * i),
                       command=self.fireMaker(i)
                       ).pack()

    def callback(self, i):
        print('Error: callback method not implemented. Parameter: ', i)

    def fire(self, i):
        print(i)

    def fireMaker(self, i):
        return lambda: self.fire(i)

    def onConnectAction(self):
        if self.box.current() == 0:
            self.errorWindow("连接失败，请检查设备/端口有效性")
            return
        self.box.configure(state='disabled')
        self.button.configure(state='disabled')
        # self.window.state('icon')  # 最小化
        # self.window.withdraw()#隐藏窗口
        self.callback(str(self.box.get()))

    def start(self):
        self.window.mainloop()

    def errorWindow(self, err: str):
        tkmsg.showwarning("错误", err)
        exit(-1)
        return
