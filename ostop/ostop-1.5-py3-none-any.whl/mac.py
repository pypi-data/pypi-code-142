"""file to hold all files related to running top on Mac"""

# needed imports
import psutil
from datetime import datetime
from hurry.filesize import size

# create objects
now = datetime.now()


class OverallOSInfo:
    """A class to neatly grab the information about the overall OS."""

    def get_numProcesses(self) -> (int):
        return len(list(psutil.process_iter()))

    def get_loadAverages(self):
        return psutil.getloadavg()

    def get_cpuUsage(self):
        return psutil.cpu_times()

    def get_overallCPUPerc(self):
        # return the average CPU percentage
        # to be used for later calculations
        return 4.89

    def get_overallCPUUsage(self) -> (int):
        cpu_usage = psutil.cpu_times()
        overall = sum(cpu_usage)
        return overall

    def get_virtCPUCount(self) -> (int):
        return psutil.cpu_count()

    def get_physCPUCount(self) -> (int):
        return psutil.cpu_count(logical=False)

    def get_numUsers(self) -> (int):
        return len(psutil.users())

    def get_bootTime(self):
        return datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    def get_physMem(self):
        return psutil.virtual_memory()

    def get_virtMem(self) -> (str):
        return size(psutil.virtual_memory().total)

    def get_swapMem(self):
        return psutil.swap_memory()

    def get_networkInfo(self):
        return psutil.net_io_counters()

    def get_diskInfo(self):
        return psutil.disk_io_counters()


def process_stats():
    """Function to calculate order of processes in top command."""

    # create process list and initializations of needed func variables
    processes = []
    sleeping = 0
    running = 0
    threads = 0

    os = OverallOSInfo()
    overallCPUPerc = os.get_overallCPUPerc()

    # calculate various statistics over every process
    # psutil can grab
    for process in psutil.process_iter():

        name = ""
        user = ""
        status = ""
        cpuPerc = 0

        try:
            # PID
            id = process.pid

            # try to calculate the CPU % usage
            # sum up memory usage and divide for CPU %
            proc = psutil.Process(id)
            cpuPerc = ((proc.memory_info()[0] / 2.0**30) / overallCPUPerc) * 100

            # process name
            name = process.name()

            # status
            status = process.status()

            # get username that process is from
            user = process.username()

        except:
            cpuPerc = 0

        if process.status() == "sleeping":
            # count process if it is sleeping
            sleeping += 1
        elif process.status() == "running":
            # count process if it is running
            running += 1

        try:
            # count all threads from the process if able
            threads += process.num_threads()
        except:
            threads += 0

        # calculate the time that the process begin running
        start = datetime.fromtimestamp(process.create_time())

        # get the current time
        current = datetime.now()

        # calculate the difference between the process
        # start time and the current time
        difference = current - start

        # change the time difference into a usable format
        seconds = int(difference.total_seconds())
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        # concatenate together the calculated difference
        formatted_time = str(hours) + ":" + str(minutes) + ":" + str(seconds)

        # create a list in the list containing the calculated process info
        processes.append(
            [id, name[:12], round(cpuPerc, 2), formatted_time, user[:11], status]
        )

    # order the list in descending order of cpu percentage
    processes.sort(key=lambda processes: processes[2], reverse=True)

    # return calculated metrics
    return processes, sleeping, running, threads, current


def mactop():
    """Function to compile all diagnostic information into a organized display."""

    os = OverallOSInfo()

    processes, sleeping, running, threads, currentTime = process_stats()

    print(
        f"Processes: {os.get_numProcesses()} total, {running} running, {sleeping} sleeping, {threads} threads",
        "{:>20}".format(currentTime.strftime("%H:%M:%S")),
    )

    load_averages = os.get_loadAverages()
    cpu_usage = os.get_cpuUsage()
    overall_usage = os.get_overallCPUUsage()

    print(
        f"Load Avg: {round(load_averages[0], 2)}, {round(load_averages[1], 2)}, {round(load_averages[2], 2)}  CPU usage: {round((cpu_usage[0]/overall_usage) * 100, 2)}% user, {round((cpu_usage[2]/overall_usage) * 100,2)}% sys, {round((cpu_usage[3]/overall_usage) * 100,2)}% idle"
    )

    print(
        f"CPU counts: {os.get_virtCPUCount()} total, {os.get_physCPUCount()} physical  Users: {os.get_numUsers()}  Boot Time: {os.get_bootTime()}"
    )

    physmem = os.get_physMem()

    print(
        f"PhysMem: {os.get_virtMem()} used, {size(physmem[7])} wired, {physmem[5]} inactive."
    )

    swap = os.get_swapMem()

    print(f"VM: {os.get_virtMem()} vsize, {swap[4]}(0) swapins, {swap[5]}(0) swapouts")

    network_info = os.get_networkInfo()

    print(
        f"Networks: packets: {network_info[3]}/{size(network_info[3])} in, {network_info[2]}/{size(network_info[2])} out."
    )

    disk_info = os.get_diskInfo()

    print(
        f"Disks: {disk_info[0]}/{size(disk_info[0])} read, {disk_info[1]}/{size(disk_info[1])} written"
    )

    # lower section print
    print("\nPID       COMMAND    CPU%   TIME       USER     STATUS")
    for i in range(14):
        proc = processes[i]
        print("{: <7} {: <12} {: <5} {: <8} {: <11} {: <10}".format(*proc))
