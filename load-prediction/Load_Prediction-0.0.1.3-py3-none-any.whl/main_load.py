# main_load.py

from load_prediction import *
import datetime as dt
from datetime import datetime
import sys

c = Common('')
sitecode = c.site_code()
# print("sitecode:", sitecode)

dt_now = dt.datetime.now()
dt_tomorrow = dt_now + dt.timedelta(days=1)
op_hour = dt_now.strftime("%H%M")

# 테스트시 사용
# dt_now = dt.datetime(2018, 8, 8)
# dt_hm = dt.time(9, 0)

if len(sys.argv) >= 6:
    dt_now = dt.datetime(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    dt_hm = dt.time(int(sys.argv[4]), int(sys.argv[5]))
    print(f"날짜: {sys.argv[1]}{sys.argv[2]}{sys.argv[3]}")
    print(f"시간: {sys.argv[4]}{sys.argv[5]}")
    print("인자의 개수: %d" %(len(sys.argv)))
    print(f"파일명: {sys.argv[0]}")
    print(f"날짜: {sys.argv[1]}{sys.argv[2]}{sys.argv[3]}")
    print(f"시간: {sys.argv[4]}{sys.argv[5]}")

dt_tomorrow = dt_now + dt.timedelta(days=1)
op_hour = dt_hm.strftime("%H%M")

predict_today = dt_now.strftime("%Y%m%d")
predict_tomorrow = dt_tomorrow.strftime("%Y%m%d")
print("오늘:", dt_now, "내일:", dt_tomorrow, "시간:", op_hour)
print("predict_today:", predict_today, "predict_tomorrow:", predict_tomorrow)

# 보정일수, 보정시각
loadcorrectionday, correctionhour = c.revision_days()
print("loadcorrectionday:", loadcorrectionday, "correctionhour", correctionhour)

# 예측일 설정
if op_hour < correctionhour:
    prediction_date = predict_today
else:
    prediction_date = predict_tomorrow

# 조건1 (냉난반 예측 기간 판단)
air_condition = c.determine_air_condition(prediction_date)
print("air_condition:", air_condition)

# 휴일/평일 구분
weekholiday, holidaycode = c.is_weekday(prediction_date)
print("평일/휴일 구분:", weekholiday)

# 조건2 (실측수요부하 테이블의 냉난방별 부하실측일수, 부하보정일수 비교)
# 평일 휴일 구분 : '1'이 아닌 값으로 지정하여 전체일자를 센다
all_real_load_days = c.real_load_days(str(air_condition), prediction_date, '0')
print("부하실측일수:", all_real_load_days)

# real_load_days = 3
# loadcorrectionday = 10
# correctionhour = '1740'

# 조건2 (실측수요부하 테이블의 냉난방별 부하실측일수, 부하보정일수 비교)
if all_real_load_days < loadcorrectionday:

    # 조건3 (건물 특성 정보)
    # 운영지점정보 테이블의 [부하예측방식] 0=부하예측방법1을 적용하지 않음, 1=부하예측방법 1을 적용
    loadpredictionmethod = c.load_prediction_method()
    # loadpredictionmethod = 0
    if loadpredictionmethod == 0:
        print("[조건3]")
        print("부하예측 적용을 하지 않습니다.")
        exit()

    if loadpredictionmethod == 1:
        # 조건4
        # 예측부하 테이블의 냉난방 부하예측일수와 부하보정일수 비교
        predict_load_days = c.predict_load_days(air_condition, prediction_date, str(weekholiday))
        # print("[조건4]")
        print("predict_load_days:", predict_load_days)

        # df_all_data = c.load_by_real_foretime_realweather(prediction_date, air_condition)

        # 부하예측 방법1 : 실측수요부하 테이블에 데이터가 없을 때, 예측부하 테이블에 데이터를 입력하기 위한 함수
        # 실측수요부하 테이블의 과거 데이터를 기반으로 하여 기상실황 정보를 가지고 예측부하를 구하기 위한 함수(제주도용)

        if predict_load_days < loadcorrectionday:
            # [조건5] 건물 특성 정보
            print("건물 특성 정보를 이용한 부하예측")
            # 조건 5
            c.insert_airvent_load(prediction_date, air_condition)
            c.insert_interior_heat_load(prediction_date, air_condition)
            c.insert_heat_trans_load(prediction_date, air_condition)
            c.insert_solar_rad_load(prediction_date, air_condition)
            c.insert_loadprediction_info(prediction_date, weekholiday, air_condition)

        if predict_load_days >= loadcorrectionday:
            # 조건 5
            # dt_now = dt.datetime.now()
            # dt_hm = dt_now.strftime("%H%M")
            print("[조건5] 부하예측 방법3")
            loadprediction_method(3, prediction_date, air_condition)

# 조건2 (실측수요부하 테이블의 냉난방별 부하실측일수, 부하보정일수 비교)
if all_real_load_days >= loadcorrectionday:
    # print("테이블 정보")
    # 조건3 (건물 특성 정보)
    # 평일 휴일 구분 : '1'로 지정하여 평일일자를 센다
    real_load_days = c.real_load_days(str(air_condition), prediction_date, '1')
    print("평일 부하실측일수:", real_load_days)
    if real_load_days < loadcorrectionday:
        print("[조건5] 부하예측 방법3")
        loadprediction_method(3, prediction_date, air_condition, op_hour)

    if real_load_days >= loadcorrectionday:
        print("[조건2] 부하예측 방법2")
        loadprediction_method(2, prediction_date, air_condition, op_hour)

