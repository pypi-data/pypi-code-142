import platform
import psutil
import pandas as pd
import time
import getopt
import logging
import logging.handlers 
import sys
import verboselogs

logger = verboselogs.VerboseLogger('demo')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

# Command line option defaults.
verbosity = 0

# Parse command line options.
opts, args = getopt.getopt(sys.argv[1:], 'vqh', ['verbose', 'quiet', 'help'])

# Map command line options to variables.
for option, argument in opts:
    if option in ('-v', '--verbose'):
        verbosity += 1
    elif option in ('-q', '--quiet'):
        verbosity -= 1
    elif option in ('-h', '--help'):
        print(__doc__.strip())
        sys.exit(0)
    else:
        assert False, "Unhandled option!"

# Configure logger for requested verbosity.
if verbosity >= 4:
    logger.setLevel(logging.SPAM)
elif verbosity >= 3:
    logger.setLevel(logging.DEBUG)
elif verbosity >= 2:
    logger.setLevel(logging.VERBOSE)
elif verbosity >= 1:
    logger.setLevel(logging.NOTICE)
elif verbosity < 0:
    logger.setLevel(logging.WARNING)

class Stream_data_analyser:
    def __init__(self):
        self.current_time=[]
        self.Computer_network_name=[]
        self.Machine_type=[]
        self.Processor_type=[]
        self.Platform_type=[]
        self.Operating_system=[]
        self.Operating_system_release=[]
        self.Operating_system_version=[]
        self.Number_of_physical_cores=[]
        self.Number_of_logical_cores=[]
        self.Current_CPU_frequency=[]
        self.Min_CPU_frequency=[]
        self.Max_CPU_frequency=[]
        self.Current_CPU_utilization=[]
        self.Current_per_CPU_utilization=[]
        self.Total_RAM_installed=[]
        self.Available_RAM=[]
        self.Used_RAM=[]
        self.RAM_usage=[]
        self.current_battery_percent=[]
        self.battery_plugged_status=[]
        

    def get_machine_info(self):
        try:
            t = time.localtime()
            self.current_time.append(time.strftime("%H:%M:%S", t))

            #Computer network name
            self.Computer_network_name.append(platform.node())
            
            #Machine type
            self.Machine_type.append(platform.machine())
            
            #Processor type
            self.Processor_type.append(platform.processor())
            
            #Platform type
            self.Platform_type.append(platform.platform())
            
            #Operating system
            self.Operating_system.append(platform.system())
            
            #Operating system release
            self.Operating_system_release.append(platform.release())
            
            #Operating system version
            self.Operating_system_version.append(platform.version())
            
            machine_info_df=pd.DataFrame(list(zip(self.current_time, self.Computer_network_name, self.Machine_type, self.Processor_type, self.Platform_type, self.Operating_system, self.Operating_system_release, self.Operating_system_version)),
                            columns=['Current Time','Computer network name', 'Machine_type', 'Processor_type', 'Platform_type', 'Operating_system', 'Operating_system_release', 'Operating_system_version'])
            
            print(machine_info_df)
        except:
            print("this is exception")

  
    def get_core_info(self):
        try:
            t = time.localtime()
            self.current_time.append(time.strftime("%H:%M:%S", t))
            
            #Physical cores
            self.Number_of_physical_cores.append(psutil.cpu_count(logical=False))
            
            #Logical cores
            self.Number_of_logical_cores.append(psutil.cpu_count(logical=True))
            
            Core_info_df=pd.DataFrame(list(zip(self.current_time, self.Number_of_physical_cores, self.Number_of_logical_cores)),
                            columns=['Current Time', 'Number_of_physical_cores', 'Number_of_logical_cores'])
            
            print(Core_info_df)
            
        except:
            print("This is exception")
        
  
    def get_CPU_freq_info(self):
        try:
            t = time.localtime()
            self.current_time.append(time.strftime("%H:%M:%S", t))
            
            #Current frequency
            self.Current_CPU_frequency.append(psutil.cpu_freq().current)
            
            #Min frequency
            self.Min_CPU_frequency.append(psutil.cpu_freq().min)
            
            #Max frequency
            self.Max_CPU_frequency.append(psutil.cpu_freq().max)
            
            CPU_freq_info_df=pd.DataFrame(list(zip(self.current_time, self.Current_CPU_frequency, self.Min_CPU_frequency, self.Max_CPU_frequency)),
                            columns=['Current Time', 'Current_CPU_frequency', 'Min_CPU_frequency', 'Max_CPU_frequency'])
            
            print(CPU_freq_info_df)
            
        except:
            print("This is exception")
    
    def get_CPU_util_info(self):
        try:
            t = time.localtime()
            self.current_time.append(time.strftime("%H:%M:%S", t))
            
            #System-wide CPU utilization
            self.Current_CPU_utilization.append(psutil.cpu_percent(interval=1))
            
            #System-wide per-CPU utilization
            self.Current_per_CPU_utilization.append(psutil.cpu_percent(interval=1, percpu=True))
            
            CPU_util_info_df=pd.DataFrame(list(zip(self.current_time, self.Current_CPU_utilization, self.Current_per_CPU_utilization)),
                            columns=['Current Time', 'Current CPU utilization', 'Current per CPU utilization'])
            
            print(CPU_util_info_df)
            
        except:
            print("This is exception")
    
    def get_RAM_info(self):
        try:
            t = time.localtime()
            self.current_time.append(time.strftime("%H:%M:%S", t)) 
            
            #Total RAM
            self.Total_RAM_installed.append(round(psutil.virtual_memory().total/1000000000, 2))

            #Available RAM
            self.Available_RAM.append(round(psutil.virtual_memory().available/1000000000, 2))
            
            #Used RAM
            self.Used_RAM.append(round(psutil.virtual_memory().used/1000000000, 2))

            #RAM usage
            self.RAM_usage.append(psutil.virtual_memory().percent)
            
            RAM_info_df=pd.DataFrame(list(zip(self.current_time, self.Total_RAM_installed, self.Available_RAM, self.Used_RAM, self.RAM_usage)),
                            columns=['Current Time', 'Total RAM installed', 'Available RAM', 'Used RAM', 'RAM usage'])
            
            print(RAM_info_df)
            
        except:
            print("This is exception")
    
    def get_battery_info(self):
        try:
            t = time.localtime()
            self.current_time.append(time.strftime("%H:%M:%S", t))
            
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            self.current_battery_percent.append(battery.percent)
            self.battery_plugged_status.append("Plugged In" if plugged else "Not Plugged In")
            
            battery_info_df=pd.DataFrame(list(zip(self.current_time, self.current_battery_percent, self.battery_plugged_status)),
                            columns=['Current Time', 'current battery', 'battery plugged status'])
            
            print(battery_info_df)
        except:
            print("This is exception")
            
    


