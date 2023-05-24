
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

# print(datetime_only_data() + " " + sd)

# date_day = datetime.date.today()
# print(date_day.day)
# date_time = datetime.datetime.now()
# # Получение часа суток от времени
# print(date_time.hour)




