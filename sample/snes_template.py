import struct
import sys

device_path = "/dev/input/js0"
EVENT_FORMAT = "LhBB";
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

controler = False
while True:
    try:
        with open(device_path, "rb") as device:
            event = device.read(EVENT_SIZE)
        print("Connect snes!")
        break
    except IOError:
        controler = False

try:
    with open(device_path, "rb") as device:
        event = device.read(EVENT_SIZE)
        while event:
            (ds3_time, ds3_val, ds3_type, ds3_num) = struct.unpack(EVENT_FORMAT, event)
            # if you want to use lease mode button, change ds3_val == 1 to ds3_val == 0
            if ds3_type == 1 and ds3_num == 0 and ds3_val == 1:
                print("A")
            if ds3_type == 1 and ds3_num == 1 and ds3_val == 1:
                print("B")
            if ds3_type == 1 and ds3_num == 2 and ds3_val == 1:
                print("X")
            if ds3_type == 1 and ds3_num == 3 and ds3_val == 1:
                print("Y")
            if ds3_type == 1 and ds3_num == 4 and ds3_val == 1:
                print("L")
            if ds3_type == 1 and ds3_num == 5 and ds3_val == 1:
                print("R")
            if ds3_type == 1 and ds3_num == 6 and ds3_val == 1:
                print("SELECT")
            if ds3_type == 1 and ds3_num == 7 and ds3_val == 1:
                print("START")
            if ds3_type == 2 and ds3_num == 1 and ds3_val == -32767:
                print("UP")
            if ds3_type == 2 and ds3_num == 1 and ds3_val == 32767:
                print("DOWN")
            if ds3_type == 2 and ds3_num == 0 and ds3_val == -32767:
                print("LEFT")
            if ds3_type == 2 and ds3_num == 0 and ds3_val == 32767:
                print("RIGHT")
            event = device.read(EVENT_SIZE)

except IOError:
    print("can not connect controler")
    sys.exit(1)
