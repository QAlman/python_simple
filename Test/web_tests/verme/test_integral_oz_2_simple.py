# 15   мобильная версия

import keyboard
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_15():
    @pytest.fixture()
    def test_setup(self):
        global driver

        chrome_options = webdriver.ChromeOptions()
        mobile_emulation = {
            "deviceName": "Apple iPhone 5",
            "deviceMetrics": {"width": 375, "height": 667, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Mobile Safari/537.36 Edg/92.0.902.78"
        }

        # mobile_emulation = {"deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1"}
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--window-size=1920,1200")
        # chrome_options.add_argument("--window-size=375,667")
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("start-maximized")
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument("--enable-file-cookies")
        # chrome_options.add_argument('auto-open-devtools-for-tabs')
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-blink-features')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        driver.implicitly_wait(30)
        driver.set_page_load_timeout(30)
        driver.set_script_timeout(30)
        Map_coordinates = dict({
            "latitude": 53.0351,
            "longitude": 158.6516,
            "accuracy": 100
        })
        driver.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)

        # driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        #     "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36'})

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        self.base_url = "https://www.ozon.ru/product/bumerang-etnicheskiy-krasnyy-drakon-narody-vostoka-derevo-46-sm-823487495"

        yield
        driver.close()
        driver.quit()

    def test_untitled_test_case_test_mobile_1(self, test_setup):
        driver.get(self.base_url)

        time.sleep(3)
        keyboard.press_and_release('ctrl+shift+i')
        time.sleep(3)
        keyboard.press_and_release('ctrl+shift+m')
        time.sleep(3)
        driver.refresh()
        time.sleep(5)

        actions = ActionChains(driver)
        actions.send_keys(Keys.CONTROL, Keys.SHIFT, "i")

        actions.perform()
        time.sleep(2)

        driver.execute_script("window.open('https://www.ozon.ru/cart')")
        time.sleep(10)
        keyboard.press_and_release('ctrl+shift+i')
        time.sleep(3)
        keyboard.press_and_release('ctrl+shift+m')
        time.sleep(5)

        keyboard.press_and_release('ctrl+f5')
        time.sleep(10)

        driver.switch_to.window(driver.window_handles[1])

        time.sleep(3)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[text()='Укажите адрес доставки']"))).click()  #
        time.sleep(3)
        el = driver.find_element(By.XPATH, "//span[@class='qd7'][text()='Изменить']")

        actions = ActionChains(driver)
        actions.move_to_element(el)
        time.sleep(1)
        actions.click(el)
        actions.perform()

        time.sleep(3)

        # --------------на модальное окно с выбором городов
        el = driver.find_element(By.XPATH, "(//div[@data-widget='blockVertical'])[2]")
        actions = ActionChains(driver)
        actions.move_to_element(el)
        time.sleep(1)
        actions.perform()
        time.sleep(2)
        # ---------------

        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@type='search']"))).click()  #
        time.sleep(2)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@type='search']"))).send_keys("Петропавловск-Камчатский")  #
        time.sleep(2)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='q4d tsBodyL'][text()='Петропавловск-Камчатский']"))).click()  #

        time.sleep(2)
        driver.get(self.base_url)  # с измененным адресом теперь
        time.sleep(22222)

        # ----------------------------------------
