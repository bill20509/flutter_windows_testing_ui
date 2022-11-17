from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from libs.YMK import pages
from libs.YMK.locators import ResultLocators, PhotoMakeupLocators, ShareLookLocators


class Result(pages.YMK_base.YMKbase):
    def __init__(self, driver):
        super().__init__(driver)

    def click_photo_picker(self):
        self.wait_element_visible(ResultLocators.Album)
        self.click_element(ResultLocators.Album)
        return pages.photomakeup_page.PhotoMakeup(self.driver)

    def check_result_page_interstitial_ad(self, timeout=5):
        try:
            self.find_element(ResultLocators.Home)
            return 0
        except (ValueError, Exception):
            return 1

    def check_result_page_ad_banner(self, timeout=5):
        try:
            self.wait_element_visible(ResultLocators.result_page_view, 5)
            print("Result page shown")
            try:
                self.find_element(ResultLocators.result_page_ad_banner)
                return 1
            except (ValueError, Exception):
                return 0
        except (ValueError, Exception):
            try:
                self.wait_element_visible(ResultLocators.rating_page, timeout)
                self.driver.press_keycode(4)
                print("Close rating page")
            except (ValueError, Exception):
                try:
                    self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Close Ad').click()
                    # self.driver.find_element(By.XPATH, '//android.widget.LinearLayout[@content-desc=\"Close Ad\"]').click()
                    print("Close video AD")
                except (ValueError, Exception):
                    self.driver.find_element(By.CLASS_NAME, "android.webkit.WebView")
                    for i in range(15):
                        try:
                            self.wait_element_visible(ResultLocators.result_page_view, 2)
                            print("Close AD")
                            break
                        except (ValueError, Exception):
                            self.driver.press_keycode(4)

            try:
                self.find_element(ResultLocators.result_page_ad_banner)
                return 1
            except (ValueError, Exception):
                return 0

    def click_back(self):
        self.wait_element_visible(ResultLocators.Back)
        self.click_element(ResultLocators.Back)
        return pages.photomakeup_page.PhotoMakeup(self.driver)

    def share_look(self, title):
        for i in range(10):
            try:
                self.click_element(ResultLocators.Share_look)
                break
            except (ValueError, Exception):
                self.wait_element_visible(ResultLocators.result_page_view, 30)
                self.scroll_vertical(ResultLocators.result_page_view, speed=2000)
        self.wait_element_invisible(PhotoMakeupLocators.waiting_cursor, 60)
        self.wait_element_visible(ShareLookLocators.share, 60)
        self.send_keys_to_element(ShareLookLocators.post_title, title)
        self.click_element(ShareLookLocators.share)
        self.wait_element_visible(ShareLookLocators.share_item_icon, 180)
        return self

    def show_result_page(self, timeout=3):
        try:
            self.wait_element_visible(ResultLocators.result_page_view, 5)
            print("Result page shown")
        except (ValueError, Exception):
            try:
                self.wait_element_visible(ResultLocators.rating_page, timeout)
                self.driver.press_keycode(4)
                print("Close rating page")
            except (ValueError, Exception):
                try:
                    self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Close Ad').click()
                    # self.driver.find_element(By.XPATH, '//android.widget.LinearLayout[@content-desc=\"Close Ad\"]').click()
                    print("Close video AD")
                except (ValueError, Exception):
                    self.driver.find_element(By.CLASS_NAME, "android.webkit.WebView")
                    for i in range(15):
                        try:
                            self.wait_element_visible(ResultLocators.result_page_view, 2)
                            print("Close AD")
                            break
                        except (ValueError, Exception):
                            self.driver.press_keycode(4)
        return pages.result_page.Result(self.driver)

    def click_home(self):
        self.wait_element_visible(ResultLocators.Home)
        self.click_element(ResultLocators.Home)
        return pages.launcher_page.Launcher(self.driver)

    def find_ycp_card(self):
        for i in range(10):
            try:
                self.find_element(ResultLocators.ycp_card_padding)
                break
            except (ValueError, Exception):
                self.wait_element_visible(ResultLocators.result_page_view)
                self.scroll_vertical(ResultLocators.result_page_view, speed=2000)
        return self

    def find_ycn_card(self):
        for i in range(10):
            try:
                self.find_element(ResultLocators.ycn_card_padding)
                break
            except (ValueError, Exception):
                self.wait_element_visible(ResultLocators.result_page_view)
                self.scroll_vertical(ResultLocators.result_page_view, speed=2000)
        return self

    def find_collage_card(self):
        for i in range(10):
            try:
                self.find_element(ResultLocators.create_collage_btn)
                break
            except (ValueError, Exception):
                self.wait_element_visible(ResultLocators.result_page_view)
                self.scroll_vertical(ResultLocators.result_page_view, speed=2000)
        return self

    def click_to_ycp(self):
        self.wait_element_visible(ResultLocators.ycp_card_icon)  # YCP_card_icon only appears when YCP is installed.
        self.message("YCP installed, proceed!")
        self.click_element(ResultLocators.create_with_ycp)
        self.wait_element_invisible(ResultLocators.result_page_view)
        return self

    def click_to_ycn(self):
        self.wait_element_visible(ResultLocators.ycn_card_icon)  # YCN_card_icon only appears when YCN is installed.
        self.message("YCN installed, proceed!")
        self.click_element(ResultLocators.create_with_ycn)
        self.wait_element_invisible(ResultLocators.result_page_view)
        return self

    def click_to_collage(self):
        self.wait_element_visible(ResultLocators.create_collage_btn)
        self.click_element(ResultLocators.create_collage_btn)
        self.message("Entering Before After Collage!")
        self.wait_element_invisible(ResultLocators.result_page_view)
        return self

    def click_collage_save(self):
        self.wait_element_visible(ResultLocators.collage_save_btn)
        self.click_element(ResultLocators.collage_save_btn)
        self.message("Saving Collage!")
        self.wait_element_invisible(ResultLocators.result_page_view)
        return self

    def click_collage_share(self):
        self.wait_element_visible(ResultLocators.collage_share_btn)
        self.click_element(ResultLocators.collage_share_btn)
        self.message("Clicked SHARE!")
        self.wait_element_invisible(ResultLocators.collage_share_btn)
        return self

    def click_to_ycp_open_with(self):
        self.wait_element_visible(ResultLocators.create_with_ycp)
        self.click_element(ResultLocators.create_with_ycp)
        self.wait_element_invisible(ResultLocators.result_page_view)
        return self
    # This function is for test_edit_result_to_ycp case exception when YCP is not installed.

    def click_to_ycn_open_with(self):
        self.wait_element_visible(ResultLocators.create_with_ycn)
        self.click_element(ResultLocators.create_with_ycn)
        self.wait_element_invisible(ResultLocators.result_page_view)
        return self
    # This function is for test_edit_result_to_ycn case exception when YCN is not installed.

    def open_with_playstore(self):
        self.wait_element_visible(ResultLocators.open_with_panel)
        self.click_element_by_name(ResultLocators.open_with_app, "Google Play Store")
        self.wait_element_invisible(ResultLocators.open_with_panel)
        return self
    # This function is for test_edit_result_to_ycp case exception when YCP is not installed.

    def ycp_permission_allow(self):
        try:
            self.wait_element_visible(ResultLocators.ycp_permission_ok)
            self.click_element(ResultLocators.ycp_permission_ok)
            self.message("YCP permission allowed!")
        except (ValueError, Exception):
            self.message("Seems YCP permission already allowed, proceed!")
        return self

    def ycp_bipa_agree(self):
        try:
            self.wait_element_visible(ResultLocators.ycp_bipa_agree)
            self.click_element(ResultLocators.ycp_bipa_agree)
            self.message("YCP BIPA agreed!")
        except (ValueError, Exception):
            self.message("Seems YCP BIPA already agreed, proceed!")
        return self
