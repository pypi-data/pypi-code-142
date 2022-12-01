import tensorflow as tf
import energy_monitor
from energy_callback import raplMonitor
import os
import pandas as pd


class Callback(tf.keras.callbacks.Callback):
    """
    Args:
        - country (str): Country for estimating gCO2e per kWh Default: 'United Kingdom'
        - csv_path (str): Filepath to csv file to log results. Default: './tb_experiment_1.csv'
    """
    def __init__(self, metric_name="duration", country='United Kingdom',
                 csv_path='./tb_experiment_1.csv'):
        self.__epoch_start = None
        self.__metric_name = metric_name
        self.country = country
        self.csv_path = csv_path
        self.write_data = {}
        if os.access('/sys/class/powercap/intel-rapl:0/energy_uj', os.R_OK):
            self.monitor = raplMonitor.RaplMonitor()
            print("Using rapl")
        else:
            self.monitor = energy_monitor.monitor()
            print("Using energy_monitor")
        self.joules = []
        self.co2e = []

    def on_epoch_begin(self, epoch, logs=None):
        self.__epoch_start = tf.timestamp()
        self.monitor.start()

    def on_epoch_end(self, epoch, logs=None):
        logs[self.__metric_name] = (tf.timestamp() - self.__epoch_start).numpy()
        self.monitor.stop()
        self.joules.append(self.monitor.joules)
        self.co2e.append(self.monitor.joules * 0.0000002778 * self.get_carbon_by_country())  # 1J = 0.0000002778kWh

    def get_carbon_by_country(self):
        # Source https://ourworldindata.org/grapher/carbon-intensity-electricity
        data = pd.read_csv('energy_callback/data/carbon-intensity-electricity.csv')
        country = self.country
        # Filter by country
        country_data = data[data.Entity == country]
        # Filter by latest year
        latest_data = country_data.loc[country_data['Year'] == max(country_data['Year'])]

        # Return cCO2/kWh for given country
        return latest_data['Carbon intensity of electricity (gCO2/kWh)'].values[0]

    def get_co2e(self):
        return self.co2e

    def get_joules(self):
        return self.joules

    def get_csv(self, history=None):
        df = pd.DataFrame({'joules': self.get_joules(), 'co2e': self.get_co2e()})

        if history:
            for key in history.history.keys():
                df[key] = history.history[key]

        df.to_csv(self.csv_path)
