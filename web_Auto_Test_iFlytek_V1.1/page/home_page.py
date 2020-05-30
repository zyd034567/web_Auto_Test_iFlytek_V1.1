from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from base.base_page import BasePage, BaseHandle,BaseAction
from utils import DriverUtil


class HomePage(BasePage):
    """
    首页-对象库层
    """

    def __init__(self):
        super().__init__()
        self.driver = DriverUtil.get_driver()

        # 首页
        self.home_button = (By.ID, "homepage")
        # 转文字/翻译
        self.translate = (By.CLASS_NAME, 'menu-add')
        # 智能硬件
        self.intelligent_hardware = (By.CLASS_NAME, "head-menu-hardware")
        # 会员/充值
        self.membership_recharge = (By.ID, "czksc1")
        # 帮助中心
        self.help_center = (By.CLASS_NAME, "head-menu-server")
        # 企业服务
        self.enterprise_service = (By.CLASS_NAME, "head-menu-enterprise-server")
        # 下载客户端
        self.download_client = (By.LINK_TEXT, "下载客户端")
        # 立即抢购弹窗关闭按钮
        self.snap_the_popover_close_button = (By.XPATH, "/ html / body / div[11] / div / span")
        # 用户协议确认按钮
        self.user_agreement_confirmation_button = (By.XPATH, "//*[@id='p-save']/font/font")
        # 关于我们
        self.about_us = (By.LINK_TEXT, "关于我们")

    # 首页
    def find_home_button(self):
        return self.find_element(self.home_button)

    # 转文字/翻译
    def find_translate(self):
        return self.find_element(self.translate)

    # 智能硬件
    def find_intelligent_hardwares(self):
        return self.find_element(self.intelligent_hardware)

    # 会员/充值
    def find_membership_recharge(self):
        return self.find_element(self.membership_recharge)

    # 帮助中心
    def find_help_center(self):
        return self.find_element(self.help_center)

    # 企业服务
    def find_enterprise_service(self):
        return self.find_element(self.enterprise_service)

    # 下载客户端
    def find_download_client(self):
        return self.find_element(self.download_client)

    # 立即抢购弹窗关闭按钮
    def find_snap_the_popover_close_button(self):
        return self.find_element(self.snap_the_popover_close_button)

    # 用户协议确认按钮
    def find_user_agreement_confirmation_button(self):
        return self.find_element(self.user_agreement_confirmation_button)

    # 关于我们按钮
    def find_about_us(self):
        return self.find_element(self.driver.scroll_find_element(self.about_us))
        # return self.find_element(self.about_us)


class HomeHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        super().__init__()
        self.driver = DriverUtil.get_driver()
        self.home_page = HomePage()

    # 悬停转文字 / 翻译
    def hover_translate(self):
        ActionChains(self.driver).move_to_element(self.home_page.find_translate()).perform()

    # 悬停智能硬件
    def hover_intelligent_hardwares(self):
        ActionChains(self.driver).move_to_element(self.home_page.find_intelligent_hardwares()).perform()

    # 悬停帮助
    def hover_help_center(self):
        ActionChains(self.driver).move_to_element(self.home_page.find_help_center()).perform()

    # 悬停 企业服务
    def hover_enterprise_service(self):
        ActionChains(self.driver).move_to_element(self.home_page.find_enterprise_service()).perform()

    # 点击会员/充值
    def click_membership_recharge(self):
        self.home_page.find_membership_recharge().click()

    # 点击下载客户端
    def click_download_client(self):
        self.home_page.find_download_client().click()

    # 点击立即抢购弹窗关闭按钮
    def click_snap_the_popover_close_button(self):
        self.home_page.find_snap_the_popover_close_button().click()

    # 点击用户协议确认按钮
    def click_user_agreement_confirmation_button(self):
        self.home_page.find_user_agreement_confirmation_button().click()

    # 点击关于我们按钮
    def click_about_us(self):
        self.home_page.find_about_us().click()


class HomeProxy:
    """
    业务层
    """

    def __init__(self):
        self.home_handle = HomeHandle()

    # 展示翻译列表
    def show_translate_list(self):
        self.home_handle.hover_translate()

    # 展示智能硬件
    def show_intelligent_hardware_list(self):
        self.home_handle.hover_intelligent_hardwares()

    # 展示帮助中心
    def show_help_center(self):
        self.home_handle.hover_help_center()

    # 展示企业服务
    def show_enterprise_service(self):
        self.home_handle.hover_enterprise_service()

    # 进入会员/充值
    def entrance_membership_recharge(self):
        self.home_handle.click_membership_recharge()

    # 进入下载客户端
    def entrance_download_client(self):
        self.home_handle.click_download_client()

    # 关闭抢购弹窗
    def close_snap_the_popover_close_button(self):
        self.home_handle.click_snap_the_popover_close_button()

    # 确认关闭抢购弹窗
    def affirm_user_agreement_confirmation_button(self):
        self.home_handle.click_user_agreement_confirmation_button()

    # 进入关于我们
    def entrance_about_us(self):
        self.home_handle.click_about_us()




