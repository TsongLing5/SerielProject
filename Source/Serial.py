import _thread
import serial
import time
# import thread

SerialPort='/dev/tty.wchusbserial1410'

class MSerialPort:
    message = ''
    status = 0   #close

    def __init__(self, port, buand):
        self.port = serial.Serial(port, buand)
        if not self.port.isOpen():
            self.status = 1
            pass
            # self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()
            self.status=1
            print('Opening serial!')

    def port_close(self):
        self.port.close()
        self.status=0
        print('Closing serial!')

    def send_data(self, data):
        number = self.port.write(data)
        return number

    def getPortStatus(self):
        return self.port.is_open


    def read_data(self):
        while True:
            data = self.port.readline()
            print(data)
            self.message += data

    def getData(self):
        return self.message


if __name__ == '__main__':
    pass
    mSerial = MSerialPort(SerialPort, 115200)
    mSerial.port_open()
    _thread.start_new_thread(mSerial.read_data, ())
    while True:
        time.sleep(1)

        if(mSerial.message):
            pass
            # print(mSerial.message)
            # mSerial.message=''
        # print("mSerial.message")
