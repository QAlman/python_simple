class Settings:

    python = 'python'
    path_to_project = ''
    time_element_Wait = 30

    branch = 'pvp-at'
    mobile_stand_name = 'Android_emulator_Pixel2'

    # API
    Authorization = False
    content_type = False
    use_internal_link_in_api = False

    # WEB
    selenium_server = 'http://selenoid:4444/wd/hub'
    Browser = {
         'Name': 'chrome',
        'headless': False,
        #"'headless': True,
        #'Remote': True
        'Remote': False
    }

    GLOBAL = {
        'pvp-at': {
            'Name': 'Catalog',
            'main_page': 'https://github.com/QAlman/',
            'Internal_Link': 'https://github.com/QAlman/',
        },
        'python_verme_stage': {
            'Name': 'Catalog',
            'main_page': 'https://github.com/QAlman/',
            'Internal_Link': 'https://github.com/QAlman/',




            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': 'https://github.com/QAlman/',
                'External_Link': 'https://github.com/QAlman/',
                'AUTH_URL': 'https://github.com/QAlman/',
                'CERT_FILE': '',
                'client_id': '',
                'realm_name': '',
            },
    #         'SQL_SERVER': {
    #             'TypeSQL': '',
    #             'SERVER': '',
    #             'PORT': 2424,
    #             'DATABASE': '',
    #             'login': '',
    #             'password': '',
    #             'DRIVER': '',
    #         },
    #         'USERS': {
    #             'SystemOperator': {
    #                 'Name': "",
    #                 'User_id': "10c37c2c-b0e9-11ec-90da-ae981e1e0fca",
    #                 'client_secret': "bNxKnPEZTpnnSom9nhYuBMdmyOboBGPNKOM/tMCaTQYWgDgVU1ueJDGpVcDrb9Ak",
    #                 'Login': "",
    #                 'Password': "",
    #                 },
    #             'test_admin': {
    #                     'Name': "",
    #                     'Login': "",
    #                     'Password': "",
    #                 }
    #         }
        }
    }
    #
    # mobile_stand = {
    #     'Android_emulator_Nexus5': {
    #         'platformName': "Android",
    #         'platformVersion': "11",
    #         'deviceName': 'Nexus5',
    #         # 'app': "D:\Test debg.apk",
    #         'appPackage': "com.test",
    #         'appActivity': "com.base.activity.SplashActivity",
    #     }
    # }
