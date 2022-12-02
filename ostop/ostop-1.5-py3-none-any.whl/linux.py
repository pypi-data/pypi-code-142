"""file to hold all files related to running top on Linux"""

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

    def get_overallCPUUsage(self) -> (int):
        cpu_usage = psutil.cpu_times()
        overall = sum(cpu_usage)
        return overall

    def get_overallCPUPerc(self):
        # return the average CPU percentage
        # to be used for later calculations
        return 4.89

    def get_memRegions(self):
        # only the rss is available through psutil on Windows
        p = psutil.Process()
        mem = p.memory_maps()

        total_mem_regions = 0
        rss_mem_regions = 0
        private_mem_regions = 0

        # iterate through all memory_map enteries and grab wanted values
        for i in range(len(mem)):
            total_mem_regions += mem[i][1]
            rss_mem_regions += mem[i][2]
            private_mem_regions += mem[i][3]

        return total_mem_regions, rss_mem_regions, private_mem_regions

    def get_virtMem(self):
        return psutil.virtual_memory()

    def get_swapMem(self):
        return psutil.swap_memory()

    def get_networkInfo(self):
        return psutil.net_io_counters()

    def get_diskInfo(self):
        return psutil.disk_io_counters()


def process_stats():
    """This function calculates the order of processes in terms of CPU%"""

    # create process list and initializations of needed variables
    processes = []
    sleeping = 0
    running = 0
    threads = 0

    os = OverallOSInfo()
    overallCPUPerc = os.get_overallCPUPerc()

    # iterate through all processes and grab info for all
    for process in psutil.process_iter():

        name = ""
        user = ""
        status = ""
        cpuPerc = 0

        try:
            # pid
            id = process.pid

            # process name
            name = process.name()

            # status
            status = process.status()

            # username
            user = process.username()

            # calculate CPU perc
            proc = psutil.Process(id)
            cpuPerc = ((proc.memory_info()[0] / 2.0**30) / overallCPUPerc) * 100

        except:
            pass

        # sleeping or running
        if process.status() == "sleeping":
            # count process if it is sleeping
            sleeping += 1
        elif process.status() == "running":
            # count process if it is running
            running += 1

        # threads
        try:
            # count all threads from the process if able
            threads += process.num_threads()
        except:
            threads += 0

        # time running
        start = datetime.fromtimestamp(process.create_time())
        current = datetime.now()

        difference = current - start

        # change the time difference into a usable format
        seconds = int(difference.total_seconds())
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        # concatenate together the calculated difference
        formatted_time = str(hours) + ":" + str(minutes) + ":" + str(seconds)

        # add process info to process list
        # create a list in the list containing the calculated process info
        processes.append(
            [id, name[:12], round(cpuPerc, 2), formatted_time, user, status]
        )

    # order the list in descending order of cpu percentage
    processes.sort(key=lambda processes: processes[2], reverse=True)

    # return list and other metrics
    return processes, sleeping, running, threads, current


def linuxtop():
    """This function compiles all diagnostic info and prints it to the terminal"""

    os = OverallOSInfo()

    processes, sleeping, running, threads, currentTime = process_stats()

    print(
        f"Processes: {os.get_numProcesses()} total, {running} running, {sleeping} sleeping, {threads} threads",
        "{:>20}".format(currentTime.strftime("%H:%M:%S")),
    )

    load_avg = os.get_loadAverages()
    cpu_usage = os.get_cpuUsage()
    overall_usage = os.get_overallCPUUsage()
    print(
        f"Load Avg: {round(load_avg[0], 2)}, {round(load_avg[1], 2)}, {round(load_avg[2], 2)}  CPU usage: {round((cpu_usage[0]/overall_usage) * 100, 2)}% user, {round((cpu_usage[2]/overall_usage) * 100,2)}% sys, {round((cpu_usage[3]/overall_usage) * 100,2)}% idle"
    )

    total_mem_regions, rss_mem_regions, private_mem_regions = os.get_memRegions()
    print(
        f"MemRegions: {total_mem_regions} total, {rss_mem_regions} resident, {private_mem_regions} private"
    )

    vm = os.get_virtMem()
    swap = os.get_swapMem()
    print(f"PhysMem: {size(vm[0])} total, {size(vm[1])} available")
    print(f"VM: {size(vm[0])} vsize, {swap[4]}(0) swapins, {swap[5]}(0) swapouts")

    network_info = os.get_networkInfo()
    print(f"Networks: packets: {network_info[2]} in, {network_info[3]} out")

    disk_info = os.get_diskInfo()
    print(f"Disks: {disk_info[0]} read, {disk_info[1]} written")

    # lower section print
    print("\nPID       COMMAND    CPU%   TIME       USER     STATUS")
    for i in range(14):
        proc = processes[i]
        print("{: <7} {: <12} {: <5} {: <8} {: <11} {: <10}".format(*proc))
