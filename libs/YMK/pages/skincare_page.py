from libs.YMK.locators import SkincareLocators, PickPhotoLocators, DialogLocators
from libs.YMK import pages


class Skincare(pages.YMK_base.YMKbase):
    def __init__(self, driver):
        super().__init__(driver)

    def auto_detect(self):
        self.wait_element_visible(SkincareLocators.Skin_diary_button)
        return self

    def click_skin_diary(self):
        self.wait_element_visible(SkincareLocators.Skin_diary_button)
        self.click_element(SkincareLocators.Skin_diary_button)
        return self

    def click_avatar(self):
        self.wait_element_visible(SkincareLocators.Avatar)
        self.click_element(SkincareLocators.Avatar)
        return self

    def delete_photo(self):
        self.wait_element_visible(SkincareLocators.Delete_button)
        self.click_element(SkincareLocators.Delete_button)
        self.wait_element_visible(SkincareLocators.Dialog_delete)
        self.click_element(SkincareLocators.Dialog_delete)
        return self

    def click_bipa_agree(self):
        try:  # no bipa
            self.wait_element_visible(DialogLocators.BIPA_Agree, timeout=2)
            self.click_element(DialogLocators.BIPA_Agree)
        except (ValueError, Exception):
            pass
        return self

