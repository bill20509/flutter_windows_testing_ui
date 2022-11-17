from libs.YMK.locators import SmashboxLocators, ShareLookLocators
from libs.YMK import pages


class Smashbox(pages.YMK_base.YMKbase):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_smashbox_analysis_report_page(self):
        try:
            self.wait_element_visible(SmashboxLocators.result_page, timeout=30)
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
            self.wait_element_visible(SmashboxLocators.share_post)
            self.click_element(SmashboxLocators.share_post)
        except (ValueError, Exception):
            pass
        return pages.bc_page.BC(self.driver)

    def share_to_bc(self, post_title):
        self.click_share_to_bc() \
            .click_share_post() \
            .write_post_with_auto_attached_photo(post_title)
        self.wait_element_visible(SmashboxLocators.save_photo_button, 180)

    def try_sku(self):
        for i in range(3):
            try:
                self.find_element_by_text("PROVA ORA >")
                self.click_element_by_text("PROVA ORA >")
                try:
                    self.wait_text_element_visible("LOOK SOFT")
                except:
                    print("can't find...")
                break
            except(ValueError, Exception):
                self.swipe_up()
        return self

    def change_palette(self, palette):
        try:
            self.wait_text_element_visible(palette)
            self.click_element_by_text(palette)
        except(ValueError, Exception):
            pass
        return self

    def click_capture_button(self):
        try:
            self.wait_element_visible(SmashboxLocators.capture_button)
            self.click_element(SmashboxLocators.capture_button)
            self.wait_element_visible(SmashboxLocators.preview_image)
        except (ValueError, Exception):
            pass
        return self

    def click_save_photo_button(self):
        try:
            self.wait_element_visible(SmashboxLocators.save_photo_button)
            self.click_element(SmashboxLocators.save_photo_button)
            self.wait_time(5)
        except (ValueError, Exception):
            pass
        return self

