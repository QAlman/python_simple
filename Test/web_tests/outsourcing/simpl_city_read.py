
import FW.WEB.outsourcing.city_test



def load_city_txt() :
                # el = f"(//{txt}[contains(.,'{txt_1}')])[{txt_2}]"
                # fin = self.get_count_elements_my(el)

    #fin = len(FW.WEB.outsourcing.city_test.CityTest.cities)

    fin = FW.WEB.outsourcing.city_test.CityTest.cities



    return  fin




zz = load_city_txt()
print(zz)

for i  in zz:
    print("zz = "  + str(i) )

tom = ("Tom", 22, "Google")
for item in tom:
    print(item)
