import json
from typing import Dict, Any, Union
from .error import PathException, GetExcetion, UpdateExcetion


class Connect:
    """
    JSON파일을 연결하여 전체적인 기능을 제공하는 클래스입니다.

    ## Parameter
    ### path
    JSON 파일이 있는 경로를 설정합니다.
    ### encoding
    JSON 파일을 읽을 형식을 설정합니다.
    ### esure_ascii
    데이터가 저장된 json파일이 한글이 깨지는 것을 막아줍니다.


    ## Exception
    ### PathException
    JSON 파일을 찾을 수 없을때 반환되는 예외클래스입니다.
    """

    def __init__(
        self, path: str, encoding: str = "utf-8", ensure_ascii: bool = False
    ) -> None:
        try:
            with open(path, "r", encoding=encoding) as f:
                json.load(f)
        except Exception as exception:
            raise PathException(exception)
        else:
            self.path = path
            self.encoding = encoding
            self.ensure_ascii = ensure_ascii

    def get(self, path: str = None) -> Dict[str, Any]:
        """
        데이터를 가져옵니다.

        ## Parameter
        ### path
        json 파일 내에서 부분 데이터를 가져올때 설정하는 값입니다.\n
        경로는 `/`으로 구분합니다.\n
        None값일시 모든 데이터를 가져옵니다.

        #### 예시
        `get(path="Data/one")`
        \n
        ##### 데이터 형식
        {
            'Data' : {
                'one' : '하나',
                'two' : '둘'

            }
        }

        ##### Return
        `'하나'`
        """
        try:
            with open(self.path, "r", encoding=self.encoding) as f:
                data = json.load(f)
            if path != None:
                path = path.split("/")
                for i in path:
                    data = data[str(i)]
            return data
        except Exception as exception:
            raise PathException(exception)

    def set(self, data: Dict[str, Any]) -> bool:
        """
        전체 데이터를 `data`로 덮어씌웁니다.\n
        성공적으로 저장하면 `True`를 반환합니다.
        """
        try:
            with open(self.path, "w", encoding=self.encoding) as f:
                json.dump(data, f, indent=4, ensure_ascii=self.ensure_ascii)
            return True
        except Exception as exception:
            raise UpdateExcetion(exception)

    def update(self, data: Dict[str, Any]) -> bool:
        """
        전체 데이터에 `data`의 값을 추가합니다.\n
        성공적으로 저장하면 `True`를 반환합니다.
        """
        get_data = self.get()
        key_list = list(data.keys())
        try:
            for i in key_list:
                get_data[i] = data[i]
            with open(
                self.path, "w", encoding=self.encoding
            ) as f:
                json.dump(get_data, f, indent=4, ensure_ascii=self.ensure_ascii)
            return True
        except Exception as exception:
            raise UpdateExcetion(exception)
