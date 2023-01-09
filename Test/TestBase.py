from FW.ApplicationManager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_class(self):
        pass
        #self.main_page = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page']
        #self.main_page = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page']


    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def teardown_class(self):
        pass
