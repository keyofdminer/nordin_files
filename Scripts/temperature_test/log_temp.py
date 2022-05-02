from time import sleep
import datetime
import logging
import serial
import json
import serial.serialutil
import serial.tools.list_ports
from keyence import Keyence
from galil import Galil


class adafruit_adt7410_reader(serial.Serial):
    def __init__(self, hwid='PID=16C0:0483 SER=1431350', verbose=False):
        super().__init__(baudrate=115200, timeout=2)        # create a serial object to open the port with
        self.verbose = verbose
        self.hwid = hwid
        self.port = None
        self.port, self.hwid = findUsbPort(self.hwid)       # find the device we are looking for
        if self.port is None:
            raise ValueError('ItsyBitsy M4 not found')
        if self.is_open:
            self.close()
        self.open()                                         # open the port and flush all buffers
        self.reset_input_buffer()
        self.reset_output_buffer()
        print("Connected to {} at {}".format(self.hwid, self.port))

    def transmit(self, cmd):
        self.write(bytes(cmd + '\r', encoding='ascii'))     # write to serial tx buffer
        return self.receive()                               # wait for response from serial rx buffer

    def receive(self):
        response = b''
        response += self.readline()                         # wait for the first line to fill in the rx buffer
        while self.in_waiting:                              # while there is more data in the rx buffer
            response += self.readline()                     # read next line from rx buffer
        return response.decode().rstrip()                   # return decoded byte response (as string with newlines stripped)

def findUsbPort(hwid):
    ports = list(serial.tools.list_ports.comports())        # list all available serial ports
    for p in ports:
        print(p.hwid)
        if hwid in p.hwid:                                  # find the matching hardware ID
            return (p.device, p.hwid)                       # return a handle to the device and the full hardware ID string
    return None                                             # return none if the device is not found

if __name__ == '__main__':
    with open("hardware_configuration.json", "r") as file_handle:
        config_dict = json.load(file_handle)
    config_dict = config_dict["MR1v1"]
    
    galil = Galil(
        config_dict=config_dict["galil_settings"], log_level=logging.ERROR
    )
    galil.connect()
    galil.initialize()
    galil.home()

    galil.absMove(cnts=-500000, speed=100, axis="X")
    galil.absMove(cnts=-1350000, speed=100, axis="Y")
    galil.absMove(mm=47.300, speed=100, axis="Z")
    galil.goToZmax()


    a = adafruit_adt7410_reader()
    keyence_sensor = Keyence(log_level=logging.ERROR)
    filename = datetime.datetime.now().strftime("temperature_log_%Y_%m_%d-%H_%M_%S")+".log"
    with open(filename, 'a') as the_file:
        the_file.write(f"timestamp,sensor1,sensor1c,sensor1f,sensor2,sensor2c,sensor2f,sensor3,sensor3c,sensor3f,sensor4,sensor4c,sensor4f,keyence\n")
    while True:
        with open(filename, 'a') as the_file:
            try:
                time_string = datetime.datetime.now().strftime('%m/%d/%Y_%H:%M:%S.%f')
                keyence_measurement = keyence_sensor.read_all()[1]
                data = a.transmit("GET")
                print(f"{time_string} {data} {keyence_measurement}")
#                the_file.write(time_string + data + f"Keyence: {keyence_measurement}" + "\n")
                the_file.write(f"{time_string},{data},{keyence_measurement},\n".replace(";", ","))
                sleep(2)
            except KeyboardInterrupt:
                exit(0)                                     # exit cleanly when killed by user input
