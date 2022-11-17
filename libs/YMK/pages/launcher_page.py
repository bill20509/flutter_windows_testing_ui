from libs.YMK.locators import LauncherLocators, MeLocators, PhotoMakeupLocators, PickPhotoLocators, DialogLocators
from libs.YMK import pages


class Launcher(pages.YMK_base.YMKbase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_makeupcam_button(self):
        self.click_element(LauncherLocators.Makeup_cam)
        return pages.makeupcam_page.MakeupCam(self.driver)

    def click_photomakeup_button(self):
        self.wait_element_visible(LauncherLocators.Makeup_cam)
        self.click_element(LauncherLocators.Photo_makeup)
        return pages.photopicker_page.PhotoPicker(self.driver)

    def click_aging_tile(self):
        self.wait_element_visible(LauncherLocators.Aging_tile)
        self.click_element(LauncherLocators.Aging_tile)
        return pages.aging_page.Aging(self.driver)

    def check_iap_and_close(self):
        try:
            self.wait_element_visible(LauncherLocators.Makeup_cam, timeout=5)
        except (ValueError, Exception):
            self.driver.keyevent(4)
        return self

    def check_churn_user_and_close(self):
        try:
            self.wait_element_visible(LauncherLocators.Makeup_cam, timeout=5)
        except (ValueError, Exception):
            self.driver.keyevent(4)
        # try:
        #     self.wait_element_visible(ChurnUserRecoveryLocators.Close_button)
        #     self.click_element(ChurnUserRecoveryLocators.Close_button)
        # except (ValueError, Exception):
        #     pass
        return self

    def check_launcher_page_ad(self):
        i = 0
        while i < 5:
            try:
                self.wait_element_visible(LauncherLocators.IAP_banner, timeout=5)
                self.deeplink_to_setting()\
                    .click_country()\
                    .switch_country_to("South Korea") \
                    .waiting_cursor() \
                    .click_back()
                self.deeplink_to_launcher().wait_time(10)
            except (ValueError, Exception):
                try:
                    self.wait_element_visible(LauncherLocators.AD_banner, timeout=5)
                    return 1
                except (ValueError, Exception):
                    i = i + 1
                    self.swipe_up()
        if i >= 5:
            return 0

    def check_hw_back_ad(self):
        self.wait_element_visible(LauncherLocators.Makeup_cam, timeout=5)
        self.driver.keyevent(4)
        try:
            self.wait_element_visible(LauncherLocators.AD_hw_back)
            return 1
        except (ValueError, Exception):
            return 0

    def click_bc_button(self):
        self.wait_element_visible(LauncherLocators.bc_button)
        self.click_element(LauncherLocators.bc_button)
        return pages.bc_page.BC(self.driver)

    def makeupcam_button_is_exist(self):
        try:
            self.wait_element_visible(LauncherLocators.Makeup_cam, timeout=5)
            # 有makeup cam button
            return 1
        except(ValueError, Exception):
            return 0

    def check_ad_back_from_cam(self):
        i = 0
        while i < 3:
            self.click_makeupcam_button().wait_time().click_back()
            result = self.makeupcam_button_is_exist()
            if result == 0:
                return 1
            i = i + 1
        return 0

    def click_skincare_tile(self):
        self.wait_element_visible(LauncherLocators.Skincare_tile)
        self.click_element(LauncherLocators.Skincare_tile)
        return pages.skincare_page.Skincare(self.driver)

    def click_get_inspired_button(self):
        self.wait_element_visible(LauncherLocators.Get_Inspired_button)
        self.click_element(LauncherLocators.Get_Inspired_button)
        return self

    def click_crown_button(self):
        self.wait_element_visible(LauncherLocators.Crown)
        self.click_element(LauncherLocators.Crown)
        return self

    def click_ycv_tile(self):
        self.wait_element_visible(LauncherLocators.YCV_tile)
        self.click_element(LauncherLocators.YCV_tile)
        return self

    def click_ycp_tile(self):
        self.wait_element_visible(LauncherLocators.YCP_tile)
        self.click_element(LauncherLocators.YCP_tile)
        return self

    def click_get_youcam_ycp(self):
        for i in range(10):
            try:
                self.click_element_by_text("YouCam Perfect")
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=10000)
        return self

    def click_get_youcam_ycv(self):
        for i in range(10):
            try:
                self.click_element_by_text("YouCam Video")
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=10000)
        return self

    def find_hot_feature(self):
        for i in range(10):
            try:
                self.find_element(LauncherLocators.Features_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=2000)
        return self

    def try_hot_feature(self):
        for i in range(10):
            try:
                self.click_element(LauncherLocators.Features_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=2000)
        return pages.photomakeup_page.PhotoMakeup(self.driver)

    def find_popular_look(self):
        for i in range(10):
            try:
                self.find_element(LauncherLocators.Look_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=2000)
        return self

    def try_popular_look(self):
        for i in range(10):
            try:
                self.click_element(LauncherLocators.Look_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=2000)
        return pages.photomakeup_page.PhotoMakeup(self.driver)

    def find_how_to(self):
        for i in range(10):
            try:
                self.find_element(LauncherLocators.Howto_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=2000)
        return self

    def try_how_to(self):
        for i in range(10):
            try:
                self.click_element(LauncherLocators.Howto_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=2000)
        return pages.bc_page.BC(self.driver)

    def find_trending(self):
        for i in range(10):
            try:
                self.find_element(LauncherLocators.Community_trending_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=5000)
        return self

    def try_trending(self):
        for i in range(10):
            try:
                self.click_element(LauncherLocators.Community_trending_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=5000)
        return self

    def find_makeover(self):
        for i in range(10):
            try:
                self.find_element(LauncherLocators.Instant_Makeover_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=5000)
        return self

    def try_makeover(self):
        for i in range(10):
            try:
                self.click_element(LauncherLocators.Instant_Makeover_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=5000)
        return pages.photomakeup_page.PhotoMakeup(self.driver)

    def find_shows(self):
        for i in range(10):
            try:
                self.find_element(LauncherLocators.Shows_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=2000)
        return self

    def try_shows(self):
        for i in range(10):
            try:
                self.click_element(LauncherLocators.Shows_card)
                break
            except (ValueError, Exception):
                self.scroll_vertical(LauncherLocators.Launcher_view, speed=2000)
        return self

    def click_me_button(self):
        self.wait_element_visible(LauncherLocators.Me_button)
        self.click_element(LauncherLocators.Me_button)
        return pages.me_page.MePage(self.driver)



