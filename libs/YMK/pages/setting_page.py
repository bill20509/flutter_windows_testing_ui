from selenium.webdriver import Keys
from selenium import webdriver
from libs.YMK.locators import SettingLocators, MeLocators, BCLocators
from libs.YMK import pages
import time


class SettingPage(pages.YMK_base.YMKbase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_back(self):
        self.wait_element_visible(SettingLocators.back_button)
        self.click_element(SettingLocators.back_button)
        return pages.me_page.MePage(self.driver)

    def click_about_me(self):
        self.wait_element_visible(SettingLocators.about_me)
        self.click_element(SettingLocators.about_me)
        return AboutMe(self.driver)

    def click_auto_save(self):
        for i in range(10):
            try:
                self.click_child_element(SettingLocators.auto_save, SettingLocators.switcher_item)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_front_camera_mirror(self):
        for i in range(10):
            try:
                self.click_child_element(SettingLocators.front_camera_mirror, SettingLocators.switcher_item)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_skin_beautifier(self):
        for i in range(10):
            try:
                self.click_child_element(SettingLocators.skin_beautifier, SettingLocators.switcher_item)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_access_gps(self):
        for i in range(10):
            try:
                self.click_child_element(SettingLocators.gps, SettingLocators.switcher_item)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_photo_watermark(self):
        for i in range(10):
            try:
                self.click_child_element(SettingLocators.photo_watermark, SettingLocators.switcher_item)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_video_watermark(self):
        for i in range(10):
            try:
                self.click_child_element(SettingLocators.video_watermark, SettingLocators.switcher_item)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_quality(self):
        for i in range(10):
            try:
                self.click_element(SettingLocators.quality)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return Quality(self.driver)

    def click_faq(self):
        for i in range(10):
            try:
                self.click_element(SettingLocators.faq)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return Faq(self.driver)

    def click_about(self):
        for i in range(10):
            try:
                self.click_element(SettingLocators.about)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return About(self.driver)

    def click_events(self):
        for i in range(10):
            try:
                self.click_element(SettingLocators.events)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_tutorials(self):
        for i in range(10):
            try:
                self.click_element(SettingLocators.tutorial)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_rate_us(self):
        for i in range(10):
            try:
                self.click_element(SettingLocators.rate_us)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_follow_us(self):
        for i in range(10):
            try:
                self.click_element(SettingLocators.follow_us)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_country(self):
        for i in range(10):
            try:
                self.click_element(SettingLocators.country)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return Country(self.driver)

    def find_video_watermark(self):
        for i in range(10):
            try:
                self.find_element(SettingLocators.video_watermark)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def find_photo_watermark(self):
        for i in range(10):
            try:
                self.find_element(SettingLocators.photo_watermark)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_premium_banner(self):
        self.wait_element_visible(SettingLocators.premium_banner)
        self.click_element(SettingLocators.premium_banner)
        return self

    def check_save_path(self):
        for i in range(10):
            try:
                self.find_element(SettingLocators.gps_item)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def check_country(self):
        for i in range(10):
            try:
                self.find_element(SettingLocators.tutorial)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=2000)
        return self

    def click_log_out(self):
        for i in range(10):
            try:
                self.find_element(SettingLocators.Logout_button)
                self.click_element(SettingLocators.Logout_button)
                self.wait_element_visible(SettingLocators.Dialog_logout_button)
                self.click_element(SettingLocators.Dialog_logout_button)
                break
            except (ValueError, Exception):
                self.scroll_vertical(SettingLocators.view, speed=10000)
        return self

    def login_bc_account(self, account, password):
        try:
            self.wait_element_visible(SettingLocators.Account_login)
            self.click_element(SettingLocators.Account_login)
            self.wait_element_visible(SettingLocators.Log_in_here)
            self.click_element(SettingLocators.Log_in_here)
            self.wait_element_visible(SettingLocators.account)
            self.wait_element_visible(SettingLocators.password)
            self.send_keys_to_element(SettingLocators.account, account)
            self.send_keys_to_element(SettingLocators.password, password)
            self.wait_element_visible(SettingLocators.Login_button)
            self.click_element(SettingLocators.Login_button)
            time.sleep(2)
            print(account, "login successfully!")
        except (ValueError, Exception):
            current_email = self.get_text_from_element(SettingLocators.email)
            if account == current_email:
                print("current account is:", current_email, "Don't need to login again")
            else:
                for i in range(5):
                    try:
                        self.find_element(SettingLocators.Logout_button)
                        self.click_element(SettingLocators.Logout_button)
                        self.wait_element_visible(SettingLocators.Dialog_logout_button)
                        self.click_element(SettingLocators.Dialog_logout_button)
                        print("logout current account:", current_email)
                        self.wait_element_visible(MeLocators.setting_button)
                        self.click_element(MeLocators.setting_button)
                        self.wait_element_visible(SettingLocators.Account_login)
                        self.click_element(SettingLocators.Account_login)
                        self.wait_element_visible(SettingLocators.Log_in_here)
                        self.click_element(SettingLocators.Log_in_here)
                        self.wait_element_visible(SettingLocators.account)
                        self.wait_element_visible(SettingLocators.password)
                        self.send_keys_to_element(SettingLocators.account, account)
                        self.send_keys_to_element(SettingLocators.password, password)
                        self.wait_element_visible(SettingLocators.Login_button)
                        self.click_element(SettingLocators.Login_button)
                        time.sleep(2)
                        print(account, "login successfully!")
                        break
                    except (ValueError, Exception):
                        self.scroll_vertical(SettingLocators.view, speed=10000)
                        time.sleep(1)

        return pages.setting_page.SettingPage(self.driver)


