from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class EnterpriseServicePage(BasePage):
    """
    页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 语音转写、翻译API、支持公网调用和私有化部署
        self.voice_recognition_service = (By.XPATH, '//*[@id="cp"]/div/div/div[1]/a')

        # 帐户智能管理、高效安全、支持企业统一支付
        self.enterprise_login = (By.XPATH, "//*[@data-track='导航_企业帐号登录']")

        # 会议现场语音识别及翻译等服务的现场支持
        self.intelligent_conference_service = (By.XPATH, "//*[@data-track='导航_智能会议服务']")

        # 辅助快速会议纪要编辑出稿，智能会议信息管理
        self.intelligent_conference_system = (By.XPATH, "//*[@data-track='导航_智能会议系统']")

        # 同期声字幕制作、虚拟播报，智能编目与监管
        self.smart_media_overall_solution = (By.XPATH, "//*[@data-track='导航_智慧媒体整体解决方案']")

    # 语音转写、翻译API、支持公网调用和私有化部署
    def find_voice_recognition_service(self):
        return self.find_element(self.voice_recognition_service)

    # 帐户智能管理、高效安全、支持企业统一支付
    def find_enterprise_login(self):
        return self.find_element(self.enterprise_login)

    # 会议现场语音识别及翻译等服务的现场支持
    def find_intelligent_conference_service(self):
        return self.find_element(self.intelligent_conference_service)

    # 辅助快速会议纪要编辑出稿，智能会议信息管理
    def find_intelligent_conference_system(self):
        return self.find_element(self.intelligent_conference_system)

    # 同期声字幕制作、虚拟播报，智能编目与监管
    def find_smart_media_overall_solution(self):
        return self.find_element(self.smart_media_overall_solution)


class EnterpriseServiceHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.enterprise_service_page = EnterpriseServicePage()

    # 点击  语音转写、翻译API、支持公网调用和私有化部署
    def click_voice_recognition_service(self):
        self.enterprise_service_page.find_voice_recognition_service().click()

    # 点击 帐户智能管理、高效安全、支持企业统一支付
    def click_enterprise_login(self):
        self.enterprise_service_page.find_enterprise_login().click()

    # 点击  会议现场语音识别及翻译等服务的现场支持
    def click_intelligent_conference_service(self):
        self.enterprise_service_page.find_intelligent_conference_service().click()

    # 点击  辅助快速会议纪要编辑出稿，智能会议信息管理
    def click_intelligent_conference_system(self):
        self.enterprise_service_page.find_intelligent_conference_system().click()

    # 点击 同期声字幕制作、虚拟播报，智能编目与监管
    def click_smart_media_overall_solution(self):
        self.enterprise_service_page.find_smart_media_overall_solution().click()


class EnterpriseServiceProxy:
    """
    业务层
    """

    def __init__(self):
        self.enterprise_service_handle = EnterpriseServiceHandle()

    # 进入 语音转写、翻译API、支持公网调用和私有化部署
    def access_voice_recognition_service(self):
        self.enterprise_service_handle.click_voice_recognition_service()

    # 进入 帐户智能管理、高效安全、支持企业统一支付
    def access_enterprise_login(self):
        self.enterprise_service_handle.click_enterprise_login()

    # 进入 会议现场语音识别及翻译等服务的现场支持
    def access_intelligent_conference_service(self):
        self.enterprise_service_handle.click_intelligent_conference_service()

    # 进入 辅助快速会议纪要编辑出稿，智能会议信息管理
    def access_intelligent_conference_system(self):
        self.enterprise_service_handle.click_intelligent_conference_system()

    # 进入 同期声字幕制作、虚拟播报，智能编目与监管
    def access_smart_media_overall_solution(self):
        self.enterprise_service_handle.click_smart_media_overall_solution()




