from libs.YMK.locators import PickPhotoLocators, AccessoriesLocators
from libs.YMK import pages


class Accessories(pages.YMK_base.YMKbase):
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

    def click_store(self):
        self.click_element(AccessoriesLocators.store_button)
        return pages.store_page.Store

    def select_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self

    def tap_central(self):
        self.tap_element_coordinates(AccessoriesLocators.editroom_view)
        return self


class Eyewear(Accessories):
    # X 215 Y 922
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_eyewear_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self


class Headband(Accessories):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_headband_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self


class Necklace(Accessories):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_necklace_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self


class Earrings(Accessories):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_earring_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self


class Hat(Accessories):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_hat_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self
