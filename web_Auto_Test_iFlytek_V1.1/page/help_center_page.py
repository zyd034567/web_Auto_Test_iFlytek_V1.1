from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class HelpCenterPage(BasePage):
    """
    首页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 了解价格标题
        self.to_know_the_price_title = (By.XPATH, "//*[@id='fw']/div/div/div[1]/div[1]/div/font/font")
        # 机器快转（中文、英文）
        self.machine_quick_turn = (By.PARTIAL_LINK_TEXT, "机器快转")
        # 人工精转
        self.artificial_fine_turn = (By.PARTIAL_LINK_TEXT, "人工精转")
        # 多语种翻译服务
        self.multilingual_translation_service = (By.PARTIAL_LINK_TEXT, "多语种翻译服务")

        # 操作流程标题
        self.operation_procedure_title = (By.XPATH, "//*[@id='fw']/div/div/div[1]/div[2]/div")
        # 语音转文字
        self.voice_to_text = (By.LINK_TEXT, "语音转文字")
        # 多语种翻译
        self.multilingual_translation = (By.LINK_TEXT, "多语种翻译")

        # 常见问题标题
        self.frequently_asked_questions_title = (By.XPATH, "//*[@id='fw']/div/div/div[2]/div[1]/div")
        # 机器快转与人工精转有什么区别
        self.machine_speed_and_manual_precision = (By.PARTIAL_LINK_TEXT, "机器快转与人工精转有什么区别")
        # 网站转文字的收费标准是什么？
        self.the_website_turns_the_text_the_charge_standard = (By.PARTIAL_LINK_TEXT, "网站转文字的收费标准是什么")
        # 网站支持哪些格式的音频转文字？
        self.the_site_supports_the_format_of_audio_to_text = (By.PARTIAL_LINK_TEXT, "网站支持哪些格式的音频转文字")
        # 人工翻译各级别的区别？
        self.human_translation_level_differences = (By.PARTIAL_LINK_TEXT, "人工翻译各级别的区别")
        # 更多
        self.more = (By.LINK_TEXT, '更多')

        # 服务介绍标题
        self.service_introduction_title = (By.XPATH, "//*[@id='fw']/div/div/div[2]/div[2]/div")
        # 服务介绍
        self.service_introduction = (By.LINK_TEXT, '服务介绍')

    #  了解价格标题
    def find_to_know_the_price_title(self):
        return self.find_element(self.to_know_the_price_title)

    #  机器快转（中文、英文）
    def find_machine_quick_turn(self):
        return self.find_element(self.machine_quick_turn)

    # 人工精转
    def find_artificial_fine_turn(self):
        return self.find_element(self.artificial_fine_turn)

    # 多语种翻译服务
    def find_multilingual_translation_service(self):
        return self.find_element(self.multilingual_translation_service)

    # 操作流程标题
    def find_operation_procedure_title(self):
        return self.find_element(self.operation_procedure_title)

    # 语音转文字
    def find_voice_to_text(self):
        return self.find_element(self.voice_to_text)

    # 多语种翻译
    def find_multilingual_translation(self):
        return self.find_element(self.multilingual_translation)

    # 常见问题标题
    def find_frequently_asked_questions_title(self):
        return self.find_element(self.frequently_asked_questions_title)

    # 机器快转与人工精转有什么区别
    def find_machine_speed_and_manual_precision(self):
        return self.find_element(self.machine_speed_and_manual_precision)

    # 网站转文字的收费标准是什么？
    def find_the_website_turns_the_text_the_charge_standard(self):
        return self.find_element(self.the_website_turns_the_text_the_charge_standard)

    # 网站支持哪些格式的音频转文字？
    def find_the_site_supports_the_format_of_audio_to_text(self):
        return self.find_element(self.the_site_supports_the_format_of_audio_to_text)

    #  人工翻译各级别的区别？
    def find_human_translation_level_differences(self):
        return self.find_element(self.human_translation_level_differences)

    # 更多
    def find_more(self):
        return self.find_element(self.more)

    # 服务介绍标题
    def find_service_introduction_title(self):
        return self.find_element(self.service_introduction_title)

    # 服务介绍
    def find_service_introduction(self):
        return self.find_element(self.service_introduction)


class HelpCenterHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.help_center_page = HelpCenterPage()

    # 检查“了解价格”文本
    def select_to_know_the_price_title(self):
        return self.help_center_page.find_to_know_the_price_title().text

    # 机器快转（中文、英文）
    def click_machine_quick_turn(self):
        self.help_center_page.find_machine_quick_turn().click()

    # 点击人工精转
    def click_artificial_fine_turn(self):
        self.help_center_page.find_artificial_fine_turn().click()

    # 点击多语种翻译服务
    def click_multilingual_translation_service(self):
        self.help_center_page.find_multilingual_translation_service().click()

    # 检查“操作流程”标题
    def select_operation_procedure_title(self):
        return self.help_center_page.find_operation_procedure_title().text

    # 点击语音转文字
    def click_voice_to_text(self):
        self.help_center_page.find_voice_to_text().click()

    # 点击多语种翻译
    def click_multilingual_translation(self):
        self.help_center_page.find_multilingual_translation().click()

    # 检查“常见问题”标题
    def select_frequently_asked_questions_title(self):
        return self.help_center_page.find_frequently_asked_questions_title().text

    # 点击 机器快转与人工精转有什么区别
    def click_machine_speed_and_manual_precision(self):
        self.help_center_page.find_machine_speed_and_manual_precision().click()

    # 点击 网站转文字的收费标准是什么？
    def click_the_website_turns_the_text_the_charge_standard(self):
        self.help_center_page.find_the_website_turns_the_text_the_charge_standard().click()

    # 点击 网站支持哪些格式的音频转文字？
    def click_the_site_supports_the_format_of_audio_to_text(self):
        self.help_center_page.find_the_site_supports_the_format_of_audio_to_text().click()

    # 点击 人工翻译各级别的区别？
    def click_human_translation_level_differences(self):
        self.help_center_page.find_human_translation_level_differences().click()

    #  点击 更多
    def click_find_more(self):
        self.help_center_page.find_more().click()

    # 检查“服务介绍”标题
    def select_service_introduction_title(self):
        return self.help_center_page.find_service_introduction_title().text

    # 点击 服务介绍
    def click_service_introduction(self):
        self.help_center_page.find_service_introduction().click()


class HelpCenterProxy:
    """
    业务层
    """

    def __init__(self):
        self.help_center_handle = HelpCenterHandle()

    # 获取"语音转文字"文本
    def gain_select_to_know_the_price_title(self, expect):
        msg = self.help_center_handle.select_to_know_the_price_title()
        return expect == msg

    # 进入机器快转（中文、英文）
    def access_machine_quick_turn(self):
        self.help_center_handle.click_machine_quick_turn()

    # 进入人工精转
    def access_artificial_fine_turn(self):
        self.help_center_handle.click_artificial_fine_turn()

    # 进入多语种翻译服务
    def access_multilingual_translation(self):
        self.help_center_handle.click_multilingual_translation()

    # 获取“操作流程”标题文本
    def gain_operation_procedure_title(self, expect):
        msg = self.help_center_handle.select_operation_procedure_title()
        return expect == msg

    # 进入语音转文字
    def access_voice_to_text(self):
        self.help_center_handle.click_voice_to_text()

    # 进入多语种翻译
    def access_multilingual_translatio_flow(self):
        self.help_center_handle.click_multilingual_translation()

    # 获取“常见问题”标题文本
    def gain_frequently_asked_questions_title(self, expect):
        msg = self.help_center_handle.select_frequently_asked_questions_title()
        return expect == msg

    # 进入 机器快转与人工精转有什么区别
    def access_machine_speed_and_manual_precision(self):
        self.help_center_handle.click_machine_speed_and_manual_precision()

    # 进入 网站转文字的收费标准是什么？
    def access_the_website_turns_the_text_the_charge_standard(self):
        self.help_center_handle.click_the_website_turns_the_text_the_charge_standard()

    # 进入 网站支持哪些格式的音频转文字？
    def access_the_site_supports_the_format_of_audio_to_text(self):
        self.help_center_handle.click_the_site_supports_the_format_of_audio_to_text()

    # 进入 人工翻译各级别的区别？
    def access_human_translation_level_differences(self):
        self.help_center_handle.click_human_translation_level_differences()

    # 进入  更多
    def access_find_more(self):
        self.help_center_handle.click_find_more()

    # 获取“服务介绍”标题文本
    def gain_service_introduction_title(self, expect):
        msg = self.help_center_handle.select_service_introduction_title()
        return expect == msg

    # 进入 服务介绍
    def access_service_introduction(self):
        self.help_center_handle.click_service_introduction()
