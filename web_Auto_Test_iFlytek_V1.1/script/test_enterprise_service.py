import time
import unittest
import utils
from page.enterprise_service_page import EnterpriseServiceProxy
from page.home_page import HomeProxy

from page.translate_page import TranslateProxy
from utils import DriverUtil
from parameterized import parameterized
import json
import logging
import config


class TestEnterpriseService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.enterprise_service_proxy = EnterpriseServiceProxy()
        cls.home_proxy = HomeProxy()

    def setUp(self):
        self.driver.get("https://testbox.iflytek.com/")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()
        pass

    def test_enterprise_service(self):
        self.home_proxy.show_enterprise_service()
        self.enterprise_service_proxy.access_voice_recognition_service()
        time.sleep(2)
        self.driver.back()

        self.home_proxy.show_enterprise_service()
        self.enterprise_service_proxy.access_enterprise_login()
        time.sleep(2)
        self.driver.back()

        self.home_proxy.show_enterprise_service()
        self.enterprise_service_proxy.access_intelligent_conference_service()
        time.sleep(2)
        self.driver.back()

        self.home_proxy.show_enterprise_service()
        self.enterprise_service_proxy.access_intelligent_conference_system()
        time.sleep(2)
        self.driver.back()

        self.home_proxy.show_enterprise_service()
        self.enterprise_service_proxy.access_smart_media_overall_solution()
        time.sleep(2)
        self.driver.back()

        #  断言
        # try:
        #     time.sleep(3)
        #     print("title=", self.driver.title)
        #     self.assertIn(expect, self.driver.title)
        # except Exception as e:
        #     logging.error("断言的时候出现了异常")
        #     logging.exception(e)



