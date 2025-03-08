import threading
import os
from datetime import datetime
import numpy as np
from zaber_motion.ascii import Connection
from zaber_motion import Units
import sys
import time
import pythoncom  # Added for COM initialization

from horiba_ccd_interface import acquire_max_intensity

stop_flag = False

def start_program():
    global move_units, disp_units, hor_dis, hor_step, ver_dis, ver_step, hor_home, ver_home, sleep_time
    global stop_flag

    #move_units = Units.LENGTH_MILLIMETRES
    #disp_units = Units.LENGTH_MILLIMETRES
    move_units = Units.LENGTH_MICROMETRES
    isp_units = Units.LENGTH_MICROMETRES

    hor_dis = 5  # maximum travel distance 75 mm
    hor_step = 1
    ver_dis = 5  # maximum travel distance 25 mm
    ver_step = 1
    hor_home = 52711.85
    ver_home = 12820.17
    
    sleep_time = 3  # time in seconds

    arr_x = int(hor_dis / hor_step)
    arr_y = int(ver_dis / ver_step)

    global X_coor, T_coor, intensity_data
    X_coor = np.zeros((arr_y, arr_x))
    T_coor = np.zeros((arr_y, arr_x))
    intensity_data = np.zeros((arr_y, arr_x))

    thread = threading.Thread(target=run_program)
    thread.start()

def stop_program():
    global stop_flag
    stop_flag = True
    print("Stopping program...")

def run_program():
    global stop_flag
    x = datetime.now()
    
    # Initialize COM for this thread
    pythoncom.CoInitialize()
    
    folder_dat = os.path.join(
        "C:/Users\hnakamur/Box Sync/Nakamura_Lab/Users/Sudeep/SHG_Measurements/Data for SHG/From_Syncereity_Camera/2025_03_27/SHG mapping Data",
        x.strftime("20%y_%m_%d")
    )

    os.makedirs(folder_dat, exist_ok=True)

    file_name = "SHG_Map_SnS68b_I1_0_deg" + str(x.strftime("20%y_%m_%d_%H%M%S")) + ".txt"
    filepath = os.path.join(folder_dat, file_name)

    with open(filepath, "a+") as data_file:
        data_file.write("Hor-psn\tVer-psn\tMax-Intensity\n")

        with Connection.open_serial_port("COM5") as connection:
            device_list = connection.detect_devices()
            if len(device_list) < 2:
                print("Error: Less than 2 devices found. Check connections.")
                return
            
            print(f"Detected {len(device_list)} devices: {device_list}")
            
            deviceX = device_list[0]
            deviceT = device_list[1]
            
            axisX = deviceX.get_axis(1)
            axisT = deviceT.get_axis(1)

            if axisT is None or axisX is None:
                print("Error: One of the device axes could not be accessed!")
                return

            print(f"axisX: {axisX}, axisT: {axisT}")

            print("Homing Device 2 (T)")
            axisX.move_absolute(ver_home, move_units)
            axisT.move_absolute(ver_home, move_units)

            for i in range(int(ver_dis / ver_step)):
                if stop_flag:
                    print("Program stopped.")
                    return

                position_T = axisT.get_position(move_units)
                axisX.move_absolute(hor_home, move_units)
                print("Device 1 (X) returned to home position")

                for j in range(int(hor_dis / hor_step)):
                    if stop_flag:
                        print("Program stopped.")
                        return

                    position_X = axisX.get_position(move_units)

                    X_coor[i, j] = position_X
                    T_coor[i, j] = position_T
                    
                    max_intensity = acquire_max_intensity(ccd_id="CCD2", integration_time=5, mode="spec")
                    intensity_data[i, j] = max_intensity
                    # time.sleep(2)
                    
                    data_file.write(f"{position_X}\t{position_T}\t{max_intensity}\n")
                    print(f"X position: {position_X}, T position: {position_T}, Max intensity: {max_intensity}")

                    axisX.move_relative(hor_step, move_units)
                    # time.sleep(sleep_time)

                axisT.move_relative(ver_step, move_units)

start_program()