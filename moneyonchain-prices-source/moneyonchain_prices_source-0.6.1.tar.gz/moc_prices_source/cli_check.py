import json, sys
from os.path import dirname, abspath
from inspect import getsource
from types   import LambdaType


bkpath   = sys.path[:]
base_dir = dirname(abspath(__file__))
sys.path.append(dirname(base_dir))

from moc_prices_source.cli            import command, option, tabulate, trim
from moc_prices_source.weighing       import weighing
from moc_prices_source                import version
from moc_prices_source                import get_price, ALL
from moc_prices_source.computed_pairs import show_computed_pairs_fromula 

sys.path = bkpath



@command()
@option('-v', '--version', 'show_version', is_flag=True,
        help='Show version and exit.')
@option('-j', '--json', 'show_json', is_flag=True,
        help='Show data in JSON format and exit.')
@option('-w', '--weighing', 'show_weighing', is_flag=True,
        help='Show the default weighing and exit.')
@option('-c', '--computed', 'show_computed_pairs', is_flag=True,
        help='Show the computed pairs formula and exit.')
def cli_check(show_version=False, show_json=False, show_weighing=False, show_computed_pairs=False):

    if show_version:
        print(version)
        return

    if show_weighing:
        print()
        print(weighing)
        print()
        return

    if show_computed_pairs:
        show_computed_pairs_fromula()
        return 

    data = {}

    get_price(ALL, detail=data, serializable=show_json)

    if show_json:
        print(json.dumps(data, indent=4, sort_keys=True))
        return

    def format_time(t):
        return '{}s'.format(round(t.seconds + t.microseconds/1000000, 2))

    time   = data['time']
    prices = data['prices']
    values = data['values']

    table=[]
    for p in prices:
        row = []
        row.append(p["coinpair"].from_.name)
        row.append(p["coinpair"].to_.name)
        row.append(p["coinpair"].variant)
        row.append(p["description"])
        if p["ok"]:
            row.append(p["price"])
            row.append(p["coinpair"].to_.small_symbol)
        else:
            row.append(trim(p["error"], 25))
            row.append(None)
        row.append(round(p["weighing"], 2))
        if p["percentual_weighing"]:
            row.append(round(p[
                "percentual_weighing"]*100, 1))
        else:
            row.append('N/A')
        if p["time"]:
            row.append(format_time(p["time"]))
        else:
            row.append('N/A')
        table.append(row)
    if table:
        table.sort(key=str)
        print()
        print(tabulate(table, headers=[
            'From', 'To', 'V.', 'Exchnage', 'Response', 'U.', 'Weigh', '%', 'Time'
        ]))

    table=[]
    for coinpair, d in values.items():
        row = []
        if 'prices' in d:
            row.append('🠻')
        else:
            row.append('ƒ')
        row.append(coinpair)
        row.append(d['median_price'])
        row.append(d['mean_price'])
        row.append(d['weighted_median_price'])
        if 'prices' in d:
            row.append(len(d['prices']))
        else:
            row.append('N/A')
        table.append(row)
    if table:
        table.sort(key=lambda x: str(x[1]))
        print()
        print(tabulate(table, headers=[
            '', 'Coin pair', 'Mediam', 'Mean', 'Weighted median', 'Sources'
        ]))

    errors = []
    for p in prices:
        if not p["ok"] and p['weighing']:
            errors.append((p["name"], p["error"]))

    if errors:
        print()
        print("Errors detail")
        print("------ ------")
        for e in errors:
            print()
            print('{}: {}'.format(*e))

    print()
    print('Response time {}'.format(format_time(time)))
    print()



if __name__ == '__main__':
    cli_check()
