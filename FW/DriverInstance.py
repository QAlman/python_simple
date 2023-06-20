from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Data.Settings import Settings


class DriverInstance:

    def __init__(self):
        self.settings = Settings

    driver = None
    mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        }
    def get_driver(self):


        options = webdriver.ChromeOptions()
        if self.settings.Browser['headless']:
            options.headless = True
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            #options.add_argument('--window-size=1920,1080')
            #options.add_argument('--window-size=320,640')
            options.add_argument('--disable-gpu')
            #options.add_experimental_option("mobileEmulation", mobile_emulation)
            #options.add_argument("--auto-open-devtools-for-tabs")
        else:
            options.headless = False

        capabilities = DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'browser': 'ALL',
                                             'performance': 'ALL',
                                             'server': 'ALL',
                                             'client': 'ALL'}

        if self.settings.Browser['Remote']:
            self.driver = webdriver.Remote(
                command_executor=self.settings.selenium_server,
                proxy=None,
                options=options,
                desired_capabilities=capabilities)
        else:
            self.driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)

        if self.settings.Browser['headless'] is False:
            #options.add_argument('--window-size=1920,1080')
            #options.add_argument("--auto-open-devtools-for-tabs")
            Map_coordinates = dict({
                "latitude": 53.035117,
                "longitude": 158.651652,
                "accuracy": 100
            })
            self.driver.maximize_window()
            #self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)
        return self.driver

    def stop_driver(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
            self.driver = None
