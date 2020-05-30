from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层：封装定位元素的方法
class LoginPage(BasePage):

    def __init__(self):
        super().__init__()

        self.home_login = (By.CLASS_NAME, "login_icon")
        self.username = (By.ID, "account")
        self.pwd = (By.ID, "password")
        # self.code = (By.ID, "verify_code")
        self.login_btn = (By.ID, "loginrec")

    def find_home_login(self):
        return self.find_element(self.home_login)

    def find_username(self):
        return self.find_element(self.username)

    def find_pwd(self):
        return self.find_element(self.pwd)

    # def find_code(self):
    #     return self.find_element(self.code)

    def find_login_btn(self):
        return self.find_element(self.login_btn)


# 操作层：封装对元素操作的方法
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    def click_home_login(self):
        self.login_page.find_home_login().click()

    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    def input_pwd(self, pwd):
        self.input_text(self.login_page.find_pwd(), pwd)

    # def input_code(self, code):
    #     self.input_text(self.login_page.find_code(), code)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层：将一个或多个业务操作组合成一个业务功能
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录
    def login_but(self):
        self.login_handle.click_home_login()

    def login(self, username, pwd):
        self.login_handle.input_username(username)
        self.login_handle.input_pwd(pwd)
        self.login_handle.click_login_btn()
