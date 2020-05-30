from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class IntelligentHardwarePage(BasePage):
    """
    页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 讯飞听见录音宝
        self.iflytek_heard_the_recording_treasure = (By.XPATH,'//*[@id="menu_list"]/li[3]/div/div/div[1]/a')
        # 讯飞听见智能会议系统（互联网版）L1
        self.iflytek_heard = (By.XPATH, '//*[@id="menu_list"]/li[3]/div/div/div[2]/a')

    # 讯飞听见录音宝
    def find_iflytek_heard_the_recording_treasure(self):
        return self.find_element(self.iflytek_heard_the_recording_treasure)

    # 讯飞听见智能会议系统（互联网版）L1
    def find_iflytek_heard(self):
        return self.find_element(self.iflytek_heard)


class IntelligentHardwareHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.intelligent_hardware_page = IntelligentHardwarePage()

    # 点击讯飞听见录音宝
    def click_iflytek_heard_the_recording_treasure(self):
        self.intelligent_hardware_page.find_iflytek_heard_the_recording_treasure().click()

    # 点击讯飞听见智能会议系统（互联网版）L1
    def click_iflytek_heard(self):
        self.intelligent_hardware_page.find_iflytek_heard().click()


class IntelligentHardwareProxy:
    """
    业务层
    """

    def __init__(self):
        self.intelligent_hardware_handle = IntelligentHardwareHandle()

    # 进入讯飞听见录音宝
    def access_iflytek_heard_the_recording_treasure(self):
        self.intelligent_hardware_handle.click_iflytek_heard_the_recording_treasure()

    # 进入讯飞听见智能会议系统（互联网版）L1
    def access_iflytek_heard(self):
        self.intelligent_hardware_handle.click_iflytek_heard()






