from libs.YMK.locators import AgingLocators, PickPhotoLocators, DialogLocators
from libs.YMK import pages


class Aging(pages.YMK_base.YMKbase):
    def __init__(self, driver):
        super().__init__(driver)

    def adjust_intensity_to_left(self):
        self.slidebar_to_left(AgingLocators.Aging_Slider_Bar)
        return self

    def click_tryit(self):
        self.wait_element_visible(AgingLocators.Try_it)
        self.click_element(AgingLocators.Try_it)
        return self

    def choose_photo(self):
        self.wait_element_visible(AgingLocators.Choose_photo)
        self.click_element(AgingLocators.Choose_photo)
        try:
            self.wait_element_visible(AgingLocators.Start, timeout=2)
            self.click_element(AgingLocators.Start)
        except (ValueError, Exception):
            pass
        return self

    def click_photo(self):
        self.wait_element_visible(AgingLocators.Photo)
        self.click_element(AgingLocators.Photo)
        return self

    def click_grid(self):
        self.wait_element_visible(AgingLocators.Grid)
        self.click_element(AgingLocators.Grid)
        return self

    def click_video(self):
        self.wait_element_visible(AgingLocators.Video)
        self.click_element(AgingLocators.Video)
        return self

    def click_start(self):
        self.click_element(AgingLocators.Start)
        return self

    def click_allow(self):
        self.wait_element_visible(AgingLocators.Allow)
        self.click_element(AgingLocators.Allow)
        return self

    def click_back(self):
        self.click_element(AgingLocators.Back)
        return pages.launcher_page.Launcher(self.driver)

    def click_save(self):
        self.wait_element_visible(AgingLocators.Save)
        self.click_element(AgingLocators.Save)
        self.wait_element_invisible(AgingLocators.waiting_cursor, 300)
        return self

    def check_result_page_ad(self):
        try:
            self.wait_element_visible(AgingLocators.AD_result_page, timeout=5)
            return 1
        except (ValueError, Exception):
            return 0

    def check_save_page_ad(self):
        try:
            self.wait_element_visible(AgingLocators.AD_save_page, timeout=5)
            return 1
        except (ValueError, Exception):
            return 0

    def pick_photo(self, folder, photo=1):
        for i in range(5):
            try:
                self.click_element_by_name(PickPhotoLocators.select_folder, folder)
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.album_view, 2000)
        for j in range(5):
            try:
                self.select_element_by_number(PickPhotoLocators.select_photo, (photo-1))
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.photo_view, 2000)
        return self

    def wait_animation(self):
        # self.check_network_except()
        try:
            self.wait_element_invisible(AgingLocators.Time_Machine_Animation, timeout=30)
        except (ValueError, Exception):
            pass
        return self

    def click_bipa_agree(self):
        try:  # no bipa
            self.wait_element_visible(DialogLocators.BIPA_Agree, timeout=2)
            self.click_element(DialogLocators.BIPA_Agree)
        except (ValueError, Exception):
            pass
        return self

    def check_network_except(self):
        try:  # no network
            self.wait_element_visible(AgingLocators.Network_RETRY, timeout=2)
            self.click_element(AgingLocators.Network_RETRY)
        except (ValueError, Exception):  # unstable network
            try:
                self.wait_element_visible(AgingLocators.Network_error_dialog, timeout=2)
                self.click_element(AgingLocators.Network_OK)
                self.select_element_by_number(PickPhotoLocators.select_photo, 0)
            except (ValueError, Exception):
                pass
        return self

    def click_share_to_bc(self):
        try:
            self.find_element_by_text("YouCam Community")
            self.click_element_by_text("YouCam Community")
        except (ValueError, Exception):
            pass
        return self

    def click_share_post(self):
        try:
            self.wait_element_visible(AgingLocators.share_post)
            self.click_element(AgingLocators.share_post)
        except (ValueError, Exception):
            pass
        return pages.bc_page.BC(self.driver)

    def share_to_bc(self, post_title):
        self.click_share_to_bc() \
            .click_share_post() \
            .write_post_with_auto_attached_photo(post_title)
        self.wait_element_visible(AgingLocators.Aging_saved_page, 180)
