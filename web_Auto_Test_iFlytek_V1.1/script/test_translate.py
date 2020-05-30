import time
import unittest

from selenium.webdriver.common.by import By

from base.base_page import BaseAction
from page.home_page import HomeProxy

from page.translate_page import TranslateProxy
from utils import DriverUtil
from parameterized import parameterized
import json
import logging
import config


class TestTranslate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.translate_proxy = TranslateProxy()
        cls.home_proxy = HomeProxy()
        cls.base_action = BaseAction()

    def setUp(self):
        self.driver.get("https://testbox.iflytek.com/")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()
        pass

    def test_translate(self):
        self.home_proxy.show_translate_list()
        self.translate_proxy.access_the_machine_runs_fast()
        time.sleep(2)
        self.base_action.save_screenshot()    # 进行截图
        self.base_action.sliding_scroll_bar()
        self.driver.back()
        time.sleep(5)

        self.home_proxy.show_translate_list()
        self.translate_proxy.access_chinese_manual_precision()
        time.sleep(2)
        self.driver.back()

        self.home_proxy.show_translate_list()
        self.translate_proxy.access_english_machine_turn_fast()
        time.sleep(2)
        self.driver.back()

        self.home_proxy.show_translate_list()
        self.translate_proxy.access_real_time_voice_to_text()
        time.sleep(2)
        self.driver.back()

        self.home_proxy.show_translate_list()
        self.translate_proxy.access_click_human_translation()
        time.sleep(2)
        self.driver.back()

        self.home_proxy.show_translate_list()
        self.translate_proxy.access_click_machine_translation()
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



