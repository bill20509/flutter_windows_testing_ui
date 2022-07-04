from libs.YMK.locators import PickPhotoLocators, EffectsLocators
from libs.YMK import pages


class Effects(pages.YMK_base.YMKbase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def pick_photo(self, folder, photo=1):
        for i in range(5):
            try:
                self.click_element_by_name(PickPhotoLocators.select_folder, folder)
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.album_view)
        for j in range(5):
            try:
                self.select_element_by_number(PickPhotoLocators.select_photo, (photo-1))
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.photo_view)
        return self

    def select_collection(self, number):
        for i in range(5):
            try:
                self.select_element_by_number(EffectsLocators.effect_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(EffectsLocators.effect_view)
        return self

    def select_effect(self, number):
        for i in range(5):
            try:
                self.select_element_by_number(EffectsLocators.effect_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(EffectsLocators.effect_view)
        return self

    def adjust_intensity_to_right(self):
        self.slidebar_to_right(EffectsLocators.intensity_seekbar)
        return self

    def adjust_intensity_to_left(self):
        self.slidebar_to_left(EffectsLocators.intensity_seekbar)
        return self

    def click_store(self):
        self.click_element(EffectsLocators.store_button)
        return pages.store_page.Store(self.driver)
