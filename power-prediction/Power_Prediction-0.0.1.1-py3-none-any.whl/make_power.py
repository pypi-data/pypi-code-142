# 15분 전력량 데이터 생성

import datetime
import numpy as np
from common_function import Common


def make_power_15m(real_datetime):

    accumulate_power = 0
    real_power = 0

    # 예측 일시
    real_date = real_datetime.date()
    real_hour = real_datetime.hour
    real_min = real_datetime.minute

    # 예측 일시 전후 시간
    beforedate_time = real_datetime - datetime.timedelta(minutes=15)     # 15분 전 일시
    real_before10_time = real_datetime - datetime.timedelta(minutes=10)  # 10분 전 일시
    real_before5_time = real_datetime - datetime.timedelta(minutes=5)    # 5분 전 일시
    real_next5_time = real_datetime + datetime.timedelta(minutes=5)      # 5분 후 일시

    current_time = real_datetime.strftime("%Y-%m-%d %H:%M:%S")
    before_datetime = beforedate_time.strftime("%Y-%m-%d %H:%M:%S")
    real_before10time = real_before10_time.strftime("%Y-%m-%d %H:%M:%S")
    real_before5time = real_before5_time.strftime("%Y-%m-%d %H:%M:%S")
    real_next5time = real_next5_time.strftime("%Y-%m-%d %H:%M:%S")

    # current_date = real_datetime.strftime("%Y%m%d")
    real_hour_min = real_datetime.strftime("%H:%M:%S")
    RealDate = real_datetime.strftime("%Y%m%d")
    RealHour = real_datetime.strftime("%H00")
    RealMin = real_datetime.strftime("%M")

    # 평일 (월:1 ~ 금:5) : 1       주말 (토:6, 일:7) : 0
    weekholiday = real_datetime.weekday() + 1
    if weekholiday < 6:
        WeekHoliday = 1
    else:
        WeekHoliday = 0

    weekholiday = c.is_holiday(RealDate)

    if weekholiday == '0':
        WeekHoliday = 0

    # print("WeekHoliday:", WeekHoliday)

    # 데이터 가져오기
    # 건물번호 추출하기 삭제 : 건물번호는 하나
    # buildingno_list = c.select_building_no()

    #for buildingno in buildingno_list:
    df_mmiid_esrc = c.select_mmiid_esrc()

    # for bno in buildingno: print("bno:", bno)
    for mmi_id, e_src in df_mmiid_esrc:
        # print("mmi_id:", mmi_id, "e_src:", e_src)

        # 15분 전력량 마지막 데이터의 실측 시간
        last_date = c.select_last_real_power(str(e_src))
        # print("last_date", last_date)
        #if last_date_cnt > 0:
        year = int(last_date[0][0:4])
        month = int(last_date[0][4:6])
        day = int(last_date[0][6:8])
        hour = int(last_date[0][8:10])
        min = int(last_date[0][12:14])
        lastdate_time = datetime.datetime(year, month, day, hour, min)
        # DB에서 처리:   lastdate_time = datetime.datetime(1900, 1, 1, 0, 0)
        last_datetime = lastdate_time.strftime("%Y-%m-%d %H:%M:%S")

        # 15분 전력량과 누적전력 산출
        if (lastdate_time == beforedate_time):  # 15분 전력량 데이터에서 15분 전의 데이터가 있는지 체크
            # 15분 전의 누적전력(누적0)과 전력량(전력량0) 가져오기
            b_real_CurrentPowerKwh, b_RealPower15M, b_RealPeakPower15M = c.select_real_power(str(e_src), last_datetime)

            # 5분전력 센싱데이터에서 0분 ~ 5분 후 누적전력 가져오기
            savetime, n5_CurrentPowerKwh, b_peak_PowerKwInc = c.select_peak_power(mmi_id, current_time, real_next5time)

            # 5분 전력 센싱 데이터에서 15분 ~ 20분 후 누적전력(누적1)이 있는 경우
            if n5_CurrentPowerKwh != 0:
                net_power, power_diff = c.net_power_calculation(b_real_CurrentPowerKwh, n5_CurrentPowerKwh)
                real_power = round(net_power, 3)  # 전력량 = 순전력량
                accumulate_power = round(n5_CurrentPowerKwh, 3)  # 누적전력 = 누적1
                # print("line:", 93)
            else:
                # (5분전력 센싱데이터) 5분 ~ 0분 전 누적전력 가져오기
                savetime, b5_CurrentPowerKwh, b_peak_PowerKwInc = c.select_peak_power(mmi_id, real_before5time, current_time)

                # 5분 전력 센싱 데이터에서 10분 ~ 15분 후 누적전력(누적2)이 있는 경우
                if b5_CurrentPowerKwh != 0:
                    net_power, power_diff = c.net_power_calculation(b_real_CurrentPowerKwh, b5_CurrentPowerKwh)
                    real_power = round(net_power / 2 * 3, 3)  # 전력량 = 순전력량 / 2 * 3
                    accumulate_power = round(power_diff + real_power, 3)  # 누적전력 = 누적차이 + 전력량
                    # print("line:", 103)
                else:
                    # 5분 전력 센싱 데이터에서 10분 ~ 5분 전 누적전력 가져오기
                    savetime, b10_CurrentPowerKwh, b_peak_PowerKwInc = c.select_peak_power(mmi_id, real_before10time, real_before5time)

                    if b10_CurrentPowerKwh != 0:
                        net_power, power_diff = c.net_power_calculation(b_real_CurrentPowerKwh, b10_CurrentPowerKwh)
                        real_power = round(net_power * 3, 3)  # 전력량 = 순전력량 * 3
                        accumulate_power = round(power_diff + real_power, 3)  # 누적전력 = 누적차이 + 전력량
                        # print("line:", 112)
                    else:
                        # 5분 전력 센싱 데이터에서 15분간 센싱 데이터가 없는 경우
                        if WeekHoliday == 1:  # 평일인 경우
                            real_power = round(b_RealPower15M, 3)  # 전력량 = 전력량0
                            accumulate_power = round(b_real_CurrentPowerKwh + real_power, 3)  # 누적전력 = 누적0 + 전력량
                            # print("line:", 118)
                        else:
                            # b_holiday_RealPower15M = 0
                            # 15분 전력량 데이터에서 시각과 분이 같은 휴일 데이터 가져오기
                            b_holiday_RealPower15M = c.holiday_real_power(RealDate, real_hour_min)

                            # 15분 전력량 데이터에서 과거 날짜 중 같은 시간의 휴일 데이터가 있는 경우
                            if b_holiday_RealPower15M > 0:
                                real_power = round(b_holiday_RealPower15M, 3)
                                accumulate_power = round(b_real_CurrentPowerKwh + real_power, 3)
                                # print("line:", 128)
                            # 15분 전력량 데이터에서 휴일 데이터가 없는 경우
                            else:
                                real_power = round(b_RealPower15M, 3)
                                accumulate_power = round(b_real_CurrentPowerKwh + real_power, 3)
                                # print("line:", 133)
        else:
            # 15분 전력량 데이터에서 15분 전의 데이터가 없는 경우(최초)
            # 5분 전력 센싱 데이터에서 0분 ~ 5분 후 누적전력(누적1) 가져오기
            # print("mmi_id:", mmi_id, "current_time:", current_time, "real_next5time:", real_next5time)
            savetime, b_peak15_CurrentPowerKwh, b_peak_PowerKwInc = c.select_peak_power(mmi_id, current_time, real_next5time)
            # print("savetime:", savetime, "b_peak15_CurrentPowerKwh:", b_peak15_CurrentPowerKwh, "b_peak_PowerKwInc:", b_peak_PowerKwInc)

            # 5분 전력 센싱 데이터에서 10분 ~ 15분 후 누적전력(누적4) 가져오기
            # print("mmi_id:", mmi_id, "before_datetime:", before_datetime, "real_before10time:", real_before10time)
            savetime, b_peak5_CurrentPowerKwh, b_peak_PowerKwInc = c.select_peak_power(mmi_id, before_datetime, real_before10time)
            # print("savetime:", savetime, "b_peak5_CurrentPowerKwh:", b_peak5_CurrentPowerKwh, "b_peak_PowerKwInc:", b_peak_PowerKwInc)

            # print("b_peak5_CurrentPowerKwh:", b_peak5_CurrentPowerKwh, "b_peak15_CurrentPowerKwh:", b_peak15_CurrentPowerKwh)
            if b_peak15_CurrentPowerKwh == 0 and b_peak5_CurrentPowerKwh == 0:
                before_15datetime = beforedate_time.strftime("%Y%m%d%H00%M")
                # print("before_15datetime:", before_15datetime)
                current_power_kwh = c.select_CurrentPowerKwh_power(str(e_src), before_15datetime)
                net_power = 0
                accumulate_power = current_power_kwh
            elif b_peak15_CurrentPowerKwh == 0:
                net_power = 0
                accumulate_power = b_peak5_CurrentPowerKwh
            else:
                net_power, power_diff = c.net_power_calculation(b_peak5_CurrentPowerKwh, b_peak15_CurrentPowerKwh)
                real_power = net_power  # 전력량 = 순전력량
                accumulate_power = b_peak15_CurrentPowerKwh  # 누적전력 = 누적1
            # print("line:", 146)

        # 5분 전력 센싱 데이터에서 15분간 최대 순시전력 가져오기
        peak_power = c.select_peakpower(mmi_id, real_before10_time, real_next5time)

        if peak_power == 0:
            peak_power = b_RealPeakPower15M
        print("peak_power:", peak_power)

        c.insert_power_real_15m(str(e_src), RealDate, RealHour, RealMin, peak_power, accumulate_power, real_power, WeekHoliday)
        print("시간:", current_time, "energy_source:", e_src, "휴일여부:", WeekHoliday, ":", "피크전력:", peak_power,
              "누적전력량:", accumulate_power, "전력량:", real_power)

sitecode = ''
c = Common(sitecode)
sitecode = c.site_code()

"""
currenttime = datetime.datetime(2022, 1, 2, 13, 15)  # + datetime.timedelta(minutes=15*n)
print("currenttime:", currenttime)
make_power_15m(currenttime)
"""
