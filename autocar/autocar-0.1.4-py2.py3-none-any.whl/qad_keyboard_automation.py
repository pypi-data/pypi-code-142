import xlwings as xw
import pyautogui as gui
import pandas as pd
from time import sleep
import keyboard
import ctypes

# pyautogui variable
gui.FAILSAFE = True

# Set workbook variables
xl_app = xw.apps.active
wb: xw.Book = xw.Book.caller()
ws_check_cancel: xw.Sheet = wb.sheets['Check Cancellation Maintenance']
ws_settings: xw.Sheet = wb.sheets['Settings']
ws_pmnt_man_checks: xw.Sheet = wb.sheets['Payment Manual Checks']
ws_un_pmnt_sel_man: xw.Sheet = wb.sheets['UN Payment Selection Manual']
ws_pmnt_maint: xw.Sheet = wb.sheets['Payment Maintenance']

sleep_time = ws_settings['c_sleep_time'].value


def _countdown(ws: xw.Sheet, cell1: str, cell2: str, cell3: str, cell4: str, cell5: str):
    ws[cell1 + ':' + cell5].color = None
    print('__Starting In__')
    sleep(1)
    ws[cell1].color = '#FFFF00'
    print('5')
    sleep(1)
    ws[cell2].color = '#FFFF00'
    print('4')
    sleep(1)
    ws[cell3].color = '#FFCC00'
    print('3')
    sleep(1)
    ws[cell4].color = '#FFCC00'
    print('2')
    sleep(1)
    ws[cell5].color = '#00B050'
    print('1')
    sleep(1)
    ws[cell1 + ':' + cell5].color = None
    print('__Begin__\n')


def _get_capslock_state():
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


def button_check_cancellation_maintenance():
    if _get_capslock_state() == 1:
        xl_app.alert('Please turn off CAPSLOCK', title='Turn Off CAPSLOCK', mode='info')
    else:
        # Update sheet and table below:
        df: pd.DataFrame = ws_check_cancel['t_check_cancel[[#All]]'].options(pd.DataFrame, index=False).value
        print(df, '\n')

        msgbox_return = xl_app.alert('Are you ready to continue?', title='Ready', mode='info', buttons='yes_no')
        if msgbox_return == 'yes':
            _countdown(ws_check_cancel, 'B4', 'C4', 'D4', 'E4', 'F4')

            table_row = 7
            ws_check_cancel['B' + str(table_row) + ':B' + str(table_row + len(df.index) - 1)].color = None

            i = 1
            for _, row in df.iterrows():
                col_val0 = row[df.columns[0]]
                col_val1 = row[df.columns[1]]

                if isinstance(col_val0, float):
                    col_val0 = int(col_val0)

                print(str(i) + ' of ' + str(len(df.index)) + ' ' + df.columns[0] + ': ' + str(col_val0))

                # Keyboard Entry -----------------------------------------------------------
                gui.typewrite(str(col_val0))
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                gui.typewrite(str(col_val1))
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                # Keyboard Entry -----------------------------------------------------------
                ws_check_cancel['B' + str(table_row)].color = '#92D050'

                i += 1
                table_row += 1
            xl_app.alert('Complete', title='Complete', mode='info')


def button_payment_manual_checks():
    if _get_capslock_state() == 1:
        xl_app.alert('Please turn off CAPSLOCK', title='Turn Off CAPSLOCK', mode='info')
    else:
        # Update sheet and table below
        df: pd.DataFrame = ws_pmnt_man_checks['t_pmnt_man_checks[[#All]]'].options(pd.DataFrame, index=False).value
        print(df, '\n')

        msgbox_return = xl_app.alert('Are you ready to continue?', title='Ready', mode='info', buttons='yes_no')
        if msgbox_return == 'yes':
            # Update sheet below
            _countdown(ws_pmnt_man_checks, 'B4', 'C4', 'D4', 'E4', 'F4')

            table_row = 7
            # Update sheet below
            ws_pmnt_man_checks['B' + str(table_row) + ':B' + str(table_row + len(df.index) - 1)].color = None

            i = 1
            for _, row in df.iterrows():
                col_val0 = row[df.columns[0]]

                if isinstance(col_val0, float):
                    col_val0 = int(col_val0)

                print(str(i) + ' of ' + str(len(df.index)) + ' ' + df.columns[0] + ': ' + str(col_val0))

                # Keyboard Entry -----------------------------------------------------------
                gui.typewrite(str(col_val0))
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                # Keyboard Entry -----------------------------------------------------------

                # Update sheet below
                ws_pmnt_man_checks['B' + str(table_row)].color = '#92D050'

                i += 1
                table_row += 1
            xl_app.alert('Complete', title='Complete', mode='info')


