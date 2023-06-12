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

zz = x.strftime("%Y%m%d.%H%M")

print(x)
print(y)
print(z)
print(zz)


date_time = datetime.datetime.today()
sd = (date_time.strftime('%H:%M'))

print(sd)




def smpl(c1 = None, c2 = None , c3=None):
    d = "12345 Werty fghj !@!"
    assert c1 in d, "wwwwww"
    assert c2 in d, "ddddd"
    if c3 == None:
        pass
    else:
        assert c3 in d, "ddddd"

    return True

s1 = "12345"
s2 = "fg"
s3 = "!"



z = smpl(s1, s2, s3)
print("z = " + str(z))

#
# # print(date.strftime('%H:%M'))
#
# # print(datetime_only_data() + " " + sd)
#
# # date_day = datetime.date.today()
# # print(date_day.day)
# # date_time = datetime.datetime.now()
# # # Получение часа суток от времени
# # print(date_time.hour)
#
#
#
#
# archive = zipfile.ZipFile('C:\\1\\export_paymentorder_talkbank_20230607.161708.zip', 'r')
# archive1 = archive.namelist()
# fin = (str(archive1)[2:-2])
#
#
# xtx = archive.open(fin, 'r', pwd=None, force_zip64=False)
#
# archive.printdir()
#
# txt_data = pd.read_excel(xtx)
#
# print(txt_data)
# #print(str(archive1)[2:-2])
#
# #ABC#1.png  20230607.161708
# #export_paymentorder_talkbank_20230607.002247.zip
#
#
# path = pathlib.Path('C:\\1')
# abc = path.glob('export_paymentorder_talkbank_20230607.161708.zip')
# #def_ = path.glob('export_paymentorder_talkbank_[0-9].png')
#
# # Veter = Veter[0].rsplit(".", 1)[0]
# print(Veter)