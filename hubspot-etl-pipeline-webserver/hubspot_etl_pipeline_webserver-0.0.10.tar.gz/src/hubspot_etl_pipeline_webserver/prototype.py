from datetime import datetime
import os
import os.path
import glob
from random import random
from threading import Thread
import zipfile

from time import sleep

from flask import Flask, request

from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from google.cloud import bigquery

import pandas as pd

app = Flask(__name__)


def log(msg: str) -> None:
    now = datetime.now()
    now_str = now.isoformat().replace('T', ' ')
    print('[%s] %s' % (now_str, msg))


TABLE_ID = 'test-import-365201.hubspot.import-test'


def submit_for_bigquery(file_path: str) -> None:
    log(f'Submitting {file_path} to bigquery table...')

    client = bigquery.Client()
    job_config=bigquery.LoadJobConfig(
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_APPEND'
    )

    df = pd.read_csv(file_path, na_values=['(No value)'])
    df.columns = df.columns.str.replace(' ', '_')
    df.rename(columns={
        'ad_group_id': 'ad_group_id_new',
        'ad_id': 'ad_id_new'
    }, inplace=True)
    df.columns = df.columns.str.upper()

    load_job = client.load_table_from_dataframe(df, TABLE_ID, job_config=job_config)
    load_job.result() # IMPORTANT!!! Wait for the upload to finish before deleting the file!

    os.remove(file_path)


def async_download(download_link: str) -> None:
    options = ChromeOptions()
    options.add_argument('--user-data-dir=/home/wesleyb/.config/google-chrome')
    options.add_argument('--profile-folder=Default')
    options.headless = False
    driver = Chrome(executable_path='./chromedriver', options=options)
    """ options = FirefoxOptions()
    options.profile = FirefoxProfile('/home/wesley/.mozilla/firefox/vzru4llv.default-release')
    driver = Firefox(options=options) """
    driver.get(download_link)
    """ Wait for the google sign in button to load and click it. """
    try:
        sign_w_google_link = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'google-sign-in')))
        # wait a random amount between 1 and 3 seconds to click.
        sleep(random() * 1.0)
        sign_w_google_link.click()
    except:
        log('The sign in with google button took more than 60 seconds to load. Maybe we are already logged.')

    """ uehfiasufiehsuifhusfhdsf """
    try:
        sign_in_email = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[2]')))
        sign_in_email.click()
    except:
        log('Could not find the email adops@ziangcheng.com on the page.')

    sleep(60) # wait (more than) enough time for the download to finish
    driver.quit()

    # gets the last downloaded file in the downloads folder
    globs = glob.glob('/home/wesleyb/Downloads/*.zip')
    files = list(filter(os.path.isfile, globs))
    files.sort(key=lambda x: -os.path.getmtime(x))

    if len(files) == 0:
        log('No file downloaded. Something is wrong.')
        quit(1)

    file = files[0]
    print(file)

    # extract the report file
    with zipfile.ZipFile(file, 'r') as zip_file:
        files = zip_file.namelist()
        for entry_file in files:
            if entry_file != 'hubspot-export-summary.csv':
                file_pth = zip_file.extract(entry_file)
                submit_for_bigquery(file_pth)
    os.remove(file)


def download_and_process(download_link: str) -> None:
    thread = Thread(target=async_download, args=(download_link, ))
    thread.start()
    return 'OK'


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        body: dict = request.get_json()
        download_link: str = body.get('download_link', '')
        if download_link:
            return download_and_process(download_link)
    return 'You are not supposed to be here.'


if __name__ == "__main__":
    app.run(port=5500)
