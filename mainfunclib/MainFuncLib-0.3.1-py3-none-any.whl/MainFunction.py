# All the needed imports for the code below
import time
import datetime
from polygon.rest import RESTClient # polygon.rest allows to just install the full polygon package without any problems
from sqlalchemy import text
from math import floor
from .Portfolio import *

"""
Function slightly modified from polygon sample code to format the date string

Arguments:
    - ts: last_trade.timestamp (timestap from the last_trade object)

Returns:
    - datetime object
"""


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

"""
This creates a table for storing the raw, unaggregated price data for each currency pair in the SQLite database

Arguments:
    - engine: Engine object from sqlalchemy

    - curr: Tuple, with the currency pair

Returns:
    - None
"""


def initialize_raw_data_table(engine, curr):
    with engine.begin() as conn:
        conn.execute(
            text("CREATE TABLE " + curr[0] + curr[1] + "_raw(ticktime text, fxrate  numeric, inserttime text);"))


"""
This creates a table for storing the (6 min interval) aggregated price data for a certain currency pair in the SQLite database, 
a table for storing the parameteres related to the Keltner Channels and a table for the balance and profit (or loss)

Arguments:
    - engine: Engine object from sqlalchemy

    - curr: Tuple, with the currency pair

Returns:
    - None
"""


def initialize_aggregated_table(engine, curr):
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE " + curr[0] + curr[1] + "_agg(inserttime text, avgfxrate numeric);"))

        # Create extra table to keep track of max, min, VOL, mean, FD and returns
        conn.execute(text("CREATE TABLE " + curr[0] + curr[
            1] + "_maxmin(max numeric, min numeric, VOL numeric, mean numeric, FD numeric, return numeric);"))

        # Create another table to keep track of balance for all currency pairs and profit (or loss)
        conn.execute(
            text("CREATE TABLE " + curr[0] + curr[1] + "_balance(balance_in_USD numeric, profit_loss_in_USD numeric);"))


"""
This function intializes a dictionary for the currency pair with all the parameters that we need to keep track off
during our trades.

This function also initiliazes a start mean and a start volatility to begin the code with, used in the sanity check. 
For the the start mean the current price is used and for the start volatility 2% is used, with the reasoning that 
it is statistically very unlikely to have such high volatility (especially in a 6 minute interval).

Arguments:
    - currency_pair: Tuple, with the currency pair

    - client: Object, Polygon REST api client

Returns:
    - Dictionary
"""


def intialize_dictionary(currency_pair, client):
    ticker = "C:" + currency_pair[0] + currency_pair[1]
    last_quote = client.get_last_quote(ticker)
    prev_mean = (last_quote.ask_price + last_quote.bid_price) / 2
    portfolio = Portfolio(currency_pair[0], currency_pair[1], client)

    return {"prev_band_nb": 0, "nb_crosses": 0, "prev_vol": 0.02, "prev_mean": prev_mean,
            "max": 0, "min": 9999, "portfolio": portfolio}


"""
This function is called every 6 minutes to aggregate the data, store it in the aggregate table, and then delete the raw data

Arguments:
    - engine: Engine object from sqlalchemy

    - curr: Tuple, with the currency pair

    - curr_dict: Dictionary, contains all the required parameters

    - start_time: Float, the start time in seconds of the code

Returns:
    - None

"""


