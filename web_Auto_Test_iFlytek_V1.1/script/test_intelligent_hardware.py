import time
import unittest
import utils
from page.home_page import HomeProxy
from page.intelligent_hardware_page import IntelligentHardwareProxy

from page.translate_page import TranslateProxy
from utils import DriverUtil
from parameterized import parameterized
import json
import logging
import config


class TestIntelligentHardware(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.intelligent_hardware_proxy = IntelligentHardwareProxy()
        cls.home_proxy = HomeProxy()

    def setUp(self):
        self.driver.get("https://testbox.iflytek.com/")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()
        pass

    def test_intelligent_hardware(self):
        self.home_proxy.show_intelligent_hardware_list()
        self.intelligent_hardware_proxy.access_iflytek_heard_the_recording_treasure()
        time.sleep(2)
        self.driver.back()
        self.home_proxy.show_intelligent_hardware_list()
        self.intelligent_hardware_proxy.access_iflytek_heard()
        time.sleep(2)


        #  断言
        # try:
        #     time.sleep(3)
        #     print("title=", self.driver.title)
        #     self.assertIn(expect, self.driver.title)
        # except Exception as e:
        #     logging.error("断言的时候出现了异常")
        #     logging.exception(e)



