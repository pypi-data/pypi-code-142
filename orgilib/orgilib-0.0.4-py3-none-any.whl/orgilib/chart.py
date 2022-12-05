import json

def wprint_dataframe():
    print('orangelib.line: df 파라미터 에러.')
def wprint_dataframe_x():
    print('orangelib.line: x 컬럼이 DataFrame 에 없습니다.')
def wprint_x():
    print('orangelib.line: x 파라미터가 없습니다.')
def wprint_dataframe_y():
    print('orangelib.line: y 컬럼이 DataFrame 에 없습니다.')
def wprint_y():
    print('orangelib.line: y 파라미터가 없습니다.')
def wprint_unkown_type():
    print('알수 없는 차트타입')

# Chart
def show(**kwargs):
    df = kwargs.get('df', None)
    x = kwargs.get('x', None)
    y = kwargs.get('y', None)
    title = kwargs.get('title', '')
    subtitle = kwargs.get('subtitle', '')
    export_type = kwargs.get('type', 'unknown')

    if df is None:
        wprint_dataframe()
    elif x is None:
        wprint_x()
    elif x not in df:
        wprint_dataframe_x()
    elif y is None:
        wprint_y()
    elif y not in df:
        wprint_dataframe_y()
    elif export_type != 'line' and export_type != 'scatter' and export_type != 'bar':
        wprint_unkown_type()
    else:
        try:
            response = {
                'exportType': export_type,
                'rows': df.to_json(orient='records'),
                'x': x,
                'y': y,
                'title': title,
                'subtitle': subtitle
            }
            print(json.dumps(response))
        except:
            print('orangelib 에러: show function ')