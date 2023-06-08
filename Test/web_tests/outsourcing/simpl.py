import glob
import zipfile
import pandas as pd
import pathlib
#
# xxx = "Абу Али С "
# xxxx = xxx[0:1]
# zzzz = "А"
# print(type(xxxx), type(zzzz))
#
# x = "£10.80"
#
# fee = "£0.30"
# am = "£10.50"
#
# z_fee = float(fee[1:8])
# z_am = float(am[1:8])
#
# v = z_fee +z_am
#
# ss = "10.50 GBP"
# zs = ss[0:5]
#
# f = "10.50"
# g = "10.5"
#
# assert xxxx == zzzz, "Wou"
import datetime

# n = 3
# for i in range(0,  n):
#     # if i == (n-1):
#     print("f" + str(n))

fin = 3
while fin >= 1:
    #print("fin" + str(fin))
    if fin == 0:
           break
    fin -= 1

# print(z_fee, z_am, v)
# print(zs)

x = datetime.datetime.now()

y = x.strftime("%d.%m.%Y")

z = x.strftime("%d%m%Y")

print(x)
print(y)
print(z)


# from datetime import datetime
# import locale
# locale.setlocale(locale.LC_TIME, 'ru')
# mydate='3.10.2021'
#
# month = datetime.strptime(mydate, "%d.%m.%Y").strftime("%B")
# print(month)


# date = '3.10.2021'
#
# def transform_date(date):
#
#     months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
#            'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
#     day,month,year = date.split('.')
#     return f'{day} {months[int(month) - 1]} {year} г.'
#
# print(transform_date(date))


date_time = datetime.datetime.today()
sd = (date_time.strftime('%H:%M'))
# print(date.strftime('%H:%M'))


def datetime_only_data() -> str:
    x = datetime.datetime.now()
    date_time = datetime.datetime.today()
    sd = (date_time.strftime('%H:%M'))
    date_day = datetime.date.today()
    dd = date_day.day
    date = x.strftime("%m.%Y")
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    month, year = date.split('.')

    fin = f'{months[int(month) - 1]} {year} г.'
    full = str(dd) + " " + str(fin) + " " + str(sd)
    return full

print(datetime_only_data())

#zo = datetime.datetime.now(ZoneInfo("America/Los_Angeles"))

offset = datetime.timedelta(hours=3)
zo = datetime.timezone(offset, name='МСК')
print("zo = " + str(zo))

zov = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(seconds=1)))
print("zov = " + str(zov))

# print(datetime_only_data() + " " + sd)

# date_day = datetime.date.today()
# print(date_day.day)
# date_time = datetime.datetime.now()
# # Получение часа суток от времени
# print(date_time.hour)


# with ZipFile("metanit.zip", "a") as myzip:
#     # записываем в архив новый файл "hello5.txt"
#     with myzip.open("hello5.txt", "w") as hello_file:
#         encoded_str = bytes("Python...", "UTF-8")
#         hello_file.write(encoded_str)

#zz = x.strftime("%Y%m%d.%H%M")

zz = '20230611.1157'

#vv = f'export_paymentorder_talkbank_{zz}08.zip'
vv = f'export_selfemployed_alfabank_{zz}12.xlsx'
vvv = vv[:-6]
# print("vvv = " + vvv)
ooo = glob.glob('C:\\1\\' + vvv + '*.xlsx')
path_1 = str(ooo)[2:-2]
#print("ooo = " + str(ooo))
print("path_1 = " + path_1)
#archive = zipfile.ZipFile(path_1, 'r')
#archive = zipfile.ZipFile(f'C:\\1\\export_paymentorder_talkbank_20230607.161708.zip', 'r')
#archive1 = archive.namelist()

#fin = (str(archive1)[2:-2])
#g = glob.glob('*.')

#xtx = archive.open( fin ,'r', pwd=None, force_zip64=False)
#print(xtx.readlines())
#archive.printdir()
#Let us verify the operation..
#txtdata = archive.read('1.xlsx')
columns = ['Компания-клиент', 'Кластер ','Дневное время','Ночное время', 'Хрень']
txt_data = pd.read_excel(path_1)
df = pd.DataFrame(txt_data)

#txt_fin = pd.read_excel(xtx, header=None, names = columns)
#df = pd.DataFrame(txt_data)
#assert 'Компания-клиент' in df.columns, "Колонки нет"

#print(txtdata)
#print(archive)
#print(xtx)
print(txt_data)

#print(txt_fin)

#print('txt_check = '  + str(txt_check))

#check if 'team' column exists in DataFrame

#print(str(archive1)[2:-2])


#ABC#1.png  20230607.161708
#export_paymentorder_talkbank_20230607.002247.zip


#path = pathlib.Path('C:\\1')
#abc = path.glob('export_paymentorder_talkbank_20230607.161708.zip')
#def_ = path.glob('export_paymentorder_talkbank_[0-9].png')

# Veter = Veter[0].rsplit(".", 1)[0]
# print(Veter)