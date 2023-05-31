import random
import string


class DataTest:
    login = "test_outsourcing_2023"
    password = "freftTRHTRH!@#13564"

    txt_data_l_n = "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm 1234567890"
    txt_data_l_1 = "ЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъ ए बी सी डी डी  "
    txt_data_l_2 = " ए बी सी डी डी  "
    txt_data_l_3 = "មួយខគឃឃ"
    txt_data_l_4 = " ABC efg"
    txt_data_l_5 = '&@£$€¥*=+#% az AZ 09 `,."-&()' + " ' "
    txt_data_l_6 = '!? _ { } [ ]  \ | / < > ^  ± § ` ~ '
    txt_data_l_7 = '😀🐕😁😘😐🪀🏠'
    txt_data_l_8 = u'\\ud83d\\udc4d'

    txt_blank = "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b"

    txt_script_807 = '{ "agency__code": "verme_ag", "route_state__code__in": ["employee_ready_non_medical", "employee_ready_non_food", "employee_ready_food", "employee_booked_shift", "employee_shift", "employee_5_shift"], "paymentbankemployee__status": "request_sent", "paymentbankemployee__payment_bank__code": "alfa_is" }'

    txt_script_806 = '{ "agency__code": "verme_ag" }'

    txt_script_805 = '{ "route_state__code__ne": "employee_doc_removed", "agency_employee__agency__headquater__code": "Verme_1" }'

    txt_script_804 = '{ "agency__code": "verme_ag" }'

    txt_script_803 = '{ "agency__code": "verme_ag", "start_date__year": 2023, "start_date__month": 5 }'


    url_admin = "https://outsourcing-auto.verme.ru/admin"

    to_file_01 = '01.jpg'
    to_file_02 = '02.jpg'
    to_file_03 = '03.jpg'

    # ------------random 1------

    def generate_random_string(length_1=6):
        letters = string.digits
        rand_string = ''.join(random.choice(letters) for i in range(length_1))
        return rand_string

    generate_random_string()

    string_6 = generate_random_string()

    # -------------random 1-------

    # ------------random 2------
    def generate_random_string_2(length_1=4):
        letters = string.digits
        rand_string_2 = ''.join(random.choice(letters) for i in range(length_1))
        return rand_string_2

    generate_random_string_2()

    string_4 = generate_random_string_2()

    # -------------random 2-------

    # ------------random 3------
    def generate_random_string_3(length_1=9):
        letters = string.digits
        rand_string_3 = ''.join(random.choice(letters) for i in range(length_1))
        return rand_string_3

    generate_random_string_3()

    string_9 = generate_random_string_3()

    # -------------random 3-------

    # -----------random 4--------
    def generate_random_string_4(length_2=5):
        letters_4 = 'aăáâbcdđeêghiklmnoôơpqrstuưxy'
        rand_string_4 = ''.join(random.choice(letters_4) for i in range(length_2))
        return rand_string_4

    generate_random_string_4()

    string_small = generate_random_string_4()

    print(generate_random_string_4())

    # -----------random 4-------

    # -----------random 5--------
    def generate_random_string_5(length_2=9):
        letters_5 = 'AăÂBCDĐEêGHIKLMNOÔƠPQRSTUƯXY'
        rand_string_5 = ''.join(random.choice(letters_5) for i in range(length_2))
        return rand_string_5

    generate_random_string_5()

    string_big = generate_random_string_5()

    print(generate_random_string_5())

    # -----------random 5-------

    # -----------random 6--------
    def generate_random_string_6(length_2=18):
        letters_5 = 'ABCDE@#$%&FGHabc123456789defg12345!@#$%&6789hijklmnop@#$%&qrstuvwxyzIJKL123456789MNPQR@#$%&STUVWXYZ'
        rand_string_5 = ''.join(random.choice(letters_5) for i in range(length_2))
        return rand_string_5

    generate_random_string_6()

    string_pass = generate_random_string_6()

    print(generate_random_string_6())
    # -----------random 6-------

    print(txt_data_l_7)

    # -----------random 7--------
    def generate_random_string_7(length_2=12):
        letters_5 = 'ABCDEhijklmnopqrstuvwxyzIJKL123456789MNPQRSTUVWXYZ'
        rand_string_5 = ''.join(random.choice(letters_5) for i in range(length_2))
        return rand_string_5

    generate_random_string_7()

    string_description = generate_random_string_7()

    print(generate_random_string_6())
    # -----------random 6-------

    print(txt_data_l_7)