class AboutMe(SettingPage):
    def click_apply(self):
        self.wait_element_visible(SettingLocators.apply)
        self.click_element(SettingLocators.apply)
        return pages.setting_page.SettingPage(self.driver)

    def input_text_about_me(self):
        self.wait_element_visible(SettingLocators.about_me_text)
        self.send_keys_to_element(SettingLocators.about_me_text, "I am a Robot!")
        return self

    def input_text_website(self):
        self.wait_element_visible(SettingLocators.about_me_website)
        self.send_keys_to_element(SettingLocators.about_me_website, "www.yahoo.com")
        return self


class Quality(SettingPage):
    def click_back(self):
        self.wait_element_visible(SettingLocators.back_quality)
        self.click_element(SettingLocators.back_quality)
        return pages.setting_page.SettingPage(self.driver)

    def select_high(self):
        self.click_element_by_text("High")
        return self

    def select_ultrahigh(self):
        self.click_element_by_text("Ultra High")
        return self

    def select_normal(self):
        self.click_element_by_text("Normal")
        return self

    def select_smart_hd(self):
        self.click_element_by_text("Smart HD PRO")
        return self


class Faq(SettingPage):
    def click_send_feedback(self):
        for i in range(10):
            try:
                self.click_element_by_text("Send feedback")
                break
            except (ValueError, Exception):
                time.sleep(2)
        return Feedback(self.driver)


class Feedback(SettingPage):
    def input_text_feedback(self):
        self.wait_element_visible(SettingLocators.feedback_text)
        self.send_keys_to_element(SettingLocators.feedback_text, "Auto testing by QA")
        return self

    def click_submit(self):
        self.wait_element_visible(SettingLocators.submit)
        self.click_element(SettingLocators.submit)
        return self


class About(SettingPage):
    def click_legal_notice(self):
        self.click_element_by_text("Legal Notices")
        return self

    def click_term_of_service(self):
        self.click_element_by_text("Terms of Service")
        return self

    def click_privacy_policy(self):
        self.click_element_by_text("Privacy Policy")
        return self


class Country(SettingPage):
    def select_country(self, country):
        self.wait_element_visible(SettingLocators.search_bar)
        self.send_keys_to_element(SettingLocators.search_bar, country)
        self.wait_element_visible(SettingLocators.country_name)
        self.click_element(SettingLocators.country_name)
        self.wait_element_visible(SettingLocators.dialog_ok)
        self.click_element(SettingLocators.dialog_ok)
        return SettingPage(self.driver)

    def switch_country(self):
        country = self.get_text_from_element(SettingLocators.current_country_name)
        print("Current country is ", country)
        if country == "United States":
            self.send_keys_to_element(SettingLocators.search_bar, "France")
            self.wait_element_visible(SettingLocators.country_name)
            self.click_element(SettingLocators.country_name)
            self.wait_element_visible(SettingLocators.dialog_ok)
            self.click_element(SettingLocators.dialog_ok)
            print("Switch country to France")
        else:
            self.send_keys_to_element(SettingLocators.search_bar, "United States")
            self.wait_element_visible(SettingLocators.country_name)
            self.click_element(SettingLocators.country_name)
            self.wait_element_visible(SettingLocators.dialog_ok)
            self.click_element(SettingLocators.dialog_ok)
            print("Switch country to United States")
        return SettingPage(self.driver)

    def switch_country_to(self, name):
        self.send_keys_to_element(SettingLocators.search_bar, name)
        self.wait_element_visible(SettingLocators.country_name)
        self.click_element(SettingLocators.country_name)
        try:
            self.wait_element_visible(SettingLocators.dialog_ok)
            self.click_element(SettingLocators.dialog_ok)
        except (ValueError, Exception):
            self.driver.press_keycode(4)
        return SettingPage(self.driver)
