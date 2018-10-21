# import serial
#
# ser=serial.Serial("/dev/tty.wchusbserial1420",115200,timeout=0.5) #使用USB连接串行口
# # print(ser.name)     #测试用
# ser.open
# while(1):
#     s = ser.read(14)
#     print(s)
#
import threading
import tkinter
from concurrent.futures import thread
from tkinter import *

# from serial import serial
from tkinter import messagebox, ttk
from tkinter import ttk

import ctypes

import _thread
import serial
import time

from Source.Serial import MSerialPort

baud=['115200','19200','14400','9600']
SerialPort='/dev/tty.wchusbserial1410'

global ser
global window
global conbt
global baudChosen
global mBaud
global humi,temp
global mSerial
global td

def init():
    global ser
    global window
    global conbt
    global humi, temp
    global baudChosen
    global mBaud
    global mSerial
    global tSerial
    global td

    mBaud=115200
    # ser = serial.Serial(SerialPort, mBaud, timeout=0.5)  # 使用USB连接串行口
    mSerial = MSerialPort(SerialPort, mBaud)

    td = threading.Thread(target=mSerial.read_data)
    td.setDaemon(True)
    td.start()

    timer = threading.Timer(5, SerialTimer)
    timer.start()
    # thread_read = threading.Thread(target=mSerial.read_data)
    # thread_read.setDaemon(True)
    # thread_read.start()

    # tSerial = threading.Thread(target=mSerial.read_data, args=())
    # timer = threading.Timer(1, SerialTimer())
    # timer.start()

    # ser.close()
    window = tkinter.Tk()


    window.title('温湿度计')
    window.geometry('200x200')


    temp=Label(window,text='温度：......')
    temp.pack()
    humi=Label(window,text='湿度：......')
    humi.configure(bg = "dark green")
    humi.pack()


    # center_window(window, 300, 240)

    # Listbox code
    # list = Listbox(window)
    # # list.grid()
    # for it in baud:
    #     list.insert(END, it)
    # list.pack()


    # combobox code
    # combVal=tkinter.StringVar
    # comboxList=ttk.ComboBox(window,textvariable=combVal)
    #
    # comboxList["values"] = ("1", "2", "3", "4")
    # comboxList.current(0)
    # comboxList.bind("<<ComboboxSelected>>", callback)
    # comboxList.pack()

#################Chose Baud component
    baudrate = tkinter.StringVar()
    baudChosen = ttk.Combobox(window, width=12, textvariable=baudrate,state='readonly')
    baudChosen['values'] = baud  # 设置下拉列表的值
    baudChosen.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
    baudChosen.bind("<<ComboboxSelected>>",getBaud)
    baudChosen.current(0)
    baudChosen.pack()


########## 连接断开按钮的button
    # if(mSerial.status):
    #     str='连接1'
    # else:
    #     str='断开1'
    conbt = Button(window, text=str,command=serialCrt)
    changeSerialSts()
    conbt.pack()
    # disbt = Button(window, text='断开连接', command=disconnectSerial)
    # disbt.pack()

    get = Button(window, text='get',command=read)  #NOP
    get.pack()

    window.maxsize(1200, 600)
    window.minsize(600, 240)
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

#     pass
#
# def onSerial():
#     while(1):
#
#         data=ser.read(14)
#         print(data)
#         if(data):
#             print(data)
#         else:
#             print('null')
#         time.sleep(500)
#         # read()

def getBaud(*args):
    defaultBaud=baudChosen.get()
    # print('baud is 00')
    print(str(defaultBaud))


def changeSerialSts():
    global mSerial
    if(mSerial.getPortStatus()):
        conbt.configure(text='断开')
        # print('isOpen')
        # ser.close()
    else:
        conbt.configure(text='连接')
        # print('isClosed')
        # ser.open()

def serialCrt():
    global mSerial
    global td
    # global tSerial
    if(mSerial.getPortStatus()):
        mSerial.port_close()
        # _thread.exit()
        # tSerial._stop()
        # td.stop()
        # _thread.exit_thread()

        print('close serial')
    else:
        print('BBaud:'+str(mBaud))
        mSerial.port_open()

        # _thread.start_new_thread(mSerial.read_data, ())


        # mSerial.port_open()

        # tSerial.start()
        # _thread.start_new_thread(mSerial.read_data, ())
        print('try to open')
    changeSerialSts()

def disconnectSerial():
    global mSerial
    mSerial.port_close()
    changeSerialSts()

def read():
    global mSerial
    if(mSerial.getPortStatus()):
        # s=ser.read(14)
        print(mSerial.message)
    else:
        print('Serial is closed!')

def SerialTimer():
    t=str(mSerial.message[0:4],encoding = "utf-8")
    h=str(mSerial.message[7:11],encoding="utf-8")
    temp.configure(text='湿度：'+t+' %rh')
    humi.configure(text='温度：'+h+' ℃ ')
    print('我是定时器')
    print(mSerial.message)
    timer = threading.Timer(5.5, SerialTimer)
    timer.start()

#######while exit the program,close serial
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        # pass
        # if(s)
        if(mSerial.getPortStatus()):
            pass
        else:
            disconnectSerial()
            print("close successful!")
        window.destroy()
# def SerialTimer():
#     global timer
#     global mSerial
#     print(mSerial.getData())
#
#     timer = threading.Timer(5.5, SerialTimer)
#     timer.start()

if __name__ == '__main__':
# if __name__=='__main__':
    init()
    # thread.start_new_thread(onSerial,())
    # while(TRUE):
    # t = threading.Thread(target=onSerial, name='serialHandle')
    # t.start()
    # t.join()
    # mSerial.open()


    # while(1):
        # time.sleep(5)
        # print("print suuce")
        #
        # print('huoq'+mSerial.getData())
    # while(1):
    #     pass
    #     time.sleep(500)
    #     data=ser.read(14)
    #     print(data)