def aggregate_raw_data_tables(engine, curr, curr_dict, start_time):
    with engine.begin() as conn:

        # Gives back a Result object. (See: https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.execute)
        price_res = conn.execute(text(
            "SELECT AVG(fxrate) as avg_price, COUNT(fxrate) as tot_count FROM " + curr[0] + curr[1] + "_raw;")).first()
        mean = avg_price = price_res[0]

        date_res = conn.execute(text("SELECT MAX(ticktime) as last_date FROM " + curr[0] + curr[1] + "_raw;")).first()
        last_date = date_res[0]

        conn.execute(
            text("INSERT INTO " + curr[0] + curr[1] + "_agg (inserttime, avgfxrate) VALUES (:inserttime, :avgfxrate);"),
            [{"inserttime": last_date, "avgfxrate": avg_price}])

        # vol = max - min
        vol = curr_dict["max"] - curr_dict["min"]
        # previous vol
        curr_dict["prev_vol"] = vol

        # Calculate the returns here
        if time.time() < start_time + 390:
            return_ = None
        else:
            return_ = (avg_price - curr_dict["prev_mean"]) / curr_dict["prev_mean"]

        # previous mean
        curr_dict["prev_mean"] = mean

        # Prevent division by 0 error and set first FD to null
        if time.time() < start_time + 390 or vol == 0:
            frac_dem = None
        else:
            frac_dem = curr_dict["nb_crosses"] / vol

        conn.execute(text("INSERT INTO " + curr[0] + curr[
            1] + "_maxmin (max, min, VOL, mean, FD, return) VALUES (:max, :min, :VOL, :mean, :FD, :return);"), [
                         {"max": curr_dict["max"], "min": curr_dict["min"], "VOL": vol, "mean": mean, "FD": frac_dem,
                          "return": return_}])



"""
Function which clears the raw data tables once we have aggregated the data in a 6 minute interval and resets the number of
crosses, band_nb, max and min parameters for the Keltner Channels.

Arguments:
    - engine: Engine object from sqlalchemy

    - curr: Tuple, with the currency pair

    - curr_dict: Dictionary, contains all the required parameters

Returns:
    - None
"""


def reset_raw_data_tables(engine, curr, curr_dict):
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE " + curr[0] + curr[1] + "_raw;"))
        conn.execute(
            text("CREATE TABLE " + curr[0] + curr[1] + "_raw(ticktime text, fxrate  numeric, inserttime text);"))

        # reset number of crosses, band_nb and max, min
        # Assumption: we start each time in band nb 0, not 100% correct, but should not lead to big differences
        curr_dict["nb_crosses"] = 0
        curr_dict["band_nb"] = 0
        curr_dict["max"] = 0
        curr_dict["min"] = 9999  # min is set to a random high number


"""
This the sanity check for the returned values of Polygon. I noticed that Polygon sometimes returns an incorrect value that is 
almost exact the same as 1/correct. This makes me believe that Polygon probably sometimes switches the from and to currency.

I use the reasoning that it is statiscally very unlikely that avg_price > prev_mean + 750*0.025*prev_vol and,
avg_price < prev_mean - 750*0.025*prev_vol

Arguments:
    - client: Object of Polygon client

    - avg_price: Float, avg price of currency pair

    - currency_pair: Tuple, with the currency pair

    - curr_dict: Dictionary, contains all the required parameters

Returns:
    - avg_price

"""


def filter_out_incorrect_values(client, avg_price, currency_pair, curr_dict):
    if (avg_price > curr_dict["prev_mean"] + 750 * 0.025 * curr_dict["prev_vol"] or avg_price < curr_dict[
        "prev_mean"] - 750 * 0.025 * curr_dict["prev_vol"]) and curr_dict["prev_vol"] != 0:
        print("Very unlikely value detected:", avg_price)

        # Call the API again with the required parameters, using different call method
        try:
            ticker = "C:" + currency_pair[0] + currency_pair[1]
            last_quote = client.get_last_quote(ticker)
            avg_price = (last_quote.ask_price + last_quote.bid_price) / 2

        except:
            pass

    if (avg_price > curr_dict["prev_mean"] + 750 * 0.025 * curr_dict["prev_vol"] or avg_price < curr_dict[
        "prev_mean"] - 750 * 0.025 * curr_dict["prev_vol"]) and curr_dict["prev_vol"] != 0:
        # Value is still wrong, discard the value
        avg_prive = None  # None values are ignored when doing operation on sql database, such as AVG()

    return avg_price


"""
This the sanity check for the returned values of Polygon. I noticed that Polygon sometimes returns an incorrect value that is 
almost exact the same as 1/correct. This makes me believe that Polygon probably sometimes switches the from and to currency.

I use the reasoning that it is statiscally very unlikely that avg_price > prev_mean + 750*0.025*prev_vol and,
avg_price < prev_mean - 750*0.025*prev_vol

Arguments:
    - engine: Engine object from sqlalchemy

    - curr: Tuple, with the currency pair

    - curr_dict: Dictionary, contains all the required parameters

    - position_type: String, that is either "SHORT" or "LONG" depending on the type of the position

Returns:
    - None

"""


