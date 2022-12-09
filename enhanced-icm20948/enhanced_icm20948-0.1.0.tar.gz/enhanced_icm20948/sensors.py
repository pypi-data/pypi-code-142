from enhanced_icm20948 import asm_sensors

__version__ = "0.1.0"
class Sensor:
    def __init__(self, core):
        self.core = core
        
    def get_name(self):
        return self.core.sensorName
    
    def set_name(self, name: str):
        self.core.sensorName = name
    
    def get_i2c_bus(self):
        return self.core.get_i2c_bus()
    
    def get_i2c_address(self):
        return self.core.get_i2c_address()
    
    def get_sensor_id(self):
        return self.core.get_sensor_id()
    
    def get_max_frequency(self):
        return self.core.get_max_frequency()
    

class ICM20948(Sensor):
    
    INVALID_RANGE =                           0xFF

    ACCEL_RANGE_2G =                          0x00
    ACCEL_RANGE_4G =                          0x02
    ACCEL_RANGE_8G =                          0x04
    ACCEL_RANGE_16G =                         0x06
        
    GYRO_RANGE_250DPS =                       0x00
    GYRO_RANGE_500DPS =                       0x02
    GYRO_RANGE_1000DPS =                      0x04
    GYRO_RANGE_2000DPS =                      0x06

    MAG_POWER_DOWN_MODE =                     0x00
    MAG_SINGLE_MEASURE_MODE =                 0x01
    MAG_FREQ_10HZ_MODE =                      0x02
    MAG_FREQ_20HZ_MODE =                      0x04
    MAG_FREQ_50HZ_MODE =                      0x06
    MAG_FREQ_100HZ_MODE =                     0x08
    MAG_SELF_TEST_MODE =                      0x10
    
    
    def __init__(self, i2cBus: int, i2cAddress: int = asm_sensors.ICM20948_DEFAULT_I2C_ADDRESS, sensorName: str = ""):
        super().__init__(asm_sensors.ICM20948(i2cBus, i2cAddress))
        if (len(sensorName) > 0):
            self.set_name(sensorName)
            
    def get_accel_frequency(self):
        return self.core.get_accel_frequency()
    
    def get_gyro_frequency(self):
        return self.core.get_gyro_frequency()
    
    def get_mag_frequency(self):
        return self.core.get_mag_frequency()
    
    def set_accel_frequency_divisor(self, divisor: int):
        return self.core.set_accel_frequency_divisor(divisor)
    
    def set_gyro_frequency_divisor(self, divisor: int):
        return self.core.set_gyro_frequency_divisor(divisor)
    
    def set_mag_mode(self, mode: int):
        return self.core.set_mag_mode(mode)
    
    def get_accel_range(self):
        return self.core.get_accel_range()
    
    def get_gyro_range(self):
        return self.core.get_gyro_range()
    
    def set_accel_range(self, range: int):
        return self.core.set_accel_range(range)
    
    def set_gyro_range(self, range: int):
        return self.core.set_gyro_range(range)
    
    def get_accel_data(self):
        return self.core.get_accel_data()
    
    def get_gyro_data(self):
        return self.core.get_gyro_data()
    
    def get_mag_data(self):
        return self.core.get_mag_data()
    
    def get_temp_data(self):
        return self.core.get_temp_data()
    
    def get_orientation_quaternion(self):
        return self.core.get_orientation_quaternion()
    
    def get_euler_angles(self):
        return self.core.get_euler_angles()
        

        
        
class SensorBatch:
    def __init__(self):
        self.core = asm_sensors.SensorBatch()
    
    def add_sensor(self, sensor):
        return self.core.add_sensor(sensor.core)
    
    def start_reading(self):
        return self.core.start_reading()
        
    def stop_reading(self):
        return self.core.stop_reading()
    
    def get_max_frequency(self):
        return self.core.get_max_frequency()
    
    def start_estimating_orientation(self):
        return self.core.start_estimating_orientation()
    
    def stop_estimating_orientation(self):
        return self.core.stop_estimating_orientation()
        