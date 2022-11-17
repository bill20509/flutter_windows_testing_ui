import time
from libs.YMK import pages
from libs.YMK.locators import TemplateStoreLocator
from selenium.webdriver.common.by import By


class Store(pages.YMK_base.YMKbase):
    def __init__(self, driver):
        super().__init__(driver)

    def click_looks(self):
        self.click_element_by_text("Looks")
        return self

    def click_download(self):
        self.click_element_by_text("Download")
        return self

    def click_use(self):
        self.click_element_by_text("Use")
        return self

    def select_premium_collection(self):
        self.click_element_by_text("9a4a7288-61e4-49af-8f62-15cc56c86b71")
        return self

    def click_all(self):
        # self.click_child_element(TemplateStoreLocator.Look.text_view, TemplateStoreLocator.Look.all)
        self.click_element_by_text("All >")
        return self


class Hair(Store):
    def __init__(self, driver):
        super().__init__(driver)

    def select_female_new_download_wig(self, number=1, downloadtimeout=5):
        time.sleep(3)
        self.switch_context(1)
        self.switch_windows(0)
        count = 0
        while count < 5:
            try:
                self.wait_element_visible(TemplateStoreLocator.Hair.female_new_download_wig, timeout=10)
                self.select_element_by_number(TemplateStoreLocator.Hair.female_new_download_wig, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(TemplateStoreLocator.Hair.female_new_list)
                count += 1
        time.sleep(downloadtimeout)
        return self

    def select_female_new_use_wig(self, number=1):
        count = 0
        while count < 5:
            try:
                self.select_element_by_number(TemplateStoreLocator.Hair.female_new_download_wig, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(TemplateStoreLocator.Hair.female_new_list)
                count += 1
        self.switch_context(0)
        return pages.photomakeup_page.HairStyle(self.driver)


class Look(Store):
    def __init__(self, driver):
        super().__init__(driver)

    def click_club_chic_look(self):
        for i in range(10):
            try:
                self.click_element_by_text("Sum_thumb_4")
                break
            except (ValueError, Exception):
                time.sleep(2)
        time.sleep(5)
        self.click_element_by_text("Sum_thumb_4")
        return pages.photomakeup_page.Looks(self.driver)

    def click_night_out_look(self):
        for i in range(10):
            try:
                self.click_element_by_text("Sum_thumb_2")
                break
            except (ValueError, Exception):
                time.sleep(2)
        time.sleep(5)
        self.click_element_by_text("Sum_thumb_2")
        return pages.photomakeup_page.Looks(self.driver)

    def click_daring_look(self):
        for i in range(10):
            try:
                self.click_element_by_text("Sum_thumb_3")
                break
            except (ValueError, Exception):
                time.sleep(2)
        time.sleep(5)
        self.click_element_by_text("Sum_thumb_3")
        return pages.photomakeup_page.Looks(self.driver)


class Effect(Store):
    def __init__(self, driver):
        super().__init__(driver)

    # def click_summer_pack(self, number=1):
    #     time.sleep(3)
    #     self.switch_context(1)
    #     self.switch_windows(0)
    #     count = 0
    #     while count < 5:
    #         try:
    #             self.wait_element_visible(TemplateStoreLocator.Hair.female_new_download_wig, timeout=10)
    #             self.select_element_by_number(TemplateStoreLocator.Hair.female_new_download_wig, (number - 1))
    #             break
    #         except (ValueError, Exception):
    #             self.scroll_vertical(TemplateStoreLocator.Effect.content_view)
    #             count += 1
    #     return self

    def click_effect_pack_download(self):
        for i in range(10):
            try:
                self.click_element_by_text("Download")
                break
            except (ValueError, Exception):
                time.sleep(2)
        time.sleep(15)
        self.click_element_by_text("Use")
        return pages.effects_page.Effects(self.driver)


class Lipart(Store):
    def __init__(self, driver):
        super().__init__(driver)
#
#     def click_lipart_pattern1(self):
#         self.switch_context(1)
#         self.switch_windows(0)
#         for i in range(10):
#             try:
#                 self.driver.find_element(By.CLASS_NAME, "android.widget.Image").click()
#                 break
#             except (ValueError, Exception):
#                 time.sleep(2)
#         time.sleep(5)
#         self.driver.find_element(By.CLASS_NAME, "android.widget.Image").click()
#         return self
