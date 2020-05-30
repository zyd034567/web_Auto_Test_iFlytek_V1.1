import time
import unittest
import utils
# from page.index_page import IndexProxy
from base.base_page import BaseAction
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from utils import DriverUtil
from parameterized import parameterized
import json
import logging
import config


# 读取数据文件，构建测试数据
def build_data():
    test_data = []
    with open(config.BASE_DIR + "/data/login.json", encoding="UTF-8") as f:
        data = json.load(f)
        print(type(data))
        print("data=", data)
        for login_data in data:
            case_data = (login_data.get("username"),
                         login_data.get("pwd")
                         )
            test_data.append(case_data)
    logging.info("test_data={}".format(test_data))
    return test_data


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.login_proxy = LoginProxy()
        cls.home_proxy = HomeProxy()
        cls.base_action = BaseAction()

    def setUp(self):
        self.driver.get("https://testbox.iflytek.com/")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()
        pass

    @parameterized.expand(build_data)
    def test_login(self, username, pwd):
        logging.info("username={} pwd={} ".format(username, pwd))

        # 登录
        self.login_proxy.login_but()
        time.sleep(2)
        self.login_proxy.login(username, pwd)
        self.base_action.save_screenshot()
        time.sleep(2)
        self.home_proxy.close_snap_the_popover_close_button()

        #  断言
        # try:
        #     time.sleep(3)
        #     print("title=", self.driver.title)
        #     self.assertIn(expect, self.driver.title)
        # except Exception as e:
        #     logging.error("断言的时候出现了异常")
        #     logging.exception(e)

