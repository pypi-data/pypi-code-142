
def _read_sysfs_file(path):
    with open(path, "r") as f:
        contents = f.read().strip()
        return contents


class RaplMonitor:

    def __init__(self):
        self.start_reading = 0
        self.end_reading = 0
        self.max_reading = 0
        self.rapl_dir = '/sys/class/powercap/intel-rapl:0/'
        self.joules = 0

    def get_rapl(self):

        energy_uj = int(_read_sysfs_file(self.rapl_dir + "energy_uj"))
        max_uj = int(_read_sysfs_file(self.rapl_dir + "max_energy_range_uj"))

        return energy_uj, max_uj

    def start(self):
        self.start_reading, self.max_reading = self.get_rapl()

    def stop(self):
        self.end_reading, _ = self.get_rapl()
        # check if reading has reached max and ticked over
        if self.end_reading < self.start_reading:
            microjoules = self.max_reading - self.start_reading + self.end_reading
        else:
            microjoules = self.end_reading - self.start_reading
        self.joules = microjoules*0.000001  # convert from uJ to J

    def joules(self):
        return self.joules
