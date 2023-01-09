from selenium.webdriver.common.by import By

from FW.WEB.AnyPage import AnyPage


class Locator:
    subject_textarea = (By.CSS_SELECTOR, '[test_id="subject"] textarea')


class TicketsList(AnyPage):
    pass