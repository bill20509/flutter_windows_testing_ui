from libs.YMK.locators import EffectsLocators
from libs.YMK import pages


class Effects(pages.photomakeup_page.PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_collection(self, number):
        for i in range(5):
            try:
                self.select_element_by_number(EffectsLocators.effect_item, (number - 1))
                break
            except (ValueError, Exception):
                self.wait_element_visible(EffectsLocators.effect_item)
                self.scroll_horizontal(EffectsLocators.effect_view)
        return self

    def select_effect(self, number):
        for i in range(5):
            try:
                self.select_element_by_number(EffectsLocators.effect_item, number)
                break
            except (ValueError, Exception):
                self.wait_element_visible(EffectsLocators.effect_view)
                self.scroll_horizontal(EffectsLocators.effect_view)
        return self

    def adjust_intensity_to_right(self):
        self.wait_element_visible(EffectsLocators.intensity_seekbar)
        self.slidebar_to_right(EffectsLocators.intensity_seekbar)
        return self

    def adjust_intensity_to_left(self):
        self.wait_element_visible(EffectsLocators.intensity_seekbar)
        self.slidebar_to_left(EffectsLocators.intensity_seekbar)
        return self

    def click_store(self):
        self.wait_element_visible(EffectsLocators.store_button)
        self.click_element(EffectsLocators.store_button)
        return pages.store_page.Effect(self.driver)

    def click_premium_effect_pack(self):
        for i in range(10):
            try:
                self.click_element(EffectsLocators.crown_effect_pack)
                break
            except(ValueError, Exception):
                self.wait_element_visible(EffectsLocators.effect_view)
                self.slidebar_to_left(EffectsLocators.effect_view)
                self.wait_time(1)
        return self

    def wait_download_pack(self):
        self.wait_element_invisible(EffectsLocators.pack_download_progress)
        return self

    def click_effect(self):
        self.wait_element_visible(EffectsLocators.effect_name)
        self.click_element(EffectsLocators.effect_name)
        return self
