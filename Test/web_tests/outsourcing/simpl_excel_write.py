import time
from random import random
import datetime
import pandas as pd
import openpyxl
import allure
import pytest
from pandas import ExcelWriter

import FW.WEB.outsourcing.url_test
from Test.web_tests.WebBase import WebBase
from selenium.webdriver.common.keys import Keys
import os


def write_xlsx_only():
    # ooo = glob.glob('C:\\1\\' + vvv + '*.zip') # шаблон обработанный win
    #ooo = glob.glob('./' + vvv + '*.zip')  # шаблон обработанный lin
    #path_1 = str(ooo)[2:-2]

    path = 'C:\\3\\report.xlsx'

    scu = 'Бинокль KENKO Mirage 7x50'

    sdf = [{'Товар': [f'{scu}'],'Цена': ['English Premier League (2)'], 'Статус': ['English Premier League (2)'],
                       'Дата': [176000000]}]

    df = pd.DataFrame(sdf)

    with ExcelWriter(path, mode="w" if os.path.exists(path) else "a+") as writer:
        df.sample().to_excel(writer, index=False,  engine="openpyxl")

    # filename = r'C:\\3\\report.xlsx'
    #
    # append_df_to_excel(filename, df)
    #
    # append_df_to_excel(filename, df, header=None, index=False)
    # el = f"(//{txt}[contains(.,'{txt_1}')])[{txt_2}]"
    # fin = self.get_count_elements_my(el)

    return

write_xlsx_only()


