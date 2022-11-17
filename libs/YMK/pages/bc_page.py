from libs.YMK.locators import BCLocators
from libs.YMK import pages


class BC(pages.YMK_base.YMKbase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def check_trending_page_ad(self):
        i = 0
        while i < 10:
            try:
                self.wait_element_visible(BCLocators.bc_ad_panel, timeout=5)
                break
            except (ValueError, Exception):
                i = i + 1
                self.swipe_up(speed=500)

        if i < 10:
            self.move_ad_show_in_screen()
            return 1
        else:
            return 0

    def move_ad_show_in_screen(self):
        try:
            ad_location = self.find_element(BCLocators.bc_ad_panel).get_location_from_element()
            navigator_bar_location = self.find_element(BCLocators.navigator_bar).get_location_from_element()
            screen_size = self.get_screen_size()
            if ad_location["y"] > navigator_bar_location["y"]:
                self.swipe_up(speed=2500)
            elif ad_location["y"] > (int(screen_size[1]) * 0.4):
                self.driver.swipe(int(screen_size[0] * 0.5), int(screen_size[1] * 0.5), int(screen_size[0] * 0.5),
                                  int(screen_size[1] * 0.25), 5000)
        except (ValueError, Exception):
            pass
        return self

    def write_post_with_auto_attached_photo(self, post_title):
        try:
            self.wait_element_visible(BCLocators.post_button)
            self.send_keys_to_element(BCLocators.post_title, post_title)
            self.click_element(BCLocators.post_button)
            try:
                self.wait_element_visible(BCLocators.rating_dialog, timeout=2)
                self.driver.keyevent(4)
            except (ValueError, Exception):
                pass
        except (ValueError, Exception):
            pass
        return self


class LoginDialog(BC):

    def click_login_here(self):
        self.wait_element_visible(BCLocators.Log_in_here)
        self.click_element(BCLocators.Log_in_here)
        return self

    def login_bc_account(self, account, password):
        self.wait_element_visible(BCLocators.account)
        self.wait_element_visible(BCLocators.password)
        self.send_keys_to_element(BCLocators.account, account)
        self.send_keys_to_element(BCLocators.password, password)
        self.wait_element_visible(BCLocators.Login_button)
        self.click_element(BCLocators.Login_button)
        return pages.setting_page.SettingPage(self.driver)
