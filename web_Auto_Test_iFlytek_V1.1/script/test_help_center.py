import time
import unittest
import utils
from page.help_center_page import HelpCenterProxy
from page.home_page import HomeProxy
from utils import DriverUtil
from parameterized import parameterized
import json
import logging
import config


class TestHelpCenter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.help_center_proxy = HelpCenterProxy()
        cls.home_proxy = HomeProxy()

    def setUp(self):
        self.driver.get("https://testbox.iflytek.com/")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()
        pass

    def test_help_center(self):
        self.home_proxy.show_help_center()
        self.help_center_proxy.access_machine_quick_turn()
        time.sleep(2)
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_artificial_fine_turn()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_multilingual_translation()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_voice_to_text()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_multilingual_translatio_flow()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_machine_speed_and_manual_precision()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_the_website_turns_the_text_the_charge_standard()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_the_site_supports_the_format_of_audio_to_text()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_human_translation_level_differences()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_find_more()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        self.home_proxy.show_help_center()
        self.help_center_proxy.access_service_introduction()
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(handle[0])

        #  断言
        # try:
        #     time.sleep(3)
        #     print("title=", self.driver.title)
        #     self.assertIn(expect, self.driver.title)
        # except Exception as e:
        #     logging.error("断言的时候出现了异常")
        #     logging.exception(e)
