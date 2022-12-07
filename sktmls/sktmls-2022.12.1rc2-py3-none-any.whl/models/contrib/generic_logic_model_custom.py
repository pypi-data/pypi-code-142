from typing import Any, Dict, List, Union

import numpy as np
from pandas import DataFrame
from pytz import timezone
import torch

from sktmls import MLSRuntimeENV
from sktmls.apis import MLSProfileAPIClient, MLSGraphAPIClient
from sktmls.dynamodb import DynamoDBClient
from sktmls.models import MLSGenericModel, MLSModelError, MLSTrainableCustom
from sktmls.utils import LogicProcessor

TZ = timezone("Asia/Seoul")

logic_processor = LogicProcessor()


class GenericLogicModelCustom(MLSGenericModel, MLSTrainableCustom):
    """
    MLS 모델 레지스트리에 등록되는 단일 모델 기반의 클래스입니다.
    전처리 로직은 json 형태로 후처리 로직은 별도로 정의한 함수를 전달하여 프로세스합니다.
    """

    def __init__(
        self,
        model_name: str,
        model_version: str,
        features: List[str],
        model=None,
        preprocess_logic: Dict[str, List[Any]] = None,
        postprocess_logic=None,
        predict_fn: str = "predict",
        data: Dict[str, Any] = {},
        user_profile_nm: str = None,
        pf_value: List[str] = None,
    ):
        assert isinstance(features, list), "`features`은 list 타입이어야 합니다."

        if preprocess_logic is not None:
            assert isinstance(preprocess_logic, dict), "`preprocess_logic`은 dict 타입이어야 합니다."
            for key in preprocess_logic.keys():
                assert (
                    key in ["var", "missing", "missing_some", "pf", "with", "for"] or key in logic_processor.operations
                )
        else:
            preprocess_logic = {"merge": [{"var": f} for f in features]}

        if postprocess_logic is not None:
            assert hasattr(postprocess_logic, "__call__") is True, "postprocess_logic 값은 함수이어야 합니다."
        else:
            pass

        assert isinstance(predict_fn, str), "`predict_fn`은 str 타입이어야 합니다."
        assert predict_fn in [
            "predict",
            "predict_proba",
            "none",
        ], "`predict_fn`은 predict, predict_proba, none 중 하나의 값이어야 합니다."

        assert isinstance(data, dict), "`data`는 dict 타입이어야 합니다."

        if user_profile_nm is not None:
            assert isinstance(user_profile_nm, str), "`user_profile_nm`는 str 타입이어야 합니다."
            assert (user_profile_nm is not None) and (
                pf_value is not None
            ), "`user_profile_nm`은 `pf_value`와 함께 입력을 받아야 합니다."
        else:
            user_profile_nm = None

        if pf_value is not None:
            assert isinstance(pf_value, list), "`pf_value`는 list 타입이어야 합니다."
            assert (user_profile_nm is not None) and (
                pf_value is not None
            ), "`user_profile_nm`은 `pf_value`와 함께 입력을 받아야 합니다."
        else:
            pf_value = None

        super().__init__([model], model_name, model_version, features)

        self.preprocess_logic = preprocess_logic
        self.postprocess_logic = postprocess_logic
        self.predict_fn = predict_fn
        self.data = data
        self.user_profile_nm = user_profile_nm
        self.pf_value = pf_value

    def predict(self, x: List[Any], **kwargs) -> Dict[str, Any]:
        pf_client = kwargs.get("pf_client") or MLSProfileAPIClient(runtime_env=MLSRuntimeENV.MMS)
        graph_client = kwargs.get("graph_client") or MLSGraphAPIClient(runtime_env=MLSRuntimeENV.MMS)
        dynamodb_client = kwargs.get("dynamodb_client") or DynamoDBClient(runtime_env=MLSRuntimeENV.MMS)

        preprocessed_x = self._preprocess(x, kwargs.get("keys", []), pf_client, graph_client, dynamodb_client)
        y = self._ml_predict(preprocessed_x)
        items = self._postprocess(x, kwargs.get("keys", []), y, pf_client, graph_client, dynamodb_client) or []

        return {"items": items}

    def _preprocess(
        self,
        x: List[Any],
        additional_keys: List[Any],
        pf_client: MLSProfileAPIClient,
        graph_client: MLSGraphAPIClient,
        dynamodb_client: DynamoDBClient,
    ) -> List[Any]:
        if len(self.features) != len(x):
            raise MLSModelError("GenericLogicModelCustom: `x`의 길이가 `features`의 길이와 다릅니다.")

        data = {name: x[i] for i, name in enumerate(self.features) if x[i] not in [None, []]}
        data["additional_keys"] = additional_keys
        data.update(self.data)

        try:
            return logic_processor.apply(
                self.preprocess_logic,
                data=data,
                pf_client=pf_client,
                graph_client=graph_client,
                dynamodb_client=dynamodb_client,
            )
        except Exception as e:
            raise MLSModelError(f"GenericLogicModelCustom: 전처리에 실패했습니다. {e}")

    def _ml_predict(self, preprocessed_x: List[Any]) -> Union[float, List[float], str, None]:
        try:
            if self.predict_fn == "none" and self.model_lib != "pytorch":
                return None

            if not isinstance(preprocessed_x[0], list):
                preprocessed_x = [preprocessed_x]

            if self.model_lib == "autogluon":
                input_data = DataFrame(
                    preprocessed_x, columns=[f for f in self.features if f not in self.non_training_features]
                )
            elif self.model_lib == "pytorch":
                input_data = torch.tensor(preprocessed_x, dtype=torch.float)
            else:
                input_data = np.array(preprocessed_x)

            if self.model_lib == "pytorch":
                y = self.models[0](input_data).detach().numpy()
            elif self.predict_fn == "predict":
                y = self.models[0].predict(input_data)
            else:
                y = self.models[0].predict_proba(input_data)
                if self.model_lib == "autogluon" and isinstance(y, DataFrame):
                    y = y.to_numpy()

            if len(y) == 1:
                y = y[0]

            try:
                return y.tolist()
            except AttributeError:
                return y

        except Exception as e:
            raise MLSModelError(f"GenericLogicModelCustom: ML Prediction에 실패했습니다. {e}")

    def _postprocess(
        self,
        x: List[Any],
        additional_keys: List[Any],
        y: Union[float, List[float], None],
        pf_client: MLSProfileAPIClient,
        graph_client: MLSGraphAPIClient,
        dynamodb_client: DynamoDBClient,
    ) -> List[Dict[str, Any]]:

        data = {name: x[i] for i, name in enumerate(self.features) if x[i] not in [None, []]}
        data["additional_keys"] = additional_keys
        data["y"] = y
        data.update(self.data)
        if self.pf_value:
            pf_values = pf_client.get_user_profile(
                profile_id=self.user_profile_nm, user_id=data["user_id"], keys=self.pf_value
            )
            assert None not in pf_values.values(), "후처리 시 사용되는 변수의 값은 사용되는 유저 프로파일에 있어야 합니다."
            data.update(pf_values)
        else:
            pass

        try:
            return self.postprocess_logic(data)
        except Exception as e:
            raise MLSModelError(f"GenericLogicModelCustom: 후처리에 실패했습니다. {e}")
