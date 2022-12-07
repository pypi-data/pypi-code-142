import pandas as pd
import webbrowser
import requests
from typing import Union


class TimeseriesTools():
    """
    Class to interact with timeseries.tools
    """

    def __init__(self):
        """
        Constructor
        """
        self.supabase_url = "https://protbtpwnrctyeayuomi.supabase.co"
        self.supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InByb3RidHB3bnJjdHllYXl1b21pIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjkxNDA5MTksImV4cCI6MTk4NDcxNjkxOX0.AVZV_P4wOHHq8cHvzbGZ0Ryd8zwmgzZyrF1ODVKcET0"

    def login(self, email: str, password: str):
        """
        Login to timeseries.tools
            Parameters:
            email (str): E-Mail
            password (str): Password
        """

        print('Logging in...')
        response = requests.post(self.supabase_url + '/auth/v1/token?grant_type=password', json={
            "email": email,
            "password": password
        }, headers={
            'apikey': self.supabase_key,
            'Content-Type': 'application/json',
        })

        if response.status_code == 200:
            body = response.json()
            self.session = body
            print('Login successful!', self.session['user']['email'])
            return
        if response.status_code == 400:
            body = response.json()
            print(body['error_description'])
            return

        print('Something went wrong, status code: ' + str(response.status_code))

    def create_tearsheet(self, data: Union[pd.DataFrame, pd.Series], open_browser=True):
        """
        Create a tearsheet on timeseries.tools

            Parameters:
            data (pd.DataFrame or pd.Series): Timeseries, index must be datetime
            open_browser (bool): Open browser after upload

        """

        if not isinstance(data.index, pd.DatetimeIndex):
            raise Exception("Index must be of type DatetimeIndex")

        if (not self.session):
            raise Exception(
                "Not logged in. If you don't have an account, please visit https://timeseries.tools and create one.")

        data.index = data.index.map(lambda x: x.timestamp() * 1000)
        data = data.sort_index()

        if isinstance(data, pd.DataFrame):
            raise Exception(
                "pd.DataFrame not supported yet, please provide a pd.Series")

        if isinstance(data, pd.Series):

            if data.shape[0] >= 10000:
                raise Exception(
                    "Too many rows, we currently support a maximum of 10.000 rows")

            if data.dtype == 'object':
                raise Exception(
                    "Object type not supported, please convert to numeric")

            timeseries_name = data.name if data.name else "My Time series"

            timeseries_data = {"epoch_timestamp_in_ms": data.index.to_list(),
                               "values": data.to_list()}

            request_data = {
                "created_by": self.session['user']['id'],
                "data": timeseries_data,
                "name": timeseries_name,
                "is_example": False
            }

            response = requests.post(self.supabase_url + '/rest/v1/timeseries', json=request_data, headers={
                "apikey": self.supabase_key,
                "Authorization": "Bearer " + self.session['access_token'],
                "Content-Type": "application/json",
                "Prefer": "return=representation"
            })

            if response.status_code == 201:

                created_timeseries_array = response.json()

                if len(created_timeseries_array) > 0:
                    created_timeseries = created_timeseries_array[0]

                    if open_browser:
                        webbrowser.open(
                            'https://timeseries.tools/r/' + created_timeseries['id'] + '?ref=python')

                    return created_timeseries['id']
                else:
                    print('Something went wrong, nothing returned')

            else:
                print('Something went wrong, upload failed')