def check_stoploss_limits(engine, curr, curr_dict, position_type):
    with engine.begin() as conn:

        result = conn.execute(text(
            "SELECT SUM(return) as sum_returns, COUNT(return) as tot_count  FROM " + curr[0] + curr[1] + "_maxmin;"))
        for row in result:
            sum_returns = row.sum_returns
            return_count = row.tot_count + 1  # +1 because the first one is none, doesn't get counted by SQL

        # Python 3.10 would allow to use a switch statement here, makes the code cleaner
        if return_count == 10 and abs(sum_returns) > 0.00250:
            print(f"[UPDATE], stop loss limit is reached for {curr[0]}_{curr[1]} at 0.250% and trade is closed")

            realised_loss = curr_dict["portfolio"].close_trade(position_type)
            print(f"[UPDATE], realized loss of {curr[0]}_{curr[1]} is {realised_loss}")

            # Stop the thread and stop the trade
            raise ValueError("Stop loss limit reached layer 1")

        elif return_count == 20 and abs(sum_returns) > 0.00150:
            print(f"[UPDATE], stop loss limit is reached for {curr[0]}_{curr[1]} at 0.150% and trade is closed")

            realised_loss = curr_dict["portfolio"].close_trade(position_type)
            print(f"[UPDATE], realized loss of {curr[0]}_{curr[1]} is {realised_loss}")

            # Stop the thread and stop the trade
            raise ValueError("Stop loss limit reached layer 2")

        elif return_count == 30 and abs(sum_returns) > 0.00100:
            print(f"[UPDATE], stop loss limit is reached for {curr[0]}_{curr[1]} at 0.100% and trade is closed")

            realised_loss = curr_dict["portfolio"].close_trade(position_type)
            print(f"[UPDATE], realized loss of {curr[0]}_{curr[1]} is {realised_loss}")

            # Stop the thread and stop the trade
            raise ValueError("Stop loss limit reached layer 3")

        elif return_count > 40 and return_count % 10 == 0 and abs(sum_returns) > 0.00050:
            print(f"[UPDATE], stop loss limit is reached for {curr[0]}_{curr[1]} at 0.050% and trade is closed")

            realised_loss = curr_dict["portfolio"].close_trade(position_type)
            print(f"[UPDATE], realized loss of {curr[0]}_{curr[1]} is {realised_loss}")

            # Stop the thread and stop the trade
            raise ValueError("Stop loss limit reached layer 4")

        elif return_count % 10 == 0 and return_count != 0:

            if position_type == "LONG" and return_count <= 40:
                curr_dict["portfolio"].buy_curr(100)

            elif position_type == "SHORT" and return_count <= 40:
                curr_dict["portfolio"].sell_curr(100)

            profit = curr_dict["portfolio"].calculate_profit(position_type)
            balance = curr_dict["portfolio"].convert_balance(position_type)

            conn.execute(text("INSERT INTO " + curr[0] + curr[
                1] + "_balance(balance_in_USD, profit_loss_in_USD) VALUES (:balance_in_USD, :profit_loss_in_USD)"),
                         [{"balance_in_USD": balance, "profit_loss_in_USD": profit}])


"""
This main function repeatedly calls the polygon api every 1 seconds for 10 hours and stores the results.

Arguments:
    - currency_pairs: Nested list with all the information about each currency pair

    - engine: Engine object from sqlalchemy

    - duration, Integer, time in seconds for how long the trade should last

    - position_type: String, that is either "SHORT" or "LONG" depending on the type of the position

Returns:
    - None
"""


