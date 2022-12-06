# common_functions.py

import pymssql
import pandas as pd
import datetime as dt
import mssql_auth
import numpy as np
import datetime
# from load_prediction import sitecode

login = mssql_auth.info


class Common:
    __host = login["host"]
    __user = login["user"]
    __password = login["passwd"]
    __database = login["database"]
    __charset = login["charset"]
    sitecode = ""

    def __init__(self, sitecode):
        self.sitecode = sitecode
        Common.sitecode = sitecode

    # MSSQL 접속
    @classmethod
    def conn(cls):
        return pymssql.connect(cls.__host, cls.__user, cls.__password, cls.__database, charset='UTF8')

    # 운영지점 코드 (T_SITE_INFORMATION)
    # noinspection PyMethodMayBeStatic
    def site_code(self):
        db = Common.conn()
        cursor = db.cursor()
        cursor.execute("SELECT top 1 ltrim(SiteCode) FROM T_SITE_INFORMATION WHERE OperationYN = 'Y' ")

        all_row = cursor.fetchall()
        scode = all_row[0][0]
        cursor.close()
        db.close()

        Common.sitecode = scode
        return scode

    # 냉방/난방 시작일자
    # noinspection PyMethodMayBeStatic
    def operating_start_date(self):
        db = Common.conn()
        cursor = db.cursor()
        sql = "SELECT  ltrim(ColdStartDate), ltrim(HeatingStartDate) \
                 FROM T_OPERATING_CONFIG \
                WHERE SiteCode = '" + Common.sitecode + "' "
        cursor.execute(sql)

        # 실행문 조회
        all_row = cursor.fetchall()
        cold_startdate = all_row[0][0]
        heating_startdate = all_row[0][1]

        cursor.close()
        db.close()

        return cold_startdate, heating_startdate

    # 냉방시작월, 냉방종료월
    # noinspection PyMethodMayBeStatic
    def cooling_month(self):
        db = Common.conn()
        cursor = db.cursor()
        sql = "SELECT  Coldstartmonth, Coldendmonth \
                 FROM T_OPERATING_CONFIG \
                WHERE sitecode = '" + Common.sitecode + "'"
        cursor.execute(sql)

        # 실행문 조회
        all_row = cursor.fetchall()
        start_month = all_row[0][0]
        end_month = all_row[0][1]
        start_month = str(start_month)
        end_month = str(end_month)

        cursor.close()
        db.close()
        return start_month, end_month

    # 조건2: 실측수요부하 테이블의 냉난방별 부하실측일수
    # 평일휴일구분이 '1' 이면 평일 일수, 아니면 전체 일수
    # noinspection PyMethodMayBeStatic
    def real_load_days(self, air_condition, predicttiondate, weekday_yn):
        db = Common.conn()
        cursor = db.cursor()

        sql = " SELECT count(DISTINCT(r.RealDate)) \
                  FROM T_REAL_DEMAND_LOAD_INFO AS r \
                       LEFT OUTER JOIN T_LOAD_PREDICTION_INFO p \
                          ON r.SiteCode = p.sitecode AND r.BuildingNo = p.buildingno \
                         AND r.zoneno =  p.zoneno \
                 WHERE r.SiteCode = '" + Common.sitecode + "' \
                   AND isnull(p.ColdHeatingIndication, '0') = '" + air_condition + "' \
                   AND r.WeekHoliday IN (CASE WHEN '" + weekday_yn + "' = 1 THEN 1 ELSE r.WeekHoliday END) \
                   AND r.RealDate between \
                                  format(CAST(dateadd(year, -1, '" + predicttiondate + "' ) AS date), 'yyyy0101') \
                                  AND convert(varchar(10),dateadd(d, -1,'" + predicttiondate + "'),112) "
        cursor.execute(sql)
        # 실행문 조회
        real_loaddays = cursor.fetchall()
        real_loaddays = real_loaddays[0][0]

        cursor.close()
        db.close()
        return real_loaddays

    # 조건4: 예측부하 테이블의 냉난방 부하예측일수
    # noinspection PyMethodMayBeStatic
    def predict_load_days(self, air_condition, predicttiondate, weekday_yn):
        db = Common.conn()
        cursor = db.cursor()
        sql = "SELECT COUNT(DISTINCT(PredictionDate)) \
                 FROM T_LOAD_PREDICTION_INFO \
                WHERE SiteCode = '" + Common.sitecode + "' \
                  AND isnull(ColdHeatingIndication, '0') = '" + air_condition + "' \
                  AND WeekHoliday IN (CASE WHEN '" + weekday_yn + "' = 1 THEN 1 ELSE WeekHoliday END) \
                  AND PredictionDate between \
                                  format(CAST(dateadd(year,-1, '" + predicttiondate + "' ) AS date), 'yyyy0101') \
                                  AND convert(varchar(10),dateadd(d, -1,'" + predicttiondate + "'),112) "
        cursor.execute(sql)
        predict_load_days = cursor.fetchall()
        predict_load_days = predict_load_days[0][0]
        cursor.close()
        db.close()
        return predict_load_days

    # 부하보정일수, 보정기준시각 (운영환경 테이블)
    # noinspection PyMethodMayBeStatic
    def revision_days(self):
        db = Common.conn()
        cursor = db.cursor()
        sql = "SELECT LoadCorrectionDay, CorrectionHour  \
                 FROM T_OPERATING_CONFIG \
                WHERE sitecode = '" + Common.sitecode + "' "
        cursor.execute(sql)

        # 실행문 조회
        operating_config = cursor.fetchall()
        load_correction_day = operating_config[0][0]
        correction_hour = operating_config[0][1]

        cursor.close()
        db.close()
        return load_correction_day, correction_hour

    # 냉방 기준온도, 난방 기준온도
    # noinspection PyMethodMayBeStatic
    def base_temp(self):
        db = Common.conn()
        cursor = db.cursor()
        sql = "SELECT ColdBaseTemp, HeatingBaseTemp  \
                 FROM T_OPERATING_CONFIG \
                WHERE sitecode = '" + Common.sitecode + "' "
        cursor.execute(sql)

        # 실행문 조회
        operating_config = cursor.fetchall()
        cold_basetemp = operating_config[0][0]
        heating_basetemp = operating_config[0][1]

        cursor.close()
        db.close()
        return cold_basetemp, heating_basetemp

    # 부하예측방식 (운영지점정보)
    # noinspection PyMethodMayBeStatic
    def load_prediction_method(self):
        db = Common.conn()
        cursor = db.cursor()
        cursor.execute("SELECT LoadPredictionMethod FROM T_SITE_INFORMATION \
                         WHERE sitecode = '" + Common.sitecode + "' --AND OperationYN = 'Y' ")

        loadpredictionmethod = cursor.fetchall()
        loadpredictionmethod = loadpredictionmethod[0][0]
        cursor.close()
        db.close()

        return loadpredictionmethod

    # 존정보 테이블 설정 정보 가져오기
    # noinspection PyMethodMayBeStatic
    def zone_info(self, buildingno, zoneno, air_condition):
        db = Common.conn()
        cursor = db.cursor()
        sql = ""
        if air_condition == '1':
            sql = "SELECT ColdSetupTemp, ColdSetupEnthalpy \
                     FROM T_ZONE_INFO \
                    WHERE SiteCode = '" + Common.sitecode + "' \
                      AND BuildingNo = '" + buildingno + "' \
                      AND zoneno = '" + zoneno + "' "
        if air_condition == '2':
            sql = "SELECT HeatingSetupTemp, HeatingSetupEnthalpy \
                     FROM T_ZONE_INFO \
                    WHERE SiteCode = '" + Common.sitecode + "' \
                      AND BuildingNo = '" + buildingno + "' \
                      AND ZoneNo = '" + zoneno + "' "
        cursor.execute(sql)

        # 실행문 조회
        all_rows = cursor.fetchall()
        setup_temp = all_rows[0][0]
        setup_enthalpy = all_rows[0][1]

        cursor.close()
        db.close()
        return round(setup_temp, 2), round(setup_enthalpy, 2)

    # 오늘 현재 시간에 따라 오늘 부하예측인지 내일 부하예측인지 구분
    # noinspection PyMethodMayBeStatic
    def forecast_date(self):
        load_correction_day, correction_hour = Common.revision_days(Common.sitecode)

        dt_today = dt.datetime.now()
        tomorrow = dt_today + pd.DateOffset(1)

        dt_today_hour = dt_today.strftime("%H%M")
        dt_today = dt_today.strftime("%Y%m%d")
        tomorrow = tomorrow.strftime("%Y%m%d")

        if dt_today_hour >= correction_hour:
            forecastdate = tomorrow
        else:
            forecastdate = dt_today
        return forecastdate

    # 평균기온(오늘 이전 1~3일 간의 오전 9시 평균기온) (기상청 1시간 기상 실황)
    # noinspection PyMethodMayBeStatic
    def avg_temp(self, announcedate):
        db = Common.conn()
        cursor = db.cursor()
        sql = "SELECT avg(o.REALTEMP) \
                 FROM T_1HOUR_WEATHER_REAL_INFO o \
                WHERE o.ANNOUNCEDATE BETWEEN convert(varchar(10),dateadd(d, -2, '" + announcedate + "'), 112) \
                                             AND '" + announcedate + "' \
                  AND o.ANNOUNCEHOUR = '0900' \
                  AND o.SiteCode = '" + Common.sitecode + "' "

        cursor.execute(sql)

        # 실행문 조회
        avgtemp = cursor.fetchall()
        avgtemp = avgtemp[0][0]
        # avgtemp = round(avgtemp[0][0], 2)

        cursor.close()
        db.close()
        return avgtemp

    # 간절기 확인: 예측일자가 실측수요부하 테이블에는 없고 예측부하 테이블에 있으면 간절기
    # noinspection PyMethodMayBeStatic
    def season_changes(self, predictiondate):
        this_month = int(predictiondate[4:6])
        season_changes_yn = "N"
        if 3 <= this_month <= 5 or 9 <= this_month <= 11:
            db = Common.conn()
            cursor = db.cursor()
            sql = " SELECT COUNT(distinct p.PredictionDate) \
                      FROM T_LOAD_PREDICTION_INFO p \
                      LEFT OUTER JOIN T_REAL_DEMAND_LOAD_INFO r \
                        ON p.SiteCode = r.SiteCode \
                       AND p.BuildingNo = r.BuildingNo \
                       AND p.ZoneNo = r.ZoneNo \
                       AND p.PredictionDate = r.RealDate \
                       AND p.WeekHoliday = r.WeekHoliday \
                     WHERE p.SiteCode = '" + Common.sitecode + "' \
                       AND p.WeekHoliday = 1 \
                       AND r.RealDate IS NULL \
                       AND p.PredictionDate = '" + predictiondate + "' "
            cursor.execute(sql)
            all_rows = cursor.fetchall()
            predictiondate_cnt = all_rows[0][0]
            cursor.close()
            db.close()
            # print("predictiondate_cnt:[", predictiondate_cnt, "]")
            if predictiondate_cnt == 1:
                season_changes_yn = 'Y'
        return season_changes_yn

    # 예측부하 테이블에서 냉반방구분 확인
    # noinspection PyMethodMayBeStatic
    def search_ColdHeatingIndication(self, predictiondate):
        db = Common.conn()
        cursor = db.cursor()
        sql = "SELECT top 1 isnull(max(p.ColdHeatingIndication),0) \
                 FROM T_LOAD_PREDICTION_INFO AS p \
                WHERE p.SiteCode = '" + Common.sitecode + "' \
                  AND format(CAST(p.PredictionDate AS date), 'yyyyMMdd') = '" + predictiondate + "' "
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        coolheatindication = all_rows[0][0]
        cursor.close()
        db.close()
        return int(coolheatindication)

    # [청구항1 S20] 시작
    # 기상청 서버(100)에서 전송받은 과거 및 미래 예측 기상 데이터를 통해 부하예측 판단부(40)에서
    # 부하 예측 대상이 냉방부하인지 난방부하인지 결정하는 단계
    # 냉난방 예측 기간 판단
    # noinspection PyMethodMayBeStatic
    def determine_air_condition(self, predictiondate):
        cold_startdate, heating_startdate = Common.operating_start_date(Common.sitecode)
        cold_basetemp, heating_basetemp = Common.base_temp(Common.sitecode)
        start_month, end_month = Common.cooling_month(Common.sitecode)
        avgtemp = Common.avg_temp(Common.sitecode, predictiondate)
        this_month = int(predictiondate[4:6])
        air_condition = Common.search_ColdHeatingIndication(Common.sitecode, predictiondate)
        # print("coldstartdate", cold_startdate, "heatingstartdate", heating_startdate)
        # print("this_month", this_month, "startmonth", start_month, "endmonth", end_month)

        if air_condition == 0:
            if cold_startdate is None and heating_startdate is not None:
                if this_month < int(start_month) - 1:
                    air_condition = "2"  # 난방기간
                elif this_month > int(end_month) + 1:
                    air_condition = "2"  # 난방기간
                elif this_month <= int(end_month) + 1 and predictiondate >= heating_startdate:
                    air_condition = "2"  # 난방 예측기간(가을 환절기)

                elif this_month == (int(start_month) - 1) and avgtemp >= cold_basetemp:
                    air_condition = "1"  # 냉방 예측기간(봄 환절기)
                    # 운영환경 update : 냉방시작일자 = 내일(forecast_date), 난방시작일자 = NULL
                    db = Common.conn()
                    cursor = db.cursor()
                    sql = "UPDATE T_OPERATING_CONFIG           \
                               SET coldstartdate = '" + predictiondate + "', heatingstartdate = NULL \
                            WHERE sitecode = '" + Common.sitecode + "' "
                    cursor.execute(sql)
                    db.commit()
                    cursor.close()
                    db.close()
                else:
                    air_condition = "2"  # 난방 예측기간(봄 환절기)

            if cold_startdate is not None and heating_startdate is None:
                if this_month <= int(end_month):
                    air_condition = "1"
                elif this_month <= (int(end_month) + 1) and avgtemp <= heating_basetemp:
                    air_condition = "2"
                    # 운영환경 update : 난방시작일자 = 내일(forecast_date), 냉방시작일자 = NULL
                    db = Common.conn()
                    cursor = db.cursor()
                    sql = "UPDATE T_OPERATING_CONFIG           \
                               SET ColdStartDate = NULL, HeatingStartDate = '" + predictiondate + "' \
                            WHERE SiteCode = '" + Common.sitecode + "' "
                    cursor.execute(sql)
                    db.commit()
                    cursor.close()
                    db.close()
                else:
                    air_condition = "1"

            if cold_startdate is None and heating_startdate is None:
                if (this_month >= int(start_month)) and (this_month <= int(end_month)):
                    air_condition = "1"
                    # 운영환경 update : 냉방시작일자 = 내일(forecast_date), 난방시작일자 = NULL
                    db = Common.conn()
                    cursor = db.cursor()
                    sql = "UPDATE T_OPERATING_CONFIG           \
                               SET ColdStartDate = '" + predictiondate + "', HeatingStartDate = NULL \
                            WHERE SiteCode = '" + Common.sitecode + "' "
                    cursor.execute(sql)
                    db.commit()
                    cursor.close()
                    db.close()
                elif (this_month == int(start_month) - 1) and (avgtemp >= cold_basetemp):
                    air_condition = "1"
                    # 운영환경 update : 냉방시작일자 = 내일(forecast_date), 난방시작일자 = NULL
                    db = Common.conn()
                    cursor = db.cursor()
                    sql = "UPDATE T_OPERATING_CONFIG           \
                               SET ColdStartDate = '" + predictiondate + "', HeatingStartDate = NULL \
                            WHERE SiteCode = '" + Common.sitecode + "' "
                    cursor.execute(sql)
                    db.commit()
                    cursor.close()
                    db.close()
                elif this_month == int(start_month) - 1:
                    air_condition = "2"
                    # 운영환경 update : 난방시작일자 = 내일(forecast_date), 냉방시작일자 = NULL
                    db = Common.conn()
                    cursor = db.cursor()
                    sql = "UPDATE T_OPERATING_CONFIG           \
                               SET ColdStartDate = NULL, HeatingStartDate = '" + predictiondate + "' \
                            WHERE SiteCode = '" + Common.sitecode + "' "
                    cursor.execute(sql)
                    db.commit()
                    cursor.close()
                    db.close()
                elif (this_month == int(start_month) + 1) and (avgtemp <= heating_basetemp):
                    air_condition = "2"
                    # 운영환경 update : 난방시작일자 = 내일(forecast_date), 냉방시작일자 = NULL
                    db = Common.conn()
                    cursor = db.cursor()
                    sql = "UPDATE T_OPERATING_CONFIG           \
                               SET ColdStartDate = NULL, HeatingStartDate = '" + predictiondate + "' \
                            WHERE SiteCode = '" + Common.sitecode + "' "
                    cursor.execute(sql)
                    db.commit()
                    cursor.close()
                    db.close()
                elif this_month == int(start_month) + 1:
                    air_condition = "1"
                    # 운영환경 update : 냉방시작일자 = 내일(forecast_date), 난방시작일자 = NULL
                    db = Common.conn()
                    cursor = db.cursor()
                    sql = "UPDATE T_OPERATING_CONFIG           \
                               SET ColdStartDate = '" + predictiondate + "', HeatingStartDate = NULL \
                            WHERE SiteCode = '" + Common.sitecode + "' "
                    cursor.execute(sql)
                    db.commit()
                    cursor.close()
                    db.close()
                else:
                    air_condition = "2"
                    # 운영환경 update : 난방시작일자 = 내일(forecast_date), 냉방시작일자 = NULL
                    db = Common.conn()
                    cursor = db.cursor()
                    sql = "UPDATE T_OPERATING_CONFIG           \
                               SET ColdStartDate = NULL, HeatingStartDate = '" + predictiondate + "' \
                            WHERE SiteCode = '" + Common.sitecode + "' "
                    cursor.execute(sql)
                    db.commit()
                    cursor.close()
                    db.close()
        return air_condition
    # [청구항1 S20] 끝

    # 공휴일인지 체크
    # noinspection PyMethodMayBeStatic
    def is_holiday(self, predictiondate):
        db = Common.conn()
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM T_HOLIDAY \
                         WHERE sitecode = '" + Common.sitecode + "' AND Holiday = '" + predictiondate + "' ")
        holiday = cursor.fetchall()
        holiday_cnt = holiday[0][0]
        if holiday_cnt == 1:
            isholiday = 'Y'
        else:
            isholiday = 'N'
        cursor.close()
        db.close()
        return isholiday

    # 공휴일 포함해서 휴일, 평일 구분
    # noinspection PyMethodMayBeStatic
    def is_weekday(self, predictiondate):
        isholiday = Common.is_holiday(Common.sitecode, predictiondate)

        datetime_date = dt.datetime.strptime(predictiondate, '%Y%m%d')
        datetime_week = datetime_date.weekday() + 1

        db = Common.conn()
        cursor = db.cursor()
        cursor.execute("SELECT HOLIDAYCODE FROM T_SITE_INFORMATION \
                         WHERE sitecode = '" + Common.sitecode + "' ")
        holiday_code = cursor.fetchall()
        holiday_code = holiday_code[0][0]

        if isholiday == 'Y' or datetime_week == holiday_code or (holiday_code == 7 and datetime_week == 6):
            datetime_week = 0
        else:
            datetime_week = 1

        cursor.close()
        db.close()
        return datetime_week, holiday_code

    """
    # 휴일코드
    # noinspection PyMethodMayBeStatic
    def holiday_code(self):
        db = Common.conn()
        cursor = db.cursor()
        sql = "SELECT  HOLIDAYCODE \
                  FROM T_SITE_INFORMATION \
                 WHERE sitecode = '" + Common.sitecode + "'"
        cursor.execute(sql)

        # 실행문 조회
        all_row = cursor.fetchall()
        holiday_code = all_row[0][0]

        cursor.close()
        db.close()
        return holiday_code
    """

    # [청구항1 S41] 시작
    # 관제서버(10)에 저장되는 과거 데이터들을 가져오는 단계
    # 방법1
    # 실측수요부하 테이블에 데이터가 없을 때 예측부하 테이블에 입력할 데이터를 생성하기 위한 함수
    # 실측수요부하 테이블의 과거 데이터 기반으로 하여 기상실황 정보를 가지고 예측부하를 구하기 위한 함수(제주도용)
    # noinspection PyMethodMayBeStatic
    def load_by_real_foretime_realweather(self, predictiondate, air_condition):
        db = Common.conn()
        cursor = db.cursor()

        sql = " SELECT r.BuildingNo, r.ZoneNo, r.RealDate AS Date, r.RealHour AS Hour, r.WeekHoliday as Week \
                       CASE WHEN '" + str(air_condition) + "' = '1' THEN w.REALTEMP - z.ColdSetupTemp \
                            ELSE w.REALTEMP - z.HeatingSetupTemp END AS TempDiff, \
                       CASE WHEN z.SOLARRADYN = 0 THEN 0 ELSE w.REALSOLARRADQ END AS SOLARRADQ, \
                       CASE WHEN '" + str(air_condition) + "' = '1' THEN w.REALENTHALPY - z.ColdSetupEnthalpy \
                            ELSE w.REALENTHALPY - z.HeatingSetupEnthalpy END AS EnthalpyDiff, \
                            sum(r.RealDemandLoad) AS Load \
                  FROM T_REAL_DEMAND_LOAD_INFO r \
                       INNER JOIN T_1HOUR_WEATHER_REAL_INFO w \
                          ON r.SiteCode = w.sitecode AND r.RealDate = w.ANNOUNCEDATE \
                         AND LTRIM(r.RealHour) = LTRIM(w.ANNOUNCEHOUR) \
                       INNER JOIN T_ZONE_INFO z \
                          ON r.SiteCode = z.sitecode AND r.BuildingNo = z.buildingno \
                         AND r.ZoneNo = z.zoneno \
                 WHERE r.SiteCode = '" + Common.sitecode + "' \
                   AND r.RealDate between \
                             format(CAST(dateadd(year, -1, '" + predictiondate + "') AS date), 'yyyy0101') \
                          AND convert(varchar(10),dateadd(d, 0, '" + predictiondate + "'), 121) \
                 GROUP BY r.BuildingNo, r.ZoneNo, r.RealDate, r.RealHour, \
                          w.REALTEMP, z.ColdSetupTemp, z.HeatingSetupTemp, z.SOLARRADYN, \
                          w.REALSOLARRADQ, w.REALENTHALPY, z.ColdSetupEnthalpy, z.HeatingSetupEnthalpy "
        data_frame = pd.read_sql(sql, db)
        cursor.close()
        db.close()
        return data_frame

    # 방법2 (냉난방 기간)
    # 실측부하를 기반으로 머신러닝을 적용하기 위한 실측예수요부하 테이블 데이터
    # noinspection PyMethodMayBeStatic
    def load_by_real_foretime(self, predictiondate, air_condition):
        season_changes_yn = Common.season_changes(Common.sitecode, predictiondate)
        # print("season_changes_yn:",season_changes_yn)
        week_day, holiday_code = Common.is_weekday(Common.sitecode, predictiondate)

        if season_changes_yn == 'N':
            db = Common.conn()
            cursor = db.cursor()

            # 실측수요부하 테이블에 있는 존에 대해서 부하예측
            sql = " SELECT z.BuildingNo, z.ZoneNo, \
                           w.PREDICTIONDATE AS Date, w.PREDICTIONHOUR AS Hour, \
                           CASE WHEN ISNULL(h.Holiday, 'N') != 'N' \
                                 OR (s.HOLIDAYCODE = 7 AND (DATEPART(weekday, '" + predictiondate + "') = 1 \
                                                        OR DATEPART(weekday, '" + predictiondate + "') = 7)) \
                                 OR (s.HOLIDAYCODE = 1 AND (DATEPART(weekday, '" + predictiondate + "') = 2)) \
                                 OR (s.HOLIDAYCODE = 2 AND (DATEPART(weekday, '" + predictiondate + "') = 3)) \
                                 OR (s.HOLIDAYCODE = 3 AND (DATEPART(weekday, '" + predictiondate + "') = 4)) \
                                 OR (s.HOLIDAYCODE = 4 AND (DATEPART(weekday, '" + predictiondate + "') = 5)) \
                                 OR (s.HOLIDAYCODE = 5 AND (DATEPART(weekday, '" + predictiondate + "') = 6)) \
                                 OR (s.HOLIDAYCODE = 6 AND (DATEPART(weekday, '" + predictiondate + "') = 7)) \
                                 THEN 0 \
                                ELSE 1 END AS WeekHoliday, \
                           CASE WHEN '" + str(air_condition) + "' = '1' THEN \
                                     w.PREDICTIONTEMP - z.ColdSetupTemp \
                                ELSE w.PREDICTIONTEMP - z.HeatingSetupTemp END AS TempDiff, \
                           CASE WHEN z.SOLARRADYN = 0 THEN 0 ELSE w.PREDICTIONSOLARRADQ END AS SOLARRADQ, \
                           CASE WHEN '" + str(air_condition) + "' = '1' THEN \
                                     w.PREDICTIONENTHALPY - z.ColdSetupEnthalpy \
                                ELSE w.PREDICTIONENTHALPY - z.HeatingSetupEnthalpy END AS EnthalpyDiff, \
                           0 AS Load, \
                           eu.PowerUnitRate, \
                           eu.NightPowerUnitRate, \
                           eu.GasUnitRate, \
                           eu.DHUnitRate \
                      FROM T_1HOUR_WEATHER_PREDICT_INFO w \
                           INNER JOIN T_BUILDING_INFO b \
                              ON w.SITECODE = b.SITECODE \
                           INNER JOIN T_ZONE_INFO z \
                              ON w.SiteCode = z.sitecode AND b.BuildingNo = z.buildingno \
                           INNER JOIN T_SITE_INFORMATION s \
                              ON s.SITECODE = w.SITECODE \
                           INNER JOIN T_OPERATING_CONFIG o \
                              ON o.SiteCode = w.SITECODE \
                           LEFT OUTER JOIN T_HOLIDAY h \
                              ON w.SITECODE = h.SiteCode AND h.Holiday = '" + predictiondate + "' \
                           INNER JOIN T_ENERGY_UNIT eu \
                              ON w.SITECODE = eu.SITECODE \
                             AND eu.Month = format(CAST('" + predictiondate + "' AS date), 'MM') \
                           LEFT OUTER JOIN T_REAL_DEMAND_LOAD_INFO r \
                              ON w.SiteCode = r.SiteCode \
                             AND b.BuildingNo = r.BuildingNo \
                             AND w.PREDICTIONDATE = r.RealDate \
                             AND w.PREDICTIONHOUR = r.RealHour \
                             AND r.ZoneNo = z.ZoneNo \
                      WHERE w.SiteCode = '" + Common.sitecode + "' \
                        AND format(CAST(w.PREDICTIONDATE AS date), 'yyyyMMdd') = '" + predictiondate + "' \
                        AND w.PREDICTIONHOUR BETWEEN CASE WHEN '" + str(air_condition) + "' = '1' \
                                                          THEN o.ColdStartHour \
                                                          ELSE o.HeatingStartHour END \
                                              AND CASE WHEN '" + str(air_condition) + "' = '1' THEN o.ColdEndHour \
                                                       ELSE o.HeatingEndHour END \
                    UNION \
                    SELECT r.BuildingNo, r.ZoneNo, r.RealDate AS Date, r.RealHour AS Hour, \
                           r.WeekHoliday AS WeekHoliday, \
                           CASE WHEN '" + str(air_condition) + "' = '1' THEN w.REALTEMP - z.ColdSetupTemp \
                                ELSE w.REALTEMP - z.HeatingSetupTemp END AS TempDiff, \
                           CASE WHEN z.SOLARRADYN = 0 THEN 0 ELSE w.REALSOLARRADQ END AS SOLARRADQ, \
                           CASE WHEN '" + str(air_condition) + "' = '1' THEN w.REALENTHALPY - z.ColdSetupEnthalpy \
                                ELSE w.REALENTHALPY - z.HeatingSetupEnthalpy END AS EnthalpyDiff, \
                           SUM(r.RealDemandLoad) AS Load, \
                           0 AS PowerUnitRate, \
                           0 AS NightPowerUnitRate, \
                           0 AS GasUnitRate, \
                           0 AS DHUnitRate \
                      FROM T_REAL_DEMAND_LOAD_INFO AS r \
                           INNER JOIN T_1HOUR_WEATHER_REAL_INFO w \
                              ON r.SiteCode = w.sitecode AND r.RealDate = w.ANNOUNCEDATE \
                             AND r.RealHour = w.ANNOUNCEHOUR \
                           INNER JOIN T_ZONE_INFO z \
                              ON r.SiteCode = z.sitecode AND r.BuildingNo = z.buildingno \
                             AND r.ZoneNo = z.zoneno \
                           INNER JOIN T_SITE_INFORMATION s \
                              ON r.SiteCode = s.sitecode \
                           INNER JOIN T_OPERATING_CONFIG o \
                              ON r.SiteCode = o.SITECODE \
                     WHERE r.SiteCode = '" + Common.sitecode + "' \
                       AND r.WeekHoliday IN (CASE WHEN '" + str(week_day) + "' = 1 THEN 1 ELSE r.WeekHoliday END) \
                       AND r.RealDate between \
                                 format(CAST(dateadd(year,-1, '" + predictiondate + "' ) AS date), 'yyyy0101') \
                             AND convert(varchar(10),dateadd(d, -1,'" + predictiondate + "'),121) \
                       AND r.RealHOUR BETWEEN CASE WHEN '" + str(air_condition) + "' = '1' THEN o.ColdStartHour \
                                                   ELSE o.HeatingStartHour END \
                                              AND CASE WHEN '" + str(air_condition) + "' = '1' THEN o.ColdEndHour \
                                                       ELSE o.HeatingEndHour END \
                      GROUP BY r.BuildingNo, r.ZoneNo, r.RealDate, r.RealHour, r.WeekHoliday, \
                               w.REALTEMP, z.ColdSetupTemp, z.HeatingSetupTemp, z.SOLARRADYN, w.REALSOLARRADQ, \
                               w.REALENTHALPY, z.ColdSetupEnthalpy, z.HeatingSetupEnthalpy "

            df = pd.read_sql(sql, db)
            cursor.close()
            db.close()
            return df

        if season_changes_yn == 'Y':
            db = Common.conn()
            cursor = db.cursor()

            sql = " SELECT z.BuildingNo, z.ZoneNo, \
                           w.PREDICTIONDATE AS Date, w.PREDICTIONHOUR AS Hour, \
                           CASE WHEN ISNULL(h.Holiday, 'N') != 'N' \
                                 OR (s.HOLIDAYCODE = 7 AND (DATEPART(weekday, '" + predictiondate + "') = 1 \
                                                        OR DATEPART(weekday, '" + predictiondate + "') = 7)) \
                                 OR (s.HOLIDAYCODE = 1 AND (DATEPART(weekday, '" + predictiondate + "') = 2)) \
                                 OR (s.HOLIDAYCODE = 2 AND (DATEPART(weekday, '" + predictiondate + "') = 3)) \
                                 OR (s.HOLIDAYCODE = 3 AND (DATEPART(weekday, '" + predictiondate + "') = 4)) \
                                 OR (s.HOLIDAYCODE = 4 AND (DATEPART(weekday, '" + predictiondate + "') = 5)) \
                                 OR (s.HOLIDAYCODE = 5 AND (DATEPART(weekday, '" + predictiondate + "') = 6)) \
                                 OR (s.HOLIDAYCODE = 6 AND (DATEPART(weekday, '" + predictiondate + "') = 7)) \
                                 THEN 0 \
                                ELSE 1 END AS WeekHoliday, \
                           CASE WHEN '" + str(air_condition) + "' = '1' THEN \
                                     w.PREDICTIONTEMP - z.ColdSetupTemp \
                                ELSE w.PREDICTIONTEMP - z.HeatingSetupTemp END AS TempDiff, \
                           CASE WHEN z.SOLARRADYN = 0 THEN 0 ELSE w.PREDICTIONSOLARRADQ END AS SOLARRADQ, \
                           CASE WHEN '" + str(air_condition) + "' = '1' THEN \
                                     w.PREDICTIONENTHALPY - z.ColdSetupEnthalpy \
                                ELSE w.PREDICTIONENTHALPY - z.HeatingSetupEnthalpy END AS EnthalpyDiff, \
                           0 AS Load, \
                           eu.PowerUnitRate, \
                           eu.NightPowerUnitRate, \
                           eu.GasUnitRate, \
                           eu.DHUnitRate \
                      FROM T_1HOUR_WEATHER_PREDICT_INFO w \
                           INNER JOIN T_BUILDING_INFO b \
                              ON w.SITECODE = b.SITECODE \
                           INNER JOIN T_ZONE_INFO z \
                              ON w.SiteCode = z.sitecode AND b.BuildingNo = z.buildingno \
                           INNER JOIN T_SITE_INFORMATION s \
                              ON s.SITECODE = w.SITECODE \
                           INNER JOIN T_OPERATING_CONFIG o \
                              ON o.SiteCode = w.SITECODE \
                           LEFT OUTER JOIN T_HOLIDAY h \
                              ON w.SITECODE = h.SiteCode AND h.Holiday = '" + predictiondate + "' \
                           INNER JOIN T_ENERGY_UNIT eu \
                              ON w.SITECODE = eu.SITECODE \
                             AND eu.Month = format(CAST('" + predictiondate + "' AS date), 'MM') \
                           LEFT OUTER JOIN T_REAL_DEMAND_LOAD_INFO r \
                              ON w.SiteCode = r.SiteCode \
                             AND b.BuildingNo = r.BuildingNo \
                             AND w.PREDICTIONDATE = r.RealDate \
                             AND w.PREDICTIONHOUR = r.RealHour \
                             AND r.ZoneNo = z.ZoneNo \
                      WHERE w.SiteCode = '" + Common.sitecode + "' \
                        AND format(CAST(w.PREDICTIONDATE AS date), 'yyyyMMdd') = '" + predictiondate + "' \
                        AND w.PREDICTIONHOUR BETWEEN CASE WHEN '" + str(air_condition) + "' = '1' \
                                                          THEN o.ColdStartHour \
                                                          ELSE o.HeatingStartHour END \
                                              AND CASE WHEN '" + str(air_condition) + "' = '1' THEN o.ColdEndHour \
                                                       ELSE o.HeatingEndHour END \
                    UNION \
                    SELECT p.BuildingNo, p.ZoneNo, p.PREDICTIONDATE AS Date, p.PREDICTIONHOUR AS Hour, \
                           p.WeekHoliday AS WeekHoliday, p.PredictionDiffTemp AS TempDiff, \
                           CASE WHEN p.PredictionSolarRadQ = 0 THEN 0 ELSE p.PredictionSolarRadQ END AS SOLARRADQ, \
                           p.PredictionDiffEnthalpy AS EnthalpyDiff, p.PredictionLoad AS Load, \
                           0 AS PowerUnitRate, \
                           0 AS NightPowerUnitRate, \
                           0 AS GasUnitRate, \
                           0 AS DHUnitRate \
                      FROM T_LOAD_PREDICTION_INFO p \
                      LEFT OUTER JOIN T_REAL_DEMAND_LOAD_INFO r \
                        ON p.SiteCode = r.SiteCode \
                       AND p.BuildingNo = r.BuildingNo \
                       AND p.ZoneNo = r.ZoneNo \
                       AND p.PredictionDate = r.RealDate \
                       AND p.WeekHoliday = r.WeekHoliday \
                     INNER JOIN T_SITE_INFORMATION s \
                        ON p.SiteCode = s.sitecode \
                     INNER JOIN T_OPERATING_CONFIG o \
                        ON p.SiteCode = o.SITECODE \
                     WHERE p.SiteCode = '" + Common.sitecode + "' \
                       AND r.RealDate IS NULL \
                       AND p.WeekHoliday IN (CASE WHEN '" + str(week_day) + "' = 1 THEN 1 ELSE p.WeekHoliday END) \
                       AND p.PREDICTIONDATE between \
                             format(CAST(dateadd(year,-1, '" + predictiondate + "') AS date), 'yyyy0101') \
                             AND convert(varchar(10),dateadd(d, -1, '" + predictiondate + "'),121)  \
                       AND p.PREDICTIONDATE between \
                                     format(CAST(dateadd(year,-1, '" + predictiondate + "') AS date), 'yyyy0101') \
                                      AND convert(varchar(10),dateadd(d, 0, '" + predictiondate + "'),121) "
            df = pd.read_sql(sql, db)
            cursor.close()
            db.close()
            return df

    # 방법3 (간절기)
    # 예측부하 테이블의 과거 데이터 기반으로 하여 기상예측 정보를 가지고 예측부하를 구하기 위한 함수(제주도용)
    # 냉난방별로 예측부하 테이블에 있고, 실측수요부하테이블에 없는 날짜
    # noinspection PyMethodMayBeStatic
    def load_by_predict_foretime(self, predictiondate, air_condition):
        db = Common.conn()
        cursor = db.cursor()
        sql = " SELECT z.BuildingNo, z.ZoneNo, \
                       w.PREDICTIONDATE AS Date, w.PREDICTIONHOUR AS Hour, \
                       CASE WHEN ISNULL(h.Holiday, 'N') != 'N' \
                             OR (s.HOLIDAYCODE = 7 AND (DATEPART(weekday, '" + predictiondate + "') = 1 \
                                                    OR DATEPART(weekday, '" + predictiondate + "') = 7)) \
                             OR (s.HOLIDAYCODE = 1 AND (DATEPART(weekday, '" + predictiondate + "') = 2)) \
                             OR (s.HOLIDAYCODE = 2 AND (DATEPART(weekday, '" + predictiondate + "') = 3)) \
                             OR (s.HOLIDAYCODE = 3 AND (DATEPART(weekday, '" + predictiondate + "') = 4)) \
                             OR (s.HOLIDAYCODE = 4 AND (DATEPART(weekday, '" + predictiondate + "') = 5)) \
                             OR (s.HOLIDAYCODE = 5 AND (DATEPART(weekday, '" + predictiondate + "') = 6)) \
                             OR (s.HOLIDAYCODE = 6 AND (DATEPART(weekday, '" + predictiondate + "') = 7)) \
                             THEN 0 \
                            ELSE 1 END AS WeekHoliday, \
                       CASE WHEN '" + str(air_condition) + "' = '1' THEN \
                                 w.PREDICTIONTEMP - z.ColdSetupTemp \
                            ELSE w.PREDICTIONTEMP - z.HeatingSetupTemp END AS TempDiff, \
                       CASE WHEN z.SOLARRADYN = 0 THEN 0 ELSE w.PREDICTIONSOLARRADQ END AS SOLARRADQ, \
                       CASE WHEN '" + str(air_condition) + "' = '1' THEN \
                                 w.PREDICTIONENTHALPY - z.ColdSetupEnthalpy \
                            ELSE w.PREDICTIONENTHALPY - z.HeatingSetupEnthalpy END AS EnthalpyDiff, \
                       0 AS Load, \
                       eu.PowerUnitRate, \
                       eu.NightPowerUnitRate, \
                       eu.GasUnitRate, \
                       eu.DHUnitRate \
                  FROM T_1HOUR_WEATHER_PREDICT_INFO w \
                       LEFT OUTER JOIN T_HOLIDAY h \
                          ON w.SITECODE = h.SiteCode AND h.Holiday = '" + predictiondate + "' \
                       INNER JOIN T_BUILDING_INFO b \
                          ON w.SITECODE = b.SITECODE \
                       INNER JOIN T_ZONE_INFO z \
                          ON w.SiteCode = z.sitecode AND b.BuildingNo = z.buildingno \
                       INNER JOIN T_SITE_INFORMATION s \
                          ON s.SITECODE = w.SITECODE \
                       INNER JOIN T_OPERATING_CONFIG o \
                          ON o.SiteCode = w.SITECODE \
                       INNER JOIN T_LOAD_PREDICTION_INFO p \
                          ON w.SiteCode = p.SiteCode \
                         AND b.BuildingNo = p.BuildingNo \
                         AND z.ZoneNo = p.ZoneNo \
                       INNER JOIN T_ENERGY_UNIT eu \
                          ON w.SITECODE = eu.SITECODE \
                         AND eu.Month = format(CAST('" + predictiondate + "' AS date), 'MM') \
                  WHERE w.SiteCode = '" + Common.sitecode + "' \
                    AND format(CAST(w.PREDICTIONDATE AS date), 'yyyyMMdd') = '" + predictiondate + "' \
                    AND w.PREDICTIONHOUR BETWEEN CASE WHEN '" + str(air_condition) + "' = '1' \
                                                      THEN o.ColdStartHour \
                                                      ELSE o.HeatingStartHour END \
                                          AND CASE WHEN '" + str(air_condition) + "' = '1' THEN o.ColdEndHour \
                                                   ELSE o.HeatingEndHour END \
                 UNION \
                SELECT p.BuildingNo, p.ZoneNo, p.PREDICTIONDATE AS Date, p.PREDICTIONHOUR AS Hour, \
                       p.WeekHoliday as WeekHoliday, p.PredictionDiffTemp AS TempDiff, \
                       CASE WHEN p.PredictionSolarRadQ = 0 THEN 0 ELSE p.PredictionSolarRadQ END AS SOLARRADQ, \
                       p.PredictionDiffEnthalpy AS EnthalpyDiff, p.PredictionLoad AS Load, \
                       0 AS PowerUnitRate, \
                       0 AS NightPowerUnitRate, \
                       0 AS GasUnitRate, \
                       0 AS DHUnitRate \
                  FROM T_LOAD_PREDICTION_INFO p \
                 WHERE p.SiteCode = '" + Common.sitecode + "' \
                   AND isnull(p.ColdHeatingIndication, '0') = '" + str(air_condition) + "' \
                   AND p.PREDICTIONDATE between \
                         format(CAST(dateadd(year,-1, '" + predictiondate + "') AS date), 'yyyy0101') \
                         AND convert(varchar(10),dateadd(d, -1, '" + predictiondate + "'), 121) "
        df = pd.read_sql(sql, db)
        cursor.close()
        db.close()
        return df
    # [청구항1 S41] 끝

    # 실측수요부하 테이블에 데이터가 없을 때 예측부하 테이블에 입력할 데이터를 생성하여 입력하기 위한 함수
    # noinspection PyMethodMayBeStatic
    def insert_loadpredictioninfo(self, df_row, coolheating_indication, dt_hm):
        db = Common.conn()
        cursor = db.cursor()
        sql = " DELETE FROM T_LOAD_PREDICTION_INFO \
                 WHERE SITECODE = '" + Common.sitecode + "' \
                    AND BuildingNo = '" + df_row.BuildingNo + "' \
                    AND ZoneNo = '" + str(df_row.ZoneNo) + "' \
                    AND PREDICTIONDATE = '" + df_row.Date + "' \
                    AND PREDICTIONHOUR = '" + df_row.Hour + "' "
        cursor.execute(sql)
        db.commit()

        sql = "INSERT INTO T_LOAD_PREDICTION_INFO(SITECODE, BUILDINGNO, ZONENO, PREDICTIONDATE, \
                      PREDICTIONHOUR, PREDICTIONGUBUN, WEEKHOLIDAY,PREDICTIONDIFFTEMP, \
                      PREDICTIONDIFFENTHALPY, PREDICTIONSOLARRADQ, PREDICTIONLOAD, POWERUNITRATE, \
                      NIGHTPOWERUNITRATE, GASUNITRATE, DHUNITRATE, COLDHEATINGINDICATION) \
               VALUES(%s, %s, %d, %s, %s, %s, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d) "
        val = (Common.sitecode, df_row.BuildingNo, df_row.ZoneNo, df_row.Date, df_row.Hour, 'N',
               df_row.Week, df_row.TempDiff, df_row.EnthalpyDiff, df_row.SOLARRADQ, df_row.PredictLoad,
               round(df_row.PowerUnitRate*df_row.PredictLoad/860, 2),
               round(df_row.NightPowerUnitRate*df_row.PredictLoad/860, 2),
               round(df_row.GasUnitRate*df_row.PredictLoad*4.1868/1000, 2),
               round(df_row.DHUnitRate*df_row.PredictLoad/1000,2), coolheating_indication)
        # val = (sitecode, df_row.BuildingNo, df_row.ZoneNo, df_row.Date, df_row.Hour, 'N', 1, df_row.TempDiff,
        #        df_row.EnthalpyDiff, df_row.SOLARRADQ, df_row.PredictLoad, df_row.Revision,
        #        df_row.RevisionPredictLoad, 0, 0, ColdHeatingIndication)
        cursor.execute(sql, val)
        db.commit()

        cursor.close()
        db.close()
        return

    # 예측시간이 아닐 경우
    # noinspection PyMethodMayBeStatic
    def insert_non_prediction_range(self, building_no, zone_no, p_date, holiday, s_hour, e_hour, coolheating_indication):
        db = Common.conn()
        cursor = db.cursor()

        for hour in range(s_hour-1):
            if len(str(hour)) == 1:
                p_hour = "0" + str(hour) + "00"
            elif len(str(hour)) == 2:
                p_hour = str(hour) + "00"
            sql = " DELETE FROM T_LOAD_PREDICTION_INFO \
                     WHERE SITECODE = '" + Common.sitecode + "' \
                        AND BuildingNo = '" + building_no + "' \
                        AND ZoneNo = '" + str(zone_no) + "' \
                        AND PREDICTIONDATE = '" + p_date + "' \
                        AND PREDICTIONHOUR = '" + p_hour + "' "
            cursor.execute(sql)
            db.commit()

            sql = "INSERT INTO T_LOAD_PREDICTION_INFO(SITECODE, BUILDINGNO, ZONENO, PREDICTIONDATE, \
                          PREDICTIONHOUR, PREDICTIONGUBUN, WEEKHOLIDAY,PREDICTIONDIFFTEMP, \
                          PREDICTIONDIFFENTHALPY, PREDICTIONSOLARRADQ, PREDICTIONLOAD, POWERUNITRATE, \
                          NIGHTPOWERUNITRATE, GASUNITRATE, DHUNITRATE, COLDHEATINGINDICATION) \
                   VALUES(%s, %s, %d, %s, %s, %s, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d) "
            val = (Common.sitecode, building_no, zone_no, p_date, p_hour, 'N', holiday,
                   0, 0, 0, 0, 0, 0, 0, 0, coolheating_indication)
            cursor.execute(sql, val)
            db.commit()

        for hour in range(e_hour+1, 24):
            if len(str(hour)) == 1:
                p_hour = "0" + str(e_hour) + "00"
            elif len(str(hour)) == 2:
                p_hour = str(hour) + "00"

            sql = " DELETE FROM T_LOAD_PREDICTION_INFO \
                     WHERE SITECODE = '" + Common.sitecode + "' \
                        AND BuildingNo = '" + building_no + "' \
                        AND ZoneNo = '" + str(zone_no) + "' \
                        AND PREDICTIONDATE = '" + p_date + "' \
                        AND PREDICTIONHOUR = '" + p_hour + "' "
            cursor.execute(sql)
            db.commit()

            sql = "INSERT INTO T_LOAD_PREDICTION_INFO(SITECODE, BUILDINGNO, ZONENO, PREDICTIONDATE, \
                          PREDICTIONHOUR, PREDICTIONGUBUN, WEEKHOLIDAY,PREDICTIONDIFFTEMP, \
                          PREDICTIONDIFFENTHALPY, PREDICTIONSOLARRADQ, PREDICTIONLOAD, POWERUNITRATE, \
                          NIGHTPOWERUNITRATE, GASUNITRATE, DHUNITRATE, COLDHEATINGINDICATION) \
                   VALUES(%s, %s, %d, %s, %s, %s, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d) "
            val = (Common.sitecode, building_no, zone_no, p_date, p_hour, 'N', holiday,
                   0, 0, 0, 0, 0, 0, 0, 0, coolheating_indication)
            cursor.execute(sql, val)
            db.commit()

        cursor.close()
        db.close()
        return


    # 보정대상은 방법2로 평일에 부하예측하는 경우이며
    # 방법2로 부하예측하는 시작일을 찾아낸다
    # noinspection PyMethodMayBeStatic
    def revision_load_date(self, prediction_date, air_condition):
        loadcorrectionday, correctionhour = Common.revision_days(self)
        real_load_days = Common.real_load_days(self, str(air_condition), prediction_date, '1')
        # print("평일 부하실측일수:", real_load_days, "운영 지정일수:", loadcorrectionday)
        real_load_date = prediction_date
        if real_load_days == loadcorrectionday:
            # print("[조건2] 부하예측 방법2")
            return prediction_date
        elif real_load_days > loadcorrectionday:
            for i in range(100):
                realload_date = pd.to_datetime(real_load_date)
                realload_date = realload_date - datetime.timedelta(days=1)
                real_load_date = realload_date.strftime("%Y%m%d")
                #print("보정시작일자 : ", real_load_date)
                real_load_days = Common.real_load_days(self, str(air_condition), real_load_date, '1')
                if real_load_days == loadcorrectionday:
                    #print("보정시작일자 : ", real_load_date)
                    return real_load_date
        elif real_load_days < loadcorrectionday:
            # print("[방법2] 보정 대상이 아님")
            """            
            for i in range(loadcorrectionday - real_load_days + 2):
                print("loop : ", i)
                print("대상 날짜 : ", real_load_date)
                realload_date = pd.to_datetime(real_load_date)
                realload_date = realload_date + datetime.timedelta(days=1)
                real_load_date = realload_date.strftime("%Y%m%d")
                real_load_days = Common.real_load_days(self, str(air_condition), real_load_date, '1')
                print("real_load_days : ", real_load_days, "real_load_date : ", real_load_date)
                if real_load_days > loadcorrectionday + 1:
                    return real_load_date
            """
            return prediction_date

    # 최근 일주일 간의 평일의 각 실측수요예측과 부하예측의 합을 구해서 실측수요부하/예측수요부하 하여
    # 보정 계수를 계산
    # noinspection PyMethodMayBeStatic
    def revision_load(self, predictiondate, real_load_date):
        db = Common.conn()
        cursor = db.cursor()
        sql = "SELECT s.BuildingNo, s.ZoneNo, s.RealHour, round(SUM(s.RealDemandLoad),2) \
                      AS RealDemandLoad, round(SUM(s.PredictionLoad),2) AS PredictionLoad, \
                      CASE WHEN SUM(s.PredictionLoad) = 0 THEN 1 \
                           ELSE SUM(s.RealDemandLoad)/SUM(s.PredictionLoad) END AS Revision \
                 FROM ( \
                    SELECT r.BuildingNo, r.ZoneNo, r.RealDate, r.RealHour, r.RealDemandLoad, p.PredictionLoad \
                      FROM \
                          ( SELECT r.BuildingNo, r.ZoneNo, r.RealDate, r.RealHour, r.RealDemandLoad \
                              FROM T_REAL_DEMAND_LOAD_INFO r \
                             WHERE r.SiteCode = '" + Common.sitecode + "' \
                               AND r.RealDemandLoad > 0 \
                               AND r.RealDate in \
                                      (SELECT distinct TOP 7 r.RealDate \
                                          FROM T_REAL_DEMAND_LOAD_INFO r \
                                         WHERE r.SiteCode = '" + Common.sitecode + "' \
                                           AND r.RealDate < '" + predictiondate + "' \
                                           AND r.RealDate >= '" + real_load_date + "' \
                                           AND r.WeekHoliday = 1 \
                                          GROUP BY r.BuildingNo, r.ZoneNo, r.RealDate \
                                          ORDER BY r.RealDate DESC) \
                          ) r \
                         ,(SELECT p.BuildingNo, p.ZoneNo, p.PredictionDate, p.PredictionHour, p.PredictionLoad \
                              FROM T_LOAD_PREDICTION_INFO p \
                             WHERE p.SiteCode = '" + Common.sitecode + "' \
                               AND p.PredictionLoad > 0 \
                               AND p.PredictionDate IN \
                                      ( SELECT distinct TOP 7 p.PredictionDate \
                                          FROM T_LOAD_PREDICTION_INFO p \
                                         WHERE p.SiteCode = '" + Common.sitecode + "' \
                                           AND p.PredictionDate < '" + predictiondate + "' \
                                           AND p.WeekHoliday = 1 \
                                          GROUP BY p.BuildingNo, p.ZoneNo, p.PredictionDate \
                                          ORDER BY p.PredictionDate DESC) \
                              ) p \
                     WHERE r.BuildingNo = p.BuildingNo \
                       AND r.ZoneNo = p.ZoneNo \
                       AND r.RealDate = p.PredictionDate \
                       AND r.RealHour = p.PredictionHour \
                    ) s \
                GROUP BY s.BuildingNo, s.ZoneNo, s.RealHour "
        dataframe_revision = pd.read_sql(sql, db)
        cursor.close()
        db.close()
        return dataframe_revision

        """
        if method_no == 3:
            db = Common.conn()
            cursor = db.cursor()
            sql = "SELECT s.BuildingNo, s.ZoneNo, s.RealHour, round(SUM(s.RealDemandLoad),2) "
            dataframe_revision = pd.read_sql(sql, db)
            cursor.close()
            db.close()
            return dataframe_revision
        """

    # noinspection PyMethodMayBeStatic
    def get_outlier(self, df, column, weight):
        # load에 해당하는 column 데이터만 추출, 1/4 분위와 3/4 분위 지점을 np.percentile로 구함.
        load = df[column]
        quantile_25 = np.percentile(load.values, 25)
        quantile_75 = np.percentile(load.values, 75)
        # IQR을 구하고, IQR에 1.5를 곱하여 최대값과 최소값 지점 구함.
        iqr = quantile_75 - quantile_25
        iqr_weight = iqr * weight
        lowest_val = quantile_25 - iqr_weight
        highest_val = quantile_75 + iqr_weight
        # 최대값 보다 크거나, 최소값 보다 작은 값을 아웃라이어로 설정하고 DataFrame index 반환.
        outlier_index = load[(load < lowest_val) | (load > highest_val)].index
        return outlier_index

    # 환기침기부하 테이블
    # noinspection PyMethodMayBeStatic
    def insert_airvent_load(self, predict_date, coldheat_gubun):
        db = Common.conn()
        cursor = db.cursor()
        sql = "DELETE FROM T_AIRVENT_LOAD \
                WHERE SITECODE = '" + Common.sitecode + "' AND PredictionDate = '" + predict_date + "' "
        cursor.execute(sql)
        db.commit()

        sql = " INSERT INTO T_AIRVENT_LOAD ( \
                    SITECODE, \
                    BuildingNo, \
                    ZoneNo, \
                    PredictionDate, \
                    PredictionHour, \
                    ColdHeatingIndication, \
                    SetupEnthalpy, \
                    PredictionEnthalpy, \
                    PredictionAirVentQty, \
                    PredictionAirInfilQty, \
                    PredictionAirVentLoad, \
                    ChartTimeStamp \
                ) \
                ( \
                 SELECT \
                   A.SITECODE, \
                   A.BuildingNo, \
                   A.ZoneNo, \
                   H.PREDICTIONDATE, \
                   H.PREDICTIONHOUR, \
                   /*--냉난방구분 coldHeat_gubun */ \
                   '" + str(coldheat_gubun) + "' AS ColdHeatingIndication, \
                   /* --설정엔탈피 */\
                   (CASE WHEN '" + str(coldheat_gubun) + "' = 1 THEN Z.ColdSetupEnthalpy \
                         ELSE Z.HeatingSetupEnthalpy END) AS SetupEnthalpy, \
                   /*--예측엔탈피 */\
                   H.PREDICTIONENTHALPY as PredictionEnthalpy, \
                   /*--예측환기량 */\
                   (CASE WHEN '" + str(coldheat_gubun) + "' = 1 THEN A.ColdVentilationQty \
                         ELSE A.HeatingVentilationQty END) AS PredictionAirVentQty, \
                   /*--예측침기량 */\
                   (CASE WHEN '" + str(coldheat_gubun) + "' = 1 THEN A.ColdInfiltrationQty \
                         ELSE A.HeatingInfiltrationQty END) AS PredictionAirInfilQty, \
                   /*--예측환기침기부하 */\
                   /*--동절기면서 AHUMassFlowQty = 0 공조기가 없으면 */ \
                   /*--환기침기예측부하 */\
                   ROUND((CASE WHEN (A.AHUMassFlowQty = 0) THEN \
                            /*--PredictionAirVentQty */ \
                            ((CASE WHEN '" + str(coldheat_gubun) + "' = 1 THEN A.ColdVentilationQty \
                                   ELSE A.HeatingVentilationQty END) \
                            /*--PredictionAirInfilQty */ \
                            + (CASE WHEN '" + str(coldheat_gubun) + "' = 1 THEN A.ColdInfiltrationQty \
                                    ELSE A.HeatingInfiltrationQty END)) \
                            /*--PredictionEnthalpy */ \
                            * (H.PREDICTIONENTHALPY \
                            /*--SetupEnthalpy */ \
                            - (CASE WHEN '" + str(coldheat_gubun) + "' = 1 THEN Z.ColdSetupEnthalpy \
                                   ELSE Z.HeatingSetupEnthalpy END)) \
                     /*--동절기면서 AHUMassFlowQty > 0 --공조기가 있으면 */ \
                     ELSE (A.OutdoorInductionRate * A.AHUMassFlowQty) \
                            /*--PredictionEnthalpy */ \
                            * (H.PREDICTIONENTHALPY \
                            - (CASE WHEN '" + str(coldheat_gubun) + "' = 1 THEN Z.ColdSetupEnthalpy \
                                    ELSE Z.HeatingSetupEnthalpy END)) \
                   END), 4) AS PredictionAirVentLoad, \
                   /*--타임스탬프 */ \
                   SUBSTRING(H.PREDICTIONDATE, 1, 4) + '-' + SUBSTRING(H.PREDICTIONDATE, 5, 2) + '-' + \
                   SUBSTRING(H.PREDICTIONDATE, 7, 2) + ' ' + SUBSTRING(H.PREDICTIONHOUR, 1, 2) + ':' + \
                   SUBSTRING(H.PREDICTIONHOUR, 3, 2) AS ChartTimeStamp \
               FROM T_AIRVENT_INFO A \
                   ,T_ZONE_INFO Z \
                   ,T_OPERATING_CONFIG O \
                   ,T_1HOUR_WEATHER_PREDICT_INFO H \
              WHERE A.SITECODE = '" + Common.sitecode + "' \
                AND A.SITECODE = Z.SITECODE \
                AND A.SITECODE = O.SITECODE \
                AND A.BuildingNo = Z.BuildingNo \
                AND A.ZoneNo = Z.ZoneNo \
                AND A.SITECODE = H.SITECODE \
                AND H.PREDICTIONDATE = '" + predict_date + "' \
            )"
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()
        return


    # 내부발생열부하 테이블
    # noinspection PyMethodMayBeStatic
    def insert_interior_heat_load(self, predict_date, coldheat_gubun):
        db = Common.conn()
        cursor = db.cursor()
        sql = "DELETE FROM T_INTERIOR_HEAT_LOAD \
                WHERE SITECODE = '" + Common.sitecode + "' AND PredictionDate = '" + predict_date + "' "
        cursor.execute(sql)
        db.commit()

        sql = " INSERT INTO T_INTERIOR_HEAT_LOAD ( \
                    SITECODE, \
                    BuildingNo, \
                    ZoneNo, \
                    PredictionDate, \
                    PredictionHour, \
                    PredictionInteriorHeatingLoad, \
                    ChartTimeStamp \
                ) \
                ( SELECT \
                    I.SITECODE, \
                    I.BuildingNo, \
                    I.ZoneNo, \
                    H.PREDICTIONDATE, \
                    H.PREDICTIONHOUR, \
                    ROUND((CASE WHEN (CAST(H.PREDICTIONHOUR AS INT)/100 >= I.WorkStartTime \
                                      AND CAST(H.PREDICTIONHOUR AS INT)/100 <= I.WorkEndTime) THEN \
                                               /*--근무시간 범위 인 경우 */ \
                                               (CASE WHEN (CAST(H.PREDICTIONHOUR AS INT)/100 > I.LunchStartTime \
                                                      AND CAST(H.PREDICTIONHOUR AS INT)/100 <= I.LunchEndTime) THEN \
                                                              /*--점심시간 범위 인 경우 */ \
                                                              (I.InteriorHeatingLoad * I.LunchTimeRate) \
                                                      /*--점심시간 범위가 아닌 경우 */ \
                                                      ELSE (I.InteriorHeatingLoad * I.WorkTimeRate) \
                                               END) \
                                /*--근무시간 범위가 아닌 경우 */ \
                                ELSE (I.InteriorHeatingLoad * 0.0) \
                    END), 4) AS PredictionInteriorHeatingLoad, \
                    /*--타임스탬프 */ \
                    SUBSTRING(H.PREDICTIONDATE, 1, 4) + '-' + SUBSTRING(H.PREDICTIONDATE, 5, 2) + '-' +  \
                    SUBSTRING(H.PREDICTIONDATE, 7, 2) + ' ' + SUBSTRING(H.PREDICTIONHOUR, 1, 2) + ':' +  \
                    SUBSTRING(H.PREDICTIONHOUR, 3, 2) AS ChartTimeStamp \
                    FROM T_INTERIOR_HEAT_INFO I, T_ZONE_INFO Z, T_1HOUR_WEATHER_PREDICT_INFO H \
                   WHERE I.SITECODE = '" + Common.sitecode + "' \
                     AND I.SITECODE = Z.SITECODE \
                     AND I.SITECODE = H.SITECODE \
                     AND I.BuildingNo = Z.BuildingNo \
                     AND I.ZoneNo = Z.ZoneNo \
                     AND H.PREDICTIONDATE = '" + predict_date + "' \
                )"
        # print("T_INTERIOR_HEAT_LOAD sql:\n", sql)
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()
        return

    # 전열부하 테이블
    # noinspection PyMethodMayBeStatic
    def insert_heat_trans_load(self, predict_date, coldheat_gubun):
        db = Common.conn()
        cursor = db.cursor()
        sql = "DELETE FROM T_HEAT_TRANS_LOAD \
                WHERE SITECODE = '" + Common.sitecode + "' AND PredictionDate = '" + predict_date + "' "
        cursor.execute(sql)
        db.commit()

        sql = " INSERT INTO T_HEAT_TRANS_LOAD ( \
                    SITECODE, \
                    BuildingNo, \
                    ZoneNo, \
                    PredictionDate, \
                    PredictionHour, \
                    ColdHeatingIndication, \
                    SetupTemp, \
                    PredictionTemp, \
                    PredictionHeatTransLoad, \
                    ChartTimeStamp \
                ) \
                ( SELECT \
                       AA.SITECODE, \
                       AA.BuildingNo, \
                       AA.ZoneNo, \
                       H.PREDICTIONDATE, \
                       H.PREDICTIONHOUR, \
                       '" + str(coldheat_gubun) + "' AS ColdHeatingIndication, \
                       (CASE WHEN '" + str(coldheat_gubun) + "' = 1 THEN Z.ColdSetupTemp \
                             ELSE Z.HeatingSetupTemp END) AS SetupTemp, \
                       MAX(H.PREDICTIONTEMP) AS PREDICTIONTEMP,  \
                       /*--2017.8.17 수정 */ \
                       /*--내부발생열부하계산 */\
                       ROUND(SUM(sum1) * (MAX(H.PREDICTIONTEMP) - (CASE WHEN '" + str(coldheat_gubun) + "' = 1 \
                                                                            THEN Z.ColdSetupTemp \
                                                                        ELSE Z.HeatingSetupTemp END)\
                            ) * 0.86\
                       ,4) as PredictionHeatTransLoad, \
                       SUBSTRING(H.PREDICTIONDATE, 1, 4) + '-' + SUBSTRING(H.PREDICTIONDATE, 5, 2) + '-' + \
                       SUBSTRING(H.PREDICTIONDATE, 7, 2) + ' ' + SUBSTRING(H.PREDICTIONHOUR, 1, 2) + ':' + \
                       SUBSTRING(H.PREDICTIONHOUR, 3, 2) AS ChartTimeStamp \
                 FROM  ( SELECT SITECODE, BuildingNo, ZoneNo, WallHeatCharacterCoeff as s1, \
                                WallArea as s2, (WallHeatCharacterCoeff * WallArea) as sum1 \
                           FROM T_WALL_INFO \
                          WHERE SITECODE = '" + Common.sitecode + "' \
                          UNION ALL \
                         SELECT SITECODE, BuildingNo, ZoneNo, WindowHeatCharacterCoeff AS s1, \
                                WindowArea AS s2, (WindowHeatCharacterCoeff * WindowArea) AS sum1 \
                           FROM T_WINDOW_INFO \
                          WHERE SITECODE = '" + Common.sitecode + "' \
                       ) AA\
                      ,T_ZONE_INFO Z\
                      ,T_OPERATING_CONFIG O\
                      ,T_1HOUR_WEATHER_PREDICT_INFO H \
                 WHERE AA.SITECODE = H.SITECODE \
                   AND AA.SITECODE = Z.SITECODE \
                   AND AA.SITECODE = O.SITECODE \
                   AND AA.BuildingNo = Z.BuildingNo \
                   AND AA.ZoneNo = Z.ZoneNo \
                 GROUP BY AA.SITECODE, AA.BuildingNo, AA.ZoneNo, H.PREDICTIONDATE, H.PREDICTIONHOUR, \
                          O.ColdStartMonth, O.ColdEndMonth, Z.ColdSetupTemp, Z.HeatingSetupTemp \
                 HAVING H.PREDICTIONDATE = '" + predict_date + "' \
                )"
        # print("sql:\n", sql)
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()
        return


    # 일사부하 테이블
    # noinspection PyMethodMayBeStatic
    def insert_solar_rad_load(self, predict_date, coldheat_gubun):
        db = Common.conn()
        cursor = db.cursor()
        sql = "DELETE FROM T_SOLAR_RAD_LOAD \
                WHERE SITECODE = '" + Common.sitecode + "' AND PredictionDate = '" + predict_date + "' "
        cursor.execute(sql)
        db.commit()

        sql = " INSERT INTO T_SOLAR_RAD_LOAD ( \
                    SITECODE, \
                    BuildingNo, \
                    ZoneNo, \
                    PredictionDate, \
                    PredictionHour, \
                    PredictionClearness, \
                    PredictionAltitude, \
                    PredictionAzimuth, \
                    PredictionSolarRadQ, \
                    PredictionDiffCoeff, \
                    PredictionDirectSolarRadQ, \
                    PredictionDiffSolarRadQ, \
                    PredictionEastSolarRadQ, \
                    PredictionWestSolarRadQ, \
                    PredictionSouthSolarRadQ, \
                    PredictionNorthSolarRadQ, \
                    PredictionSolarRadLoad, \
                    ChartTimeStamp \
                ) \
                ( \
                  SELECT \
                    R.SITECODE, \
                    R.BuildingNo, \
                    R.ZoneNo, \
                    R.PREDICTIONDATE, \
                    R.PREDICTIONHOUR, \
                    R.PREDICTIONCLEARNESS, \
                    R.PREDICTIONALTITUDE, \
                    R.PREDICTIONAZIMUTH, \
                    R.PREDICTIONSOLARRADQ, \
                    R.PredictionDiffCoeff, \
                    R.PredictionDirectSolarRadQ, \
                    R.PredictionDiffSolarRadQ, \
                    R.PredictionEastSolarRadQ, \
                    R.PredictionWestSolarRadQ, \
                    R.PredictionSouthSolarRadQ, \
                    R.PredictionNorthSolarRadQ, \
                    R.PredictionSolarRadLoad, \
                    /*--타임스탬프 */ \
                    SUBSTRING(R.PREDICTIONDATE, 1, 4) + '-' + SUBSTRING(R.PREDICTIONDATE, 5, 2) + '-' + \
                      SUBSTRING(R.PREDICTIONDATE, 7, 2) + ' ' + SUBSTRING(R.PREDICTIONHOUR, 1, 2) + ':' + \
                      SUBSTRING(R.PREDICTIONHOUR, 3, 2) AS ChartTimeStamp \
                    FROM \
                         (   SELECT \
                                    TT.SITECODE, \
                                    TT.BuildingNo, \
                                    TT.ZoneNo, \
                                    TT.PREDICTIONDATE, \
                                    TT.PREDICTIONHOUR, \
                                    TT.PREDICTIONCLEARNESS, \
                                    TT.PREDICTIONALTITUDE, \
                                    TT.PREDICTIONAZIMUTH, \
                                    TT.PREDICTIONSOLARRADQ, \
                                    TT.PredictionDiffCoeff, \
                                    TT.PredictionDirectSolarRadQ, \
                                    TT.PredictionDiffSolarRadQ, \
                                    ROUND(SUM(TT.PredictionEastSolarRadQ), 4) AS PredictionEastSolarRadQ, \
                                    ROUND(SUM(TT.PredictionWestSolarRadQ), 4) AS PredictionWestSolarRadQ, \
                                    ROUND(SUM(TT.PredictionSouthSolarRadQ), 4) AS PredictionSouthSolarRadQ, \
                                    ROUND(SUM(TT.PredictionNorthSolarRadQ), 4) AS PredictionNorthSolarRadQ, \
                                    /*--2017.8.17 수정 - '/ 0.86' -> '* 0.86' */ \
                                    ROUND(SUM(TT.PredictionSolarRadLoad) * 0.86, 4) AS PredictionSolarRadLoad \
                               FROM \
                                 ( SELECT \
                                          BB.SITECODE, \
                                          BB.BuildingNo, \
                                          BB.ZoneNo, \
                                          AA.PREDICTIONDATE, \
                                          AA.PREDICTIONHOUR, \
                                          /*--예측청명도 */ \
                                          AA.PREDICTIONCLEARNESS, \
                                          /*--예측태양고도 */ \
                                          AA.PREDICTIONALTITUDE, \
                                          /*--예측태양방위각 */ \
                                          AA.PREDICTIONAZIMUTH, \
                                          /*--예측수평면일사량 */ \
                                          AA.PREDICTIONSOLARRADQ, \
                                          /*--일사확산계수 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS), 4) AS PredictionDiffCoeff, \
                                          /*--예측직달일사량 */ \
                                          ROUND((1 - (0.384 - 0.416 * PREDICTIONCLEARNESS)) * PREDICTIONSOLARRADQ, 4) \
                                          AS PredictionDirectSolarRadQ, \
                                          /*--예측 확산일사량 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ, 4)  \
                                          AS PredictionDiffSolarRadQ, \
                                          /*--동쪽 일사량 */ \
                                          ROUND((CASE WHEN ( ((COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 90) \
                                                               * PI() / 180.0) / SIN(PREDICTIONALTITUDE) ) \
                                                               * PREDICTIONALTITUDE) < 0)  \
                                                      THEN (0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ \
                                                      ELSE (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 90)  \
                                                            * PI() / 180.0) / SIN(PREDICTIONALTITUDE) ) \
                                                            * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                            * PREDICTIONSOLARRADQ \
                                                            + (0.384 - 0.416 * PREDICTIONCLEARNESS) \
                                                            * PREDICTIONSOLARRADQ END)\
                                               , 4) AS PredictionEastSolarRadQ, \
                                          0 AS PredictionWestSolarRadQ, \
                                          0 AS PredictionSouthSolarRadQ, \
                                          0 AS PredictionNorthSolarRadQ, \
                                          /*--동쪽 일사부하 */ \
                                          ROUND(BB.PredictionEastSolarRadLoad * \
                                            ((CASE WHEN (((COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 90)  \
                                                            * PI() / 180.0) / SIN(PREDICTIONALTITUDE) ) \
                                                            * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                            * PREDICTIONSOLARRADQ) < 0) \
                                                   THEN ((0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ) \
                                              ELSE ( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 90) \
                                                       * PI() / 180.0) / SIN(PREDICTIONALTITUDE) ) \
                                                       * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                       * PREDICTIONSOLARRADQ + (0.384 - 0.416 * PREDICTIONCLEARNESS) \
                                                       * PREDICTIONSOLARRADQ) END)), 4) AS PredictionSolarRadLoad \
                                   FROM (SELECT \
                                                SITECODE, \
                                                PREDICTIONDATE, \
                                                PREDICTIONHOUR, \
                                                PREDICTIONCLEARNESS, \
                                                PREDICTIONALTITUDE, \
                                                PREDICTIONAZIMUTH, \
                                                PREDICTIONSOLARRADQ \
                                                FROM T_1HOUR_WEATHER_PREDICT_INFO \
                                          WHERE SITECODE = '" + Common.sitecode + "' \
                                            AND PREDICTIONDATE =  '" + predict_date + "' \
                                        )AA, \
                                        (SELECT W.SITECODE, W.BuildingNo, W.ZoneNo, \
                                                 ((CASE WHEN (W.WallSolarCharacterCoeff is NULL)  \
                                                        THEN 0 ELSE W.WallSolarCharacterCoeff END)  \
                                                  *(CASE WHEN (W.WallArea is NULL) THEN 0 ELSE W.WallArea END))  \
                                                  +((CASE WHEN (I.WindowSolarCharacterCoeff is NULL) THEN 0 \
                                                          ELSE I.WindowSolarCharacterCoeff END) \
                                                  *(CASE WHEN (I.WindowArea is NULL) THEN 0 \
                                                    ELSE I.WindowArea END)) as PredictionEastSolarRadLoad \
                                            FROM T_WALL_INFO W \
                                                 FULL OUTER JOIN T_WINDOW_INFO I \
                                                 ON W.WallAzimuth = I.WindowAzimuth \
                                             AND W.SITECODE = '" + Common.sitecode + "' \
                                             AND W.SITECODE = I.SITECODE \
                                             AND W.BuildingNo = I.BuildingNo \
                                             AND W.ZoneNo = I.ZoneNo \
                                           WHERE  W.WallAzimuth = 'E' \
                                       ) BB \
                                  WHERE  AA.SITECODE = BB.SITECODE \
                               UNION ALL \
                                /*--서쪽 일사부하 계산 */ \
                                  SELECT \
                                          BB.SITECODE, \
                                          BB.BuildingNo, \
                                          BB.ZoneNo, \
                                          AA.PREDICTIONDATE, \
                                          AA.PREDICTIONHOUR, \
                                          /*--예측청명도 */ \
                                          AA.PREDICTIONCLEARNESS, \
                                          /*--예측태양고도 */ \
                                          AA.PREDICTIONALTITUDE, \
                                          /*--예측태양방위각 */ \
                                          AA.PREDICTIONAZIMUTH, \
                                          /*--예측수평면일사량 */ \
                                          AA.PREDICTIONSOLARRADQ, \
                                          /*--일사확산계수 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS), 4) AS PredictionDiffCoeff, \
                                          /*--예측직달일사량 */ \
                                          ROUND((1 - (0.384 - 0.416 * PREDICTIONCLEARNESS)) * PREDICTIONSOLARRADQ, 4)  \
                                          AS PredictionDirectSolarRadQ, \
                                          /*--예측 확산일사량 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ, 4)  \
                                          AS PredictionDiffSolarRadQ, \
                                          /*--서쪽 일사량 */ \
                                          0 AS PredictionEastSolarRadQ, \
                                          ROUND( (CASE WHEN (((COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 270) \
                                                            * PI() / 180.0) / SIN(PREDICTIONALTITUDE) )  \
                                                            * PREDICTIONALTITUDE) < 0)  \
                                                      THEN (0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ \
                                                  ELSE (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 270)  \
                                                        * PI() / 180.0) / SIN(PREDICTIONALTITUDE) ) \
                                                        * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                        * PREDICTIONSOLARRADQ + (0.384 - 0.416 * PREDICTIONCLEARNESS) \
                                                        * PREDICTIONSOLARRADQ END), 4) AS PredictionWestSolarRadQ, \
                                          0 AS PredictionSouthSolarRadQ, \
                                          0 AS PredictionNorthSolarRadQ, \
                                          /*--서쪽 일사부하 */ \
                                          ROUND(BB.PredictionWestSolarRadLoad * \
                                            ( (CASE WHEN (( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 270)  \
                                                          * PI() / 180.0) / SIN(PREDICTIONALTITUDE) )  \
                                                          * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                          * PREDICTIONSOLARRADQ) < 0) \
                                                    THEN ((0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ) \
                                                   ELSE ( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 270)  \
                                                        * PI() / 180.0) / SIN(PREDICTIONALTITUDE) )  \
                                                        * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                        * PREDICTIONSOLARRADQ + (0.384 - 0.416 * PREDICTIONCLEARNESS)  \
                                                        * PREDICTIONSOLARRADQ) END) ), 4) AS PredictionSolarRadLoad \
                                    FROM ( \
                                            SELECT \
                                                    SITECODE, \
                                                    PREDICTIONDATE, \
                                                    PREDICTIONHOUR, \
                                                    PREDICTIONCLEARNESS, \
                                                    PREDICTIONALTITUDE, \
                                                    PREDICTIONAZIMUTH, \
                                                    PREDICTIONSOLARRADQ \
                                              FROM T_1HOUR_WEATHER_PREDICT_INFO \
                                             WHERE SITECODE = '" + Common.sitecode + "' \
                                               AND PREDICTIONDATE =  '" + predict_date + "' \
                                             ) AA, \
                                          ( SELECT W.SITECODE, W.BuildingNo, W.ZoneNo, \
                                                   ((CASE WHEN (W.WallSolarCharacterCoeff is NULL)  \
                                                          THEN 0 ELSE W.WallSolarCharacterCoeff END) \
                                                   * (CASE WHEN (W.WallArea is NULL) THEN 0 ELSE W.WallArea END)) \
                                                   + ((CASE WHEN (I.WindowSolarCharacterCoeff is NULL)  \
                                                            THEN 0 ELSE I.WindowSolarCharacterCoeff END)  \
                                                   * (CASE WHEN (I.WindowArea is NULL) THEN 0 ELSE I.WindowArea END)) \
                                                      AS PredictionWestSolarRadLoad \
                                              FROM T_WALL_INFO W \
                                                   FULL OUTER JOIN T_WINDOW_INFO I \
                                                  ON W.WallAzimuth = I.WindowAzimuth \
                                               AND W.SITECODE = '" + Common.sitecode + "' \
                                               AND W.SITECODE = I.SITECODE \
                                               AND W.BuildingNo = I.BuildingNo \
                                               AND W.ZoneNo = I.ZoneNo \
                                             WHERE W.WallAzimuth = 'W' \
                                             ) BB \
                                    WHERE AA.SITECODE = BB.SITECODE \
                                  UNION ALL \
                                 /*--남쪽 일사부하 계산 */ \
                                 SELECT \
                                          BB.SITECODE, \
                                          BB.BuildingNo, \
                                          BB.ZoneNo, \
                                          AA.PREDICTIONDATE, \
                                          AA.PREDICTIONHOUR, \
                                          /*--예측청명도 */ \
                                          AA.PREDICTIONCLEARNESS, \
                                          /*--예측태양고도 */ \
                                          AA.PREDICTIONALTITUDE, \
                                          /*--예측태양방위각 */ \
                                          AA.PREDICTIONAZIMUTH, \
                                          /*--예측수평면일사량 */ \
                                          AA.PREDICTIONSOLARRADQ, \
                                          /*--일사확산계수 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS), 4) AS PredictionDiffCoeff, \
                                          /*--예측직달일사량 */ \
                                          ROUND((1 - (0.384 - 0.416 * PREDICTIONCLEARNESS)) * PREDICTIONSOLARRADQ, 4)  \
                                          AS PredictionDirectSolarRadQ, \
                                          /*--예측 확산일사량 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ, 4)  \
                                          AS PredictionDiffSolarRadQ, \
                                          /*--남쪽 일사량 */ \
                                          0 AS PredictionEastSolarRadQ, \
                                          0 AS PredictionWestSolarRadQ, \
                                          ROUND((CASE WHEN (( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 0)  \
                                                            * PI() / 180.0) / SIN(PREDICTIONALTITUDE) ) \
                                                            * PREDICTIONALTITUDE) < 0) \
                                                      THEN (0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ \
                                                 ELSE ( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 0)  \
                                                        * PI() / 180.0) / SIN(PREDICTIONALTITUDE) )  \
                                                        * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                        * PREDICTIONSOLARRADQ + (0.384 - 0.416 * PREDICTIONCLEARNESS)  \
                                                        * PREDICTIONSOLARRADQ) END), 4) as PredictionSouthSolarRadQ, \
                                          /*--남쪽 일사부하 */ \
                                          0 AS PredictionNorthSolarRadQ, \
                                          ROUND(BB.PredictionSouthSolarRadLoad * \
                                            ( (CASE WHEN (( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 0)  \
                                                            * PI() / 180.0) / SIN(PREDICTIONALTITUDE) ) \
                                                            * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                            * PREDICTIONSOLARRADQ) < 0) \
                                                    THEN ((0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ) \
                                               ELSE ( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 0)  \
                                                      * PI() / 180.0) / SIN(PREDICTIONALTITUDE) )  \
                                                      * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                      * PREDICTIONSOLARRADQ + (0.384 - 0.416 * PREDICTIONCLEARNESS)  \
                                                      * PREDICTIONSOLARRADQ) END) ), 4) AS PredictionSolarRadLoad \
                                   FROM( \
                                          SELECT \
                                                SITECODE, \
                                                PREDICTIONDATE, \
                                                PREDICTIONHOUR, \
                                                PREDICTIONCLEARNESS, \
                                                PREDICTIONALTITUDE, \
                                                PREDICTIONAZIMUTH, \
                                                PREDICTIONSOLARRADQ \
                                            FROM T_1HOUR_WEATHER_PREDICT_INFO \
                                           WHERE SITECODE = '" + Common.sitecode + "' \
                                             AND PREDICTIONDATE = '" + predict_date + "' \
                                            ) AA, \
                                         (SELECT W.SITECODE, W.BuildingNo, W.ZoneNo, \
                                                 ((CASE WHEN (W.WallSolarCharacterCoeff is NULL)  \
                                                        THEN 0 ELSE W.WallSolarCharacterCoeff END)  \
                                                   * (CASE WHEN (W.WallArea is NULL) THEN 0 ELSE W.WallArea END)) \
                                                   + ((CASE WHEN (I.WindowSolarCharacterCoeff is NULL) THEN 0  \
                                                            ELSE I.WindowSolarCharacterCoeff END) \
                                                   * (CASE WHEN (I.WindowArea is NULL) THEN 0 ELSE I.WindowArea END))  \
                                                 AS PredictionSouthSolarRadLoad \
                                            FROM T_WALL_INFO W \
                                                 FULL OUTER JOIN T_WINDOW_INFO I \
                                                 ON W.WallAzimuth = I.WindowAzimuth \
                                               AND W.SITECODE = '" + Common.sitecode + "' \
                                              AND W.SITECODE = I.SITECODE \
                                              AND W.BuildingNo = I.BuildingNo \
                                              AND W.ZoneNo = I.ZoneNo \
                                            WHERE W.WallAzimuth = 'S' \
                                            ) BB \
                                  WHERE  AA.SITECODE = BB.SITECODE \
                                 UNION ALL \
                                 /*--북쪽 일사부하 계산 */ \
                                 SELECT \
                                          BB.SITECODE, \
                                          BB.BuildingNo, \
                                          BB.ZoneNo, \
                                          AA.PREDICTIONDATE, \
                                          AA.PREDICTIONHOUR, \
                                          /*--예측청명도 */ \
                                          AA.PREDICTIONCLEARNESS, \
                                          /*--예측태양고도 */ \
                                          AA.PREDICTIONALTITUDE, \
                                          /*--예측태양방위각 */ \
                                          AA.PREDICTIONAZIMUTH, \
                                          /*--예측수평면일사량 */ \
                                          AA.PREDICTIONSOLARRADQ, \
                                          /*--일사확산계수 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS), 4) AS PredictionDiffCoeff, \
                                          /*--예측직달일사량 */ \
                                          ROUND((1 - (0.384 - 0.416 * PREDICTIONCLEARNESS)) * PREDICTIONSOLARRADQ, 4) \
                                          AS PredictionDirectSolarRadQ, \
                                          /*--예측 확산일사량 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ, 4) \
                                          AS PredictionDiffSolarRadQ, \
                                          /*--북쪽 일사량 */ \
                                          0 AS PredictionEastSolarRadQ, \
                                          0 AS PredictionWestSolarRadQ, \
                                          0 AS PredictionSouthSolarRadQ, \
                                          ROUND((CASE WHEN (( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 180) \
                                                            * PI() / 180.0) / SIN(PREDICTIONALTITUDE) )  \
                                                            * PREDICTIONALTITUDE) < 0)  \
                                                      THEN (0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ \
                                                 ELSE ( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 180)  \
                                                        * PI() / 180.0) / SIN(PREDICTIONALTITUDE) ) \
                                                        * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                        * PREDICTIONSOLARRADQ + (0.384 - 0.416 * PREDICTIONCLEARNESS) \
                                                        * PREDICTIONSOLARRADQ) END), 4) AS PredictionNorthSolarRadQ, \
                                          /*--북쪽 일사부하 */ \
                                          ROUND(BB.PredictionNorthSolarRadLoad * \
                                            ( (CASE WHEN (( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 180)  \
                                                            * PI() / 180.0) / SIN(PREDICTIONALTITUDE) )  \
                                                            * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                            * PREDICTIONSOLARRADQ) < 0) \
                                                    THEN ((0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ) \
                                                    ELSE ( (COS(PREDICTIONALTITUDE) * COS((PREDICTIONAZIMUTH - 180)  \
                                                         * PI() / 180.0) / SIN(PREDICTIONALTITUDE) ) \
                                                         * (1 - (0.384 - 0.416 * PREDICTIONCLEARNESS))  \
                                                         * PREDICTIONSOLARRADQ + (0.384 - 0.416 * PREDICTIONCLEARNESS) \
                                                         * PREDICTIONSOLARRADQ) END) ), 4) AS PredictionSolarRadLoad \
                                     FROM ( \
                                            SELECT SITECODE, \
                                                    PREDICTIONDATE, \
                                                    PREDICTIONHOUR, \
                                                    PREDICTIONCLEARNESS, \
                                                    PREDICTIONALTITUDE, \
                                                    PREDICTIONAZIMUTH, \
                                                    PREDICTIONSOLARRADQ \
                                             FROM T_1HOUR_WEATHER_PREDICT_INFO \
                                            WHERE SITECODE = '" + Common.sitecode + "' \
                                              AND PREDICTIONDATE = '" + predict_date + "' \
                                            ) AA, \
                                            ( SELECT W.SITECODE, W.BuildingNo, W.ZoneNo, \
                                                     ((CASE WHEN (W.WallSolarCharacterCoeff is NULL) THEN 0 \
                                                       ELSE W.WallSolarCharacterCoeff END) \
                                                     * (CASE WHEN (W.WallArea is NULL) THEN 0 ELSE W.WallArea END)) \
                                                     + ((CASE WHEN (I.WindowSolarCharacterCoeff is NULL) THEN 0  \
                                                              ELSE I.WindowSolarCharacterCoeff END)  \
                                                     * (CASE WHEN (I.WindowArea is NULL) THEN 0 ELSE I.WindowArea END))\
                                                     AS PredictionNorthSolarRadLoad \
                                                 FROM T_WALL_INFO W \
                                                      FULL OUTER JOIN T_WINDOW_INFO I \
                                                      ON W.WallAzimuth = I.WindowAzimuth \
                                                    AND W.SITECODE = '" + Common.sitecode + "' \
                                                    AND W.SITECODE = I.SITECODE \
                                                    AND W.BuildingNo = I.BuildingNo \
                                                    AND W.ZoneNo = I.ZoneNo \
                                                  WHERE W.WallAzimuth = 'N' \
                                                ) BB \
                                    WHERE AA.SITECODE = BB.SITECODE \
                                 UNION ALL \
                                 /*--지붕 일사부하 계산 */ \
                                 SELECT \
                                          BB.SITECODE, \
                                          BB.BuildingNo, \
                                          BB.ZoneNo, \
                                          AA.PREDICTIONDATE, \
                                          AA.PREDICTIONHOUR, \
                                          /*--예측청명도 */ \
                                          AA.PREDICTIONCLEARNESS, \
                                          /*--예측태양고도 */ \
                                          AA.PREDICTIONALTITUDE, \
                                          /*--예측태양방위각 */ \
                                          AA.PREDICTIONAZIMUTH, \
                                          /*--예측수평면일사량 = 지붕일사량 */ \
                                          AA.PREDICTIONSOLARRADQ, \
                                          /*--일사확산계수 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS), 4) AS PredictionDiffCoeff, \
                                          /*--예측직달일사량 */ \
                                          ROUND((1 - (0.384 - 0.416 * PREDICTIONCLEARNESS)) * PREDICTIONSOLARRADQ, 4)  \
                                          AS PredictionDirectSolarRadQ, \
                                          /*--예측 확산일사량 */ \
                                          ROUND((0.384 - 0.416 * PREDICTIONCLEARNESS) * PREDICTIONSOLARRADQ, 4)  \
                                          AS PredictionDiffSolarRadQ, \
                                          /*--지붕 일사량 */ \
                                          0 AS PredictionEastSolarRadQ, \
                                          0 AS PredictionWestSolarRadQ, \
                                          0 AS PredictionSouthSolarRadQ, \
                                          0 AS PredictionNorthSolarRadQ, \
                                          /*--지붕 일사부하 */ \
                                          ROUND(BB.PredictionRoofSolarRadLoad * AA.PREDICTIONSOLARRADQ, 4)  \
                                          AS PredictionSolarRadLoad \
                                    FROM ( \
                                             SELECT SITECODE, \
                                                    PREDICTIONDATE, \
                                                    PREDICTIONHOUR, \
                                                    PREDICTIONCLEARNESS, \
                                                    PREDICTIONALTITUDE, \
                                                    PREDICTIONAZIMUTH, \
                                                    PREDICTIONSOLARRADQ \
                                               FROM T_1HOUR_WEATHER_PREDICT_INFO \
                                              WHERE SITECODE = '" + Common.sitecode + "' \
                                                AND PREDICTIONDATE = '" + predict_date + "' \
                                           ) AA, \
                                           ( \
                                              SELECT W.SITECODE, W.BuildingNo, W.ZoneNo, \
                                                     ((CASE WHEN (W.WallSolarCharacterCoeff is NULL) THEN 0  \
                                                            ELSE W.WallSolarCharacterCoeff END)  \
                                                     * (CASE WHEN (W.WallArea is NULL) THEN 0 ELSE W.WallArea END))  \
                                                     + ((CASE WHEN (I.WindowSolarCharacterCoeff is NULL)  \
                                                              THEN 0 ELSE I.WindowSolarCharacterCoeff END) \
                                                     * (CASE WHEN (I.WindowArea is NULL) THEN 0  \
                                                             ELSE I.WindowArea END)) as PredictionRoofSolarRadLoad \
                                               FROM T_WALL_INFO W \
                                                    FULL OUTER JOIN T_WINDOW_INFO I \
                                                    ON W.WallAzimuth = I.WindowAzimuth \
                                                AND W.SITECODE = '" + Common.sitecode + "' \
                                                AND W.SITECODE = I.SITECODE \
                                                AND W.BuildingNo = I.BuildingNo \
                                                AND W.ZoneNo = I.ZoneNo \
                                              WHERE W.WallAzimuth = 'R' \
                                           ) BB \
                                   WHERE AA.SITECODE = BB.SITECODE \
                                  ) TT \
                                  GROUP BY TT.SITECODE, \
                                              TT.BuildingNo, \
                                              TT.ZoneNo, \
                                              TT.PREDICTIONDATE, \
                                              TT.PREDICTIONHOUR, \
                                              TT.PREDICTIONCLEARNESS, \
                                              TT.PREDICTIONALTITUDE, \
                                              TT.PREDICTIONAZIMUTH, \
                                              TT.PREDICTIONSOLARRADQ, \
                                              TT.PredictionDiffCoeff, \
                                              TT.PredictionDirectSolarRadQ, \
                                              TT.PredictionDiffSolarRadQ \
                          ) R \
                        )"
        # print("T_SOLAR_RAD_LOAD sql:\n", sql)
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()
        return


    # 일사부하 테이블
    # noinspection PyMethodMayBeStatic
    def insert_loadprediction_info(self, predict_date, weekholiday, air_condition):
        db = Common.conn()
        cursor = db.cursor()
        sql = "DELETE FROM T_LOAD_PREDICTION_INFO \
                WHERE SITECODE = '" + Common.sitecode + "' AND PredictionDate = '" + predict_date + "' "
        cursor.execute(sql)
        db.commit()

        LoadCalc = "((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 ELSE S.PredictionSolarRadLoad END) + \
                       A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad + H.PredictionHeatTransLoad))"

        sql = " INSERT INTO T_LOAD_PREDICTION_INFO ( \
                    SITECODE, \
                    BuildingNo, \
                    ZoneNo, \
                    PredictionDate, \
                    PredictionHour, \
                    PredictionGubun, \
                    WeekHoliday, \
                    PredictionDiffTemp, \
                    PredictionDiffEnthalpy, \
                    PredictionSolarRadQ, \
                    PredictionLoad, \
                    PowerUnitRate, \
                    NightPowerUnitRate, \
                    GasUnitRate, \
                    DHUnitRate, \
                    ColdHeatingIndication, \
                    ChartTimeStamp \
                ) \
                ( \
            SELECT \
                   A.SITECODE, \
                   A.BuildingNo, \
                   A.ZoneNo, \
                   A.PredictionDate, \
                   A.PredictionHour, \
                   'N' AS PredictionGubun, \
                   '" + str(weekholiday) + "' AS WeekHoliday, \
                   ROUND(H.PredictionTemp - H.SetupTemp, 4) AS PredictionDiffTemp, \
                   ROUND(A.PredictionEnthalpy - A.SetupEnthalpy, 4) AS PredictionDiffEnthalpy, \
                   ROUND(ISNULL(S.PredictionSolarRadQ, 0), 4) AS PredictionSolarRadQ, \
                   /*--예측부하 */ \
                   ROUND((CASE WHEN (H.ColdHeatingIndication = 1) THEN \
                         /*--냉방이 + 면 그대로 */ \
                               (CASE WHEN (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                   ELSE S.PredictionSolarRadLoad \
                                              END) \
                                + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                + H.PredictionHeatTransLoad) > 0) THEN \
                                               ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                      ELSE S.PredictionSolarRadLoad END) \
                                               + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                               + H.PredictionHeatTransLoad) \
                                /*-- 냉방이 - 면 0 */ \
                                     ELSE 0 \
                                END) \
                          /*--난방이 + 면 0 */ \
                          ELSE (CASE WHEN (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                  ELSE S.PredictionSolarRadLoad END) \
                                                       + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                       + H.PredictionHeatTransLoad) > 0) THEN 0 \
                                     /*-- 난방이 - 면 + 로 변경 */ \
                                     ELSE ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                 ELSE S.PredictionSolarRadLoad END) \
                                                      + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                      + H.PredictionHeatTransLoad) * -1.0 \
                                END) \
                    END), 4) AS PredictionLoad, \
                   /*-- 요금계산 */ \
                   /*--전력요금 계산 */ \
                   ROUND((CASE WHEN (H.ColdHeatingIndication = 1) THEN \
                   /*--냉방이 + 면 그대로 */ \
                                 (CASE WHEN (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                    ELSE S.PredictionSolarRadLoad END) \
                                                         + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                         + H.PredictionHeatTransLoad) > 0) THEN \
                                                    ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                           ELSE S.PredictionSolarRadLoad END) \
                                                          + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                          + H.PredictionHeatTransLoad) \
                       /*-- 냉방이 - 면 0 */ \
                                       ELSE 0 END) \
                       /*--난방이 + 면 0 */ \
                               ELSE (CASE WHEN \
                                          (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                  ELSE S.PredictionSolarRadLoad END) \
                                                       + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                       + H.PredictionHeatTransLoad) > 0) THEN 0 \
                                          /*-- 난방이 - 면 + 로 변경 */ \
                                          ELSE ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                      ELSE S.PredictionSolarRadLoad END) \
                                                         + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                         + H.PredictionHeatTransLoad) * -1.0 \
                               END ) \
                       END) * (CASE WHEN ((SELECT T.PowerUnitRate FROM T_ENERGY_UNIT T \
                                            WHERE T.SITECODE = A.SITECODE AND 8 = T.Month) IS NULL) THEN 0 \
                                    ELSE (SELECT T.PowerUnitRate FROM T_ENERGY_UNIT T \
                                           WHERE T.SITECODE = A.SITECODE AND 8 = T.Month) / 860.0 \
                               END) \
                     , 0) AS PowerUnitRate, \
                     /*--심야전력요금 */ \
                   ROUND((CASE WHEN (H.ColdHeatingIndication = 1) THEN \
                       /*--냉방이 + 면 그대로 */ \
                                    (CASE WHEN (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                       ELSE S.PredictionSolarRadLoad END) \
                                                         + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                         + H.PredictionHeatTransLoad) > 0) THEN \
                                                ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                       ELSE S.PredictionSolarRadLoad END) \
                                                         + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                         + H.PredictionHeatTransLoad) \
                                          /*-- 냉방이 - 면 0 */ \
                                          ELSE 0 END) \
                       /*--난방이 + 면 0 */ \
                               ELSE (CASE WHEN (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                       ELSE S.PredictionSolarRadLoad END) \
                                                          + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                          + H.PredictionHeatTransLoad) > 0) THEN 0 \
                       /*-- 난방이 - 면 + 로 변경 */ \
                                          ELSE ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                      ELSE S.PredictionSolarRadLoad END) \
                                                          + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                          + H.PredictionHeatTransLoad) * -1.0 \
                                      END) \
                            END) * (CASE WHEN ((SELECT T.NightPowerUnitRate FROM T_ENERGY_UNIT T \
                                                 WHERE T.SITECODE = A.SITECODE AND  8 = T.Month) IS NULL) THEN 0 \
                                         ELSE (SELECT T.NightPowerUnitRate FROM T_ENERGY_UNIT T \
                                                WHERE T.SITECODE = A.SITECODE AND 8 = T.Month) / 860.0 \
                                    END) \
                      , 0) AS NightPowerUnitRate, \
                     /*--도시가스요금 */ \
                   ROUND((CASE WHEN (H.ColdHeatingIndication = 1) THEN \
                       /*--냉방이 + 면 그대로 */ \
                                     (CASE WHEN (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                        ELSE S.PredictionSolarRadLoad END) \
                                                         + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                         + H.PredictionHeatTransLoad) > 0) THEN \
                                                       ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                              ELSE S.PredictionSolarRadLoad END) \
                                                                   + A.PredictionAirVentLoad \
                                                                   + I.PredictionInteriorHeatingLoad \
                                                                   + H.PredictionHeatTransLoad) \
                       /*-- 냉방이 - 면 0 */ \
                                           ELSE 0 END) \
                       /*--난방이 + 면 0 */ \
                               ELSE (CASE WHEN (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                       ELSE S.PredictionSolarRadLoad END) \
                                                            + A.PredictionAirVentLoad \
                                                            + I.PredictionInteriorHeatingLoad \
                                                            + H.PredictionHeatTransLoad) > 0) THEN 0 \
                       /*-- 난방이 - 면 + 로 변경 */ \
                                     ELSE ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                 ELSE S.PredictionSolarRadLoad END) \
                                                      + A.PredictionAirVentLoad + I.PredictionInteriorHeatingLoad \
                                                      + H.PredictionHeatTransLoad) * -1.0 \
                               END) \
                       END) * (CASE WHEN ((SELECT T.GasUnitRate FROM T_ENERGY_UNIT T \
                                            WHERE T.SITECODE = A.SITECODE AND 8 = T.Month) IS NULL) THEN 0 \
                                    ELSE (SELECT T.GasUnitRate FROM T_ENERGY_UNIT T \
                                           WHERE T.SITECODE = A.SITECODE AND 8 = T.Month) * 4.187 / 1000.0 \
                               END) \
                       , 0) AS GasUnitRate, \
                     /*--지역난방요금 */ \
                   ROUND((CASE WHEN (H.ColdHeatingIndication = 1) THEN \
                       /*--냉방이 + 면 그대로 */ \
                                        (CASE WHEN (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                           ELSE S.PredictionSolarRadLoad END) \
                                                                + A.PredictionAirVentLoad \
                                                                + I.PredictionInteriorHeatingLoad \
                                                                + H.PredictionHeatTransLoad) > 0) THEN \
                                                               ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                                      ELSE S.PredictionSolarRadLoad END) \
                                                                           + A.PredictionAirVentLoad \
                                                                           + I.PredictionInteriorHeatingLoad \
                                                                           + H.PredictionHeatTransLoad) \
                       /*-- 냉방이 - 면 0 */ \
                                             ELSE 0 END) \
                       /*--난방이 + 면 0 */ \
                               ELSE (CASE WHEN (((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                       ELSE S.PredictionSolarRadLoad END) \
                                                            + A.PredictionAirVentLoad \
                                                            + I.PredictionInteriorHeatingLoad \
                                                            + H.PredictionHeatTransLoad) > 0) THEN 0 \
                       /*-- 난방이 - 면 + 로 변경 */ \
                                          ELSE ((CASE WHEN (S.PredictionSolarRadLoad is NULL) THEN 0 \
                                                      ELSE S.PredictionSolarRadLoad END) \
                                                           + A.PredictionAirVentLoad \
                                                           + I.PredictionInteriorHeatingLoad \
                                                           + H.PredictionHeatTransLoad) * -1.0 \
                                          END) \
                     END) * (CASE WHEN ((SELECT T.DHUnitRate FROM T_ENERGY_UNIT T \
                                          WHERE T.SITECODE = A.SITECODE AND 8 = T.Month) IS NULL) THEN 0 \
                                  ELSE (SELECT T.DHUnitRate FROM T_ENERGY_UNIT T \
                                         WHERE T.SITECODE = A.SITECODE AND 8 = T.Month) / 1000.0 \
                             END) \
                     , 0) AS DHUnitRate, \
                   '" + str(air_condition) + "' AS ColdHeatingIndication, \
                     /*--타임스탬프 */ \
                   SUBSTRING(A.PREDICTIONDATE, 1, 4) + '-' + SUBSTRING(A.PREDICTIONDATE, 5, 2) + '-' + \
                   SUBSTRING(A.PREDICTIONDATE, 7, 2) + ' ' + SUBSTRING(A.PREDICTIONHOUR, 1, 2) + ':' +  \
                   SUBSTRING(A.PREDICTIONHOUR, 3, 2) AS ChartTimeStamp \
                 FROM T_INTERIOR_HEAT_LOAD I, \
                      T_HEAT_TRANS_LOAD H, \
                      T_SOLAR_RAD_LOAD S \
                      RIGHT OUTER JOIN T_AIRVENT_LOAD A ON A.ZoneNo = S.ZoneNo \
                  AND A.SITECODE = S.SITECODE \
                  AND A.BuildingNo = S.BuildingNo \
                  AND A.PredictionDate = S.PredictionDate \
                  AND A.PredictionHour = S.PredictionHour \
                WHERE A.SITECODE = '" + Common.sitecode + "' \
                  AND A.SITECODE = I.SITECODE \
                  AND A.SITECODE = H.SITECODE \
                  AND A.BuildingNo = I.BuildingNo \
                  AND A.BuildingNo = H.BuildingNo \
                  AND A.ZoneNo = I.ZoneNo \
                  AND A.ZoneNo = H.ZoneNo \
                  AND A.PredictionDate = I.PredictionDate \
                  AND A.PredictionDate = H.PredictionDate \
                  AND A.PredictionHour = I.PredictionHour \
                  AND A.PredictionHour = H.PredictionHour \
                  AND A.PredictionDate = '" + predict_date + "' \
                )"
        # print("T_LOAD_PREDICTION_INFO sql:\n", sql)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return


    # 부하예측 방법1 : 건물 특성 정보를 이용한 부하예측
    # noinspection PyMethodMayBeStatic
    def building_features(self, predictiondate, air_condition):
        db = Common.conn()
        cursor = db.cursor()

        sql = " SELECT  z.BuildingNo, z.ZoneNo, w.PREDICTIONDATE AS Date, w.PREDICTIONHOUR AS Hour, \
                        CASE WHEN ISNULL(h.Holiday, 'N') != 'N' \
                                  OR (s.HOLIDAYCODE = 7 AND \
                              (DATEPART(weekday, '20180728') = 1 OR DATEPART(weekday, '" + predictiondate + "') = 7)) \
                                  OR (s.HOLIDAYCODE = 1 AND (DATEPART(weekday, '" + predictiondate + "') = 2)) \
                                  OR (s.HOLIDAYCODE = 2 AND (DATEPART(weekday, '" + predictiondate + "') = 3)) \
                                  OR (s.HOLIDAYCODE = 3 AND (DATEPART(weekday, '" + predictiondate + "') = 4)) \
                                  OR (s.HOLIDAYCODE = 4 AND (DATEPART(weekday, '" + predictiondate + "') = 5)) \
                                  OR (s.HOLIDAYCODE = 5 AND (DATEPART(weekday, '" + predictiondate + "') = 6)) \
                                  OR (s.HOLIDAYCODE = 6 AND (DATEPART(weekday, '" + predictiondate + "') = 7)) \
                                  THEN 0 \
                             ELSE 1 END AS Week, \
                        CASE WHEN '" + str(air_condition) + "' = '1' THEN w.PREDICTIONTEMP - z.ColdSetupTemp \
                             ELSE w.PREDICTIONTEMP - z.HeatingSetupTemp END AS TempDiff, \
                        CASE WHEN z.SOLARRADYN = 0 THEN 0 ELSE w.PREDICTIONSOLARRADQ END AS SOLARRADQ, \
                        CASE WHEN '" + str(air_condition) + "' = '1' THEN w.PREDICTIONENTHALPY - z.ColdSetupEnthalpy \
                             ELSE w.PREDICTIONENTHALPY - z.HeatingSetupEnthalpy END AS EnthalpyDiff, \
                        CASE WHEN '" + str(air_condition) + "' = '1' THEN \
                                                 round(ht.PredictionHeatTransLoad + sr.PredictionSolarRadLoad + \
                                                  al.PredictionAirVentLoad + ih.PredictionInteriorHeatingLoad, 2) \
                             ELSE round(ht.PredictionHeatTransLoad + sr.PredictionSolarRadLoad + \
                             al.PredictionAirVentLoad + ih.PredictionInteriorHeatingLoad, 2)*(-1) END AS PredictLoad, \
                        eu.PowerUnitRate, \
                        eu.NightPowerUnitRate, \
                        eu.GasUnitRate, \
                        eu.DHUnitRate \
                  FROM T_1HOUR_WEATHER_PREDICT_INFO w \
                       LEFT OUTER JOIN T_HOLIDAY h \
                         ON w.SITECODE = h.SiteCode AND h.Holiday = '" + predictiondate + "' \
                       INNER JOIN T_BUILDING_INFO b \
                          ON w.SITECODE = b.SITECODE \
                       INNER JOIN T_ZONE_INFO z \
                          ON w.SiteCode = z.sitecode AND b.BuildingNo = z.buildingno \
                       INNER JOIN T_SITE_INFORMATION s \
                          ON s.SITECODE = w.SITECODE \
                       INNER JOIN T_OPERATING_CONFIG o \
                          ON o.SiteCode = w.SITECODE \
                       INNER JOIN T_HEAT_TRANS_LOAD ht \
                          ON w.SITECODE = ht.SITECODE AND b.BuildingNo = ht.BuildingNo \
                         AND z.ZoneNo = ht.ZoneNo AND w.PREDICTIONDATE = ht.PredictionDate \
                         AND w.PREDICTIONHOUR = ht.PredictionHour \
                       INNER JOIN T_SOLAR_RAD_LOAD sr \
                          ON w.SITECODE = sr.SITECODE AND b.BuildingNo = sr.BuildingNo \
                         AND z.ZoneNo = sr.ZoneNo AND w.PREDICTIONDATE = sr.PredictionDate \
                         AND w.PREDICTIONHOUR = sr.PredictionHour \
                       INNER JOIN T_AIRVENT_LOAD al \
                          ON w.SITECODE = al.SITECODE AND b.BuildingNo = al.BuildingNo \
                         AND z.ZoneNo = al.ZoneNo AND w.PREDICTIONDATE = al.PredictionDate \
                         AND w.PREDICTIONHOUR = al.PredictionHour \
                       INNER JOIN T_INTERIOR_HEAT_LOAD ih \
                          ON w.SITECODE = ih.SITECODE AND b.BuildingNo = ih.BuildingNo \
                         AND z.ZoneNo = ih.ZoneNo AND w.PREDICTIONDATE = ih.PredictionDate \
                         AND w.PREDICTIONHOUR = ih.PredictionHour \
                       INNER JOIN T_ENERGY_UNIT eu \
                          ON w.SITECODE = eu.SITECODE \
                         AND eu.Month = format(CAST('" + predictiondate + "' AS date), 'MM') \
                 WHERE w.SiteCode = '" + Common.sitecode + "' \
                   AND w.PREDICTIONDATE = '" + predictiondate + "' \
                   AND w.PREDICTIONHOUR BETWEEN CASE WHEN '" + str(air_condition) + "' = '1' THEN o.ColdStartHour \
                                                     ELSE o.HeatingStartHour END \
                   AND CASE WHEN '" + str(air_condition) + "' = '1' THEN o.ColdEndHour ELSE o.HeatingEndHour END "

        df_method1 = pd.read_sql(sql, db)
        cursor.close()
        db.close()
        return df_method1

    # 부하예측 시간 정보 가져오기
    # noinspection PyMethodMayBeStatic
    def prediction_hour(self, buildingno, zoneno, air_condition):
        db = Common.conn()
        cursor = db.cursor()
        sql = " SELECT CASE WHEN '" + str(air_condition) + "' = '1' THEN ColdStartHour \
                            ELSE HeatingStartHour \
                       END \
                  FROM T_ZONE_INFO \
                 WHERE SiteCode = '" + Common.sitecode + "' \
                   AND BuildingNo = '" + buildingno + "' \
                   AND zoneno = '" + str(zoneno) + "' \
                UNION \
                SELECT CASE WHEN '" + str(air_condition) + "' = '1' THEN ColdEndHour \
                            ELSE HeatingEndHour \
                       END \
                  FROM T_ZONE_INFO \
                 WHERE SiteCode = '" + Common.sitecode + "' \
                   AND BuildingNo = '" + buildingno + "' \
                   AND zoneno = '" + str(zoneno) + "' "

        cursor.execute(sql)

        # 실행문 조회
        all_rows = cursor.fetchall()
        s_hour = all_rows[0]
        e_hour = all_rows[1]
        start_hour = ''.join(s_hour)
        end_hour = ''.join(e_hour)

        cursor.close()
        db.close()
        return start_hour, end_hour

    """
    # 테스트시 실행 날짜 체크
    # noinspection PyMethodMayBeStatic
    def delete_out_of_prediction_range(self, BuildingNo, ZoneNo, prediction_date, air_condition):
        db = Common.conn()
        cursor = db.cursor()
        s_hour, e_hour = Common.prediction_hour(Common.sitecode, BuildingNo, ZoneNo, str(air_condition))
        sql = " DELETE FROM T_LOAD_PREDICTION_INFO \
                 WHERE SiteCode = '" + Common.sitecode + "' \
                   AND BuildingNo = '" + BuildingNo + "' \
                   AND ZoneNo = '" + ZoneNo + "' \
                   AND PredictionDate = '" + prediction_date + "' \
                   AND PredictionHour NOT BETWEEN '" + s_hour + "' AND '" + e_hour + "' "
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return
    """

    # 테스트시 실행 날짜 체크
    # noinspection PyMethodMayBeStatic
    def op_days(self, startday, endday):
        db = Common.conn()
        cursor = db.cursor()
        """
        sql = " SELECT DISTINCT(RealDate) \
                  FROM T_REAL_DEMAND_LOAD_INFO \
                 WHERE SiteCode = 'KBHMU042' \
                   AND RealDate >= '" + startday + "' \
                   AND RealDate <= '" + endday + "' \
                 ORDER BY RealDate "
        """
        sql = " SELECT CONVERT(VARCHAR(10), DATEADD(D, NUMBER, '" + startday + "'), 112) AS [DATE] \
                  FROM MASTER..SPT_VALUES \
                 WHERE TYPE = 'P' \
                   AND number <= DATEDIFF(D, '" + startday + "', '" + endday + "') "
        op_days = pd.read_sql(sql, db)
        cursor.close()
        db.close()
        return op_days


