# load_prediction.py

from common_function import *  # Common
import common_function as c
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingRegressor as GBR
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.ensemble import AdaBoostRegressor as ABR
from sklearn.linear_model import ElasticNet as ETN
from lightgbm import LGBMRegressor as LGB
from xgboost import XGBRegressor as XGB
from sklearn.metrics import mean_squared_error, mean_absolute_error
from bayes_opt import BayesianOptimization
import numpy as np
import pandas as pd
import math
import gc
# from pandas import DataFrame
# import scipy.optimize as optimize
# from bayes_opt.event import DEFAULT_EVENTS, Events
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

# 방법1 : 실측수요부하 테이블에 데이터가 없을 때 예측부하 테이블에 데이터를 입력하기 위한 함수
# 방법2 : 실측수요부하 테이블의 과거 실측수요부하를 기반으로 머신러닝을 적용한 부하예측
# 방법3 : 부하예측 테이블의 과거 예측부하를 기반으로 머신러닝을 적용한 부하예측


def loadprediction_method(method_no, prediction_date, air_condition, dt_hm):
    start = time.time()
    pd.set_option('mode.chained_assignment', None)  # <=== 경고를 끈다

    random_seed = 1
    cnt = 0
    n = 0
    df_all_data = []

    weekholiday, holidaycode = c.is_weekday(prediction_date)

    df_predict_zone_load = pd.DataFrame(
        columns=['BuildingNo', 'ZoneNo', 'Date', 'Hour', 'Week', 'TempDiff', 'SOLARRADQ', 'EnthalpyDiff', 'Load',
                 'PredictLoad', 'PowerUnitRate', 'NightPowerUnitRate', 'GasUnitRate', 'DHUnitRate'])

    df_algorithm = pd.DataFrame(columns=['buildingno', 'algorithm'])

    # 방법1 : 실측수요부하 테이블에 데이터가 없을 때, 예측부하 테이블에 데이터를 입력하기 위한 함수
    # 실측수요부하 테이블의 과거 데이터를 기반으로 하여 기상실황 정보를 가지고 예측부하를 구하기 위한 함수(제주도용)

    # 방법2 : 실측수요부하 테이블의 과거 실측부하를 기반으로 머신러닝을 적용한 부하예측
    if method_no == 2:
        df_all_data = c.load_by_real_foretime(prediction_date, air_condition)
        real_load_date = c.revision_load_date(prediction_date, air_condition)
        print("real_load_date:", real_load_date)
        df_r = c.revision_load(prediction_date, real_load_date)
        # print("df_r:", df_r)

    # 방법3 : 부하예측 테이블의 과거 예측부하를 기반으로 머신러닝을 적용한 부하예측
    if method_no == 3:
        df_all_data = c.load_by_predict_foretime(prediction_date, air_condition)

    if method_no == 2 or method_no == 3:
        df_all = df_all_data[df_all_data['Date'] < prediction_date]
        df_future = df_all_data[df_all_data['Date'] == prediction_date]
        # print("df_all:", df_all)

        # [청구항1 S42] 시작
        # 관제서버(10)에서 가져온 과거 기상정보와 냉난방 기간 실측부하 데이터를 전처리하는 단계
        # pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        df_all = df_all[df_all['Load'] > 0]  # 실측부하가 0인 경우 제외
        # print("df_future:", df_future)
        building_no = df_all['BuildingNo'].unique()

        op_month = prediction_date[4:6]
        # print("op_month:", op_month)

    if method_no == 2 and weekholiday == 1:   #  and op_month not in ('03', '05', '09', '10'):
        # 보정계수 이상치 제거
        outlier_index_all = np.array([])
        zone_no = df_r['ZoneNo'].unique()

        for zone_list in zone_no:
            df_zone = df_r[(df_r['ZoneNo'] == zone_list)]
            hour_no = df_zone['RealHour'].unique()
            for hour_list in hour_no:
                df_hour = df_zone[(df_zone['RealHour'] == hour_list)]
                outlier_index = c.get_outlier(df=df_hour, column='Revision', weight=1.5)
                if len(outlier_index) > 0:
                    outlier_index_all = np.append(outlier_index_all, np.array(outlier_index.values))
        df_r.drop(outlier_index_all, axis=0, inplace=True)
        # 보정계수 이상치 제거 끝
        # print("보정 후 df_r:", df_r)

    if method_no != 1:
        for building_list in building_no:
            model_algo = []
            model_params = []
            load_sum = 0

            # 데이터셋 생성하기
            df_data = df_all[(df_all['BuildingNo'] == building_list)]
            df_data_future = df_future[(df_future['BuildingNo'] == building_list)]

            if method_no == 2 and weekholiday == 1:  #  and op_month not in ('03', '05', '09', '10'):
                # 이상치 제거
                outlier_index_all = np.array([])
                zone_no = df_data['ZoneNo'].unique()

                for zone_list in zone_no:
                    df_zone = df_data[(df_data['ZoneNo'] == zone_list)]
                    hour_no = df_zone['Hour'].unique()
                    for hour_list in hour_no:
                        df_hour = df_zone[(df_zone['Hour'] == hour_list)]
                        outlier_index = c.get_outlier(df=df_hour, column='Load', weight=1.5)
                        if len(outlier_index) > 0:
                            outlier_index_all = np.append(outlier_index_all, np.array(outlier_index.values))
                df_data.drop(outlier_index_all, axis=0, inplace=True)
                # 이상치 제거 끝

            # 이상치 제거 후
            df_data.reset_index(drop=True, inplace=True)
            # print("df_data['WeekHoliday']:\n", df_data["WeekHoliday"])

            # 과거 데이터 중에서 하루에 시간데이터가 1인 행은 1행을 추가(stratify 오류 가능성 배제)
            date_no = df_data['Date'].unique()
            for date_list in date_no:
                if len(df_data[df_data['Date'] == date_list]) == 1:
                    df_data.loc[len(df_data) + 1] = df_data[df_data['Date'] == date_list].values[0]
                    # print("df_data :", df_data[df_data['Date'] == date_list].values[0])
                    # print("df_data tail:", df_data.tail())

            # 과거 데이터에서 피쳐와 타겟 분리
            # df_data_target = df_data['Load']
            # del df_data['Load']
            # print("df_data:\n", df_data)

            df_data = pd.concat([df_data, df_data_future], ignore_index=True)

            df_data['Week'] = ''
            df_data['Date'] = pd.to_datetime(df_data['Date'])
            df_data.loc[df_data['WeekHoliday'] == 1, 'Week'] = df_data["Date"].dt.weekday + 1
            df_data.loc[df_data['WeekHoliday'] == 0, 'Week'] = 0
            df_data['Date'] = df_data['Date'].dt.strftime("%Y%m%d")
            # print("df_data week:", df_data[["Date", "Week", "WeekHoliday"]])
            # print("df_data all:\n", df_data)

            # 원핫인코딩
            df_dummy = pd.get_dummies(df_data, columns=['ZoneNo', 'Hour', 'Week'])
            df_dummy[['ZoneNo', 'Hour', 'Week']] = df_data[['ZoneNo', 'Hour', 'Week']]
            df_dummy['Hour'] = df_data['Hour']
            del df_dummy['BuildingNo']

            # date_list = df_dummy['Date'].unique()
            # date_count = len(date_list)
            # date_count = 10  # 임시 일부 날짜만 예측할 경우 종료할 날짜 순서

            # for m in range(start_date, date_count):
            df_real_dummy = df_dummy[(df_dummy['Date'] < prediction_date)]
            df_predict_dummy = df_dummy[(df_dummy['Date'] == prediction_date)]
            del df_dummy['Date']
            # print("df_predict_dummy:\n", df_predict_dummy)

            # [청구항1 S42] 끝

            df_real = df_real_dummy.sort_values(by=['Date', 'ZoneNo', 'Hour'])
            df_predict = df_predict_dummy.sort_values(by=['Date', 'ZoneNo', 'Hour'])
            # print("df_predict:\n", df_predict)

            df_real.reset_index(drop=True, inplace=True)
            df_predict.reset_index(drop=True, inplace=True)

            # 입력 데이터와 목표 데이터 분리
            df_real_target = df_real['Load']
            df_real_input = df_real.drop(['Load', 'ZoneNo', 'Date'], axis=1)
            df_predict_target = df_predict['Load']
            # print("df_predict_target:", df_predict_target)
            df_predict_datehour = df_predict[
                ['ZoneNo', 'Date', 'Hour', 'Week', 'TempDiff', 'SOLARRADQ', 'EnthalpyDiff',
                 'PowerUnitRate', 'NightPowerUnitRate', 'GasUnitRate', 'DHUnitRate']]
            df_predict_input = df_predict.drop(['Load', 'ZoneNo', 'Date', 'Hour'], axis=1)
            # print("df_predict_input:\n", df_predict_input)

            #print("df_predict_datehour:", df_predict_datehour)
            X = df_real_input.values
            Y = df_real_target.values
            X_predict = df_predict_input.values
            Y_predict = df_predict_target.values

            # [청구항1 S43] 시작
            # 학습모델 결정부(70)를 통해 훈련 데이터와 시험 데이터를 생성하는 단계
            # 학습 데이터와 시험 데이터 분리
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, stratify=X[:, -1],
                                                                 random_state=random_seed)


            # 훈련 데이터 n배 더 추가
            for p in range(1):
                xTrainTemp, xTestTemp, yTrainTemp, yTestTemp = train_test_split(X, Y, test_size=0.3, stratify=X[:, -1],
                                                                                 random_state=0)
                X_train = np.append(X_train, xTrainTemp, axis=0)
                X_test = np.append(X_test, xTestTemp, axis=0)
                Y_train = np.append(Y_train, yTrainTemp, axis=0)
                Y_test = np.append(Y_test, yTestTemp, axis=0)

            # print("Y:\n", Y)

            X_train = np.delete(X_train, -1, axis=1)  # hour 삭제
            X_test = np.delete(X_test, -1, axis=1)  # hour 삭제
            # [청구항1 S43] 끝

            # 스케일링
            scaling = MinMaxScaler()
            scaling.fit(X_train)
            X_train_scaled = scaling.transform(X_train)
            X_test_scaled = scaling.transform(X_test)
            X_predict_scaled = scaling.transform(X_predict)

            """
            df_x = pd.DataFrame(X_train)
            df_y = pd.DataFrame(Y_train)
            writer = pd.ExcelWriter('./jeju-zone-train' + prediction_date + '.xlsx', engine='xlsxwriter',
                                    datetime_format='yyyy-mm-dd')
            df_x.to_excel(writer, sheet_name='X_train', index=False)
            df_y.to_excel(writer, sheet_name='Y_train', index=False)
            writer.save()
            exit()
            """

            # print("X_train_scaled:\n", X_train_scaled)
            # print("X_test_scaled:\n", X_test_scaled)
            # print("X_predict_scaled:\n", X_predict_scaled)

            # [청구항1 S40] 시작
            # 기상청 서버(100)에서 전송되는 과거 및 미래의 기상데이터와, 냉난방 부하 예측값 및 실측부하를 통해
            # 학습모델 결정부(70)에서 부하 예측 성능이 가장 좋은 최선의 머신러닝 학습모델을 선정하고 훈련하는 단계
            algorithm_dict = {
                0: 'GradientBoostingRegressor',
                1: 'RandomForestRegressor',
                2: 'AdaBoostRegressor',
                3: 'XGBoostRegressor',
                4: 'LightGBMRegressor',
                5: 'Elastic Net',
            }
            output = pd.DataFrame(columns=['algo', 'mse', 'predictions', 'bestparams'])

            # [청구항1 S44] 시작
            # 학습모델 결정부(70)를 통해 최선의 머신러닝 학습모델을 선정하는 단계
            # 탐색 대상 함수 (GradientBoostingRegressor)
            def GBR_cv(max_depth, learning_rate, max_features, n_estimators):
                # 모델 정의
                model = GBR(max_depth=int(max_depth),
                            learning_rate=learning_rate,
                            max_features=int(max_features),
                            n_estimators=int(n_estimators)
                            )
                # 모델 훈련
                model.fit(X_train_scaled, Y_train)

                # 시험 예측값 출력
                Y_test_pred = model.predict(X_test_scaled)

                # 각종 metric 계산
                mse = mean_squared_error(Y_test, Y_test_pred)
                # cvrmse = np.sqrt(mse) / np.mean(Y_test)

                # 오차 최적화로 사용할 metric 반환
                return -mse

            # 실험해보고자하는 hyperparameter 집합
            gbr_bounds = {'max_depth': (2, 5),
                          'learning_rate': (0.01, 1.0),
                          'max_features': (3, 5),
                          'n_estimators': (50, 300)
                          }

            bo_gbr = BayesianOptimization(f=GBR_cv, pbounds=gbr_bounds, verbose=0, random_state=42)
            bo_gbr.maximize(init_points=2, n_iter=10, acq='ei', xi=0.01)
            # print("\n\nbo_gbr.max:\n", bo_gbr.max)

            # 파라미터 적용
            algo_model = GBR(max_depth=int(bo_gbr.max['params']['max_depth']),
                             learning_rate=bo_gbr.max['params']['learning_rate'],
                             max_features=int(bo_gbr.max['params']['max_features']),
                             n_estimators=int(bo_gbr.max['params']['n_estimators'])
                             )
            opt_model = algo_model.fit(X_train_scaled, Y_train)
            Y_pred = opt_model.predict(X_predict_scaled)

            output.loc[0] = [algorithm_dict.get(0), -bo_gbr.max['target'], Y_pred, bo_gbr.max['params']]

            # 탐색 대상 함수 (RandomForestRegressor)
            def RFR_cv(max_depth, max_features, n_estimators):

                # 모델 정의
                model = RFR(max_depth=int(max_depth),
                            max_features=int(max_features),
                            n_estimators=int(n_estimators)
                            )
                # 모델 훈련
                model.fit(X_train_scaled, Y_train)

                # 시험 예측값 출력
                Y_test_pred = model.predict(X_test_scaled)

                # 각종 metric 계산
                mse = mean_squared_error(Y_test, Y_test_pred)
                # cvrmse = np.sqrt(mse) / np.mean(Y_test)

                # 오차 최적화로 사용할 metric 반환
                return -mse

            # 실험해보고자하는 hyperparameter 집합
            rfr_bounds = {'max_depth': (2, 5),
                          'max_features': (3, 5),
                          'n_estimators': (50, 300)
                          }

            bo_rfr = BayesianOptimization(f=RFR_cv, pbounds=rfr_bounds, verbose=0, random_state=42)
            bo_rfr.maximize(init_points=2, n_iter=10, acq='ei', xi=0.01)
            # print("\n\nbo_rfr.max:\n",bo_rfr.max)

            # 파라미터 적용
            algo_model = RFR(max_depth=int(bo_rfr.max['params']['max_depth']),
                             max_features=int(bo_rfr.max['params']['max_features']),
                             n_estimators=int(bo_rfr.max['params']['n_estimators'])
                             )
            opt_model = algo_model.fit(X_train_scaled, Y_train)
            Y_pred = algo_model.predict(X_predict_scaled)

            output.loc[1] = [algorithm_dict.get(1), -bo_rfr.max['target'], Y_pred, bo_rfr.max['params']]

            # 탐색 대상 함수 (AdaBoostRegressor)
            def ABR_cv1(n_estimators, learning_rate):

                # 모델 정의
                model = ABR(n_estimators=int(n_estimators),
                            learning_rate=learning_rate,
                            loss='square'
                            )
                # 모델 훈련
                model.fit(X_train_scaled, Y_train)

                # 시험 예측값 출력
                Y_test_pred = model.predict(X_test_scaled)

                # 각종 metric 계산
                mse = mean_squared_error(Y_test, Y_test_pred)
                # cvrmse = np.sqrt(mse) / np.mean(Y_test)

                # 오차 최적화로 사용할 metric 반환
                return -mse

            def ABR_cv2(n_estimators, learning_rate):

                # 모델 정의
                model = ABR(n_estimators=int(n_estimators),
                            learning_rate=learning_rate,
                            loss='exponential'
                            )
                # 모델 훈련
                model.fit(X_train_scaled, Y_train)

                # 시험 예측값 출력
                Y_test_pred = model.predict(X_test_scaled)

                # 각종 metric 계산
                mse = mean_squared_error(Y_test, Y_test_pred)
                # cvrmse = np.sqrt(mse) / np.mean(Y_test)

                # 오차 최적화로 사용할 metric 반환
                return -mse

            # 실험해보고자하는 hyperparameter 집합
            abr_bounds = {'n_estimators': (50, 300),
                          'learning_rate': (0.01, 0.2)
                          }

            bo_abr = BayesianOptimization(f=ABR_cv1, pbounds=abr_bounds, verbose=0, random_state=42)
            bo_abr.maximize(init_points=2, n_iter=10, acq='ei', xi=0.01)
            # print("\n\nbo_abr.max 1:\n",bo_abr.max)

            # 파라미터 적용(ABR-1)
            algo_model = ABR(n_estimators=int(bo_abr.max['params']['n_estimators']),
                             learning_rate=bo_abr.max['params']['learning_rate']
                             )
            opt_model = algo_model.fit(X_train_scaled, Y_train)
            Y_pred = algo_model.predict(X_predict_scaled)

            output.loc[2] = [algorithm_dict.get(2), -bo_abr.max['target'], Y_pred, bo_abr.max['params']]

            bo_abr = BayesianOptimization(f=ABR_cv2, pbounds=abr_bounds, verbose=0, random_state=42)
            bo_abr.maximize(init_points=2, n_iter=10, acq='ei', xi=0.01)
            # print("\n\nbo_abr.max 2:\n",bo_abr.max)

            # 파라미터 적용(ABR-2)
            algo_model = ABR(n_estimators=int(bo_abr.max['params']['n_estimators']),
                             learning_rate=bo_abr.max['params']['learning_rate']
                             )
            opt_model = algo_model.fit(X_train_scaled, Y_train)
            Y_pred = algo_model.predict(X_predict_scaled)

            output.loc[3] = [algorithm_dict.get(2), -bo_abr.max['target'], Y_pred, bo_abr.max['params']]

            # 탐색 대상 함수 (XGBoostRegressor)
            def XGB_cv(max_depth, learning_rate, n_estimators):

                # 모델 정의
                model = XGB(max_depth=int(max_depth),
                            learning_rate=learning_rate,
                            n_estimators=int(n_estimators)
                            )
                # 모델 훈련
                model.fit(X_train_scaled, Y_train)

                # 시험 예측값 출력
                Y_test_pred = model.predict(X_test_scaled)

                # 각종 metric 계산
                mse = mean_squared_error(Y_test, Y_test_pred)
                # cvrmse = np.sqrt(mse) / np.mean(Y_test)

                # 오차 최적화로 사용할 metric 반환
                return -mse

            # 실험해보고자하는 hyperparameter 집합
            xgb_bounds = {'max_depth': (2, 5),
                          'learning_rate': (0.01, 0.2),
                          'n_estimators': (50, 300)
                          }

            bo_xgb = BayesianOptimization(f=XGB_cv, pbounds=xgb_bounds, verbose=0, random_state=42)
            bo_xgb.maximize(init_points=2, n_iter=10, acq='ei', xi=0.01)
            # print("\n\nbo_xgb.max:\n",bo_xgb.max)

            # 파라미터 적용
            algo_model = XGB(max_depth=int(bo_xgb.max['params']['max_depth']),
                             learning_rate=bo_xgb.max['params']['learning_rate'],
                             n_estimators=int(bo_xgb.max['params']['n_estimators'])
                             )
            opt_model = algo_model.fit(X_train_scaled, Y_train)
            Y_pred = algo_model.predict(X_predict_scaled)

            output.loc[4] = [algorithm_dict.get(3), -bo_xgb.max['target'], Y_pred, bo_xgb.max['params']]

            # 탐색 대상 함수 (LightGBMRegressor)
            def LGB_cv(max_depth, learning_rate, n_estimators):

                # 모델 정의
                model = LGB(max_depth=int(max_depth),
                            learning_rate=learning_rate,
                            n_estimators=int(n_estimators)
                            )
                # 모델 훈련
                model.fit(X_train_scaled, Y_train)

                # 시험 예측값 출력
                Y_test_pred = model.predict(X_test_scaled)

                # 각종 metric 계산
                mse = mean_squared_error(Y_test, Y_test_pred)
                # cvrmse = np.sqrt(mse) / np.mean(Y_test)

                # 오차 최적화로 사용할 metric 반환
                return -mse

            # 실험해보고자하는 hyperparameter 집합
            lgb_bounds = {'max_depth': (2, 5),
                          'learning_rate': (0.01, 0.2),
                          'n_estimators': (50, 300)
                          }

            bo_lgb = BayesianOptimization(f=LGB_cv, pbounds=lgb_bounds, verbose=0, random_state=42)
            bo_lgb.maximize(init_points=2, n_iter=10, acq='ei', xi=0.01)
            # print("\n\nbo_lgb.max:\n",bo_lgb.max)

            # 파라미터 적용
            algo_model = LGB(max_depth=int(bo_lgb.max['params']['max_depth']),
                             learning_rate=bo_lgb.max['params']['learning_rate'],
                             n_estimators=int(bo_lgb.max['params']['n_estimators'])
                             )
            opt_model = algo_model.fit(X_train_scaled, Y_train)
            Y_pred = algo_model.predict(X_predict_scaled)

            output.loc[5] = [algorithm_dict.get(4), -bo_lgb.max['target'], Y_pred, bo_lgb.max['params']]

            # 탐색 대상 함수 (Elastic Net)
            def ETN_cv(alpha, l1_ratio):

                # 모델 정의
                model = ETN(alpha=alpha,
                            l1_ratio=l1_ratio
                            )
                # 모델 훈련
                model.fit(X_train_scaled, Y_train)

                # 시험 예측값 출력
                Y_test_pred = model.predict(X_test_scaled)

                # 각종 metric 계산
                mse = mean_squared_error(Y_test, Y_test_pred)
                # cvrmse = np.sqrt(mse) / np.mean(Y_test)

                # 오차 최적화로 사용할 metric 반환
                return -mse

            # 실험해보고자하는 hyperparameter 집합
            etn_bounds = {'alpha': (0.1, 0.3),
                          'l1_ratio': (0, 1)
                          }

            bo_etn = BayesianOptimization(f=ETN_cv, pbounds=etn_bounds, verbose=0, random_state=42)
            bo_etn.maximize(init_points=2, n_iter=1, acq='ei', xi=0.01)
            # print("\n\nbo_etn.max:\n",bo_etn.max)

            # 파라미터 적용
            algo_model = ETN(alpha=bo_etn.max['params']['alpha'],
                             l1_ratio=bo_etn.max['params']['l1_ratio']
                             )
            opt_model = algo_model.fit(X_train_scaled, Y_train)
            Y_pred = algo_model.predict(X_predict_scaled)

            output.loc[6] = [algorithm_dict.get(5), -bo_etn.max['target'], Y_pred, bo_etn.max['params']]
            # [청구항1 S44] 끝
            # [청구항1 S40] 끝

            # 날짜 가져오기
            X_datehour = df_predict_datehour.values
            # print("X_datehour:\n", X_datehour)

            # 학습모델 결정부(70)를 통해 최선의 머신러닝 학습모델을 선정하는 단계
            # [청구항1 S45] 시작
            # 학습모델 결정부(70)를 통해 선정된 머신러닝 학습모델을 훈련하는 단계(S45)를 포함하는 것을
            # 특징으로 하는 다중 인공지능 학습모델을 기반으로 한 건물 냉난방 부하의 예측 방법
            # 최적화 결과 mse가 작은 순으로 정렬 및 알고리즘, 초매개변수 저장
            output.sort_values(["mse"], ascending=True, inplace=True)
            model_algo = np.append(model_algo, output.iloc[0, 0])
            model_params = np.append(model_params, output.iloc[0, 3])
            # [청구항1 S45] 끝

            # [청구항1 S50] 시작
            # 학습모델 결정부(70)를 통해 결정된 머신러닝 학습모델을 예측부하 산출부(60)에 적용하여
            # 예측부하를 산출하는 단계
            # 실측부하 및 예측부하 출력
            #record_cnt = output.iloc[0, 2].size
            #print("record_cnt:", record_cnt)

            j = 0
            for i in output.iloc[0, 2]:
                i = np.float64(i)
                load_round = np.around(i)

                # 예측부하가 0보다 적은 경우 예측부하 0
                if load_round < 0:
                    load_round = np.around(output.iloc[1, 2][j])

                # 예측부하가 0보다 적은 경우 예측부하 0
                if load_round < 0:
                    load_round = 0

                # [청구항1 S60] 시작
                # 산출된 실측부하와 예측부하 간의 오차를 예측부하 보정부(80)를 통해 검증하여
                # 예측부하를 보정하는 단계(S60)
                # 예측부하 테이블에 데이터가 없을 때 처리 추가해야함

                # revision = 1
                if method_no == 2:
                    df_revision = df_r[(df_r['BuildingNo'] == building_list) & (df_r['ZoneNo'] == X_datehour[j, 0]) & (
                            df_r['RealHour'] == X_datehour[j, 2])]

                    if df_revision.empty:
                        revision = 1
                    else:
                        revision = 1
                        revision = df_revision.iloc[0][5]
                        # 보정계수 상한치/하한치 적용
                        if revision > 1.1:
                            revision = 1.1
                        elif revision < 0.9:
                            revision = 0.9
                else:
                    revision = 1

                if weekholiday == 0:
                    revision = 1

                # print("weekholiday:", weekholiday, "holidaycode:", holidaycode)

                # print("building_list:", building_list, "X_datehour[j, 0]:", X_datehour[j, 0], "X_datehour[j, 2]:",
                #      X_datehour[j, 2])
                # print("load_round:", load_round, "revision:", revision)
                load_round_revision = int(load_round * revision)
                # print("load_round_revision:", load_round_revision)
                # [청구항1 S60] 끝

                load_sum = load_sum + load_round_revision

                if weekholiday == 0:
                    X_datehour[j, 3] = 0
                if weekholiday == 1:
                    X_datehour[j, 3] = 1

                print(building_list, "빌딩 존:%s " % str((X_datehour[j, 0])), " 일자:%s " % (X_datehour[j, 1]),
                      " 시간:%s " % str(X_datehour[j, 2]), " 휴일여부:%s " % str(X_datehour[j, 3]),
                      " 예측부하:%8d" % load_round, " 알고리즘:%s" % output.iloc[0, 0])
                df_predict_zone_load.loc[cnt] = [building_list, str(X_datehour[j, 0]), X_datehour[j, 1], X_datehour[j, 2],
                                                 X_datehour[j, 3], X_datehour[j, 4], X_datehour[j, 5], X_datehour[j, 6],
                                                 Y_predict[j], load_round_revision, X_datehour[j, 7], X_datehour[j, 8],
                                                 X_datehour[j, 9], X_datehour[j, 10]]

                """    
                print(building_list, "  존 %s " % str((X_datehour[j, 0])), "  일자 %s  " % (X_datehour[j, 1]),
                      "시간 %s  " % str(X_datehour[j, 2]), "휴일여부 %s " % str(X_datehour[j, 3]),
                      "실측부하 %.2f  " % Y_predict[j], "보정예측부하 %8d " % load_round_revision,
                      "보정계수 %.2f  " % revision, "예측부하 %8d  " % load_round, "알고리즘 %s" % output.iloc[0, 0])

                df_predict_zone_load.loc[cnt] = [building_list, str(X_datehour[j, 0]), X_datehour[j, 1],
                                                 X_datehour[j, 2],
                                                 X_datehour[j, 3], X_datehour[j, 4], X_datehour[j, 5], X_datehour[j, 6],
                                                 Y_predict[j], load_round_revision, revision, load_round,
                                                 X_datehour[j, 9], X_datehour[j, 10]]
                """

                c.insert_loadpredictioninfo(df_predict_zone_load.loc[cnt], air_condition, dt_hm)
                s_hour, e_hour = c.prediction_hour(building_list, X_datehour[j, 0], air_condition)
                if X_datehour[j, 2] == e_hour:
                    start_hour = int(int(s_hour)/ 100)
                    end_hour = int(int(e_hour) / 100)
                    c.insert_non_prediction_range(building_list, X_datehour[j, 0], X_datehour[j, 1], X_datehour[j, 3],
                                                  start_hour, end_hour, air_condition)
                cnt = cnt + 1
                j = j + 1
            # gc.collect()
            # [청구항1 S50] 끝

            # 건물별 실측부하 및 예측부하
            real_load = df_predict_zone_load[(df_predict_zone_load['BuildingNo'] == building_list)]["Load"].to_numpy()
            predict_load = df_predict_zone_load[(df_predict_zone_load['BuildingNo'] == building_list)][
                "PredictLoad"].to_numpy()

            # 건물별 성능평가 지수
            cvmbe = (np.mean(predict_load - real_load)) / np.mean(real_load)
            cvmae = (mean_absolute_error(predict_load, real_load)) / np.mean(real_load)
            cvrmse = (np.sqrt(mean_squared_error(predict_load, real_load))) / np.mean(real_load)

            print("")
            print(building_list, "  예측부하 합계  ", round(load_sum, 2))
            """
            print('Cv(MBE)  : ' + str(round(cvmbe * 100, 2)) + " %")
            print('Cv(MAE)  : ' + str(round(cvmae * 100, 2)) + " %")
            print('Cv(RMSE) : ' + str(round(cvrmse * 100, 2)) + " %")
            """

            # 건물별 최적 알고리즘 및 초매개변수 출력
            for algo, params in zip(model_algo, model_params):
                df_algorithm.loc[n] = [building_list, algo]
                n = n + 1
                print(algo, " ", params)
            print("")

        """
        # 예측부하를 존별, 날짜별, 시간별로 그룹화
        df_predict_zone_load.sort_values(["BuildingNo", "ZoneNo", "Date", "Hour"], ascending=True, inplace=True)
        df_predict_hour_load = df_predict_zone_load.groupby(["BuildingNo", "Date", "Hour"], as_index=False).sum()
        df_predict_date_load = df_predict_zone_load.groupby(["BuildingNo", "Date"], as_index=False).sum()
        df_predict_date_load['algorithm'] = df_algorithm['algorithm']

        # 엑셀 여러 sheet에 저장
        writer = pd.ExcelWriter('./jeju-zone-predict-new' + prediction_date + '.xlsx', engine='xlsxwriter',
                                datetime_format='yyyy-mm-dd')
        df_predict_zone_load.to_excel(writer, sheet_name='존별 시간별', index=False)
        df_predict_hour_load.to_excel(writer, sheet_name='시간별', index=False)
        df_predict_date_load.to_excel(writer, sheet_name='날짜별', index=False)
        del df_all_data
        writer.save()
        """
        end = time.time()

        print("소요시간: ", end - start)
        print("종료")




c = Common('')  # KBHMU042 KACLP002 NTACP064
sitecode = c.site_code()

# 조건1 (냉난반 예측 기간 판단)
# loadprediction_method(2, '20180813', 1, '0530')
# loadprediction_method(3, '20180908', 1, '0530')

"""
df_days = c.op_days('20180813', '20180907')
for day_list in df_days['DATE']:
    print("day_list:", day_list)
    loadprediction_method(2, day_list, 1, '0530')

df_days = c.op_days('20180928', '20180930')
# for day_list in df_days['RealDate']:
for day_list in df_days['DATE']:
    print("day_list:", day_list)
    loadprediction_method(3, day_list, '0530')
"""