def mainFunc(currency_pair, engine, duration, position_type):
    # Put this in an environment variable
    # The api key given by the professor
    key = "beBybSi8daPgsTp5yx5cHtHpYcrjp5Jq"

    # Open a RESTClient for making the api calls
    client = RESTClient(key)

    # Create the needed tables in the database + dictionary for the currency_pair
    initialize_raw_data_table(engine, currency_pair)
    initialize_aggregated_table(engine, currency_pair)
    curr_dict = intialize_dictionary(currency_pair, client)

    start_interval = start_time = time.time()
    end_time = start_time + duration

    print(
        f"[UPDATE] Currency pair {currency_pair[0]}_{currency_pair[1]} started at {time.localtime(start_time).tm_hour}h {time.localtime(start_time).tm_min}min.")

    if position_type == "LONG":
        curr_dict["portfolio"].buy_curr(100)

    else:
        curr_dict["portfolio"].sell_curr(100)

    # Loop that runs until the total duration of the program hits 10 hours (= 36000 seconds).
    while time.time() < end_time:

        # Aggregate the data and clear the raw data tables
        if time.time() > start_interval + 360:
            print(
                f"[UPDATE] Currency pair {currency_pair[0]}_{currency_pair[1]} aggregated at {time.localtime(start_interval + 360).tm_hour}h {time.localtime(start_interval + 360).tm_min}min.")
            aggregate_raw_data_tables(engine, currency_pair, curr_dict, start_time)
            reset_raw_data_tables(engine, currency_pair, curr_dict)
            check_stoploss_limits(engine, currency_pair, curr_dict, position_type)

            # A little time lost by running the above code
            start_interval = time.time()

        # Set the input variables to the API
        from_ = currency_pair[0]
        to = currency_pair[1]

        # Call the API with the required parameters
        try:
            resp = client.get_real_time_currency_conversion(from_, to, amount=100, precision=2)
        except:
            continue

        # This gets the Last Trade object defined in the API Resource
        last_trade = resp.last

        # Format the timestamp from the result
        dt = ts_to_datetime(last_trade.timestamp)

        # Get the current time and format its
        insert_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Calculate the price by taking the average of the bid and ask prices
        avg_price = (last_trade.bid + last_trade.ask) / 2

        # set needed parameters
        prev_vol = curr_dict["prev_vol"]
        prev_mean = curr_dict["prev_mean"]
        curr_max = curr_dict["max"]
        curr_min = curr_dict["min"]

        avg_price = filter_out_incorrect_values(client, avg_price, currency_pair, curr_dict)

        if last_trade.ask > curr_max:
            # Update current maximum
            curr_dict["max"] = last_trade.ask

        elif last_trade.bid < curr_min:
            # Update current minimum
            curr_dict["min"] = last_trade.bid

            # Assumption point on a band is not a cross, has to be > or <

        # Keltner bands, count the number of crosses in realtime
        prev_band_nb = curr_dict["prev_band_nb"]

        # Formula used to calculate the band nb:
        # band_nb = floor((abs(avg_price - prev_mean))/(0.025*prev_vol))

        if avg_price > prev_mean + 0.025 * prev_vol and prev_vol != 0:
            band_nb = floor((avg_price - prev_mean) / (0.025 * prev_vol))

        elif avg_price < prev_mean - 0.025 * prev_vol and prev_vol != 0:
            band_nb = floor((avg_price - prev_mean) / (-0.025 * prev_vol))

        else:
            band_nb = 0  # lays within the keltner channel

        # Can't go over 100 for the band_nb
        band_nb = 100 if band_nb > 100 else band_nb

        # Set new prev_band_nb and increment crosses counter
        curr_dict["prev_band_nb"] = band_nb
        curr_dict["nb_crosses"] = curr_dict["nb_crosses"] + abs(band_nb - prev_band_nb)

        # Write the data to the SQLite database, raw data tables
        with engine.begin() as conn:
            conn.execute(text(
                "INSERT INTO " + from_ + to + "_raw(ticktime, fxrate, inserttime) VALUES (:ticktime, :fxrate, :inserttime)"),
                         [{"ticktime": dt, "fxrate": avg_price, "inserttime": insert_time}])

        # Time the code so we have approx 1 data point per second
        time.sleep(0.5988)

    # After the while loop the trade gets closed and profit/loss is realized
    realised_profit = curr_dict["portfolio"].close_trade(position_type)
    print(
        f"[UPDATE], Closed trade of {currency_pair[0]}_{currency_pair[1]} with realized profit/loss of {realised_profit}")