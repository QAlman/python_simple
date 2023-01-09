import allure

from Test.TestBase import TestBase


class WebBase(TestBase):

    def setup_class(self):
        pass
        #self.APP.web_any_page.open_main_page()
        #self.APP.web_login.login_log_pas('admin', 'admin')

    def setup_method(self):
        #self.APP.web_any_page.open_main_page()
        pass


    def teardown_method(self):
        self.APP.web_any_page.allure_screenshot()

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()

    def create_task(self, name=None, description=None, contractor=None):
        if name is None: name = "Test task " + self.APP.time.get_time_now()
        if description is None: description = "Test Description " + self.APP.time.get_time_now()
        if contractor is None: contractor = 'Harry'

        self.APP.web_activity.click_btn_create_task_task_left_menu()
        self.APP.web_activity.fill_name(name)
        self.APP.web_activity.fill_description(description)
        self.APP.web_activity.add_contractor(contractor)
        return self.APP.web_activity.button_to_create_tickets()

    def services_create_folder(self, name_text=None, description=None, contractor=None):

        if name_text is None: name = "Аритабуратино"
        if description is None: description = "Test Description " + self.APP.time.get_time_now()
        if contractor is None: contractor = 'Harry'
        #if user is None: user = 'Галина'
        self.APP.web_activity.button_to_create_folder()
        return self.APP.web_activity.page_loaded_and()

    def services_create(self):

        self.APP.web_activity.button_to_create_services()
        return self.APP.web_activity.page_loaded_and()

    def services_creat_add(self):

        self.APP.web_activity.button_to_create_services_add()
        return self.APP.web_activity.page_loaded_and()

    def knowledge_create(self):

        self.APP.web_activity.button_to_create_article()
        return self.APP.web_activity.page_loaded_and()

    def knowledge_edit(self):

        self.APP.web_activity.button_to_edit_article()
        return self.APP.web_activity.page_loaded_and()

    # def knowledge_add(self):
    #
    #     self.APP.web_activity.button_to_add_article()
    #     return self.APP.web_activity.page_loaded_and()

    def knowledge_visible(self):

        self.APP.web_activity.button_to_visible_article()
        return self.APP.web_activity.page_loaded_and()

    def ecom_test(self):

        self.APP.web_activity.button_to_ecom()
        return self.APP.web_activity.page_loaded_and()