def button_un_payment_selection_manual():
    if _get_capslock_state() == 1:
        xl_app.alert('Please turn off CAPSLOCK', title='Turn Off CAPSLOCK', mode='info')
    else:
        # Update sheet and table below
        df: pd.DataFrame = ws_un_pmnt_sel_man['t_un_pmnt_sel_man[[#All]]'].options(pd.DataFrame, index=False).value
        print(df, '\n')

        msgbox_return = xl_app.alert('Are you ready to continue?', title='Ready', mode='info', buttons='yes_no')
        if msgbox_return == 'yes':
            # Update sheet below
            _countdown(ws_un_pmnt_sel_man, 'B4', 'C4', 'D4', 'E4', 'F4')

            table_row = 7
            # Update sheet below
            ws_un_pmnt_sel_man['B' + str(table_row) + ':B' + str(table_row + len(df.index) - 1)].color = None

            i = 1
            for _, row in df.iterrows():
                col_val0 = row[df.columns[0]]

                if isinstance(col_val0, float):
                    col_val0 = int(col_val0)

                print(str(i) + ' of ' + str(len(df.index)) + ' ' + df.columns[0] + ': ' + str(col_val0))

                # Keyboard Entry -----------------------------------------------------------
                gui.typewrite(str(col_val0))
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                gui.typewrite('0')
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                # Keyboard Entry -----------------------------------------------------------

                # Update sheet below
                ws_un_pmnt_sel_man['B' + str(table_row)].color = '#92D050'

                i += 1
                table_row += 1
            xl_app.alert('Complete', title='Complete', mode='info')


def button_pmnt_maint():
    if _get_capslock_state() == 1:
        xl_app.alert('Please turn off CAPSLOCK', title='Turn Off CAPSLOCK', mode='info')
    else:
        # Update sheet and table below
        df: pd.DataFrame = ws_pmnt_maint['t_pmnt_maint[[#All]]'].options(pd.DataFrame, index=False).value
        print(df, '\n')

        msgbox_return = xl_app.alert('Are you ready to continue?', title='Ready', mode='info', buttons='yes_no')
        if msgbox_return == 'yes':
            # Update sheet below
            _countdown(ws_pmnt_maint, 'B4', 'C4', 'D4', 'E4', 'F4')

            table_row = 7
            # Update sheet below
            ws_pmnt_maint['B' + str(table_row) + ':B' + str(table_row + len(df.index) - 1)].color = None

            i = 1
            for _, row in df.iterrows():
                col_val0 = row[df.columns[0]]

                if isinstance(col_val0, float):
                    col_val0 = int(col_val0)

                print(str(i) + ' of ' + str(len(df.index)) + ' ' + df.columns[0] + ': ' + str(col_val0))

                # Keyboard Entry -----------------------------------------------------------
                gui.typewrite(str(col_val0))
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                keyboard.press_and_release('enter')
                sleep(sleep_time)
                # Keyboard Entry -----------------------------------------------------------

                # Update sheet below
                ws_pmnt_maint['B' + str(table_row)].color = '#92D050'

                i += 1
                table_row += 1
            xl_app.alert('Complete', title='Complete', mode='info')


if __name__ == "__main__":
    xw.Book("QAD_Keyboard_Automation.xlsb").set_mock_caller()
    # Only used to debug - Set workbook variables
    # ---------
    # wb = xw.Book.caller()
    # ws_check_cancel: xw.Range = wb.sheets['Check Cancellation Maintenance']
    # ---------
