import requests
import os
import csv
import json
import argparse

try:
    username = os.environ["AEDA_API_CAR_USER"]
except KeyError:
    print("Missing enviroment variable: AEDA_API_CAR_USER")
    exit(1)
try:
    api_key = os.environ["AEDA_API_CAR_PASSWORD"]
except KeyError:
    print("Missing enviroment variable: AEDA_API_CAR_PASSWORD")
    exit(1)



def ask_aeda(reg_number, log_level=None):
    url = "https://aedacar.azurewebsites.net/api/car"
    params = {"code": "BzaCA1bdqU21cfZVn8r3KJwaoivzaOla7o6sLa-qD0elAzFulXlzyA==", 
              "username": username, 
              "regNumber": reg_number, 
              "logLevel": log_level}
    headers={"x-functions-key": api_key}
    r = requests.get(url, params=params, headers=headers)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        if errh.response.status_code == 429:
            print("Too many requests, breaking")
        else:
            pass
            # print(f"Http Error: {errh} for {reg_number}.")
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    body = r.content.decode("utf-8")
    try:
        body = json.loads(body)
    except json.decoder.JSONDecodeError:
        print("Error in json")
    print(r.status_code)
    print(r.reason)
    return body


def get_car_from_reg_number(reg_number, out_file=None, in_file=None, log_level=None):
    results = []
    if in_file is not None:
        print(f"Gettting info for reg numbers in {in_file}")
        with open(f'{in_file}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for i, row in enumerate(csv_reader):
                results.append(ask_aeda(reg_number))
    else:
        print(f"Gettting info for {reg_number}")
        results = ask_aeda(reg_number, log_level)
    if out_file is None:
        print(f"Results: {results}")
    else:
        with open(f'./{out_file}', 'w+', encoding='utf-16') as f:
            f.write(json.dumps(results))
        print(f"Results written to {out_file}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='lookup cars.')
    parser.add_argument('--regnumber', type=str, default=None, help="Search for a single regnumber. E.g. --regnumber XXXXXXX")
    parser.add_argument('--output', type=str, default=None, help="Write output to a csv file.")
    parser.add_argument('--input', type=str, default=None, help="Read regnumbers from a csv with a single column containg the numbers.")
    parser.add_argument('--loglevel', type=str, default=None, help="Only for debugging.")
    args = parser.parse_args()
    reg_number = args.regnumber
    get_car_from_reg_number(reg_number, out_file=args.output, in_file=args.input, log_level=args.loglevel)
    