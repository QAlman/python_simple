from Data.GroupData import GroupData
from Data.Settings import Settings
from FW.API.Tickets.api_requests import ApiRequests
from FW.API.APIBase import APIBase
from FW.API.Tickets.api_tasks import ApiTasks
from FW.API.connect.token import Token
from FW.DriverInstance import DriverInstance
from FW.FWBase import FWBase
from FW.WEB.Account.Login import Login
from FW.WEB.AnyPage import AnyPage
from FW.WEB.MainPage import MainPage
from FW.WEB.activity import Activity
# from FW.WEB.tickets.request.request_create import RequestCreate
# from FW.WEB.tickets.task.task_id import TaskId
# from FW.WEB.tickets.task.task_create import TaskCreate
from FW.WEB.tickets_list import TicketsList
from FW.WEB.web_base import WebBase
from FW.work_with_time import work_with_time

from FW.WEB.ecom.ecom_test import ecom_create
from FW.WEB.ecom.ecom_steps import ecom_steps



class ApplicationManager:

    group_data = GroupData()
    settings = Settings()

    def __init__(self):
        self.driver_instance = DriverInstance()
        # self.fw_base = FWBase(self)
        self.api_base = APIBase(self)
        self.api_requests = ApiRequests(self)
        # self.web_base = WebBase(self)
        # self.time = work_with_time()

        self.web_any_page = AnyPage(self)
        # self.web_main_page = MainPage(self)
        # self.web_login = Login(self)
        self.web_activity = Activity(self)
        self.web_ecom = ecom_create(self)
        self.web_steps = ecom_steps(self)
        # self.api_tasks = ApiTasks(self)
        # self.api_token = Token(self)
