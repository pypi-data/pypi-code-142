import object_oriented_script
import time


def final_result(time_stamp, repeatation_time):
    try:
        time_in_sec=time_stamp*60
        
        for t in range(int(time_in_sec/repeatation_time)):
            print(f'------------------------------------reading {t+1}--------------------------------------')
            if __name__ == "__main__":
                obj = object_oriented_script.Stream_data_analyser()
                print('Machine Information')
                obj.get_machine_info()
                print('Core Information')
                obj.get_core_info()
                print('RAM Information')
                obj.get_RAM_info()
                print('CPU Frequency Information')
                obj.get_CPU_freq_info()
                print('CPU Utilization Information')
                obj.get_CPU_util_info()
                print('Battery Information')
                obj.get_battery_info() 
                time.sleep(repeatation_time-2)
                t=t+1
    except:
        print('This is an exception!')