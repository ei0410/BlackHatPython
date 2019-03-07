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
        print("Connect PS3!")
        break
    except IOError:
        controler = False

try:
    with open(device_path, "rb") as device:
        event = device.read(EVENT_SIZE)
        while event:
            (ds3_time, ds3_val, ds3_type, ds3_num) = struct.unpack(EVENT_FORMAT, event)
            if ds3_type == 1:
    		# if you want to use lease mode button, change ds3_val == 1 to ds3_val == 0
    		    if ds3_num == 4  and ds3_val == 1:
    		    	print("UP")
    		    if ds3_num == 5  and ds3_val == 1:
    		    	print("RIGHT")
    		    if ds3_num == 6  and ds3_val == 1:
    		    	print("DOWN")
    		    if ds3_num == 7  and ds3_val == 1:
    		    	print("LEFT")
    		    if ds3_num == 12 and ds3_val == 1:
    		    	print("triangle")
    		    if ds3_num == 13 and ds3_val == 1:
    		    	print("circle")
    		    if ds3_num == 14 and ds3_val == 1:
    		    	print("cross")
    		    if ds3_num == 15 and ds3_val == 1:
    		    	print("square")
    		    if ds3_num == 10 and ds3_val == 1:
    		    	print("L1")
    		    if ds3_num == 1  and ds3_val == 1:
    		    	print("L3")
    		    if ds3_num == 11 and ds3_val == 1:
    		    	print("R1")
    		    if ds3_num == 2  and ds3_val == 1:
    		    	print("R3")
    		    if ds3_num == 0  and ds3_val == 1:
    		    	print("SELECT")
    		    if ds3_num == 3  and ds3_val == 1:
    		    	print("START")
    		    if ds3_num == 16 and ds3_val == 1:
    		    	print("PS")
    		    	#break
                    
            if ds3_type == 2:
                if ds3_num == 0:
                    print("LeftHatX  %d" % ds3_val)
                if ds3_num == 1:
                    print("LeftHatY  %d" % ds3_val)
                if ds3_num == 2:
                    print("RightHatX %d" % ds3_val)
                if ds3_num == 3:
                    print("RightHatY %d" % ds3_val)
                if ds3_num == 12:
                    print("L2 %d" % ds3_val)
                if ds3_num == 13:
                    print("R2 %d" % ds3_val)
            #print( "{0}, {1}, {2}, {3}".format( ds3_time, ds3_val, ds3_type, ds3_num ) )
            event = device.read(EVENT_SIZE)

except IOError:
    print("can not connect controler")
    sys.exit(1)
